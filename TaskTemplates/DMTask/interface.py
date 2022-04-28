# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 21:10:43 2019

@author: screa
"""
from tkinter import *
import tkinter,cv2,PIL
from PIL import Image, ImageTk
import numpy as np
import pandas as pd
import tkinter.font as font
from phase_1 import data_phase_1
from bar import bar
from generate_data_trials import cluster_data_trials, generate_data_trials
import argparse

parser = argparse.ArgumentParser(description='subject name')
parser.add_argument('--subject_name', type=str,
                help='subject name for create a folder with its results')
parser.add_argument('--w', type=int, help='width of the screen')
parser.add_argument('--h', type=int, help='height of the screen')
parser.add_argument('--samples_per_difficulty', type=int, default=60, help='number of samples per difficulty')

class interface():
    path_img_phase_1_begin='./imgs_int/phase_1_question.png'
    path_img_instruction='./imgs_int/instructions.png'
    list_p = []

    def __init__(self, subject_name="subject_test", screenwidth=None, screenheight=None):   
        self.subject_name = subject_name   
        self.background, self.confidence_rate_screen, self.eye_fixation, self.free_eye_movent, self.joystick_buttons, self.products, self.instructions1, self.products_names = data_phase_1().load()

        self.window = tkinter.Tk()
        self.window.attributes('-fullscreen', True)
        
        self.w = screenwidth if screenwidth else self.window.winfo_screenwidth()
        self.h = screenheight if screenheight else self.window.winfo_screenheight()
        self.create_canvas_inicial(self.path_img_instruction)        
        
        
    def clicked_comenzar_button(self,event):
        self.canvas.delete(self.buttonTXT)  
        self.canvas.delete(self.buttonBG) 
        self.create_canvas(self.path_img_phase_1_begin)
        self.wait_here(500)
        self.create_canvas_products()
    
    def create_canvas_inicial(self,path_img):
        cv_img = cv2.resize(cv2.imread(path_img),(self.w,self.h))    
        self.canvas = tkinter.Canvas(self.window)
        self.canvas.pack(expand='True', fill='both')        
        self.photo = ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img), master=self.window)
        self.imageOnCanvas=self.canvas.create_image(0, 0, image=self.photo, anchor='nw')
        self.create_buttons_instructions()

        self.window.bind('<Escape>',lambda e: self.window.destroy())
        self.window.geometry("%dx%d+0+0" % (self.w,self.h))
        self.window.focus_force()
        self.window.mainloop()        
        
    def create_canvas(self, path_img):
        cv_img = cv2.resize(cv2.imread(path_img),(self.w,self.h))    
        self.photo = ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img), master=self.window)
        self.canvas.create_image(0, 0, image=self.photo, anchor='nw')
        self.canvas.itemconfig(self.imageOnCanvas, image=self.photo) # change the displayed picture
        self.canvas.pack()
        
    def create_canvas_products(self):
        self.create_imgs_products_pos()
        self.canvas.create_image(0, 0, image=self.list_photos[0], anchor='nw')
        self.canvas.itemconfig(self.imageOnCanvas, image=self.list_photos[0]) # change the displayed picture
        self.cnt = 0
        bar(self.window, self.canvas, self.imageOnCanvas, self.photo, self.list_p, self.w, self.h, self.list_photos, self.cnt, self.list_imgs, self.subject_name) 

    def create_imgs_products_pos(self):
        rel_pod_w, rel_pod_h, rel_posX, rel_posY = 0.5, 0.5, 0.5, 0.1
        wp, hp = int(rel_pod_w*self.w), int(rel_pod_h*self.h)
        cv_img = cv2.resize(self.background, (self.w,self.h))
        self.list_photos = []
        self.list_imgs = []
        
        for i in range(0,len(self.products)):            
            producto = cv2.resize(self.products[i],(wp,hp))
            x1, y1  = int(rel_posX*(self.w-wp)), int(rel_posY*(self.h-hp))                    
            cv_img[y1:y1+hp,x1:x1+wp:] = producto[0:hp,0:wp,:]            
            self.photo = ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img), master=self.window)
            self.list_photos.append(self.photo)  
            self.list_imgs.append(self.products_names[i])

    def create_buttons_instructions(self):
        self.buttonBG = self.canvas.create_rectangle(self.w-int(np.floor(self.w/3.5)), self.h-int(np.floor(self.h/6)), self.w-int(np.floor(self.w/3.5))+300, self.h-int(np.floor(self.h/6))+50, fill="grey50", outline="grey90")
        self.buttonTXT = self.canvas.create_text(self.w-int(np.floor(self.w/3.5))+150, self.h-int(np.floor(self.h/6))+25 ,font=("Purisa", 16),text="Comenzar fase de ponderación")
        self.canvas.tag_bind(self.buttonBG, "<Button-1>", self.clicked_comenzar_button) 
        self.canvas.tag_bind(self.buttonTXT, "<Button-1>", self.clicked_comenzar_button)
        
    def wait_here(self,time):
        var = tkinter.IntVar()
        self.window.after(time, var.set, 1)
        self.window.wait_variable(var)


if __name__=='__main__':
    args = parser.parse_args()
    if args.subject_name:
        ins = interface(subject_name=args.subject_name, screenwidth=args.w, screenheight=args.h)
    else:
        ins = interface(screenwidth=args.w, screenheight=args.h)
    data = pd.read_csv(f"./results/{args.subject_name}/preferences.csv", header=None)
    rankings = np.asarray(data).T[0]
    
    cluster_data_trials(rankings, samples_per_difficulty=args.samples_per_difficulty, subject_name=args.subject_name, is_save=True)
    sample_full_random, screen_order, item_order = generate_data_trials(samples_per_difficulty=args.samples_per_difficulty, subject_name=args.subject_name)
    data_trials = pd.DataFrame(np.hstack([sample_full_random, np.expand_dims(screen_order, -1), np.expand_dims(item_order, -1)]), columns=["img_izq", "img_der", "distance", "cond_exp", "item_order"])
    data_trials.to_csv(f"./results/{args.subject_name}/data_trials_information.csv")
