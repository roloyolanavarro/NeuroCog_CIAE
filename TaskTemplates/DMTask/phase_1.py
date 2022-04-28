# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:15:57 2019

@author: screa
"""
from matplotlib import pyplot as plt
import os,cv2
import numpy as np
from PIL import Image

def process_image(img_path, width=800, height=600):
    #src = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    dst = cv2.imread(img_path)
    """
    bgr = src[:,:,:3] # Channels 0..2
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    alpha = src[:,:,3] # Channel 3

    #src = cv2.imread(img_path)
    #src = cv2.cvtColor(src, cv2.COLOR_BGR2BGRA)
    #imgobj = Image.open(img_path)
    #pixels = imgobj.convert('RGBA')
    #data = imgobj.getdata()
    #print(np.array(list(data)).shape)

    #bgr = src[:,:,:3] # Channels 0..2
    #gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

    #bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    #alpha = src[:,:,3] # Channel 3
    #dst = np.dstack([bgr, alpha])
    dst = np.dstack([bgr, alpha])
    dst = cv2.resize(src, (width,height))
    """
    return dst

class data_phase_1():
    """
    Carga imagenes de productos para calificar y las imagenes de la interfaz (botones, barras, etc)
    """
    
    def __init__(self):
        self.path_imgs_products='./imgs_products/'
        self.path_imgs_int='./imgs_int/'
        
    def load(self):
        products, img_names = self.load_img_products(self.path_imgs_products)
        background, confidence_rate_screen, eye_fixation, free_eye_movent, joystick_buttons,instructions1 = self.load_imgs_interface(self.path_imgs_int)
        return  background, confidence_rate_screen, eye_fixation, free_eye_movent, joystick_buttons, products, instructions1, img_names

    def load_img_products(self, path_imgs_products):  
        image_products = []      
        img_names = []    
        for filename in os.listdir(path_imgs_products): 
            im = process_image(path_imgs_products+filename, 800, 600)
            im = im[:,:,::-1]
            image_products.append(im)
            img_names.append(filename)
        print(str(len(image_products))+' items loaded...')
        return image_products, img_names
    
    #def load_imgs_interface(self,path_imgs_int, width=1920, height=1080):
    def load_imgs_interface(self, path_imgs_int, width=800, height=600):
        background = process_image(path_imgs_int+'fondogris.png', width, height)
        confidence_rate_screen = process_image(path_imgs_int+'confidence_rate_screen.png', width, height)
        eye_fixation = process_image(path_imgs_int+'fijacion.png', width, height)
        free_eye_movent = process_image(path_imgs_int+'pantallablanco.png', width, height)
        joystick_buttons = process_image(path_imgs_int+'joystick_buttons.png', width, height)
        instructions1 = process_image(path_imgs_int+'phase_1_question.png', width, height)
    
        return background, confidence_rate_screen, eye_fixation, free_eye_movent, joystick_buttons, instructions1
    

if __name__=='__main__':
    background, confidence_rate_screen, eye_fixation, free_eye_movent, joystick_buttons, products, instructions1 = data_phase_1().load()
    plt.imshow(products[0])


