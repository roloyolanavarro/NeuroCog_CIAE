# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 00:52:22 2019

@author: screa
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 21:10:43 2019

@author: screa
"""
import time
from tkinter import *
import tkinter,cv2,PIL
from PIL import Image, ImageTk
import numpy as np
import tkinter.font as font
from phase_1 import data_phase_1
from interface3 import draw
from generate_data_trials import create_trials
import threading
import argparse

#Import from Tabilo
from pylink import *
import cv2
import time
import gc
import sys
import os

parser = argparse.ArgumentParser(description='preferences')
parser.add_argument('--subject_name', type=str, default="test",
                help='csv preferences name')
parser.add_argument('--no_eye_tracker', action='store_true', help='if use eye tracker')
parser.add_argument('--w', type=int, help='width of the screen')
parser.add_argument('--h', type=int, help='height of the screen')
parser.add_argument('--samples_per_difficulty', type=int, default=60, help='number of samples per difficulty')

#Input filename
#nombre = input("nombre_EDF: ").replace('\r', '')                

#Create Log
log = open("int2_log.py","a")
sys.stdout = log
                               
RIGHT_EYE = 1
LEFT_EYE = 0
BINOCULAR = 2
NTRIALS = 3
TRIALDUR = 5000
SCREENWIDTH = 1920 
SCREENHEIGHT = 1080

class interface2():
    path_img_int1='./imgs_int/phase2_int1.png'
    path_img_int2='./imgs_int/phase2_int2.png' 
    path_img_int3 = './imgs_int/phase2_int3.png'
    path_img_int4 = './imgs_int/phase2_int4.png'
    path_img_int5 = './imgs_int/phase2_int5.png'
    path_img_int6 = './imgs_int/phase2_int6.png' 
    path_img_int7='./imgs_int/phase2_int7.png'
    path_img_int8='./imgs_int/phase2_int8.png'
    path_img_int9='./imgs_int/phase2_int9.png'
    
    def __init__(self, subject_name="preferences", screenwidth=None, screenheight=None):   
        self.subject_name = subject_name
        self.background, self.confidence_rate_screen, self.eye_fixation, self.free_eye_movent, self.joystick_buttons, self.products, self.instructions1, self.img_names = data_phase_1().load()
        self.window = tkinter.Tk()
        self.window.attributes('-fullscreen', True)
        self.w = screenwidth if screenwidth else self.window.winfo_screenwidth()
        self.h = screenheight if screenheight else self.window.winfo_screenheight()
        self.create_canvas_inicial(self.path_img_int1)     

    list_p = []

    def clicked_comenzar_button2(self,event):
        self.delete_buttons()
        self.create_canvas(self.path_img_int2)
        self.create_buttons_instructions3()
        
    def clicked_comenzar_button3(self,event):
        self.delete_buttons()
        self.create_canvas(self.path_img_int3)
        self.create_buttons_instructions4()

    def clicked_comenzar_button4(self, event):
        self.delete_buttons()
        self.create_canvas(self.path_img_int4)
        self.create_buttons_instructions5()

    def clicked_comenzar_button5(self,event):
        self.delete_buttons()
        self.create_canvas(self.path_img_int5)
        self.create_buttons_instructions6()

    def clicked_comenzar_button6(self,event):
        self.delete_buttons()
        self.create_canvas(self.path_img_int6)
        self.create_buttons_instructions7()

    def clicked_comenzar_button7(self,event):
        self.delete_buttons()
        self.create_canvas(self.path_img_int7)
        self.create_buttons_instructions8()

    def clicked_comenzar_button8(self,event):
        self.delete_buttons()
        self.window.destroy()  
    
    def create_canvas_inicial(self, path_img):
        cv_img = cv2.resize(cv2.imread(path_img),(self.w,self.h))    
        self.window.geometry("%dx%d+0+0" % (self.w,self.h))
        self.canvas = tkinter.Canvas(self.window)
        self.canvas.pack(expand='True', fill='both')        
        self.photo = ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img), master=self.window)
        self.imageOnCanvas = self.canvas.create_image(0, 0, image=self.photo, anchor='nw')
        self.create_buttons_instructions()

        self.window.bind('<Escape>', lambda e: self.window.destroy())
        self.window.focus_set()
        self.window.mainloop()        
        
    def create_canvas(self,path_img):
        cv_img = cv2.resize(cv2.imread(path_img),(self.w,self.h)) 
        tmp=cv_img[:,:,2].copy()
        cv_img[:,:,2]=cv_img[:,:,0]
        cv_img[:,:,0]=tmp
        self.photo = ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img), master=self.window)
        self.canvas.create_image(0, 0, image=self.photo, anchor='nw')
        self.canvas.itemconfig(self.imageOnCanvas, image=self.photo) # change the displayed picture
        self.canvas.pack()
        
    def create_canvas_products(self):
        self.create_imgs_products_pos()
        self.canvas.create_image(0, 0, image=self.list_photos[0], anchor='nw')
        self.canvas.itemconfig(self.imageOnCanvas, image=self.list_photos[0]) # change the displayed picture
        self.cnt=1        

    def create_imgs_products_pos(self):
        rel_pod_w, rel_pod_h, rel_posX, rel_posY = 0.3, 0.3, 0.5, 0.1
        wp, hp = int(rel_pod_w*self.w),int(rel_pod_h*self.h)
        cv_img = cv2.resize(self.background,(self.w,self.h))
        self.list_photos = []
        for i in range(0,len(self.products)):            
            producto = cv2.resize(self.products[i],(wp,hp))
            x1, y1 = int(rel_posX*(self.w-wp)),int(rel_posY*(self.h-hp))                    
            cv_img[y1:y1+hp,x1:x1+wp:]=producto[0:hp,0:wp,:]            
            self.photo = ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img), master=self.window)
            self.list_photos.append(self.photo)

    def create_buttons(self):
        self.buttonBG = self.canvas.create_rectangle(self.w-int(np.floor(self.w/5.5)), self.h-int(np.floor(self.h/8)), self.w-int(np.floor(self.w/5.5))+200, self.h-int(np.floor(self.h/8))+50, fill="grey50", outline="grey90")
        self.buttonTXT = self.canvas.create_text(self.w-int(np.floor(self.w/5.5))+100, self.h-int(np.floor(self.h/8))+25 ,font=("Purisa", 16),text="Continuar")
    
    def delete_buttons(self):
        self.canvas.delete(self.buttonTXT)  
        self.canvas.delete(self.buttonBG) 
            
    def create_buttons_instructions(self):
        self.create_buttons()
        self.canvas.tag_bind(self.buttonBG, "<Button-1>", self.clicked_comenzar_button2) 
        self.canvas.tag_bind(self.buttonTXT, "<Button-1>", self.clicked_comenzar_button2)

    def create_buttons_instructions2(self):
        self.create_buttons()
        self.canvas.tag_bind(self.buttonBG, "<Button-1>", self.clicked_comenzar_button2) 
        self.canvas.tag_bind(self.buttonTXT, "<Button-1>", self.clicked_comenzar_button2)

    def create_buttons_instructions3(self):
        self.create_buttons()
        self.canvas.tag_bind(self.buttonBG, "<Button-1>", self.clicked_comenzar_button3) 
        self.canvas.tag_bind(self.buttonTXT, "<Button-1>", self.clicked_comenzar_button3)
        
    def create_buttons_instructions4(self):
        self.create_buttons()
        self.canvas.tag_bind(self.buttonBG, "<Button-1>", self.clicked_comenzar_button4) 
        self.canvas.tag_bind(self.buttonTXT, "<Button-1>", self.clicked_comenzar_button4)
    
    def create_buttons_instructions5(self):
        self.create_buttons()
        self.canvas.tag_bind(self.buttonBG, "<Button-1>", self.clicked_comenzar_button5) 
        self.canvas.tag_bind(self.buttonTXT, "<Button-1>", self.clicked_comenzar_button5)

    def create_buttons_instructions6(self):
        self.create_buttons()
        self.canvas.tag_bind(self.buttonBG, "<Button-1>", self.clicked_comenzar_button6) 
        self.canvas.tag_bind(self.buttonTXT, "<Button-1>", self.clicked_comenzar_button6)

    def create_buttons_instructions7(self):
        self.create_buttons()
        self.canvas.tag_bind(self.buttonBG, "<Button-1>", self.clicked_comenzar_button7) 
        self.canvas.tag_bind(self.buttonTXT, "<Button-1>", self.clicked_comenzar_button7)

    def create_buttons_instructions8(self):
        self.create_buttons()
        self.canvas.tag_bind(self.buttonBG, "<Button-1>", self.clicked_comenzar_button8) 
        self.canvas.tag_bind(self.buttonTXT, "<Button-1>", self.clicked_comenzar_button8)

    def wait_here(self, time):
        var = tkinter.IntVar()
        self.window.after(time, var.set, 1)
        self.window.wait_variable(var)

    def callback():
        print(time.time())

def setup_eyelink(subject_name="test"):
    """ 
    Setup eye link
    """
    #Starts Eyelink    
    tracker = EyeLink()
    #Opens the EDF file.
    edfFileName = f"{subject_name}.EDF"
    getEYELINK().openDataFile(edfFileName)	
    #Here is the starting point of the experiment Initializes the graphics INSERT THIRD PARTY GRAPHICS INITIALIZATION HERE IF APPLICABLE 
    print("pase_1")
    openGraphics((SCREENWIDTH, SCREENHEIGHT),32)
    print("pase_1/2")
    #flush all key presses and set tracker mode to offline.
    flushGetkeyQueue() 
    getEYELINK().setOfflineMode()						  
    #Sets the display coordinate system and sends mesage to that effect to EDF file;
    getEYELINK().sendCommand("screen_pixel_coords =  0 0 %d %d" %(SCREENWIDTH - 1, SCREENHEIGHT - 1))
    getEYELINK().sendMessage("DISPLAY_COORDS  0 0 %d %d" %(SCREENWIDTH - 1, SCREENHEIGHT - 1))
    tracker_software_ver = 0
    eyelink_ver = getEYELINK().getTrackerVersion()
    if eyelink_ver == 3:
        tvstr = getEYELINK().getTrackerVersionString()
        vindex = tvstr.find("EYELINK CL")
        tracker_software_ver = int(float(tvstr[(vindex + len("EYELINK CL")):].strip()))
    if eyelink_ver >= 2:
        getEYELINK().sendCommand("select_parser_configuration 0")
        if eyelink_ver == 2: #turn off scenelink camera stuff
            getEYELINK().sendCommand("scene_camera_gazemap = NO")
    else:
        getEYELINK().sendCommand("saccade_velocity_threshold = 35")
        getEYELINK().sendCommand("saccade_acceleration_threshold = 9500") 
    # set EDF file contents 
    getEYELINK().sendCommand("file_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT")
    if tracker_software_ver >= 4:
        getEYELINK().sendCommand("file_sample_data  = LEFT,RIGHT,GAZE,AREA,GAZERES,STATUS,HTARGET,INPUT")
    else:
        getEYELINK().sendCommand("file_sample_data  = LEFT,RIGHT,GAZE,AREA,GAZERES,STATUS,INPUT")
    # set link data (used for gaze cursor) 
    getEYELINK().sendCommand("link_event_filter = LEFT,RIGHT,FIXATION,FIXUPDATE,SACCADE,BLINK,BUTTON,INPUT")
    if tracker_software_ver >= 4:
        getEYELINK().sendCommand("link_sample_data  = LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS,HTARGET,INPUT")
    else:
        getEYELINK().sendCommand("link_sample_data  = LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS,INPUT")
    #Do EYELINK calibration at begging of block
    getEYELINK().doTrackerSetup()

if __name__=='__main__':
    args = parser.parse_args()
    # Setup eyelink
    if not args.no_eye_tracker:
        setup_eyelink(subject_name=args.subject_name)
    # Create interface2
    if args.subject_name:
        itf2 = interface2(subject_name=args.subject_name, screenwidth=args.w, screenheight=args.h)
    else:    
        itf2 = interface2(screenwidth=args.w, screenheight=args.h)
    # Get samples 
    _, sample_full_random, screen_order, item_order = create_trials(args.samples_per_difficulty, args.subject_name)
    itf3 = draw(sample_full_random, screen_order, item_order, 
        samples_per_difficulty=args.samples_per_difficulty, 
        subject_name=args.subject_name, 
        no_eye_tracker=args.no_eye_tracker,
        screenwidth=args.w, 
        screenheight=args.h
    )
    # Run blocks
    for i_block in range(3):
        print("Bloque:", i_block)
        if not args.no_eye_tracker:
            #test calibrations
            setCalibrationColors( (0, 0, 0),(255, 255, 255))  	#Sets the calibration target and background color
            setTargetSize(SCREENWIDTH//70, SCREENWIDTH//300)     #select best size for calibration target
            setCalibrationSounds("", "", "")
            setDriftCorrectSounds("", "off", "off")     
            #Do EYELINK calibration at begging of block
            if i_block > 0:
                #test calibrations 2
                getEYELINK().doTrackerSetup()
        for i_trial in range(args.samples_per_difficulty):
            # record eye tracker
            if not args.no_eye_tracker:
                nSData, sData, button = None, None, 0
                #This supplies the title of the current trial at the bottom of the eyetracker display
                message = "record_status_message 'Comparacion #:, %d/%d '" % (i_trial + 1, NTRIALS)
                getEYELINK().sendCommand(message)
                #Always send a TRIALID message before starting to record. EyeLink Data Viewer defines the start of a trial by the TRIALID message. This message is different than the start of recording message START that is logged when the trial recording begins. 
                #The Data viewer will not parse any messages, events, or samples, that exist in the data file prior to this message.
                getEYELINK().sendMessage(f"TRIALID {i_trial}")
                getEYELINK().sendMessage(f"!V TRIAL_VAR_DATA {i_trial}")
                #switch tracker to ide and give it time to complete mode switch
                getEYELINK().setOfflineMode()
                msecDelay(50) 
                #start recording samples and events to edf file and over the link. 
                error = getEYELINK().startRecording(1, 1, 1, 1)
                if error:	
                    print(error)
                #disable python garbage collection to avoid delays
                gc.disable()
                #begin the realtime mode
                beginRealTimeMode(100)
                eye_used = getEYELINK().eyeAvailable() #determine which eye(s) are available 
                if eye_used == RIGHT_EYE:
                    getEYELINK().sendMessage("EYE_USED 1 RIGHT")
                elif eye_used == LEFT_EYE or eye_used == BINOCULAR:
                    getEYELINK().sendMessage("EYE_USED 0 LEFT")
                    eye_used = LEFT_EYE
                else:
                    print ("Error in getting the eye information!")
                    print(TRIAL_ERROR)
                #reset keys and buttons on tracker
                getEYELINK().flushKeybuttons(0)
            # Run trial
            itf3.run(i_block=i_block, i_trial=i_trial)
            # update eye tracker
            if not args.no_eye_tracker:
                nSData = getEYELINK().getNewestSample() # check for new sample update
                # Do we have a sample in the sample buffer? and does it differ from the one we've seen before?
                if(nSData != None and (sData == None or nSData.getTime() != sData.getTime())):
                    # it is a new sample, let's mark it for future comparisons.
                    sData = nSData 
                    # Detect if the new sample has data for the eye currently being tracked, 
                    if eye_used == RIGHT_EYE and sData.isRightSample():
                        sample = sData.getRightEye().getGaze()
                        #INSERT OWN CODE (EX: GAZE-CONTINGENT GRAPHICS NEED TO BE UPDATED)
                    elif eye_used != RIGHT_EYE and sData.isLeftSample():
                        sample = sData.getLeftEye().getGaze()
                    #END real time mode of EYELINK
                    endRealTimeMode()
                    #re-enable python garbage collection to do memory cleanup at the end of trial
                    gc.enable()
    if not args.no_eye_tracker:
        if i_block == 2:
            #END OF ALL BLOCKS  
            #Close the file and transfer it to Display PC
            getEYELINK().setOfflineMode()						  
            msecDelay(500) 
            getEYELINK().closeDataFile()
            getEYELINK().receiveDataFile(edfFileName, edfFileName)
            getEYELINK().close()

