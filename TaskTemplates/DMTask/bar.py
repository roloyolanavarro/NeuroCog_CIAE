import os
import tkinter as tk
import random,csv
import numpy as np
import pandas as pd
from interface2 import interface2

class bar():    
    value=0
    def __init__(self, window, cv, imageOnCanvas, photo, list_p, w, h, list_photos, cnt, img_names, subject_name):
        self.photo=photo
        self.imageOnCanvas=imageOnCanvas
        self.w,self.h=w,h
        self.list_photos = list_photos
        self.cnt=cnt
        self.list = list_p
        self.cv=cv
        self.window=window
        self.x1, self.y1, self.x2, self.y2=int(w/10),int(8*h/10),int(9*w/10)+30,int(8*h/10)+15
        self.img_names = img_names
        self.subject_name = subject_name

        cv.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="#ff8c00", tag='rectangle')
        cv.create_rectangle(self.x1, self.y1-15, self.x1+15, self.y2+15, fill="#ff8c00", tag='rectangle')
        cv.create_rectangle(self.x2, self.y1-15, self.x2-15, self.y2+15, fill="#ff8c00", tag='rectangle')
        cv.create_rectangle(int(self.x1+(self.x2-self.x1)/2)-7, self.y1-15, int(self.x1+(self.x2-self.x1)/2)+7, self.y2+15, fill="#ff8c00", tag='rectangle')
        cv.create_text(self.x1,self.y2+45,fill="black",font="Times 30",text="-10")
        cv.create_text(int(self.x1+(self.x2-self.x1)/2),self.y2+45,fill="black",font="Times 30",text="0")
        cv.create_text(self.x2,self.y2+45,fill="black",font="Times 30",text="10")     
        
        pos_mouse_random = int(random.randrange(self.x1, self.x2))
        self.circle = 0
        self.window.bind("<Motion>", self.motion)
        self.window.event_generate('<Motion>', warp=True, x=pos_mouse_random, y=self.y1)#int((self.x2-self.x1)/2)
        cv.tag_bind('rectangle', '<Button-1>', self.showxy)
        
    def motion(self,event):
        x, y = event.x + 3, event.y + 7  
        self.cv.delete(self.circle)    
        radius = 20     
        x_max = x + radius
        x_min = x - radius
        y_max = y + radius
        y_min = y - radius
        self.circle = self.cv.create_oval(x_max, y_max, x_min, y_min, outline="black")

    def showxy(self, event):
        if(len(self.list_photos) > self.cnt):
            self.cv.create_image(0, 0, image=self.list_photos[self.cnt], anchor='nw')
            self.cv.itemconfig(self.imageOnCanvas, image=self.list_photos[self.cnt])
            self.cv.pack()
            self.draw_oval(event)
            print("imagen", len(self.list_photos), "de", self.cnt)
        else:
            self.value = round(-10+(((event.x - self.x1)/(self.x2-self.x1))*20), 2)
            self.list.append(self.value)        
            if not os.path.exists(f'./results/{self.subject_name}'):
                os.makedirs(f'./results/{self.subject_name}')
            pref_idxs = pd.DataFrame([self.img_names, self.list]).T
            pref = pd.DataFrame(self.list)
            if len(pref) > len(self.img_names):
                pref_idxs = pref_idxs.iloc[:len(self.img_names)]
                pref = pref.iloc[:len(self.img_names)]
            pref_idxs.to_csv(f"./results/{self.subject_name}/preferences_index.csv", header=False)
            pref.to_csv(f"./results/{self.subject_name}/preferences.csv", index=False, header=False)
            print("preferences.csv guardado con exito")
            self.window.quit()
        
    def draw_oval(self,event):
        self.cv.create_oval(event.x-7,  self.y1, event.x+7,  self.y1+15, fill="#000000")
        self.value=round(-10+(((event.x- self.x1)/(self.x2-self.x1))*20),2)
        self.list.append(self.value)  
        self.wait_here(50)
        self.cnt += 1
        self.__init__(self.window, self.cv, self.imageOnCanvas, self.photo, self.list, self.w, self.h, self.list_photos, self.cnt, self.img_names, self.subject_name)
        
    def wait_here(self,time):
        var = tk.IntVar()
        self.window.after(time, var.set, 1)
        self.window.wait_variable(var)
        
        
if __name__=='__main__':
    bar()
#



    
    