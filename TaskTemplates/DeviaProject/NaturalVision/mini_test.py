# importing the relevant libraries
import logging
import random
import threading
import constants
import time
import queue
import glob
import pygame
import pylink
from pygaze import libscreen
from pygaze import libtime
from pygaze import liblog
from pygaze import libinput
from pygaze import eyetracker
from config_helper import read_config
from saccade_predictor import predict_saccade_position, predict_saccade_occurrence


stop_detector = False


def experiment_setup(cfg):

    # Start timing
    libtime.expstart()

    # Create display object
    disp = libscreen.Display(disptype=cfg['disptype'])

    # Create eyetracker object
    tracker = eyetracker.EyeTracker(disp)
    print(tracker)

    # Create keyboard object
    keyboard = libinput.Keyboard(keylist=cfg['keylist'], timeout=None)

    # Create logfile object
    log = liblog.Logfile()
    log.write(["trialnr", "endpos", "latency", "correct"])

    # Create screens (instructions, stimuli, fixation)
    instructions_screens, instructions_images = read_images_folder(images_folder=cfg['instructions_folder'],
                                              images_regex=cfg['instructions_regex'])
    stimuli_screens, stimuli_images = read_images_folder(images_folder=cfg['stimuli_folder'],
                                         images_regex=cfg['stimuli_regex'])
    fix_screen = libscreen.Screen()
    fix_screen.draw_fixation(fixtype='cross', pw=3)

    blue_screen = stimuli_screens[2]
    

    # Start eye tracking
    tracker.start_recording()

    return disp, tracker, keyboard, log, instructions_screens, stimuli_screens, fix_screen, blue_screen, stimuli_images


def read_images_folder(images_folder, images_regex):
    screens = []
    files = glob.glob(images_folder + images_regex)
    for i, image_file in enumerate(files):
        screens.append(libscreen.Screen())
        screens[i].draw_image(image=image_file)
    return screens, files







if __name__ == '__main__':
    cfg_example = read_config(config_file='config.yml')
    experiment_setup(cfg=cfg_example)
