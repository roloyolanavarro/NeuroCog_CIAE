#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on julio 05, 2022, at 20:46
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'DigitSpanTask_visual'  # from the Builder filename that created this script
expInfo = {'participante': '', 'sesion': '01', 'orden': ['AP','PA'], 'pasivas': ['RF','FR'], 'activas': ['RF','FR']}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participante'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\INU\\Documents\\GitHub\\NeuroCog_CIAE\\DigitSpanTask\\pasivas_activas_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "Bienvenida"
BienvenidaClock = core.Clock()
key_bienvenida = keyboard.Keyboard()
Bienvenida_img = visual.ImageStim(
    win=win,
    name='Bienvenida_img', 
    image='datasets/Bienvenida.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
if expInfo['activas']== 'RF':
    ordenactivas=('AR', 'AF')
else:
    ordenactivas=('AF', 'AR')

if expInfo['pasivas']== 'RF':
    ordenpasivas=('PR', 'PF')
else:
    ordenpasivas=('PF', 'PR')

if expInfo['orden']== 'AP': #activa primero
    lasfilas=[0,1]
else: # PA pasiva primero
    lasfilas=[1,2]

# Initialize components for Routine "Bienvenida2"
Bienvenida2Clock = core.Clock()
bienv2 = visual.TextStim(win=win, name='bienv2',
    text='Este experimento consta de 4 tareas cortas.\nEn cada tarea, verás una serie de números que debes recordar. \n\nA continuación, verás las instrucciones de la primera tarea.\n\n*Presiona la barra espaciadora para seguir*',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_bienv = keyboard.Keyboard()

# Initialize components for Routine "InstruccionesPasiva"
InstruccionesPasivaClock = core.Clock()
image2 = visual.ImageStim(
    win=win,
    name='image2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "firstfix_training"
firstfix_trainingClock = core.Clock()
drift_trainPR = visual.ImageStim(
    win=win,
    name='drift_trainPR', 
    image='datasets/drift.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
start_trainPR = sound.Sound('datasets/trial_init.wav', secs=0.5, stereo=True, hamming=True,
    name='start_trainPR')
start_trainPR.setVolume(1.0)
firstfixtrain = visual.TextStim(win=win, name='firstfixtrain',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "presentation_training"
presentation_trainingClock = core.Clock()
digitpresentation_training = visual.TextStim(win=win, name='digitpresentation_training',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "recall_training"
recall_trainingClock = core.Clock()
recall_train = visual.TextStim(win=win, name='recall_train',
    text='Respuesta:',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
answ_train = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.1,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='answ_train',
     autoLog=True,
)

# Initialize components for Routine "post_recall_train"
post_recall_trainClock = core.Clock()
post_recall_training = visual.TextStim(win=win, name='post_recall_training',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "start_trial"
start_trialClock = core.Clock()
end_training = visual.ImageStim(
    win=win,
    name='end_training', 
    image='datasets/finpractica.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "first_fixation"
first_fixationClock = core.Clock()
driftPR = visual.ImageStim(
    win=win,
    name='driftPR', 
    image='datasets/drift.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
startPR = sound.Sound('datasets/trial_init.wav', secs=0.5, stereo=True, hamming=True,
    name='startPR')
startPR.setVolume(1.0)
first_fix_pas = visual.TextStim(win=win, name='first_fix_pas',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Presentation_pas"
Presentation_pasClock = core.Clock()
pres_text = visual.TextStim(win=win, name='pres_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Recall_pasivas"
Recall_pasivasClock = core.Clock()
recall_txt = visual.TextStim(win=win, name='recall_txt',
    text='Respuesta:',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
answer_box = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.1,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='answer_box',
     autoLog=True,
)
#counters of correct answers
previous_count = 0 
current_count = 0

# Initialize components for Routine "post_recallPasiva"
post_recallPasivaClock = core.Clock()
postrecallPR = visual.TextStim(win=win, name='postrecallPR',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "LickertPasivas"
LickertPasivasClock = core.Clock()
Dificultad_pasivas = visual.TextStim(win=win, name='Dificultad_pasivas',
    text='¿Cuán difícil encontraste esta tarea, en general?',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
dif_licker = visual.Slider(win=win, name='dif_licker',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('muy fácil', 'fácil', 'neutro', 'difícil', 'muy difícil'), ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor=[1.0000, 1.0000, 1.0000], markerColor=[1.0000, 0.2941, -1.0000], lineColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# Initialize components for Routine "EndTask"
EndTaskClock = core.Clock()
siguiente_tarea = visual.TextStim(win=win, name='siguiente_tarea',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "Instr_Activas"
Instr_ActivasClock = core.Clock()
image2_2 = visual.ImageStim(
    win=win,
    name='image2_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "drift_press_activas"
drift_press_activasClock = core.Clock()
start_trainPR_2 = sound.Sound('datasets/trial_init.wav', secs=0.5, stereo=True, hamming=True,
    name='start_trainPR_2')
start_trainPR_2.setVolume(1.0)
drift_trainPR_2 = visual.ImageStim(
    win=win,
    name='drift_trainPR_2', 
    image='datasets/drift.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
firstfix_activas = visual.TextStim(win=win, name='firstfix_activas',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "ffix_trainactivas"
ffix_trainactivasClock = core.Clock()
firsfixtrain_activa = visual.TextStim(win=win, name='firsfixtrain_activa',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "present_train_activas"
present_train_activasClock = core.Clock()
digitpresentation_training_2 = visual.TextStim(win=win, name='digitpresentation_training_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "recall_train_activas"
recall_train_activasClock = core.Clock()
recall_train_2 = visual.TextStim(win=win, name='recall_train_2',
    text='Respuesta:',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
answ_train_2 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.1,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='answ_train_2',
     autoLog=True,
)

# Initialize components for Routine "post_recall_train_activas"
post_recall_train_activasClock = core.Clock()
post_recall_training_2 = visual.TextStim(win=win, name='post_recall_training_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "start_trialActivas"
start_trialActivasClock = core.Clock()
end_training_2 = visual.ImageStim(
    win=win,
    name='end_training_2', 
    image='datasets/finpractica.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "drift_press_activas"
drift_press_activasClock = core.Clock()
start_trainPR_2 = sound.Sound('datasets/trial_init.wav', secs=0.5, stereo=True, hamming=True,
    name='start_trainPR_2')
start_trainPR_2.setVolume(1.0)
drift_trainPR_2 = visual.ImageStim(
    win=win,
    name='drift_trainPR_2', 
    image='datasets/drift.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
firstfix_activas = visual.TextStim(win=win, name='firstfix_activas',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "first_fixActivas"
first_fixActivasClock = core.Clock()
first_fix_active = visual.TextStim(win=win, name='first_fix_active',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PresentationActivas"
PresentationActivasClock = core.Clock()
pres_text_active = visual.TextStim(win=win, name='pres_text_active',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "RecallActivas"
RecallActivasClock = core.Clock()
recall_txt_2 = visual.TextStim(win=win, name='recall_txt_2',
    text='Respuesta:',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
answer_box_2 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.1,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='answer_box_2',
     autoLog=True,
)

# Initialize components for Routine "post_recallActivas"
post_recallActivasClock = core.Clock()
postrecallPR_2 = visual.TextStim(win=win, name='postrecallPR_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "LickertActivas"
LickertActivasClock = core.Clock()
Dificultad_activas = visual.TextStim(win=win, name='Dificultad_activas',
    text='¿Cuán difícil encontraste esta tarea, en general?',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
dif_licker_2 = visual.Slider(win=win, name='dif_licker_2',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('muy fácil', 'fácil', 'neutro', 'difícil', 'muy difícil'), ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor=[1.0000, 1.0000, 1.0000], markerColor=[1.0000, 0.2941, -1.0000], lineColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# Initialize components for Routine "EndTask"
EndTaskClock = core.Clock()
siguiente_tarea = visual.TextStim(win=win, name='siguiente_tarea',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "Final"
FinalClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='¡Hemos terminado!\n\n¡Muchas gracias por tu participación!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Bienvenida"-------
continueRoutine = True
# update component parameters for each repeat
key_bienvenida.keys = []
key_bienvenida.rt = []
_key_bienvenida_allKeys = []
# keep track of which components have finished
BienvenidaComponents = [key_bienvenida, Bienvenida_img]
for thisComponent in BienvenidaComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BienvenidaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Bienvenida"-------
while continueRoutine:
    # get current time
    t = BienvenidaClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BienvenidaClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_bienvenida* updates
    if key_bienvenida.status == NOT_STARTED and t >= 0.25-frameTolerance:
        # keep track of start time/frame for later
        key_bienvenida.frameNStart = frameN  # exact frame index
        key_bienvenida.tStart = t  # local t and not account for scr refresh
        key_bienvenida.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_bienvenida, 'tStartRefresh')  # time at next scr refresh
        key_bienvenida.status = STARTED
        # keyboard checking is just starting
        key_bienvenida.clock.reset()  # now t=0
        key_bienvenida.clearEvents(eventType='keyboard')
    if key_bienvenida.status == STARTED:
        theseKeys = key_bienvenida.getKeys(keyList=['space'], waitRelease=False)
        _key_bienvenida_allKeys.extend(theseKeys)
        if len(_key_bienvenida_allKeys):
            key_bienvenida.keys = _key_bienvenida_allKeys[-1].name  # just the last key pressed
            key_bienvenida.rt = _key_bienvenida_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Bienvenida_img* updates
    if Bienvenida_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Bienvenida_img.frameNStart = frameN  # exact frame index
        Bienvenida_img.tStart = t  # local t and not account for scr refresh
        Bienvenida_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Bienvenida_img, 'tStartRefresh')  # time at next scr refresh
        Bienvenida_img.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BienvenidaComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Bienvenida"-------
for thisComponent in BienvenidaComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Bienvenida" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Bienvenida2"-------
continueRoutine = True
# update component parameters for each repeat
key_bienv.keys = []
key_bienv.rt = []
_key_bienv_allKeys = []
# keep track of which components have finished
Bienvenida2Components = [bienv2, key_bienv]
for thisComponent in Bienvenida2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Bienvenida2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Bienvenida2"-------
while continueRoutine:
    # get current time
    t = Bienvenida2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Bienvenida2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *bienv2* updates
    if bienv2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bienv2.frameNStart = frameN  # exact frame index
        bienv2.tStart = t  # local t and not account for scr refresh
        bienv2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bienv2, 'tStartRefresh')  # time at next scr refresh
        bienv2.setAutoDraw(True)
    
    # *key_bienv* updates
    waitOnFlip = False
    if key_bienv.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
        # keep track of start time/frame for later
        key_bienv.frameNStart = frameN  # exact frame index
        key_bienv.tStart = t  # local t and not account for scr refresh
        key_bienv.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_bienv, 'tStartRefresh')  # time at next scr refresh
        key_bienv.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_bienv.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_bienv.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_bienv.status == STARTED and not waitOnFlip:
        theseKeys = key_bienv.getKeys(keyList=['space'], waitRelease=False)
        _key_bienv_allKeys.extend(theseKeys)
        if len(_key_bienv_allKeys):
            key_bienv.keys = _key_bienv_allKeys[-1].name  # just the last key pressed
            key_bienv.rt = _key_bienv_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Bienvenida2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Bienvenida2"-------
for thisComponent in Bienvenida2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('bienv2.started', bienv2.tStartRefresh)
thisExp.addData('bienv2.stopped', bienv2.tStopRefresh)
# check responses
if key_bienv.keys in ['', [], None]:  # No response was made
    key_bienv.keys = None
thisExp.addData('key_bienv.keys',key_bienv.keys)
if key_bienv.keys != None:  # we had a response
    thisExp.addData('key_bienv.rt', key_bienv.rt)
thisExp.addData('key_bienv.started', key_bienv.tStartRefresh)
thisExp.addData('key_bienv.stopped', key_bienv.tStopRefresh)
thisExp.nextEntry()
# the Routine "Bienvenida2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Block_Order = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('datasets/task_order.xlsx', selection=lasfilas),
    seed=None, name='Block_Order')
thisExp.addLoop(Block_Order)  # add the loop to the experiment
thisBlock_Order = Block_Order.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_Order.rgb)
if thisBlock_Order != None:
    for paramName in thisBlock_Order:
        exec('{} = thisBlock_Order[paramName]'.format(paramName))

for thisBlock_Order in Block_Order:
    currentLoop = Block_Order
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_Order.rgb)
    if thisBlock_Order != None:
        for paramName in thisBlock_Order:
            exec('{} = thisBlock_Order[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    BlockPasivas = data.TrialHandler(nReps=nRepsBlockPasivas, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='BlockPasivas')
    thisExp.addLoop(BlockPasivas)  # add the loop to the experiment
    thisBlockPasiva = BlockPasivas.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockPasiva.rgb)
    if thisBlockPasiva != None:
        for paramName in thisBlockPasiva:
            exec('{} = thisBlockPasiva[paramName]'.format(paramName))
    
    for thisBlockPasiva in BlockPasivas:
        currentLoop = BlockPasivas
        # abbreviate parameter names if possible (e.g. rgb = thisBlockPasiva.rgb)
        if thisBlockPasiva != None:
            for paramName in thisBlockPasiva:
                exec('{} = thisBlockPasiva[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        instrucloop_Pasivas = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('datasets/instructions.xlsx'),
            seed=None, name='instrucloop_Pasivas')
        thisExp.addLoop(instrucloop_Pasivas)  # add the loop to the experiment
        thisInstrucloop_Pasiva = instrucloop_Pasivas.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisInstrucloop_Pasiva.rgb)
        if thisInstrucloop_Pasiva != None:
            for paramName in thisInstrucloop_Pasiva:
                exec('{} = thisInstrucloop_Pasiva[paramName]'.format(paramName))
        
        for thisInstrucloop_Pasiva in instrucloop_Pasivas:
            currentLoop = instrucloop_Pasivas
            # abbreviate parameter names if possible (e.g. rgb = thisInstrucloop_Pasiva.rgb)
            if thisInstrucloop_Pasiva != None:
                for paramName in thisInstrucloop_Pasiva:
                    exec('{} = thisInstrucloop_Pasiva[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "InstruccionesPasiva"-------
            continueRoutine = True
            # update component parameters for each repeat
            image2.setImage(instrucciones_pasiva)
            key_resp_2.keys = []
            key_resp_2.rt = []
            _key_resp_2_allKeys = []
            # keep track of which components have finished
            InstruccionesPasivaComponents = [image2, key_resp_2]
            for thisComponent in InstruccionesPasivaComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            InstruccionesPasivaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "InstruccionesPasiva"-------
            while continueRoutine:
                # get current time
                t = InstruccionesPasivaClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=InstruccionesPasivaClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image2* updates
                if image2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image2.frameNStart = frameN  # exact frame index
                    image2.tStart = t  # local t and not account for scr refresh
                    image2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image2, 'tStartRefresh')  # time at next scr refresh
                    image2.setAutoDraw(True)
                
                # *key_resp_2* updates
                waitOnFlip = False
                if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.tStart = t  # local t and not account for scr refresh
                    key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                if key_resp_2.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
                    _key_resp_2_allKeys.extend(theseKeys)
                    if len(_key_resp_2_allKeys):
                        key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                        key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in InstruccionesPasivaComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "InstruccionesPasiva"-------
            for thisComponent in InstruccionesPasivaComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "InstruccionesPasiva" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'instrucloop_Pasivas'
        
        # get names of stimulus parameters
        if instrucloop_Pasivas.trialList in ([], [None], None):
            params = []
        else:
            params = instrucloop_Pasivas.trialList[0].keys()
        # save data for this loop
        instrucloop_Pasivas.saveAsText(filename + 'instrucloop_Pasivas.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # set up handler to look after randomisation of conditions etc
        trial_trainingPasivas = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions("datasets/training_"+ordenpasivas[BlockPasivas.thisN]+".xlsx"),
            seed=None, name='trial_trainingPasivas')
        thisExp.addLoop(trial_trainingPasivas)  # add the loop to the experiment
        thisTrial_trainingPasiva = trial_trainingPasivas.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_trainingPasiva.rgb)
        if thisTrial_trainingPasiva != None:
            for paramName in thisTrial_trainingPasiva:
                exec('{} = thisTrial_trainingPasiva[paramName]'.format(paramName))
        
        for thisTrial_trainingPasiva in trial_trainingPasivas:
            currentLoop = trial_trainingPasivas
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_trainingPasiva.rgb)
            if thisTrial_trainingPasiva != None:
                for paramName in thisTrial_trainingPasiva:
                    exec('{} = thisTrial_trainingPasiva[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "firstfix_training"-------
            continueRoutine = True
            # update component parameters for each repeat
            start_trainPR.setSound('datasets/trial_init.wav', secs=0.5, hamming=True)
            start_trainPR.setVolume(1.0, log=False)
            firstfixtrain.setText('+')
            # keep track of which components have finished
            firstfix_trainingComponents = [drift_trainPR, start_trainPR, firstfixtrain]
            for thisComponent in firstfix_trainingComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            firstfix_trainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "firstfix_training"-------
            while continueRoutine:
                # get current time
                t = firstfix_trainingClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=firstfix_trainingClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *drift_trainPR* updates
                if drift_trainPR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    drift_trainPR.frameNStart = frameN  # exact frame index
                    drift_trainPR.tStart = t  # local t and not account for scr refresh
                    drift_trainPR.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(drift_trainPR, 'tStartRefresh')  # time at next scr refresh
                    drift_trainPR.setAutoDraw(True)
                if drift_trainPR.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > drift_trainPR.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        drift_trainPR.tStop = t  # not accounting for scr refresh
                        drift_trainPR.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(drift_trainPR, 'tStopRefresh')  # time at next scr refresh
                        drift_trainPR.setAutoDraw(False)
                # start/stop start_trainPR
                if start_trainPR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    start_trainPR.frameNStart = frameN  # exact frame index
                    start_trainPR.tStart = t  # local t and not account for scr refresh
                    start_trainPR.tStartRefresh = tThisFlipGlobal  # on global time
                    start_trainPR.play(when=win)  # sync with win flip
                if start_trainPR.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > start_trainPR.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        start_trainPR.tStop = t  # not accounting for scr refresh
                        start_trainPR.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(start_trainPR, 'tStopRefresh')  # time at next scr refresh
                        start_trainPR.stop()
                
                # *firstfixtrain* updates
                if firstfixtrain.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    firstfixtrain.frameNStart = frameN  # exact frame index
                    firstfixtrain.tStart = t  # local t and not account for scr refresh
                    firstfixtrain.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(firstfixtrain, 'tStartRefresh')  # time at next scr refresh
                    firstfixtrain.setAutoDraw(True)
                if firstfixtrain.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > firstfixtrain.tStartRefresh + fixation_time_train-frameTolerance:
                        # keep track of stop time/frame for later
                        firstfixtrain.tStop = t  # not accounting for scr refresh
                        firstfixtrain.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(firstfixtrain, 'tStopRefresh')  # time at next scr refresh
                        firstfixtrain.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in firstfix_trainingComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "firstfix_training"-------
            for thisComponent in firstfix_trainingComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            start_trainPR.stop()  # ensure sound has stopped at end of routine
            trial_trainingPasivas.addData('firstfixtrain.started', firstfixtrain.tStartRefresh)
            trial_trainingPasivas.addData('firstfixtrain.stopped', firstfixtrain.tStopRefresh)
            # the Routine "firstfix_training" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            train_digitloopPasivas = data.TrialHandler(nReps=digitSpan_train, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='train_digitloopPasivas')
            thisExp.addLoop(train_digitloopPasivas)  # add the loop to the experiment
            thisTrain_digitloopPasiva = train_digitloopPasivas.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrain_digitloopPasiva.rgb)
            if thisTrain_digitloopPasiva != None:
                for paramName in thisTrain_digitloopPasiva:
                    exec('{} = thisTrain_digitloopPasiva[paramName]'.format(paramName))
            
            for thisTrain_digitloopPasiva in train_digitloopPasivas:
                currentLoop = train_digitloopPasivas
                # abbreviate parameter names if possible (e.g. rgb = thisTrain_digitloopPasiva.rgb)
                if thisTrain_digitloopPasiva != None:
                    for paramName in thisTrain_digitloopPasiva:
                        exec('{} = thisTrain_digitloopPasiva[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "presentation_training"-------
                continueRoutine = True
                routineTimer.add(1.000000)
                # update component parameters for each repeat
                digitpresentation_training.setText(str(digits_train)[train_digitloopPasivas.thisN]

)
                # keep track of which components have finished
                presentation_trainingComponents = [digitpresentation_training]
                for thisComponent in presentation_trainingComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                presentation_trainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "presentation_training"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = presentation_trainingClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=presentation_trainingClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *digitpresentation_training* updates
                    if digitpresentation_training.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        digitpresentation_training.frameNStart = frameN  # exact frame index
                        digitpresentation_training.tStart = t  # local t and not account for scr refresh
                        digitpresentation_training.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(digitpresentation_training, 'tStartRefresh')  # time at next scr refresh
                        digitpresentation_training.setAutoDraw(True)
                    if digitpresentation_training.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > digitpresentation_training.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            digitpresentation_training.tStop = t  # not accounting for scr refresh
                            digitpresentation_training.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(digitpresentation_training, 'tStopRefresh')  # time at next scr refresh
                            digitpresentation_training.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in presentation_trainingComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "presentation_training"-------
                for thisComponent in presentation_trainingComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                train_digitloopPasivas.addData('digitpresentation_training.started', digitpresentation_training.tStartRefresh)
                train_digitloopPasivas.addData('digitpresentation_training.stopped', digitpresentation_training.tStopRefresh)
                thisExp.nextEntry()
                
            # completed digitSpan_train repeats of 'train_digitloopPasivas'
            
            # get names of stimulus parameters
            if train_digitloopPasivas.trialList in ([], [None], None):
                params = []
            else:
                params = train_digitloopPasivas.trialList[0].keys()
            # save data for this loop
            train_digitloopPasivas.saveAsText(filename + 'train_digitloopPasivas.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # ------Prepare to start Routine "recall_training"-------
            continueRoutine = True
            # update component parameters for each repeat
            answ_train.reset()
            answer_train_pasivas=int(answer_train)
            
            # keep track of which components have finished
            recall_trainingComponents = [recall_train, answ_train]
            for thisComponent in recall_trainingComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            recall_trainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "recall_training"-------
            while continueRoutine:
                # get current time
                t = recall_trainingClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=recall_trainingClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *recall_train* updates
                if recall_train.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    recall_train.frameNStart = frameN  # exact frame index
                    recall_train.tStart = t  # local t and not account for scr refresh
                    recall_train.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(recall_train, 'tStartRefresh')  # time at next scr refresh
                    recall_train.setAutoDraw(True)
                
                # *answ_train* updates
                if answ_train.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    answ_train.frameNStart = frameN  # exact frame index
                    answ_train.tStart = t  # local t and not account for scr refresh
                    answ_train.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(answ_train, 'tStartRefresh')  # time at next scr refresh
                    answ_train.setAutoDraw(True)
                if defaultKeyboard.getKeys(keyList=["return"]):
                    answ_train.text = answ_train.text.rstrip()
                    if answ_train.text == str(answer_train_pasivas):
                        correct = 1
                        fbTxt = 'Correct!'
                    else:
                        correct = 0
                        fbTxt = 'Incorrect'
                    thisExp.addData('correct', correct)
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in recall_trainingComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "recall_training"-------
            for thisComponent in recall_trainingComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trial_trainingPasivas.addData('recall_train.started', recall_train.tStartRefresh)
            trial_trainingPasivas.addData('recall_train.stopped', recall_train.tStopRefresh)
            trial_trainingPasivas.addData('answ_train.text',answ_train.text)
            trial_trainingPasivas.addData('answ_train.started', answ_train.tStartRefresh)
            trial_trainingPasivas.addData('answ_train.stopped', answ_train.tStopRefresh)
            # the Routine "recall_training" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "post_recall_train"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            post_recall_trainComponents = [post_recall_training]
            for thisComponent in post_recall_trainComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            post_recall_trainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "post_recall_train"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = post_recall_trainClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=post_recall_trainClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *post_recall_training* updates
                if post_recall_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    post_recall_training.frameNStart = frameN  # exact frame index
                    post_recall_training.tStart = t  # local t and not account for scr refresh
                    post_recall_training.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(post_recall_training, 'tStartRefresh')  # time at next scr refresh
                    post_recall_training.setAutoDraw(True)
                if post_recall_training.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > post_recall_training.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        post_recall_training.tStop = t  # not accounting for scr refresh
                        post_recall_training.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(post_recall_training, 'tStopRefresh')  # time at next scr refresh
                        post_recall_training.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in post_recall_trainComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "post_recall_train"-------
            for thisComponent in post_recall_trainComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trial_trainingPasivas.addData('post_recall_training.started', post_recall_training.tStartRefresh)
            trial_trainingPasivas.addData('post_recall_training.stopped', post_recall_training.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trial_trainingPasivas'
        
        # get names of stimulus parameters
        if trial_trainingPasivas.trialList in ([], [None], None):
            params = []
        else:
            params = trial_trainingPasivas.trialList[0].keys()
        # save data for this loop
        trial_trainingPasivas.saveAsText(filename + 'trial_trainingPasivas.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "start_trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        start_trialComponents = [end_training, key_resp]
        for thisComponent in start_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        start_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "start_trial"-------
        while continueRoutine:
            # get current time
            t = start_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=start_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *end_training* updates
            if end_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                end_training.frameNStart = frameN  # exact frame index
                end_training.tStart = t  # local t and not account for scr refresh
                end_training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(end_training, 'tStartRefresh')  # time at next scr refresh
                end_training.setAutoDraw(True)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "start_trial"-------
        for thisComponent in start_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        BlockPasivas.addData('end_training.started', end_training.tStartRefresh)
        BlockPasivas.addData('end_training.stopped', end_training.tStopRefresh)
        parar_el_trial = False
        # the Routine "start_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trial_Pasiva = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions("datasets/Dataset_"+ordenpasivas[BlockPasivas.thisN]+".xlsx"),
            seed=None, name='trial_Pasiva')
        thisExp.addLoop(trial_Pasiva)  # add the loop to the experiment
        thisTrial_Pasiva = trial_Pasiva.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_Pasiva.rgb)
        if thisTrial_Pasiva != None:
            for paramName in thisTrial_Pasiva:
                exec('{} = thisTrial_Pasiva[paramName]'.format(paramName))
        
        for thisTrial_Pasiva in trial_Pasiva:
            currentLoop = trial_Pasiva
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_Pasiva.rgb)
            if thisTrial_Pasiva != None:
                for paramName in thisTrial_Pasiva:
                    exec('{} = thisTrial_Pasiva[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "first_fixation"-------
            continueRoutine = True
            # update component parameters for each repeat
            startPR.setSound('datasets/trial_init.wav', secs=0.5, hamming=True)
            startPR.setVolume(1.0, log=False)
            first_fix_pas.setText('+')
            # keep track of which components have finished
            first_fixationComponents = [driftPR, startPR, first_fix_pas]
            for thisComponent in first_fixationComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            first_fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "first_fixation"-------
            while continueRoutine:
                # get current time
                t = first_fixationClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=first_fixationClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *driftPR* updates
                if driftPR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    driftPR.frameNStart = frameN  # exact frame index
                    driftPR.tStart = t  # local t and not account for scr refresh
                    driftPR.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(driftPR, 'tStartRefresh')  # time at next scr refresh
                    driftPR.setAutoDraw(True)
                if driftPR.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > driftPR.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        driftPR.tStop = t  # not accounting for scr refresh
                        driftPR.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(driftPR, 'tStopRefresh')  # time at next scr refresh
                        driftPR.setAutoDraw(False)
                # start/stop startPR
                if startPR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    startPR.frameNStart = frameN  # exact frame index
                    startPR.tStart = t  # local t and not account for scr refresh
                    startPR.tStartRefresh = tThisFlipGlobal  # on global time
                    startPR.play(when=win)  # sync with win flip
                if startPR.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > startPR.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        startPR.tStop = t  # not accounting for scr refresh
                        startPR.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(startPR, 'tStopRefresh')  # time at next scr refresh
                        startPR.stop()
                
                # *first_fix_pas* updates
                if first_fix_pas.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    first_fix_pas.frameNStart = frameN  # exact frame index
                    first_fix_pas.tStart = t  # local t and not account for scr refresh
                    first_fix_pas.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(first_fix_pas, 'tStartRefresh')  # time at next scr refresh
                    first_fix_pas.setAutoDraw(True)
                if first_fix_pas.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > first_fix_pas.tStartRefresh + fixation_time-frameTolerance:
                        # keep track of stop time/frame for later
                        first_fix_pas.tStop = t  # not accounting for scr refresh
                        first_fix_pas.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(first_fix_pas, 'tStopRefresh')  # time at next scr refresh
                        first_fix_pas.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in first_fixationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "first_fixation"-------
            for thisComponent in first_fixationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            startPR.stop()  # ensure sound has stopped at end of routine
            trial_Pasiva.addData('first_fix_pas.started', first_fix_pas.tStartRefresh)
            trial_Pasiva.addData('first_fix_pas.stopped', first_fix_pas.tStopRefresh)
            # the Routine "first_fixation" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            digitLoop_Pasivas = data.TrialHandler(nReps=digitSpan, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='digitLoop_Pasivas')
            thisExp.addLoop(digitLoop_Pasivas)  # add the loop to the experiment
            thisDigitLoop_Pasiva = digitLoop_Pasivas.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop_Pasiva.rgb)
            if thisDigitLoop_Pasiva != None:
                for paramName in thisDigitLoop_Pasiva:
                    exec('{} = thisDigitLoop_Pasiva[paramName]'.format(paramName))
            
            for thisDigitLoop_Pasiva in digitLoop_Pasivas:
                currentLoop = digitLoop_Pasivas
                # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop_Pasiva.rgb)
                if thisDigitLoop_Pasiva != None:
                    for paramName in thisDigitLoop_Pasiva:
                        exec('{} = thisDigitLoop_Pasiva[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "Presentation_pas"-------
                continueRoutine = True
                routineTimer.add(1.000000)
                # update component parameters for each repeat
                pres_text.setText(str(digits)[digitLoop_Pasivas.thisN]
)
                # keep track of which components have finished
                Presentation_pasComponents = [pres_text]
                for thisComponent in Presentation_pasComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                Presentation_pasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "Presentation_pas"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = Presentation_pasClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=Presentation_pasClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *pres_text* updates
                    if pres_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        pres_text.frameNStart = frameN  # exact frame index
                        pres_text.tStart = t  # local t and not account for scr refresh
                        pres_text.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(pres_text, 'tStartRefresh')  # time at next scr refresh
                        pres_text.setAutoDraw(True)
                    if pres_text.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > pres_text.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            pres_text.tStop = t  # not accounting for scr refresh
                            pres_text.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(pres_text, 'tStopRefresh')  # time at next scr refresh
                            pres_text.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in Presentation_pasComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "Presentation_pas"-------
                for thisComponent in Presentation_pasComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                digitLoop_Pasivas.addData('pres_text.started', pres_text.tStartRefresh)
                digitLoop_Pasivas.addData('pres_text.stopped', pres_text.tStopRefresh)
            # completed digitSpan repeats of 'digitLoop_Pasivas'
            
            
            # ------Prepare to start Routine "Recall_pasivas"-------
            continueRoutine = True
            # update component parameters for each repeat
            answer_box.reset()
            answer_Pasive=int(answer)
            
            
            
            # keep track of which components have finished
            Recall_pasivasComponents = [recall_txt, answer_box]
            for thisComponent in Recall_pasivasComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Recall_pasivasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Recall_pasivas"-------
            while continueRoutine:
                # get current time
                t = Recall_pasivasClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Recall_pasivasClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *recall_txt* updates
                if recall_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    recall_txt.frameNStart = frameN  # exact frame index
                    recall_txt.tStart = t  # local t and not account for scr refresh
                    recall_txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(recall_txt, 'tStartRefresh')  # time at next scr refresh
                    recall_txt.setAutoDraw(True)
                
                # *answer_box* updates
                if answer_box.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    answer_box.frameNStart = frameN  # exact frame index
                    answer_box.tStart = t  # local t and not account for scr refresh
                    answer_box.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(answer_box, 'tStartRefresh')  # time at next scr refresh
                    answer_box.setAutoDraw(True)
                if defaultKeyboard.getKeys(keyList=["return"]): #end routine when return is typed
                    answer_box.text = answer_box.text.rstrip() #deletes return from answer
                    if answer_box.text == str(answer_Pasive): #if correct
                        correct = 1
                    else:
                        correct = 0
                    thisExp.addData('correct', correct)
                    continueRoutine = False #ends routine
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Recall_pasivasComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Recall_pasivas"-------
            for thisComponent in Recall_pasivasComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trial_Pasiva.addData('recall_txt.started', recall_txt.tStartRefresh)
            trial_Pasiva.addData('recall_txt.stopped', recall_txt.tStopRefresh)
            trial_Pasiva.addData('answer_box.text',answer_box.text)
            trial_Pasiva.addData('answer_box.started', answer_box.tStartRefresh)
            trial_Pasiva.addData('answer_box.stopped', answer_box.tStopRefresh)
            ###trial 1 or 2 (span 3)
            if  trial_Pasiva.thisTrialN == 0 or trial_Pasiva.thisTrialN == 1: 
                if correct == 1: #if trial 1  
                    previous_count += 1
                    print(f' trial = {trial_Pasiva.thisTrialN} previous_count = {previous_count}')
                    
            ###trial 3 or 4 (span 4)
            elif trial_Pasiva.thisTrialN == 2 or trial_Pasiva.thisTrialN == 3: 
                if correct == 1:
                    current_count +=1 #else (if incorrect, do nothing)
                    print(f' trial = {trial_Pasiva.thisTrialN} current_count = {current_count}')
            if trial_Pasiva.thisTrialN == 3: 
                if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                    parar_el_trial = True
                    print(f'trial = {trial_Pasiva.thisTrialN} parar_el_trial = {parar_el_trial}')
                else: #if at least one correct, continue routine, and reset counters
                    previous_count = current_count #previous count equals corrects at trials 3 and 4
                    current_count = 0 
                print(f' trial = {trial_Pasiva.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
                            
            ###trial 5 or 6 (span 5)
            elif trial_Pasiva.thisTrialN == 4 or trial_Pasiva.thisTrialN == 5:
                if correct == 1:
                    current_count +=1 #else (if incorrect, do nothing)
                    print(f' trial = {trial_Pasiva.thisTrialN} current_count = {current_count}')
            if trial_Pasiva.thisTrialN == 5: 
                if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                    parar_el_trial = True
                    print(f'parar_el_trial = {parar_el_trial}')
                else: #if at least one correct, continue routine, and reset counters
                    previous_count = current_count #previous count equals corrects at trials 3 and 4
                    current_count = 0 
                print(f' trial = {trial_Pasiva.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
                            
            ###trial 7 or 8 (span 6)
            elif trial_Pasiva.thisTrialN == 6 or trial_Pasiva.thisTrialN == 7:
                if correct == 1:
                    current_count +=1 #else (if incorrect, do nothing)
                    print(f' trial = {trial_Pasiva.thisTrialN} current_count = {current_count}')
            if trial_Pasiva.thisTrialN == 7: 
                if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                    parar_el_trial = True
                    print(f'parar_el_trial = {parar_el_trial}')
                else: #if at least one correct, continue routine, and reset counters
                    previous_count = current_count #previous count equals corrects at trials 3 and 4
                    current_count = 0 
                print(f' trial = {trial_Pasiva.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
                             
            ###trial 9 or 10 (span 7)
            elif trial_Pasiva.thisTrialN == 8 or trial_Pasiva.thisTrialN == 9:
                if correct == 1:
                    current_count +=1 #else (if incorrect, do nothing)
                    print(f' trial = {trial_Pasiva.thisTrialN} current_count = {current_count}')
            if trial_Pasiva.thisTrialN == 9: 
                if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                    parar_el_trial = True
                    print(f'parar_el_trial = {parar_el_trial}')
                else: #if at least one correct, continue routine, and reset counters
                    previous_count = current_count #previous count equals corrects at trials 3 and 4
                    current_count = 0 
                print(f' trial = {trial_Pasiva.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
                 
            ###trial 11 or 12 (span 8)
            elif trial_Pasiva.thisTrialN == 10 or trial_Pasiva.thisTrialN == 11:
                if correct == 1:
                    current_count +=1 #else (if incorrect, do nothing)
                    print(f' trial = {trial_Pasiva.thisTrialN} current_count = {current_count}')
            if trial_Pasiva.thisTrialN == 11: 
                if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                    parar_el_trial = True
                    print(f'parar_el_trial = {parar_el_trial}')
                else: #if at least one correct, continue routine, and reset counters
                    previous_count = current_count #previous count equals corrects at trials 3 and 4
                    current_count = 0 
                print(f' trial = {trial_Pasiva.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
               
            ###trial 13 or 14 (span 9)
            elif trial_Pasiva.thisTrialN == 12 or trial_Pasiva.thisTrialN == 13:
                if correct == 1:
                    current_count +=1 #else (if incorrect, do nothing)
                    print(f' trial = {trial_Pasiva.thisTrialN} current_count = {current_count}')
            if trial_Pasiva.thisTrialN == 13: 
                if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                    parar_el_trial = True
                    print(f'parar_el_trial = {parar_el_trial}')
                else: #if at least one correct, continue routine, and reset counters
                    previous_count = current_count #previous count equals corrects at trials 3 and 4
                    current_count = 0 
                print(f' trial = {trial_Pasiva.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
                
            ###trial 16 (span 10)
            #elif trial_PR.thisTrialN == 15:
            #    continueRoutine = False
            # the Routine "Recall_pasivas" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "post_recallPasiva"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            post_recallPasivaComponents = [postrecallPR]
            for thisComponent in post_recallPasivaComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            post_recallPasivaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "post_recallPasiva"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = post_recallPasivaClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=post_recallPasivaClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *postrecallPR* updates
                if postrecallPR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    postrecallPR.frameNStart = frameN  # exact frame index
                    postrecallPR.tStart = t  # local t and not account for scr refresh
                    postrecallPR.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(postrecallPR, 'tStartRefresh')  # time at next scr refresh
                    postrecallPR.setAutoDraw(True)
                if postrecallPR.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > postrecallPR.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        postrecallPR.tStop = t  # not accounting for scr refresh
                        postrecallPR.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(postrecallPR, 'tStopRefresh')  # time at next scr refresh
                        postrecallPR.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in post_recallPasivaComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "post_recallPasiva"-------
            for thisComponent in post_recallPasivaComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trial_Pasiva.addData('postrecallPR.started', postrecallPR.tStartRefresh)
            trial_Pasiva.addData('postrecallPR.stopped', postrecallPR.tStopRefresh)
            if parar_el_trial:
                trial_Pasiva.finished = True
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trial_Pasiva'
        
        # get names of stimulus parameters
        if trial_Pasiva.trialList in ([], [None], None):
            params = []
        else:
            params = trial_Pasiva.trialList[0].keys()
        # save data for this loop
        trial_Pasiva.saveAsText(filename + 'trial_Pasiva.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "LickertPasivas"-------
        continueRoutine = True
        # update component parameters for each repeat
        dif_licker.reset()
        # keep track of which components have finished
        LickertPasivasComponents = [Dificultad_pasivas, dif_licker]
        for thisComponent in LickertPasivasComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        LickertPasivasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "LickertPasivas"-------
        while continueRoutine:
            # get current time
            t = LickertPasivasClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=LickertPasivasClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Dificultad_pasivas* updates
            if Dificultad_pasivas.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Dificultad_pasivas.frameNStart = frameN  # exact frame index
                Dificultad_pasivas.tStart = t  # local t and not account for scr refresh
                Dificultad_pasivas.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Dificultad_pasivas, 'tStartRefresh')  # time at next scr refresh
                Dificultad_pasivas.setAutoDraw(True)
            
            # *dif_licker* updates
            if dif_licker.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dif_licker.frameNStart = frameN  # exact frame index
                dif_licker.tStart = t  # local t and not account for scr refresh
                dif_licker.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dif_licker, 'tStartRefresh')  # time at next scr refresh
                dif_licker.setAutoDraw(True)
            
            # Check dif_licker for response to end routine
            if dif_licker.getRating() is not None and dif_licker.status == STARTED:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in LickertPasivasComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "LickertPasivas"-------
        for thisComponent in LickertPasivasComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        BlockPasivas.addData('Dificultad_pasivas.started', Dificultad_pasivas.tStartRefresh)
        BlockPasivas.addData('Dificultad_pasivas.stopped', Dificultad_pasivas.tStopRefresh)
        BlockPasivas.addData('dif_licker.response', dif_licker.getRating())
        BlockPasivas.addData('dif_licker.rt', dif_licker.getRT())
        BlockPasivas.addData('dif_licker.started', dif_licker.tStartRefresh)
        BlockPasivas.addData('dif_licker.stopped', dif_licker.tStopRefresh)
        # the Routine "LickertPasivas" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "EndTask"-------
        continueRoutine = True
        # update component parameters for each repeat
        siguiente_tarea.setText('Esta tarea terminó. \n* Presiona la barra para continuar con la siguiente*')
        key_resp_6.keys = []
        key_resp_6.rt = []
        _key_resp_6_allKeys = []
        # keep track of which components have finished
        EndTaskComponents = [siguiente_tarea, key_resp_6]
        for thisComponent in EndTaskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        EndTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "EndTask"-------
        while continueRoutine:
            # get current time
            t = EndTaskClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=EndTaskClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *siguiente_tarea* updates
            if siguiente_tarea.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                siguiente_tarea.frameNStart = frameN  # exact frame index
                siguiente_tarea.tStart = t  # local t and not account for scr refresh
                siguiente_tarea.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(siguiente_tarea, 'tStartRefresh')  # time at next scr refresh
                siguiente_tarea.setAutoDraw(True)
            
            # *key_resp_6* updates
            waitOnFlip = False
            if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                # keep track of start time/frame for later
                key_resp_6.frameNStart = frameN  # exact frame index
                key_resp_6.tStart = t  # local t and not account for scr refresh
                key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                key_resp_6.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_6.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_6_allKeys.extend(theseKeys)
                if len(_key_resp_6_allKeys):
                    key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                    key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EndTaskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "EndTask"-------
        for thisComponent in EndTaskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_6.keys in ['', [], None]:  # No response was made
            key_resp_6.keys = None
        BlockPasivas.addData('key_resp_6.keys',key_resp_6.keys)
        if key_resp_6.keys != None:  # we had a response
            BlockPasivas.addData('key_resp_6.rt', key_resp_6.rt)
        BlockPasivas.addData('key_resp_6.started', key_resp_6.tStartRefresh)
        BlockPasivas.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
        # the Routine "EndTask" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed nRepsBlockPasivas repeats of 'BlockPasivas'
    
    
    # set up handler to look after randomisation of conditions etc
    BlockActivas = data.TrialHandler(nReps=nRepsBlockActivas, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='BlockActivas')
    thisExp.addLoop(BlockActivas)  # add the loop to the experiment
    thisBlockActiva = BlockActivas.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockActiva.rgb)
    if thisBlockActiva != None:
        for paramName in thisBlockActiva:
            exec('{} = thisBlockActiva[paramName]'.format(paramName))
    
    for thisBlockActiva in BlockActivas:
        currentLoop = BlockActivas
        # abbreviate parameter names if possible (e.g. rgb = thisBlockActiva.rgb)
        if thisBlockActiva != None:
            for paramName in thisBlockActiva:
                exec('{} = thisBlockActiva[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        intrLoopActivas = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('datasets/instructions.xlsx'),
            seed=None, name='intrLoopActivas')
        thisExp.addLoop(intrLoopActivas)  # add the loop to the experiment
        thisIntrLoopActiva = intrLoopActivas.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisIntrLoopActiva.rgb)
        if thisIntrLoopActiva != None:
            for paramName in thisIntrLoopActiva:
                exec('{} = thisIntrLoopActiva[paramName]'.format(paramName))
        
        for thisIntrLoopActiva in intrLoopActivas:
            currentLoop = intrLoopActivas
            # abbreviate parameter names if possible (e.g. rgb = thisIntrLoopActiva.rgb)
            if thisIntrLoopActiva != None:
                for paramName in thisIntrLoopActiva:
                    exec('{} = thisIntrLoopActiva[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "Instr_Activas"-------
            continueRoutine = True
            # update component parameters for each repeat
            image2_2.setImage(instrucciones_activa)
            key_resp_3.keys = []
            key_resp_3.rt = []
            _key_resp_3_allKeys = []
            # keep track of which components have finished
            Instr_ActivasComponents = [image2_2, key_resp_3]
            for thisComponent in Instr_ActivasComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Instr_ActivasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Instr_Activas"-------
            while continueRoutine:
                # get current time
                t = Instr_ActivasClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Instr_ActivasClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image2_2* updates
                if image2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image2_2.frameNStart = frameN  # exact frame index
                    image2_2.tStart = t  # local t and not account for scr refresh
                    image2_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image2_2, 'tStartRefresh')  # time at next scr refresh
                    image2_2.setAutoDraw(True)
                
                # *key_resp_3* updates
                waitOnFlip = False
                if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_3.frameNStart = frameN  # exact frame index
                    key_resp_3.tStart = t  # local t and not account for scr refresh
                    key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                    key_resp_3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                if key_resp_3.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
                    _key_resp_3_allKeys.extend(theseKeys)
                    if len(_key_resp_3_allKeys):
                        key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                        key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Instr_ActivasComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Instr_Activas"-------
            for thisComponent in Instr_ActivasComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "Instr_Activas" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'intrLoopActivas'
        
        # get names of stimulus parameters
        if intrLoopActivas.trialList in ([], [None], None):
            params = []
        else:
            params = intrLoopActivas.trialList[0].keys()
        # save data for this loop
        intrLoopActivas.saveAsText(filename + 'intrLoopActivas.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # set up handler to look after randomisation of conditions etc
        trial_train_Activas = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions("datasets/training_"+ordenactivas[BlockActivas.thisN]+".xlsx"),
            seed=None, name='trial_train_Activas')
        thisExp.addLoop(trial_train_Activas)  # add the loop to the experiment
        thisTrial_train_Activa = trial_train_Activas.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_train_Activa.rgb)
        if thisTrial_train_Activa != None:
            for paramName in thisTrial_train_Activa:
                exec('{} = thisTrial_train_Activa[paramName]'.format(paramName))
        
        for thisTrial_train_Activa in trial_train_Activas:
            currentLoop = trial_train_Activas
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_train_Activa.rgb)
            if thisTrial_train_Activa != None:
                for paramName in thisTrial_train_Activa:
                    exec('{} = thisTrial_train_Activa[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "drift_press_activas"-------
            continueRoutine = True
            # update component parameters for each repeat
            start_trainPR_2.setSound('datasets/trial_init.wav', secs=0.5, hamming=True)
            start_trainPR_2.setVolume(1.0, log=False)
            key_resp_5.keys = []
            key_resp_5.rt = []
            _key_resp_5_allKeys = []
            # keep track of which components have finished
            drift_press_activasComponents = [start_trainPR_2, drift_trainPR_2, firstfix_activas, key_resp_5]
            for thisComponent in drift_press_activasComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            drift_press_activasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "drift_press_activas"-------
            while continueRoutine:
                # get current time
                t = drift_press_activasClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=drift_press_activasClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # start/stop start_trainPR_2
                if start_trainPR_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    start_trainPR_2.frameNStart = frameN  # exact frame index
                    start_trainPR_2.tStart = t  # local t and not account for scr refresh
                    start_trainPR_2.tStartRefresh = tThisFlipGlobal  # on global time
                    start_trainPR_2.play(when=win)  # sync with win flip
                if start_trainPR_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > start_trainPR_2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        start_trainPR_2.tStop = t  # not accounting for scr refresh
                        start_trainPR_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(start_trainPR_2, 'tStopRefresh')  # time at next scr refresh
                        start_trainPR_2.stop()
                
                # *drift_trainPR_2* updates
                if drift_trainPR_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    drift_trainPR_2.frameNStart = frameN  # exact frame index
                    drift_trainPR_2.tStart = t  # local t and not account for scr refresh
                    drift_trainPR_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(drift_trainPR_2, 'tStartRefresh')  # time at next scr refresh
                    drift_trainPR_2.setAutoDraw(True)
                if drift_trainPR_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > drift_trainPR_2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        drift_trainPR_2.tStop = t  # not accounting for scr refresh
                        drift_trainPR_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(drift_trainPR_2, 'tStopRefresh')  # time at next scr refresh
                        drift_trainPR_2.setAutoDraw(False)
                
                # *firstfix_activas* updates
                if firstfix_activas.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    firstfix_activas.frameNStart = frameN  # exact frame index
                    firstfix_activas.tStart = t  # local t and not account for scr refresh
                    firstfix_activas.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(firstfix_activas, 'tStartRefresh')  # time at next scr refresh
                    firstfix_activas.setAutoDraw(True)
                
                # *key_resp_5* updates
                waitOnFlip = False
                if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_5.frameNStart = frameN  # exact frame index
                    key_resp_5.tStart = t  # local t and not account for scr refresh
                    key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                    key_resp_5.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_5.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
                    _key_resp_5_allKeys.extend(theseKeys)
                    if len(_key_resp_5_allKeys):
                        key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                        key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in drift_press_activasComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "drift_press_activas"-------
            for thisComponent in drift_press_activasComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            start_trainPR_2.stop()  # ensure sound has stopped at end of routine
            trial_train_Activas.addData('firstfix_activas.started', firstfix_activas.tStartRefresh)
            trial_train_Activas.addData('firstfix_activas.stopped', firstfix_activas.tStopRefresh)
            # check responses
            if key_resp_5.keys in ['', [], None]:  # No response was made
                key_resp_5.keys = None
            trial_train_Activas.addData('key_resp_5.keys',key_resp_5.keys)
            if key_resp_5.keys != None:  # we had a response
                trial_train_Activas.addData('key_resp_5.rt', key_resp_5.rt)
            trial_train_Activas.addData('key_resp_5.started', key_resp_5.tStartRefresh)
            trial_train_Activas.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
            # the Routine "drift_press_activas" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "ffix_trainactivas"-------
            continueRoutine = True
            # update component parameters for each repeat
            firsfixtrain_activa.setText('+')
            # keep track of which components have finished
            ffix_trainactivasComponents = [firsfixtrain_activa]
            for thisComponent in ffix_trainactivasComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ffix_trainactivasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ffix_trainactivas"-------
            while continueRoutine:
                # get current time
                t = ffix_trainactivasClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ffix_trainactivasClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *firsfixtrain_activa* updates
                if firsfixtrain_activa.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    firsfixtrain_activa.frameNStart = frameN  # exact frame index
                    firsfixtrain_activa.tStart = t  # local t and not account for scr refresh
                    firsfixtrain_activa.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(firsfixtrain_activa, 'tStartRefresh')  # time at next scr refresh
                    firsfixtrain_activa.setAutoDraw(True)
                if firsfixtrain_activa.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > firsfixtrain_activa.tStartRefresh + fixation_time_train-frameTolerance:
                        # keep track of stop time/frame for later
                        firsfixtrain_activa.tStop = t  # not accounting for scr refresh
                        firsfixtrain_activa.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(firsfixtrain_activa, 'tStopRefresh')  # time at next scr refresh
                        firsfixtrain_activa.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ffix_trainactivasComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ffix_trainactivas"-------
            for thisComponent in ffix_trainactivasComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trial_train_Activas.addData('firsfixtrain_activa.started', firsfixtrain_activa.tStartRefresh)
            trial_train_Activas.addData('firsfixtrain_activa.stopped', firsfixtrain_activa.tStopRefresh)
            # the Routine "ffix_trainactivas" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            train_digitloop_Activas = data.TrialHandler(nReps=digitSpan_train, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='train_digitloop_Activas')
            thisExp.addLoop(train_digitloop_Activas)  # add the loop to the experiment
            thisTrain_digitloop_Activa = train_digitloop_Activas.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrain_digitloop_Activa.rgb)
            if thisTrain_digitloop_Activa != None:
                for paramName in thisTrain_digitloop_Activa:
                    exec('{} = thisTrain_digitloop_Activa[paramName]'.format(paramName))
            
            for thisTrain_digitloop_Activa in train_digitloop_Activas:
                currentLoop = train_digitloop_Activas
                # abbreviate parameter names if possible (e.g. rgb = thisTrain_digitloop_Activa.rgb)
                if thisTrain_digitloop_Activa != None:
                    for paramName in thisTrain_digitloop_Activa:
                        exec('{} = thisTrain_digitloop_Activa[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "present_train_activas"-------
                continueRoutine = True
                routineTimer.add(1.000000)
                # update component parameters for each repeat
                digitpresentation_training_2.setText(str(digits_train)[train_digitloop_Activas.thisN]

)
                # keep track of which components have finished
                present_train_activasComponents = [digitpresentation_training_2]
                for thisComponent in present_train_activasComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                present_train_activasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "present_train_activas"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = present_train_activasClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=present_train_activasClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *digitpresentation_training_2* updates
                    if digitpresentation_training_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        digitpresentation_training_2.frameNStart = frameN  # exact frame index
                        digitpresentation_training_2.tStart = t  # local t and not account for scr refresh
                        digitpresentation_training_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(digitpresentation_training_2, 'tStartRefresh')  # time at next scr refresh
                        digitpresentation_training_2.setAutoDraw(True)
                    if digitpresentation_training_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > digitpresentation_training_2.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            digitpresentation_training_2.tStop = t  # not accounting for scr refresh
                            digitpresentation_training_2.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(digitpresentation_training_2, 'tStopRefresh')  # time at next scr refresh
                            digitpresentation_training_2.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in present_train_activasComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "present_train_activas"-------
                for thisComponent in present_train_activasComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                train_digitloop_Activas.addData('digitpresentation_training_2.started', digitpresentation_training_2.tStartRefresh)
                train_digitloop_Activas.addData('digitpresentation_training_2.stopped', digitpresentation_training_2.tStopRefresh)
                thisExp.nextEntry()
                
            # completed digitSpan_train repeats of 'train_digitloop_Activas'
            
            # get names of stimulus parameters
            if train_digitloop_Activas.trialList in ([], [None], None):
                params = []
            else:
                params = train_digitloop_Activas.trialList[0].keys()
            # save data for this loop
            train_digitloop_Activas.saveAsText(filename + 'train_digitloop_Activas.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # ------Prepare to start Routine "recall_train_activas"-------
            continueRoutine = True
            # update component parameters for each repeat
            answ_train_2.reset()
            answer_train_activas=int(answer_train)
            # keep track of which components have finished
            recall_train_activasComponents = [recall_train_2, answ_train_2]
            for thisComponent in recall_train_activasComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            recall_train_activasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "recall_train_activas"-------
            while continueRoutine:
                # get current time
                t = recall_train_activasClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=recall_train_activasClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *recall_train_2* updates
                if recall_train_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    recall_train_2.frameNStart = frameN  # exact frame index
                    recall_train_2.tStart = t  # local t and not account for scr refresh
                    recall_train_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(recall_train_2, 'tStartRefresh')  # time at next scr refresh
                    recall_train_2.setAutoDraw(True)
                
                # *answ_train_2* updates
                if answ_train_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    answ_train_2.frameNStart = frameN  # exact frame index
                    answ_train_2.tStart = t  # local t and not account for scr refresh
                    answ_train_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(answ_train_2, 'tStartRefresh')  # time at next scr refresh
                    answ_train_2.setAutoDraw(True)
                if defaultKeyboard.getKeys(keyList=["return"]):
                    answ_train_2.text = answ_train_2.text.rstrip()
                    if answ_train_2.text == str(answer_train_activas):
                        correct = 1
                        fbTxt = 'Correct!'
                    else:
                        correct = 0
                        fbTxt = 'Incorrect'
                    thisExp.addData('correct', correct)
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in recall_train_activasComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "recall_train_activas"-------
            for thisComponent in recall_train_activasComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trial_train_Activas.addData('recall_train_2.started', recall_train_2.tStartRefresh)
            trial_train_Activas.addData('recall_train_2.stopped', recall_train_2.tStopRefresh)
            trial_train_Activas.addData('answ_train_2.text',answ_train_2.text)
            trial_train_Activas.addData('answ_train_2.started', answ_train_2.tStartRefresh)
            trial_train_Activas.addData('answ_train_2.stopped', answ_train_2.tStopRefresh)
            # the Routine "recall_train_activas" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "post_recall_train_activas"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            post_recall_train_activasComponents = [post_recall_training_2]
            for thisComponent in post_recall_train_activasComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            post_recall_train_activasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "post_recall_train_activas"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = post_recall_train_activasClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=post_recall_train_activasClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *post_recall_training_2* updates
                if post_recall_training_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    post_recall_training_2.frameNStart = frameN  # exact frame index
                    post_recall_training_2.tStart = t  # local t and not account for scr refresh
                    post_recall_training_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(post_recall_training_2, 'tStartRefresh')  # time at next scr refresh
                    post_recall_training_2.setAutoDraw(True)
                if post_recall_training_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > post_recall_training_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        post_recall_training_2.tStop = t  # not accounting for scr refresh
                        post_recall_training_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(post_recall_training_2, 'tStopRefresh')  # time at next scr refresh
                        post_recall_training_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in post_recall_train_activasComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "post_recall_train_activas"-------
            for thisComponent in post_recall_train_activasComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trial_train_Activas.addData('post_recall_training_2.started', post_recall_training_2.tStartRefresh)
            trial_train_Activas.addData('post_recall_training_2.stopped', post_recall_training_2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trial_train_Activas'
        
        # get names of stimulus parameters
        if trial_train_Activas.trialList in ([], [None], None):
            params = []
        else:
            params = trial_train_Activas.trialList[0].keys()
        # save data for this loop
        trial_train_Activas.saveAsText(filename + 'trial_train_Activas.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "start_trialActivas"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # keep track of which components have finished
        start_trialActivasComponents = [end_training_2, key_resp_4]
        for thisComponent in start_trialActivasComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        start_trialActivasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "start_trialActivas"-------
        while continueRoutine:
            # get current time
            t = start_trialActivasClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=start_trialActivasClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *end_training_2* updates
            if end_training_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                end_training_2.frameNStart = frameN  # exact frame index
                end_training_2.tStart = t  # local t and not account for scr refresh
                end_training_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(end_training_2, 'tStartRefresh')  # time at next scr refresh
                end_training_2.setAutoDraw(True)
            
            # *key_resp_4* updates
            waitOnFlip = False
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_trialActivasComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "start_trialActivas"-------
        for thisComponent in start_trialActivasComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        BlockActivas.addData('end_training_2.started', end_training_2.tStartRefresh)
        BlockActivas.addData('end_training_2.stopped', end_training_2.tStopRefresh)
        parar_el_trial = False
        previous_count = 0 
        current_count = 0
        # the Routine "start_trialActivas" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trialActivas = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions("datasets/Dataset_"+ordenactivas[BlockActivas.thisN]+".xlsx"),
            seed=None, name='trialActivas')
        thisExp.addLoop(trialActivas)  # add the loop to the experiment
        thisTrialActiva = trialActivas.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialActiva.rgb)
        if thisTrialActiva != None:
            for paramName in thisTrialActiva:
                exec('{} = thisTrialActiva[paramName]'.format(paramName))
        
        for thisTrialActiva in trialActivas:
            currentLoop = trialActivas
            # abbreviate parameter names if possible (e.g. rgb = thisTrialActiva.rgb)
            if thisTrialActiva != None:
                for paramName in thisTrialActiva:
                    exec('{} = thisTrialActiva[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "drift_press_activas"-------
            continueRoutine = True
            # update component parameters for each repeat
            start_trainPR_2.setSound('datasets/trial_init.wav', secs=0.5, hamming=True)
            start_trainPR_2.setVolume(1.0, log=False)
            key_resp_5.keys = []
            key_resp_5.rt = []
            _key_resp_5_allKeys = []
            # keep track of which components have finished
            drift_press_activasComponents = [start_trainPR_2, drift_trainPR_2, firstfix_activas, key_resp_5]
            for thisComponent in drift_press_activasComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            drift_press_activasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "drift_press_activas"-------
            while continueRoutine:
                # get current time
                t = drift_press_activasClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=drift_press_activasClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # start/stop start_trainPR_2
                if start_trainPR_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    start_trainPR_2.frameNStart = frameN  # exact frame index
                    start_trainPR_2.tStart = t  # local t and not account for scr refresh
                    start_trainPR_2.tStartRefresh = tThisFlipGlobal  # on global time
                    start_trainPR_2.play(when=win)  # sync with win flip
                if start_trainPR_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > start_trainPR_2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        start_trainPR_2.tStop = t  # not accounting for scr refresh
                        start_trainPR_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(start_trainPR_2, 'tStopRefresh')  # time at next scr refresh
                        start_trainPR_2.stop()
                
                # *drift_trainPR_2* updates
                if drift_trainPR_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    drift_trainPR_2.frameNStart = frameN  # exact frame index
                    drift_trainPR_2.tStart = t  # local t and not account for scr refresh
                    drift_trainPR_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(drift_trainPR_2, 'tStartRefresh')  # time at next scr refresh
                    drift_trainPR_2.setAutoDraw(True)
                if drift_trainPR_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > drift_trainPR_2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        drift_trainPR_2.tStop = t  # not accounting for scr refresh
                        drift_trainPR_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(drift_trainPR_2, 'tStopRefresh')  # time at next scr refresh
                        drift_trainPR_2.setAutoDraw(False)
                
                # *firstfix_activas* updates
                if firstfix_activas.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    firstfix_activas.frameNStart = frameN  # exact frame index
                    firstfix_activas.tStart = t  # local t and not account for scr refresh
                    firstfix_activas.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(firstfix_activas, 'tStartRefresh')  # time at next scr refresh
                    firstfix_activas.setAutoDraw(True)
                
                # *key_resp_5* updates
                waitOnFlip = False
                if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_5.frameNStart = frameN  # exact frame index
                    key_resp_5.tStart = t  # local t and not account for scr refresh
                    key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                    key_resp_5.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_5.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
                    _key_resp_5_allKeys.extend(theseKeys)
                    if len(_key_resp_5_allKeys):
                        key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                        key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in drift_press_activasComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "drift_press_activas"-------
            for thisComponent in drift_press_activasComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            start_trainPR_2.stop()  # ensure sound has stopped at end of routine
            trialActivas.addData('firstfix_activas.started', firstfix_activas.tStartRefresh)
            trialActivas.addData('firstfix_activas.stopped', firstfix_activas.tStopRefresh)
            # check responses
            if key_resp_5.keys in ['', [], None]:  # No response was made
                key_resp_5.keys = None
            trialActivas.addData('key_resp_5.keys',key_resp_5.keys)
            if key_resp_5.keys != None:  # we had a response
                trialActivas.addData('key_resp_5.rt', key_resp_5.rt)
            trialActivas.addData('key_resp_5.started', key_resp_5.tStartRefresh)
            trialActivas.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
            # the Routine "drift_press_activas" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "first_fixActivas"-------
            continueRoutine = True
            # update component parameters for each repeat
            first_fix_active.setText('+')
            # keep track of which components have finished
            first_fixActivasComponents = [first_fix_active]
            for thisComponent in first_fixActivasComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            first_fixActivasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "first_fixActivas"-------
            while continueRoutine:
                # get current time
                t = first_fixActivasClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=first_fixActivasClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *first_fix_active* updates
                if first_fix_active.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    first_fix_active.frameNStart = frameN  # exact frame index
                    first_fix_active.tStart = t  # local t and not account for scr refresh
                    first_fix_active.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(first_fix_active, 'tStartRefresh')  # time at next scr refresh
                    first_fix_active.setAutoDraw(True)
                if first_fix_active.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > first_fix_active.tStartRefresh + fixation_time-frameTolerance:
                        # keep track of stop time/frame for later
                        first_fix_active.tStop = t  # not accounting for scr refresh
                        first_fix_active.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(first_fix_active, 'tStopRefresh')  # time at next scr refresh
                        first_fix_active.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in first_fixActivasComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "first_fixActivas"-------
            for thisComponent in first_fixActivasComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trialActivas.addData('first_fix_active.started', first_fix_active.tStartRefresh)
            trialActivas.addData('first_fix_active.stopped', first_fix_active.tStopRefresh)
            # the Routine "first_fixActivas" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            digitLoop_Activas = data.TrialHandler(nReps=digitSpan, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='digitLoop_Activas')
            thisExp.addLoop(digitLoop_Activas)  # add the loop to the experiment
            thisDigitLoop_Activa = digitLoop_Activas.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop_Activa.rgb)
            if thisDigitLoop_Activa != None:
                for paramName in thisDigitLoop_Activa:
                    exec('{} = thisDigitLoop_Activa[paramName]'.format(paramName))
            
            for thisDigitLoop_Activa in digitLoop_Activas:
                currentLoop = digitLoop_Activas
                # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop_Activa.rgb)
                if thisDigitLoop_Activa != None:
                    for paramName in thisDigitLoop_Activa:
                        exec('{} = thisDigitLoop_Activa[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "PresentationActivas"-------
                continueRoutine = True
                routineTimer.add(1.000000)
                # update component parameters for each repeat
                pres_text_active.setText(str(digits)[digitLoop_Activas.thisN]
)
                # keep track of which components have finished
                PresentationActivasComponents = [pres_text_active]
                for thisComponent in PresentationActivasComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                PresentationActivasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "PresentationActivas"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = PresentationActivasClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=PresentationActivasClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *pres_text_active* updates
                    if pres_text_active.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        pres_text_active.frameNStart = frameN  # exact frame index
                        pres_text_active.tStart = t  # local t and not account for scr refresh
                        pres_text_active.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(pres_text_active, 'tStartRefresh')  # time at next scr refresh
                        pres_text_active.setAutoDraw(True)
                    if pres_text_active.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > pres_text_active.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            pres_text_active.tStop = t  # not accounting for scr refresh
                            pres_text_active.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(pres_text_active, 'tStopRefresh')  # time at next scr refresh
                            pres_text_active.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in PresentationActivasComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "PresentationActivas"-------
                for thisComponent in PresentationActivasComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                digitLoop_Activas.addData('pres_text_active.started', pres_text_active.tStartRefresh)
                digitLoop_Activas.addData('pres_text_active.stopped', pres_text_active.tStopRefresh)
                thisExp.nextEntry()
                
            # completed digitSpan repeats of 'digitLoop_Activas'
            
            # get names of stimulus parameters
            if digitLoop_Activas.trialList in ([], [None], None):
                params = []
            else:
                params = digitLoop_Activas.trialList[0].keys()
            # save data for this loop
            digitLoop_Activas.saveAsText(filename + 'digitLoop_Activas.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # ------Prepare to start Routine "RecallActivas"-------
            continueRoutine = True
            # update component parameters for each repeat
            answer_box_2.reset()
            #counters of correct answers
            answer_active=int(answer)
            # keep track of which components have finished
            RecallActivasComponents = [recall_txt_2, answer_box_2]
            for thisComponent in RecallActivasComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            RecallActivasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "RecallActivas"-------
            while continueRoutine:
                # get current time
                t = RecallActivasClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=RecallActivasClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *recall_txt_2* updates
                if recall_txt_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    recall_txt_2.frameNStart = frameN  # exact frame index
                    recall_txt_2.tStart = t  # local t and not account for scr refresh
                    recall_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(recall_txt_2, 'tStartRefresh')  # time at next scr refresh
                    recall_txt_2.setAutoDraw(True)
                
                # *answer_box_2* updates
                if answer_box_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    answer_box_2.frameNStart = frameN  # exact frame index
                    answer_box_2.tStart = t  # local t and not account for scr refresh
                    answer_box_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(answer_box_2, 'tStartRefresh')  # time at next scr refresh
                    answer_box_2.setAutoDraw(True)
                if defaultKeyboard.getKeys(keyList=["return"]): #end routine when return is typed
                    answer_box_2.text = answer_box_2.text.rstrip() #deletes return from answer
                    if answer_box_2.text == str(answer_active): #if correct
                        correct = 1
                    else:
                        correct = 0
                    thisExp.addData('correct', correct)
                    continueRoutine = False #ends routine
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in RecallActivasComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "RecallActivas"-------
            for thisComponent in RecallActivasComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trialActivas.addData('recall_txt_2.started', recall_txt_2.tStartRefresh)
            trialActivas.addData('recall_txt_2.stopped', recall_txt_2.tStopRefresh)
            trialActivas.addData('answer_box_2.text',answer_box_2.text)
            trialActivas.addData('answer_box_2.started', answer_box_2.tStartRefresh)
            trialActivas.addData('answer_box_2.stopped', answer_box_2.tStopRefresh)
            ###trial 1 or 2 (span 3)
            if  trialActivas.thisTrialN == 0 or trialActivas.thisTrialN == 1: 
                if correct == 1: #if trial 1  
                    previous_count += 1
                    print(f' trial = {trialActivas.thisTrialN} previous_count = {previous_count}')
                    
            ###trial 3 or 4 (span 4)
            elif trialActivas.thisTrialN == 2 or trialActivas.thisTrialN == 3: 
                if correct == 1:
                    current_count +=1 #else (if incorrect, do nothing)
                    print(f' trial = {trialActivas.thisTrialN} current_count = {current_count}')
            if trialActivas.thisTrialN == 3: 
                if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                    parar_el_trial = True
                    print(f'trial = {trialActivas.thisTrialN} parar_el_trial = {parar_el_trial}')
                else: #if at least one correct, continue routine, and reset counters
                    previous_count = current_count #previous count equals corrects at trials 3 and 4
                    current_count = 0 
                print(f' trial = {trialActivas.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
                            
            ###trial 5 or 6 (span 5)
            elif trialActivas.thisTrialN == 4 or trialActivas.thisTrialN == 5:
                if correct == 1:
                    current_count +=1 #else (if incorrect, do nothing)
                    print(f' trial = {trialActivas.thisTrialN} current_count = {current_count}')
            if trialActivas.thisTrialN == 5: 
                if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                    parar_el_trial = True
                    print(f'parar_el_trial = {parar_el_trial}')
                else: #if at least one correct, continue routine, and reset counters
                    previous_count = current_count #previous count equals corrects at trials 3 and 4
                    current_count = 0 
                print(f' trial = {trialActivas.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
                            
            ###trial 7 or 8 (span 6)
            elif trialActivas.thisTrialN == 6 or trialActivas.thisTrialN == 7:
                if correct == 1:
                    current_count +=1 #else (if incorrect, do nothing)
                    print(f' trial = {trialActivas.thisTrialN} current_count = {current_count}')
            if trialActivas.thisTrialN == 7: 
                if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                    parar_el_trial = True
                    print(f'parar_el_trial = {parar_el_trial}')
                else: #if at least one correct, continue routine, and reset counters
                    previous_count = current_count #previous count equals corrects at trials 3 and 4
                    current_count = 0 
                print(f' trial = {trialActivas.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
                             
            ###trial 9 or 10 (span 7)
            elif trialActivas.thisTrialN == 8 or trialActivas.thisTrialN == 9:
                if correct == 1:
                    current_count +=1 #else (if incorrect, do nothing)
                    print(f' trial = {trialActivas.thisTrialN} current_count = {current_count}')
            if trialActivas.thisTrialN == 9: 
                if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                    parar_el_trial = True
                    print(f'parar_el_trial = {parar_el_trial}')
                else: #if at least one correct, continue routine, and reset counters
                    previous_count = current_count #previous count equals corrects at trials 3 and 4
                    current_count = 0 
                print(f' trial = {trialActivas.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
                 
            ###trial 11 or 12 (span 8)
            elif trialActivas.thisTrialN == 10 or trialActivas.thisTrialN == 11:
                if correct == 1:
                    current_count +=1 #else (if incorrect, do nothing)
                    print(f' trial = {trialActivas.thisTrialN} current_count = {current_count}')
            if trialActivas.thisTrialN == 11: 
                if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                    parar_el_trial = True
                    print(f'parar_el_trial = {parar_el_trial}')
                else: #if at least one correct, continue routine, and reset counters
                    previous_count = current_count #previous count equals corrects at trials 3 and 4
                    current_count = 0 
                print(f' trial = {trialActivas.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
               
            ###trial 13 or 14 (span 9)
            elif trialActivas.thisTrialN == 12 or trialActivas.thisTrialN == 13:
                if correct == 1:
                    current_count +=1 #else (if incorrect, do nothing)
                    print(f' trial = {trialActivas.thisTrialN} current_count = {current_count}')
            if trialActivas.thisTrialN == 13: 
                if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                    parar_el_trial = True
                    print(f'parar_el_trial = {parar_el_trial}')
                else: #if at least one correct, continue routine, and reset counters
                    previous_count = current_count #previous count equals corrects at trials 3 and 4
                    current_count = 0 
                print(f' trial = {trialActivas.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
                
            ###trial 16 (span 10)
            #elif trial_PR.thisTrialN == 15:
            #    continueRoutine = False
            # the Routine "RecallActivas" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "post_recallActivas"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            post_recallActivasComponents = [postrecallPR_2]
            for thisComponent in post_recallActivasComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            post_recallActivasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "post_recallActivas"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = post_recallActivasClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=post_recallActivasClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *postrecallPR_2* updates
                if postrecallPR_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    postrecallPR_2.frameNStart = frameN  # exact frame index
                    postrecallPR_2.tStart = t  # local t and not account for scr refresh
                    postrecallPR_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(postrecallPR_2, 'tStartRefresh')  # time at next scr refresh
                    postrecallPR_2.setAutoDraw(True)
                if postrecallPR_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > postrecallPR_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        postrecallPR_2.tStop = t  # not accounting for scr refresh
                        postrecallPR_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(postrecallPR_2, 'tStopRefresh')  # time at next scr refresh
                        postrecallPR_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in post_recallActivasComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "post_recallActivas"-------
            for thisComponent in post_recallActivasComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trialActivas.addData('postrecallPR_2.started', postrecallPR_2.tStartRefresh)
            trialActivas.addData('postrecallPR_2.stopped', postrecallPR_2.tStopRefresh)
            if parar_el_trial:
                trialActivas.finished = True
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trialActivas'
        
        # get names of stimulus parameters
        if trialActivas.trialList in ([], [None], None):
            params = []
        else:
            params = trialActivas.trialList[0].keys()
        # save data for this loop
        trialActivas.saveAsText(filename + 'trialActivas.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "LickertActivas"-------
        continueRoutine = True
        # update component parameters for each repeat
        dif_licker_2.reset()
        # keep track of which components have finished
        LickertActivasComponents = [Dificultad_activas, dif_licker_2]
        for thisComponent in LickertActivasComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        LickertActivasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "LickertActivas"-------
        while continueRoutine:
            # get current time
            t = LickertActivasClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=LickertActivasClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Dificultad_activas* updates
            if Dificultad_activas.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Dificultad_activas.frameNStart = frameN  # exact frame index
                Dificultad_activas.tStart = t  # local t and not account for scr refresh
                Dificultad_activas.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Dificultad_activas, 'tStartRefresh')  # time at next scr refresh
                Dificultad_activas.setAutoDraw(True)
            
            # *dif_licker_2* updates
            if dif_licker_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dif_licker_2.frameNStart = frameN  # exact frame index
                dif_licker_2.tStart = t  # local t and not account for scr refresh
                dif_licker_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dif_licker_2, 'tStartRefresh')  # time at next scr refresh
                dif_licker_2.setAutoDraw(True)
            
            # Check dif_licker_2 for response to end routine
            if dif_licker_2.getRating() is not None and dif_licker_2.status == STARTED:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in LickertActivasComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "LickertActivas"-------
        for thisComponent in LickertActivasComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        BlockActivas.addData('Dificultad_activas.started', Dificultad_activas.tStartRefresh)
        BlockActivas.addData('Dificultad_activas.stopped', Dificultad_activas.tStopRefresh)
        BlockActivas.addData('dif_licker_2.response', dif_licker_2.getRating())
        BlockActivas.addData('dif_licker_2.rt', dif_licker_2.getRT())
        BlockActivas.addData('dif_licker_2.started', dif_licker_2.tStartRefresh)
        BlockActivas.addData('dif_licker_2.stopped', dif_licker_2.tStopRefresh)
        # the Routine "LickertActivas" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "EndTask"-------
        continueRoutine = True
        # update component parameters for each repeat
        siguiente_tarea.setText('Esta tarea terminó. \n* Presiona la barra para continuar con la siguiente*')
        key_resp_6.keys = []
        key_resp_6.rt = []
        _key_resp_6_allKeys = []
        # keep track of which components have finished
        EndTaskComponents = [siguiente_tarea, key_resp_6]
        for thisComponent in EndTaskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        EndTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "EndTask"-------
        while continueRoutine:
            # get current time
            t = EndTaskClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=EndTaskClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *siguiente_tarea* updates
            if siguiente_tarea.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                siguiente_tarea.frameNStart = frameN  # exact frame index
                siguiente_tarea.tStart = t  # local t and not account for scr refresh
                siguiente_tarea.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(siguiente_tarea, 'tStartRefresh')  # time at next scr refresh
                siguiente_tarea.setAutoDraw(True)
            
            # *key_resp_6* updates
            waitOnFlip = False
            if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                # keep track of start time/frame for later
                key_resp_6.frameNStart = frameN  # exact frame index
                key_resp_6.tStart = t  # local t and not account for scr refresh
                key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                key_resp_6.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_6.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_6_allKeys.extend(theseKeys)
                if len(_key_resp_6_allKeys):
                    key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                    key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EndTaskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "EndTask"-------
        for thisComponent in EndTaskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_6.keys in ['', [], None]:  # No response was made
            key_resp_6.keys = None
        BlockActivas.addData('key_resp_6.keys',key_resp_6.keys)
        if key_resp_6.keys != None:  # we had a response
            BlockActivas.addData('key_resp_6.rt', key_resp_6.rt)
        BlockActivas.addData('key_resp_6.started', key_resp_6.tStartRefresh)
        BlockActivas.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
        # the Routine "EndTask" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed nRepsBlockActivas repeats of 'BlockActivas'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Block_Order'

# get names of stimulus parameters
if Block_Order.trialList in ([], [None], None):
    params = []
else:
    params = Block_Order.trialList[0].keys()
# save data for this loop
Block_Order.saveAsText(filename + 'Block_Order.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Final"-------
continueRoutine = True
routineTimer.add(2.500000)
# update component parameters for each repeat
# keep track of which components have finished
FinalComponents = [text_2]
for thisComponent in FinalComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FinalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Final"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FinalClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FinalClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 2.5-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Final"-------
for thisComponent in FinalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
