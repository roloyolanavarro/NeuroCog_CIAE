# importing the relevant libraries
#-*- coding: utf-8 -*-
import logging
import random
import threading
import constants
import time
import queue
import glob
import csv
import pygame
import pylink
from tkinter import *
from psychopy import parallel

from tkinter.simpledialog import askstring
from pygaze.libtime import clock
from PIL import Image , ImageChops
from pygaze import libscreen
from pygaze import libtime
from pygaze import liblog
from pygaze import libinput
from pygaze import eyetracker
from config_helper import read_config
from saccade_predictor import predict_saccade_position, predict_saccade_occurrence

Image.MAX_IMAGE_PIXELS = None
stop_detector = False
global_start_pos = None
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BEHAVIOURAL = False


def show_screen2(disp, screen, tracker, log_message, time_status, duration, code):
    if log_message is not None:
        tracker.log(log_message)
        parallel.setPin(3, 1)

    if time_status:
        start_time = libtime.get_time()
        while libtime.get_time() <= start_time + duration:
            disp.fill(screen=screen)
            disp.show()
    else:
        disp.fill(screen=screen)
        disp.show()
    parallel.setPin(3, 0)


def synch_stimuli(disp, tracker,pixels_distance):
    positions = [(960, 140),
                 (960, 940),
                 (560, 540),
                 (1360, 540)]
    fix_start= libscreen.Screen()
    fix_start.draw_fixation(fixtype='cross', pw=3, diameter=24)
    fixation_time_1 = 2000
    stimulus_time = 2000
    
    for i, position in enumerate(positions):
        stimuli_screen = libscreen.Screen()
        stimuli_screen.draw_circle(colour=BLACK, pos=position, r=24, pw=3, fill=True)

        # EEG signals
        fix_start.draw_rect(colour=(255, 255, 255),
                             w=25, h=25, x=1895, y=1055, pw=500, fill=True)
        stimuli_screen.draw_rect(colour=(0, 0, 0),
                             w=25, h=25, x=1895, y=1055, pw=500, fill=True)			     
        ## Show stimuli

        # Show fixation
        show_screen2(disp, fix_start, tracker, 'test_fix_start_' + str(i), time_status=True,
                    duration=fixation_time_1, code=1)

        # Show stimuli
        show_screen2(disp, stimuli_screen, tracker, 'test_circle_' + str(i), time_status=True,
                    duration=stimulus_time, code=2)



def experiment_setup(cfg):
    # Parallel port
    parallel.setPortAddress(0x0378)
    parallel.setData(0)
    
    # Ask participant name
    application_window = Tk()
    participant = askstring("Input", "Participant name",
                            parent=application_window)
    application_window.destroy()
    #constants.BGC = (0,0,0,255)
    # Start timing
    libtime.expstart()

    # Create display object
    disp = libscreen.Display(disptype=cfg['disptype'])

    # Create eyetracker object
    tracker = eyetracker.EyeTracker(disp, data_file=participant + '.edf', eventdetection='pygaze')
    
    # Create keyboard object
    keyboard = libinput.Keyboard(timeout=None)

    # Create logfile object
    log = liblog.Logfile(filename= ".//results//" + participant)
    log.write(["trialnr", "start_pos", "prediction_pos", "prediction_status", "prediction_time"])

    # Create screens (instructions, stimuli, fixation)
    instructions_screens, instructions_images = read_images_folder(images_folder=cfg['instructions_folder'],
                                              images_regex=cfg['instructions_regex'])
    stimuli_screens, stimuli_images = read_images_folder(images_folder=cfg['stimuli_folder'],
                                         images_regex=cfg['stimuli_regex'])
    fix_screen = libscreen.Screen()
    fix_screen.draw_fixation(fixtype='cross', pw=3)

    return disp, tracker, keyboard, log, instructions_screens, stimuli_screens, fix_screen, stimuli_images, participant


def read_images_folder(images_folder, images_regex):
    screens = []
    files = glob.glob(images_folder + images_regex)
    print(files)
    random.shuffle(files)
    for i, image_file in enumerate(files):
        screens.append(libscreen.Screen())
        screens[i].set_background_colour((0, 0, 0))
        screens[i].draw_image(image=image_file)
    return screens, files


def read_stimuli_images(config_file='config.yml'):
    print('read stimuli images')


def show_instructions(instructions_screens, disp, keyboard):
    for instructions_screen in instructions_screens:
        instructions_screen.draw_text(text=u'A continuación comenzará la presentación \n de las imágenes. \n Por favor explóralas libremente.', fontsize=50, colour=(0, 0, 0))
        disp.fill(instructions_screen)
        disp.show()
        keyboard.get_key()


def free_visual_exp_run(cfg):
    # Experiment setup
    disp, tracker, keyboard, log, instructions_screens, stimuli_screens, fix_screen, stimuli_images, participant = experiment_setup(cfg=cfg)
    print('TRACKER0')
    print(tracker.eventdetection)
    # Calibrate eye tracker
    tracker.calibrate()
    
    degree_weigh = 72.0 / 57.0
    in_screen_cms = degree_weigh * 6
    pixels_distance = in_screen_cms * 32.28
    
    # Synch test
    synch_stimuli(disp, tracker, pixels_distance)
    
     # Show instructions
    show_instructions(instructions_screens=instructions_screens, disp=disp, keyboard=keyboard)

    # Saccade stats
    gabor_image_tuples = []
    gabor_options = cfg['gabor_options']
    for gabor_index, gabor_option in enumerate(gabor_options):
        gabor_image_tuples.append((Image.open(gabor_option), gabor_index))
    saccade_stats = {'total_saccades_by_trial': [],
                     'used_saccades_by_trial': [],
                     'lost_saccades_by_trial': []}
    likert0_screen = libscreen.Screen()
    likert0_screen.draw_text(u'Presione 1 si percibió un cambio, \n presione 2 si no percibió un cambio', fontsize=40)
    likert1_screen = libscreen.Screen()
    likert1_screen.draw_image(image='likert_1.png')
    likert3_screen = libscreen.Screen()
    likert3_screen.draw_image(image='likert_3.png')
    
    likert2_screens = [libscreen.Screen(), libscreen.Screen(), libscreen.Screen()]
    for screen_index, screen in enumerate(likert2_screens):
        screen.draw_image(image='likert_2_' + str(screen_index) + '.png')
    likert_stats_1 = ''
    likert_stats_2 = ''
    sampling_times = [ 25 for i in range(65)]#[ (i % 4)*5 + 25 for i in range(68)] #[ (i % 5)*5 + 15 for i in range(65)] #[ (i % 4 + 1)*10 + 10 for i in range(68)] #[100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100] #[12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
    random.shuffle(sampling_times)
    print('start recording')
    tracker.start_recording()
    # Start experiment loop
    tracker.log('Start experiment_clock_time_{}'.format(libtime.get_time()))
    tracker.log('Start experiment')
    tracker.status_msg("Start_experiment")
    gabor_image = None
    rest_screen = libscreen.Screen()
    rest_screen.draw_text(text='Descanso', fontsize=50)
    end_screen = libscreen.Screen()
    end_screen.draw_text(text=u'Fin del experimento. \n Gracias por participar :)', fontsize=50)

    with open(cfg['results_folder'] + participant + '.csv', 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['sampling_time', 'likert_1', 'likert_2', 'likert_3', 'used_saccades', 'total_saccades', 'stimulus_screen', 'likert_0'], delimiter=';')
        writer.writeheader()
        total_trials = len(stimuli_screens)
        print(str(total_trials))
        #disp.close()

        for trial_index, stimulus_screen in enumerate(stimuli_screens):
            
            # REST
            if trial_index == total_trials/2:
                show_screen(disp=disp, screen=rest_screen, tracker=tracker, log_message='rest_show')
                keyboard.get_key()
                tracker.stop_recording()
                tracker.calibrate()
                # Show instructions
                show_instructions(instructions_screens=instructions_screens, disp=disp, keyboard=keyboard)
                tracker.start_recording()

            #if trial_index == 4: # comentar en caso de experimento real
            #    break		 #######################################
            
            # Background black
            stimulus_screen.set_background_colour((0,0,0,255))

            # Choose random sampling time 
            sampling_time = sampling_times[0] #.pop()

            # Present fixation
            fix_screen.draw_rect(colour=WHITE,
                             w=25, h=25, x=1895, y=1055, pw=500, fill=True)
            show_screen(disp=disp, screen=fix_screen, tracker=tracker, log_message='fixation')
            libtime.pause(random.randint(1000, 1500))

            # Signals for eyetracker, log and eeg
            tracker.status_msg("Trial %d" % trial_index)
            tracker.log("Start_trial_{}_stimulus_screen".format(trial_index, stimulus_screen))

            # Present stimulus
            stimulus_screen.draw_rect(colour=BLACK,
                             w=25, h=25, x=1895, y=1055, pw=500, fill=True)
            show_screen(disp=disp, screen=stimulus_screen, tracker=tracker, log_message='stimulus_show')

            # Stimulus loop
            stimulus_loop(trial_index=trial_index,disp=disp, screen=stimulus_screen, tracker=tracker,
                          end_condition=True, cfg=cfg, image_file=stimuli_images[trial_index], keyboard=keyboard, 
                          log=log, saccade_stats=saccade_stats, sampling_time=sampling_time, gabor_image_tuples=gabor_image_tuples)

            likert_stats_0 = None
            likert_stats_1 = None
            likert_stats_2 = None
            likert_stats_3 = None
            #show_screen(disp=disp, screen=likert0_screen, tracker=tracker, log_message='likert0_show')
            #while True:
                #key, presstime = keyboard.get_key(keylist=['[1]', '[2]'], timeout=1)
                #if key is not None:
                    #print('key')
                    #print(key)
                    #likert_stats_0 = key
                    #break
                #show_screen(disp=disp, screen=likert0_screen, tracker=tracker, log_message=None)
            #if likert_stats_0 == '[1]':
                #if trial_index >= total_trials/2:
                    #likert_stats_3 = None
                    #show_screen(disp=disp, screen=likert1_screen, tracker=tracker, log_message='likert1_show')
                    #while True:
                        #key, presstime = keyboard.get_key(keylist=['[1]', '[2]', '[3]'], timeout=1)
                        #if key is not None:
                            #print('key')
                            #print(key)
                            #likert_stats_1 = key
                            #break
                        #show_screen(disp=disp, screen=likert1_screen, tracker=tracker, log_message=None)


                    #if likert_stats_1 == '[1]':
                        #likert2_screen = likert2_screens[0]
                    #elif likert_stats_1 == '[2]':
                        #likert2_screen = likert2_screens[1]
                    #elif likert_stats_1 == '[3]':
                        #likert2_screen = likert2_screens[2]
                    #show_screen(disp=disp, screen=likert2_screen, tracker=tracker, log_message='likert2_' + likert_stats_1 +'_show')

                    #while True:
                        #key, presstime = keyboard.get_key(keylist=['[1]', '[2]', '[3]', '[4]'], timeout=1)
                        #if key is not None:
                            #likert_stats_2 = key
                            #break
                        #show_screen(disp=disp, screen=likert2_screen, tracker=tracker, log_message=None)
                #else:
                    #likert_stats_1 = None
                    #likert_stats_2 = None
                    #show_screen(disp=disp, screen=likert3_screen, tracker=tracker, log_message='likert3_show')
                    #while True:
                        #key, presstime = keyboard.get_key(keylist=['[1]', '[2]', '[3]', '[4]', '[5]'], timeout=1)
                        #if key is not None:
                            #print('key')
                            #print(key)
                            #likert_stats_3 = key
                            #break
                        #show_screen(disp=disp, screen=likert3_screen, tracker=tracker, log_message=None)
            #else:
                #likert_stats_1 = None
                #likert_stats_2 = None
                #likert_stats_3 = None
            # TODO: REGEX NUMBER
            writer.writerow({
                'sampling_time': sampling_time,
                'likert_1': likert_stats_1,
                'likert_2': likert_stats_2,
                'likert_3': likert_stats_3,
                'used_saccades': saccade_stats['used_saccades_by_trial'][trial_index],
                'total_saccades': saccade_stats['total_saccades_by_trial'][trial_index],
                'stimulus_screen': stimuli_images[trial_index],
                'likert_0': likert_stats_0})

    # Synch test
    synch_stimuli(disp, tracker, pixels_distance)
    
    # End experiment
    show_screen(disp=disp, screen=end_screen, tracker=tracker, log_message='end_show')

    print('Saccade stats')
    print(saccade_stats)
    print('Likert stats')
    log.close()
    tracker.stop_recording()
    tracker.close()
    disp.close()
    libtime.expend()

 
def thread_function(name, q, tracker, trial_index, num_saccade):
    global stop_detector
    #endtime, startpos, endpos = tracker.wait_for_event(pylink.ENDSACC)
    #q.put(True)
    #tracker.log('start_pos_{}_end_pos_{}_time_{}_trial_{}_saccade_{}'.format(startpos,endpos, endtime,trial_index, num_saccade))
    #stop_detector = True
    while not stop_detector:
        #print('sd')
        d = pylink.getEYELINK().getNextData()
       # float_data = pylink.getEYELINK().getFloatData()
        #print('eyelink data')
       # tracker.log('Sac_info_{}'.format(float_data))
        #print(d)
        if d == pylink.ENDSACC: # creo que asi se llama el evento
            #q.put(True)
            #print('LOST_SACCADE_{}_{}'.format(trial_index, num_saccade))
            tracker.log('LOST_SACCADE_{}_{}_time_{}'.format(trial_index, num_saccade, libtime.get_time()))
            #print('pylink works')
            break
    tracker.log('END_THREAD_{}_{}'.format(trial_index, num_saccade))


def draw_gabor_outside_image(img, gabor_image_tuples, screen):
    gabor_image_tuple = random.choice(gabor_image_tuples)
    gabor_image = gabor_image_tuple[0]
    gabor_width, gabor_height = gabor_image.size
    center_patch_offset = gabor_width / 2
    #https: // code - maven.com / crop - images - using - python - pil - pillow
    area = (0, 0, 200, 200)

    # Coords in this image arent the same as in the stimulus
    cropped_img = img.crop(area)
    # TODO: CAMBIAR ESE CONVERT
    gabor_draw = ImageChops.multiply(cropped_img, gabor_image.convert('RGB'))

    # TODO: TEST THIS CODE
    mode = gabor_draw.mode
    size = gabor_draw.size
    data = gabor_draw.tobytes()
    gabor_draw_pygame = pygame.image.fromstring(data, size, mode)

    #gabor_draw.save('crop_gabor.png')
    #gabor_draw_pygame = pygame.image.load("crop_gabor.png")

    screen.screen.blit(gabor_draw_pygame, (50, 50))


def stimulus_loop(trial_index, disp, screen, tracker, end_condition, cfg, image_file, keyboard, log, saccade_stats, sampling_time, gabor_image_tuples):
    global stop_detector

    # Saccade stats index update
    saccade_stats['used_saccades_by_trial'].append(0)
    saccade_stats['lost_saccades_by_trial'].append(0)
    saccade_stats['total_saccades_by_trial'].append(0)

    # Probability of using a saccade as experimental trial, change image
    saccades_predicted = 0
    dispsize = constants.DISPSIZE 
    x_offset = dispsize[0]
    img = Image.open(image_file)
    width, height = img.size
    y_offset = dispsize[1] 
    tracker.log('NEW_STIMULUS')
    experimental_saccade_probability = cfg['experimental_saccade_probability']
    experimental_condition = cfg['experimental_condition']
    patch_size = cfg['patch_size']
    show_blink = False
    grey_scales = cfg['grey_scale']
    end_saccade_detector = None
    q = queue.Queue()
    start_time = libtime.get_time()
    #print('Start_time_{}_trial_{}_sampling_'.format(start_time, trial_index))
    draw_gabor_outside_image(img, gabor_image_tuples, screen)
    tracker.log('Start_time_{}_trial_{}_sampling_time_{}_image_{}'.format(start_time, trial_index, sampling_time, image_file))
    while end_condition:
        #q = queue.Queue()
        show_screen(disp, screen, tracker, 'loop')
        drawn = False
        lost = False
        stop_detector = False

        # Saccade detector and end of saccade detector runs parallel
        if saccades_predicted < 1:
            random_saccade = random.random()
            #end_saccade_detector = threading.Thread(target=thread_function, args=(1, q, tracker, trial_index, saccade_stats['total_saccades_by_trial'][trial_index]))
            if experimental_condition == 'patches':
                end_saccade_prediction, end_sampling_time, start_position = predict_saccade_position(tracker=tracker,
                                                                  distance_from_screen_in_cm=cfg['distance_from_screen_in_cm'],
                                                                  one_degree_cm_to_screen_equivalence=cfg['one_degree_cm_to_screen_equivalence'],
                                                                  one_cm_to_pixels=cfg['one_cm_to_pixels'],
                                                                  sampling_time=sampling_time,
                                                                  saccade_range=cfg['saccade_range'],
                                                                  end_saccade_detector=end_saccade_detector)
                tracker.log('time from start_{}'.format(libtime.get_time() - start_time))                                                  
                tracker.log('SACCADE_COUNT_{}_Prediction_{}'.format(saccade_stats['total_saccades_by_trial'][trial_index], end_saccade_prediction))
                saccade_stats['total_saccades_by_trial'][trial_index] += 1
            #elif experimental_condition == 'complete_screen':
               # t, start_position = predict_saccade_occurrence(tracker=tracker, end_saccade_detector=end_saccade_detector)
               # end_saccade_prediction = start_position


            if end_saccade_prediction is not None and random_saccade <= experimental_saccade_probability:
                if q.empty():
                    if experimental_condition == 'patches':
                        gabor_image_tuple = random.choice(gabor_image_tuples)
                        gabor_image = gabor_image_tuple[0]
                        gabor_width, gabor_height = gabor_image.size
                        center_patch_offset = gabor_width / 2
                        #https: // code - maven.com / crop - images - using - python - pil - pillow
                        area = (end_saccade_prediction[0] - (x_offset - width)/2 - center_patch_offset,
                                end_saccade_prediction[1] - (y_offset - height)/2 - center_patch_offset,
                                end_saccade_prediction[0] + patch_size - (x_offset - width)/2 - center_patch_offset,
                                end_saccade_prediction[1] + patch_size - (y_offset - height)/2 - center_patch_offset)
                        #print(area)
                        #sys.exit()
                        # Coords in this image arent the same as in the stimulus
                        cropped_img = img.crop(area)
                        # TODO: CAMBIAR ESE CONVERT
                        gabor_draw = ImageChops.multiply(cropped_img, gabor_image.convert('RGB'))

                        # TODO: TEST THIS CODE
                        mode = gabor_draw.mode
                        size = gabor_draw.size
                        data = gabor_draw.tobytes()
                        gabor_draw_pygame = pygame.image.fromstring(data, size, mode)

                        #gabor_draw.save('crop_gabor.png')
                        #gabor_draw_pygame = pygame.image.load("crop_gabor.png")

                        screen.screen.blit(gabor_draw_pygame, (end_saccade_prediction[0] - center_patch_offset, end_saccade_prediction[1] - center_patch_offset))
                        screen.draw_rect(colour=WHITE,
                             w=25, h=25, x=1895, y=1055, pw=500, fill=True)
                        #screen.draw_circle(colour=(255, 0, 0), pos=(end_saccade_prediction[0], end_saccade_prediction[1]), r=20, pw=1, fill=True)

                        show_blink = True #True
                        drawn = True
                        disp.fill(screen)
                        disp.show()
                        end_draw_time = clock.get_time()
                        parallel.setPin(2, 1)
                        tracker.log('SACCADE_USED_COUNT_{}'.format((trial_index, saccade_stats['used_saccades_by_trial'][trial_index], gabor_image_tuple)))

                        tracker.log('Time_taken_from_end_sample_to_end_drawing_{}_trial_{}_saccade_{}'.format(end_draw_time-end_sampling_time, trial_index, saccade_stats['total_saccades_by_trial'][trial_index]-1))

                        #log.write(
                          #  [str(trial_index), str(start_position), str(end_saccade_prediction), "predicted",
                          #   str(libtime.get_time())])
                        tracker.log('SACCADE_PREDICTION_START_{}_END_{}'.format(str(start_position), str(end_saccade_prediction)))
                        saccade_stats['used_saccades_by_trial'][trial_index] += 1
                        saccades_predicted += 1
                        libtime.pause(200)
                        parallel.setPin(2, 0)
                        screen.draw_rect(colour=BLACK,
                             w=25, h=25, x=1895, y=1055, pw=500, fill=True)
                        disp.fill(screen)
                        disp.show()
                else:
                    # Dont draw gabor (end of saccade detected before starting to draw
                    tracker.log('NO_DIBUJADO_{}_{}'.format(trial_index ,saccade_stats['lost_saccades_by_trial'][trial_index]))
                    saccade_stats['lost_saccades_by_trial'][trial_index] += 1
                    #log.write([str(trial_index), str(start_position), str(end_saccade_prediction), "not_predicted",
                         #      str(libtime.get_time())])
                    show_blink = False
                    drawn = False

            else:
                tracker.log('SACCADE_NOT_USED_COUNT_{}'.format((trial_index, saccade_stats['used_saccades_by_trial'][trial_index])))

        # End stimulus
        loop_time = libtime.get_time()
        
        if loop_time - start_time >= 4000:
            end_condition = False
            
        # Abrupt ending
        key, presstime = keyboard.get_key(keylist=['q'], timeout=1)
        #print('key pressed: ' +str(key))
        if key is not None:
            print('*+++++++++++++++++++++++++++++++++++')
            log.close()
            tracker.close()
            disp.close()
            libtime.expend()
            break
            
        # End detector
        #if drawn:
           # end_saccade_detector.join()
        #tracker.log('STOPPED_DETECTOR_{}_{}'.format(trial_index ,saccade_stats['lost_saccades_by_trial'][trial_index]))
        #stop_detector = True
    tracker.log('TRIAL_END')
    libtime.pause(100)
    print('**********************************')


def eeg_signal(show_blink, screen, disp, tracker, grey_scale,
               width=20, height=20, x_pos=1900, y_pos=1060, eyetracker_message='Flash_pause_', repetitions=10,
               pause_time=10):
    if show_blink:
        show_blink = False
        tracker.log('Start_flash_pause')
        for i in range(0, repetitions):
            libtime.pause(pause_time)
            color_index = i % len(grey_scale)
            screen.draw_rect(colour=grey_scale[color_index],
                             x=x_pos, y=y_pos, pw=500, w=width, h=height, fill=True)
            disp.fill(screen)
            disp.show()
        tracker.log('End_flash_pause')
    return show_blink


def show_screen(disp, screen, tracker, log_message):
    disp.fill(screen=screen)
    disp.show()
    if log_message is not None:
        tracker.log(log_message)


def drift_correction(disp, fix_screen, tracker):
    checked = False
    while not checked:
        disp.fill(fix_screen)
        disp.show()
        checked = tracker.drift_correction()


if __name__ == '__main__':
    cfg_example = read_config(config_file='config.yml')
    free_visual_exp_run(cfg=cfg_example)
