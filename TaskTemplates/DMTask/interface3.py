from collections import deque
import tkinter as tk, numpy as np, cv2, PIL
import pandas as pd
from phase_1 import data_phase_1
from generate_data_trials import create_trials
from PIL import Image, ImageTk
import argparse

#Imports from Tabilo
from psychopy import parallel #Revisar si está en el ambiente de karla y si no, si se puede instalar
from pylink import *
import cv2
import time
import gc
import sys
import os

parser = argparse.ArgumentParser(description='preferences')
parser.add_argument('--subject_name', type=str,
                help='csv preferences name')
parser.add_argument('--no_eye_tracker', action='store_true', help='if use eye tracker')
parser.add_argument('--w', type=int, help='width of the screen')
parser.add_argument('--h', type=int, help='height of the screen')
parser.add_argument('--samples_per_difficulty', type=int, default=60, help='number of samples per difficulty')
class draw():
    """
    Crea interfaz 3 
    """
    def __init__(self, sample_full_random, screen_order, item_order, samples_per_difficulty, subject_name="preferences", no_eye_tracker=False, no_egg=True, screenwidth=None, screenheight=None):   
        self.subject_name = subject_name
        self.no_eye_tracker = no_eye_tracker
        self.no_egg = no_egg
        if not self.no_egg:
            #Initiate Communication with BDF via Parallel port
            self.port = parallel.ParallelPort(address=0x0378)
            self.port.setData(0)
        self.choices = []
        self.choice_and_confidence = dict.fromkeys(["choice", "confidence"])
        self.window = tk.Tk()
        self.w = screenwidth if screenwidth else self.window.winfo_screenwidth()
        self.h = screenheight if screenheight else self.window.winfo_screenheight()
        self.window.attributes('-fullscreen', True)
        self.sample_full_random = sample_full_random
        self.screen_order = screen_order
        self.item_order = item_order
        self.window.bind('<Escape>',lambda e: self.window.destroy())
        self.window.geometry("%dx%d+0+0" % (self.w,self.h))      
        self.window.focus_force()
        self.background, self.confidence_rate_screen, self.eye_fixation, self.free_eye_movent,self.joystick_buttons,self.products,self.instructions1, self.img_names = data_phase_1().load()
        self.cruz = ImageTk.PhotoImage(image = PIL.Image.fromarray(cv2.resize(self.eye_fixation,(self.w,self.h))))
        self.confidence = ImageTk.PhotoImage(image = PIL.Image.fromarray(self.confidence_rate_screen))
        rest1_img = cv2.imread('./imgs_int/phase2/bloque_rest1.png')
        rest2_img =  cv2.imread('./imgs_int/phase2/bloque_rest2.png')
        end_img =  cv2.imread('./imgs_int/phase2/fin tarea.png')
        self.rest1_img = ImageTk.PhotoImage(image = PIL.Image.fromarray(cv2.resize(rest1_img,(self.w,self.h))))
        self.rest2_img = ImageTk.PhotoImage(image = PIL.Image.fromarray(cv2.resize(rest2_img,(self.w,self.h))))
        self.end_img = ImageTk.PhotoImage(image = PIL.Image.fromarray(cv2.resize(end_img,(self.w,self.h))))
        self.create_imgs_products_pos()
        
        self.put_image(self.window, self.cruz)
        self.samples_per_difficulty = samples_per_difficulty 
        self.i = 0 

    def run(self, i_block=0, i_trial=0):
        self.i_block = i_block 
        self.i_trial = i_trial 
        if self.i == 0:
            self.bind_enter = self.window.bind("<Return>", self.attention_callback)
        else:
            self.attention_callback(None)
        self.window.mainloop() 
        
    def put_image(self, root, img):
        self.panel = tk.Label(root, image=img)
        self.panel.pack(side="bottom", fill="both", expand="yes")
        
    def get_index(self):
        return self.i
    
    def get_times(self):
        return self.times

    def attention_callback(self, e):
        #Initialize EYELINK data
        if self.i == 0:
            self.window.unbind("<Return>", self.bind_enter)
        #Experiment
        try:
            self.change_image(self.create_imgs_products_pos(pos=self.item_order[self.i], np1=np.uint64(self.sample_full_random[self.i, 0])))
        except:
            print("error en change_image")
            self.window.destroy()
        if not self.no_egg:
            self.port.setData(5) #ex setPin(15,1)
            self.wait_here(1)
            self.port.setData(0)
        if not self.no_eye_tracker:
            drawTime = currentTime() 
            getEYELINK().sendMessage("%d DISPLAY ON" %drawTime) #Avisa a Eyelink
            getEYELINK().sendMessage("SYNCTIME %d" %drawTime)
        self.wait_here(1000)
        self.change_image(self.cruz)
        self.wait_here(200)
        self.change_image(self.create_imgs_products_pos(pos=1-self.item_order[self.i], np1=np.uint64(self.sample_full_random[self.i, 1])))
        if not self.no_egg:
            self.port.setData(5)
            self.wait_here(1)
            self.port.setData(0)
        if not self.no_eye_tracker:
            drawTime = currentTime()
            getEYELINK().sendMessage("%d DISPLAY ON" %drawTime)
        #getEYELINK().sendMessage("SYNCTIME %d" %drawTime)
        self.wait_here(1000)
        
        if self.screen_order[self.i] == 0:
            self.change_image(ImageTk.PhotoImage(image = PIL.Image.fromarray(cv2.resize(self.background, (self.w,self.h))), master=self.window))
            self.choice_and_confidence["cond_exp"] = 0
            if not self.no_eye_tracker:
                drawTime = currentTime()
                getEYELINK().sendMessage("%d DISPLAY ON" %drawTime)
                getEYELINK().sendMessage("Screen_order==0")
            if not self.no_egg:
                self.port.setData(8) 
                self.wait_here(1)
                self.port.setData(0)
        if self.screen_order[self.i] == 1:
            self.change_image(self.cruz)
            self.choice_and_confidence["cond_exp"] = 1
            if not self.no_eye_tracker:
                drawTime = currentTime()
                getEYELINK().sendMessage("%d DISPLAY ON" %drawTime)
                getEYELINK().sendMessage("Screen_order==1")
            if not self.no_egg:
                self.port.setData(8) 
                self.wait_here(1)
                self.port.setData(0)            
        if self.screen_order[self.i] == 2:
            self.change_image(self.create_imgs_products_pos(pos=2, np1=np.uint64(self.sample_full_random[self.i, 0]), np2=np.uint64(self.sample_full_random[self.i, 1])))
            self.choice_and_confidence["cond_exp"] = 2
            if not self.no_eye_tracker:
                drawTime = currentTime()
                getEYELINK().sendMessage("%d DISPLAY ON" %drawTime)
                getEYELINK().sendMessage("Screen_order==2")
            if not self.no_egg:
                self.port.setData(8) 
                self.wait_here(1)
                self.port.setData(0)
        self.bind1 = self.window.bind('<KeyPress>', self.choice)
        # Continue experiment
        pd.DataFrame(self.choices).to_csv(f"./results/{self.subject_name}/preferences2.csv", index=False)
        self.i += 1
            
    def choice(self, e):
        """
        Crear archivo
        """
        if e.keysym == 'Left':
            if not self.no_eye_tracker:
                ButtonTime = currentTime()
                getEYELINK().sendMessage("%d BUTTON ON" %ButtonTime)
            if not self.no_egg:
                self.port.setData(6)
            if not self.no_eye_tracker:
                getEYELINK().sendMessage("choice: "+ e.keysym)
            if (not self.no_egg) or (not self.no_eye_tracker):
                self.wait_here(1)
            if not self.no_egg:
                self.port.setData(0)
                print('0')
            self.choice_and_confidence["choice"] = "0"
            self.change_image(self.confidence)
        elif e.keysym == 'Right':
            if not self.no_eye_tracker:
                ButtonTime = currentTime()
                getEYELINK().sendMessage("%d BUTTON ON" %ButtonTime)
            if not self.no_egg:
                self.port.setData(7)
            if not self.no_eye_tracker:
                getEYELINK().sendMessage("choice: "+ e.keysym)
            if (not self.no_egg) or (not self.no_eye_tracker):
                self.wait_here(0)
            if not self.no_egg:
                self.port.setData(0)
                print('1')
            self.choice_and_confidence["choice"] = "1"
            self.change_image(self.confidence)
        self.window.unbind('<KeyPress>', self.bind1)
        self.bind2 = self.window.bind('<KeyPress>', self.confidence_callback) 
        
    def confidence_callback(self, e):
        """
        Crear archivo
        """
        ##Avisa a Eyelink del boton de confianza
        if not self.no_eye_tracker:
            ButtonTime = currentTime()
            getEYELINK().sendMessage("%d BUTTON ON" %ButtonTime)
        if e.keysym == '1':
            if not self.no_eye_tracker:
                getEYELINK().sendMessage("confidence: "+ e.keysym)
            if not self.no_egg:
                self.port.setData(1)
                self.wait_here(1)
                print('1')
                self.port.setData(0)
            self.choice_and_confidence["confidence"] = '1'
            self.window.unbind('<KeyPress>', self.bind2)
            self.choices.append(self.choice_and_confidence)
            self.choice_and_confidence = dict.fromkeys(["choice", "confidence"])
            self.check_end_block()
            self.window.quit()
        elif e.keysym == '2':
            if not self.no_eye_tracker:
                getEYELINK().sendMessage("confidence: " + e.keysym)
            if not self.no_egg:
                self.port.setData(2)
                self.wait_here(1)
                print('2')
                self.port.setData(0)  
            self.choice_and_confidence["confidence"] = '2'
            self.window.unbind('<KeyPress>', self.bind2)
            self.choices.append(self.choice_and_confidence)
            self.choice_and_confidence = dict.fromkeys(["choice", "confidence","cond_exp"])
            self.check_end_block()
            self.window.quit()
        elif e.keysym == '3':
            if not self.no_eye_tracker:
                getEYELINK().sendMessage("confidence: "+ e.keysym)
            if not self.no_egg:
                self.port.setData(3)
                self.wait_here(1)
                print('3')
                self.port.setData(0)
            self.choice_and_confidence["confidence"] = '3'
            self.window.unbind('<KeyPress>', self.bind2)
            self.choices.append(self.choice_and_confidence)
            self.choice_and_confidence = dict.fromkeys(["choice", "confidence"])
            self.check_end_block()
            self.window.quit()
        elif e.keysym == '4':
            if not self.no_eye_tracker:
                getEYELINK().sendMessage("confidence: "+ e.keysym)
            if not self.no_egg:
                self.port.setData(4)
                self.wait_here(1)
                print('4')
                self.port.setData(0)
            self.choice_and_confidence["confidence"] = '4'
            self.window.unbind('<KeyPress>', self.bind2)
            self.choices.append(self.choice_and_confidence)
            self.choice_and_confidence = dict.fromkeys(["choice", "confidence"])
            self.check_end_block()
            self.window.quit()
        
    def check_end_block(self):
        if (self.i_trial % self.samples_per_difficulty)+1 == self.samples_per_difficulty:
            if self.i_block == 0:
                self.change_image(self.rest1_img)
                self.create_continue_button()
            elif self.i_block == 1:
                self.change_image(self.rest2_img)
                self.create_continue_button()
            elif self.i_block >= 2:
                self.change_image(self.end_img)
                self.create_continue_button()

    def create_continue_button(self):
        var = tk.IntVar()
        button = tk.Button(self.window, text="Continuar", command=lambda: var.set(1), width=25, height=2)
        button.place(relx=.7, rely=.7, anchor="c")
        button.wait_variable(var)
        button.destroy() 

    def change_image(self, img2):
        self.panel.configure(image=img2)
        self.panel.image = img2
  
    def create_imgs_products_pos(self, pos=0, np1=0, np2=0):
        rel_pod_w, rel_pod_h = 0.3, 0.3 #0.15, 0.5
        rel_posX_l, rel_posY_l = 0.05, 0.5 #0.85, 0.5
        rel_posX_r, rel_posY_r = 0.95, 0.5
        wp, hp = int(rel_pod_w*self.w), int(rel_pod_h*self.h)        
        cv_img = cv2.resize(self.background,(self.w,self.h))
        producto1 = cv2.resize(self.products[np1],(wp,hp))        
        producto2 = cv2.resize(self.products[np2],(wp,hp))        
        x1, y1 = int(rel_posX_l*(self.w-wp)), int(rel_posY_l*(self.h-hp))
        x2, y2 = int(rel_posX_r*(self.w-wp)), int(rel_posY_r*(self.h-hp))
        if pos==0:#'left'
            cv_img[y1:y1+hp,x1:x1+wp:] = producto1[0:hp,0:wp,:]
        elif pos==1:#'right'
            cv_img[y2:y2+hp,x2:x2+wp:] = producto1[0:hp,0:wp,:]  
        elif pos==2:# 'both'             
            cv_img[y1:y1+hp,x1:x1+wp:] = producto1[0:hp,0:wp,:]  
            cv_img[y2:y2+hp,x2:x2+wp:] = producto2[0:hp,0:wp,:]  
        self.photo_l = ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img), master=self.window)
        return self.photo_l
        
    def wait_here(self, time):
        var = tk.IntVar()
        self.window.after(time, var.set, 1)
        self.window.wait_variable(var)


        
if __name__=='__main__':
    args = parser.parse_args()
    if args.subject_name:
        rankings, sample_full_random, screen_order, item_order = create_trials(args.samples_per_difficulty, subject_name=args.subject_name)
        draw(sample_full_random, screen_order, item_order, subject_name=args.subject_name)
    else:    
        rankings, sample_full_random, screen_order, item_order = create_trials(args.samples_per_difficulty)
        draw(sample_full_random, screen_order, item_order)

    
