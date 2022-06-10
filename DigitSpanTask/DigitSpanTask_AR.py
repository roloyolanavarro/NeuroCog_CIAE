#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on junio 10, 2022, at 17:42
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
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
expName = 'DigitSpanTask_AR'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\INU\\Documents\\GitHub\\NeuroCog_CIAE\\DigitSpanTask\\digit-span-visual\\DigitSpanTask_AR.py',
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
Bienvenida_text = visual.TextStim(win=win, name='Bienvenida_text',
    text='¡Bienvenid@!\n\nGracias por participar en nuestro estudio.\n\nPresiona "barra espaciadora" para ver las instrucciones',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_bienvenida = keyboard.Keyboard()
Bienvenida_img = visual.ImageStim(
    win=win,
    name='Bienvenida_img', 
    image='datasets/Bienvenida.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "Instrucciones"
InstruccionesClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "pre_fixation_train"
pre_fixation_trainClock = core.Clock()
start_train = sound.Sound('datasets/microwave-beep.wav', secs=0.5, stereo=True, hamming=True,
    name='start_train')
start_train.setVolume(1.0)
drift_train = visual.ImageStim(
    win=win,
    name='drift_train', 
    image='datasets/drift.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
fixation_press_training = visual.TextStim(win=win, name='fixation_press_training',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
activepress_training = keyboard.Keyboard()

# Initialize components for Routine "firstfix_training"
firstfix_trainingClock = core.Clock()
firstfixtrain = visual.TextStim(win=win, name='firstfixtrain',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

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
next_train = visual.ButtonStim(win, 
    text='Siguiente', font='Arial',
    pos=(0, -5),units='cm',
    letterHeight=1.0,
    size=(8,1.5), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-center',
    name='next_train'
)
next_train.buttonClock = core.Clock()

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

# Initialize components for Routine "press_fix"
press_fixClock = core.Clock()
start_AR = sound.Sound('datasets/microwave-beep.wav', secs=0.5, stereo=True, hamming=True,
    name='start_AR')
start_AR.setVolume(1.0)
drift_AR = visual.ImageStim(
    win=win,
    name='drift_AR', 
    image='datasets/drift.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
press_fixation = visual.TextStim(win=win, name='press_fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
active_press = keyboard.Keyboard()

# Initialize components for Routine "first_fixation"
first_fixationClock = core.Clock()
first_fix = visual.TextStim(win=win, name='first_fix',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Presentation"
PresentationClock = core.Clock()
pres_text = visual.TextStim(win=win, name='pres_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Recall"
RecallClock = core.Clock()
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
button_next = visual.ButtonStim(win, 
    text='Siguiente', font='Arial',
    pos=(0, -5),units='cm',
    letterHeight=1.0,
    size=(8,1.5), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-center',
    name='button_next'
)
button_next.buttonClock = core.Clock()

# Initialize components for Routine "Lickert"
LickertClock = core.Clock()
Dificultad = visual.TextStim(win=win, name='Dificultad',
    text='¿Cuán difícil encontraste la tarea en general?',
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

# Initialize components for Routine "End"
EndClock = core.Clock()
thank_you = visual.TextStim(win=win, name='thank_you',
    text='El experimento terminó.\n¡Gracias por participar!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
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
BienvenidaComponents = [Bienvenida_text, key_bienvenida, Bienvenida_img]
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
    
    # *Bienvenida_text* updates
    if Bienvenida_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Bienvenida_text.frameNStart = frameN  # exact frame index
        Bienvenida_text.tStart = t  # local t and not account for scr refresh
        Bienvenida_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Bienvenida_text, 'tStartRefresh')  # time at next scr refresh
        Bienvenida_text.setAutoDraw(True)
    
    # *key_bienvenida* updates
    if key_bienvenida.status == NOT_STARTED and t >= 0.0-frameTolerance:
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

# set up handler to look after randomisation of conditions etc
instrucloop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('datasets/instructions.xlsx'),
    seed=None, name='instrucloop')
thisExp.addLoop(instrucloop)  # add the loop to the experiment
thisInstrucloop = instrucloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstrucloop.rgb)
if thisInstrucloop != None:
    for paramName in thisInstrucloop:
        exec('{} = thisInstrucloop[paramName]'.format(paramName))

for thisInstrucloop in instrucloop:
    currentLoop = instrucloop
    # abbreviate parameter names if possible (e.g. rgb = thisInstrucloop.rgb)
    if thisInstrucloop != None:
        for paramName in thisInstrucloop:
            exec('{} = thisInstrucloop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instrucciones"-------
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(instrucciones_activa)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    InstruccionesComponents = [image, key_resp_2]
    for thisComponent in InstruccionesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InstruccionesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Instrucciones"-------
    while continueRoutine:
        # get current time
        t = InstruccionesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstruccionesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        for thisComponent in InstruccionesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instrucciones"-------
    for thisComponent in InstruccionesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Instrucciones" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'instrucloop'


# set up handler to look after randomisation of conditions etc
trial_trainingAR = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('datasets/training_ar.xlsx'),
    seed=None, name='trial_trainingAR')
thisExp.addLoop(trial_trainingAR)  # add the loop to the experiment
thisTrial_trainingAR = trial_trainingAR.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_trainingAR.rgb)
if thisTrial_trainingAR != None:
    for paramName in thisTrial_trainingAR:
        exec('{} = thisTrial_trainingAR[paramName]'.format(paramName))

for thisTrial_trainingAR in trial_trainingAR:
    currentLoop = trial_trainingAR
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_trainingAR.rgb)
    if thisTrial_trainingAR != None:
        for paramName in thisTrial_trainingAR:
            exec('{} = thisTrial_trainingAR[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "pre_fixation_train"-------
    continueRoutine = True
    # update component parameters for each repeat
    start_train.setSound('datasets/microwave-beep.wav', secs=0.5, hamming=True)
    start_train.setVolume(1.0, log=False)
    activepress_training.keys = []
    activepress_training.rt = []
    _activepress_training_allKeys = []
    # keep track of which components have finished
    pre_fixation_trainComponents = [start_train, drift_train, fixation_press_training, activepress_training]
    for thisComponent in pre_fixation_trainComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pre_fixation_trainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pre_fixation_train"-------
    while continueRoutine:
        # get current time
        t = pre_fixation_trainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pre_fixation_trainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop start_train
        if start_train.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_train.frameNStart = frameN  # exact frame index
            start_train.tStart = t  # local t and not account for scr refresh
            start_train.tStartRefresh = tThisFlipGlobal  # on global time
            start_train.play(when=win)  # sync with win flip
        if start_train.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_train.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                start_train.tStop = t  # not accounting for scr refresh
                start_train.frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_train, 'tStopRefresh')  # time at next scr refresh
                start_train.stop()
        
        # *drift_train* updates
        if drift_train.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            drift_train.frameNStart = frameN  # exact frame index
            drift_train.tStart = t  # local t and not account for scr refresh
            drift_train.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(drift_train, 'tStartRefresh')  # time at next scr refresh
            drift_train.setAutoDraw(True)
        if drift_train.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > drift_train.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                drift_train.tStop = t  # not accounting for scr refresh
                drift_train.frameNStop = frameN  # exact frame index
                win.timeOnFlip(drift_train, 'tStopRefresh')  # time at next scr refresh
                drift_train.setAutoDraw(False)
        
        # *fixation_press_training* updates
        if fixation_press_training.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            fixation_press_training.frameNStart = frameN  # exact frame index
            fixation_press_training.tStart = t  # local t and not account for scr refresh
            fixation_press_training.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_press_training, 'tStartRefresh')  # time at next scr refresh
            fixation_press_training.setAutoDraw(True)
        
        # *activepress_training* updates
        waitOnFlip = False
        if activepress_training.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            activepress_training.frameNStart = frameN  # exact frame index
            activepress_training.tStart = t  # local t and not account for scr refresh
            activepress_training.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(activepress_training, 'tStartRefresh')  # time at next scr refresh
            activepress_training.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(activepress_training.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(activepress_training.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if activepress_training.status == STARTED and not waitOnFlip:
            theseKeys = activepress_training.getKeys(keyList=['space'], waitRelease=False)
            _activepress_training_allKeys.extend(theseKeys)
            if len(_activepress_training_allKeys):
                activepress_training.keys = _activepress_training_allKeys[-1].name  # just the last key pressed
                activepress_training.rt = _activepress_training_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pre_fixation_trainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pre_fixation_train"-------
    for thisComponent in pre_fixation_trainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    start_train.stop()  # ensure sound has stopped at end of routine
    trial_trainingAR.addData('fixation_press_training.started', fixation_press_training.tStartRefresh)
    trial_trainingAR.addData('fixation_press_training.stopped', fixation_press_training.tStopRefresh)
    # the Routine "pre_fixation_train" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "firstfix_training"-------
    continueRoutine = True
    # update component parameters for each repeat
    firstfixtrain.setText('+')
    # keep track of which components have finished
    firstfix_trainingComponents = [firstfixtrain]
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
        
        # *firstfixtrain* updates
        if firstfixtrain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            firstfixtrain.frameNStart = frameN  # exact frame index
            firstfixtrain.tStart = t  # local t and not account for scr refresh
            firstfixtrain.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(firstfixtrain, 'tStartRefresh')  # time at next scr refresh
            firstfixtrain.setAutoDraw(True)
        if firstfixtrain.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > firstfixtrain.tStartRefresh + fixation_time_trainAR-frameTolerance:
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
    trial_trainingAR.addData('firstfixtrain.started', firstfixtrain.tStartRefresh)
    trial_trainingAR.addData('firstfixtrain.stopped', firstfixtrain.tStopRefresh)
    # the Routine "firstfix_training" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    train_digitloopAR = data.TrialHandler(nReps=digitSpan_trainAR, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='train_digitloopAR')
    thisExp.addLoop(train_digitloopAR)  # add the loop to the experiment
    thisTrain_digitloopAR = train_digitloopAR.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrain_digitloopAR.rgb)
    if thisTrain_digitloopAR != None:
        for paramName in thisTrain_digitloopAR:
            exec('{} = thisTrain_digitloopAR[paramName]'.format(paramName))
    
    for thisTrain_digitloopAR in train_digitloopAR:
        currentLoop = train_digitloopAR
        # abbreviate parameter names if possible (e.g. rgb = thisTrain_digitloopAR.rgb)
        if thisTrain_digitloopAR != None:
            for paramName in thisTrain_digitloopAR:
                exec('{} = thisTrain_digitloopAR[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "presentation_training"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        digitpresentation_training.setText(str(digits_trainAR)[train_digitloopAR.thisN])
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
        train_digitloopAR.addData('digitpresentation_training.started', digitpresentation_training.tStartRefresh)
        train_digitloopAR.addData('digitpresentation_training.stopped', digitpresentation_training.tStopRefresh)
        thisExp.nextEntry()
        
    # completed digitSpan_trainAR repeats of 'train_digitloopAR'
    
    
    # ------Prepare to start Routine "recall_training"-------
    continueRoutine = True
    # update component parameters for each repeat
    answ_train.reset()
    # keep track of which components have finished
    recall_trainingComponents = [recall_train, answ_train, next_train]
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
        
        # *next_train* updates
        if next_train.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            next_train.frameNStart = frameN  # exact frame index
            next_train.tStart = t  # local t and not account for scr refresh
            next_train.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_train, 'tStartRefresh')  # time at next scr refresh
            next_train.setAutoDraw(True)
        if next_train.status == STARTED:
            # check whether next_train has been pressed
            if next_train.isClicked:
                if not next_train.wasClicked:
                    next_train.timesOn.append(next_train.buttonClock.getTime()) # store time of first click
                    next_train.timesOff.append(next_train.buttonClock.getTime()) # store time clicked until
                else:
                    next_train.timesOff[-1] = next_train.buttonClock.getTime() # update time clicked until
                if not next_train.wasClicked:
                    continueRoutine = False  # end routine when next_train is clicked
                    None
                next_train.wasClicked = True  # if next_train is still clicked next frame, it is not a new click
            else:
                next_train.wasClicked = False  # if next_train is clicked next frame, it is a new click
        else:
            next_train.wasClicked = False  # if next_train is clicked next frame, it is a new click
        
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
    trial_trainingAR.addData('recall_train.started', recall_train.tStartRefresh)
    trial_trainingAR.addData('recall_train.stopped', recall_train.tStopRefresh)
    trial_trainingAR.addData('answ_train.text',answ_train.text)
    trial_trainingAR.addData('answ_train.started', answ_train.tStartRefresh)
    trial_trainingAR.addData('answ_train.stopped', answ_train.tStopRefresh)
    trial_trainingAR.addData('next_train.numClicks', next_train.numClicks)
    if next_train.numClicks:
       trial_trainingAR.addData('next_train.timesOn', next_train.timesOn)
       trial_trainingAR.addData('next_train.timesOff', next_train.timesOff)
    else:
       trial_trainingAR.addData('next_train.timesOn', "")
       trial_trainingAR.addData('next_train.timesOff', "")
    if answ_train.text == str(answer_trainAR):
        correct = 1
        fbTxt = 'Correct!'
    else:
        correct = 0
        fbTxt = 'Incorrect'
    thisExp.addData('correct', correct)
    # the Routine "recall_training" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trial_trainingAR'


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
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
thisExp.addData('end_training.started', end_training.tStartRefresh)
thisExp.addData('end_training.stopped', end_training.tStopRefresh)
# the Routine "start_trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trial_AR = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('datasets/Dataset_AR.xlsx'),
    seed=None, name='trial_AR')
thisExp.addLoop(trial_AR)  # add the loop to the experiment
thisTrial_AR = trial_AR.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_AR.rgb)
if thisTrial_AR != None:
    for paramName in thisTrial_AR:
        exec('{} = thisTrial_AR[paramName]'.format(paramName))

for thisTrial_AR in trial_AR:
    currentLoop = trial_AR
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_AR.rgb)
    if thisTrial_AR != None:
        for paramName in thisTrial_AR:
            exec('{} = thisTrial_AR[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "press_fix"-------
    continueRoutine = True
    # update component parameters for each repeat
    start_AR.setSound('datasets/microwave-beep.wav', secs=0.5, hamming=True)
    start_AR.setVolume(1.0, log=False)
    active_press.keys = []
    active_press.rt = []
    _active_press_allKeys = []
    # keep track of which components have finished
    press_fixComponents = [start_AR, drift_AR, press_fixation, active_press]
    for thisComponent in press_fixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    press_fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "press_fix"-------
    while continueRoutine:
        # get current time
        t = press_fixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=press_fixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop start_AR
        if start_AR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_AR.frameNStart = frameN  # exact frame index
            start_AR.tStart = t  # local t and not account for scr refresh
            start_AR.tStartRefresh = tThisFlipGlobal  # on global time
            start_AR.play(when=win)  # sync with win flip
        if start_AR.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_AR.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                start_AR.tStop = t  # not accounting for scr refresh
                start_AR.frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_AR, 'tStopRefresh')  # time at next scr refresh
                start_AR.stop()
        
        # *drift_AR* updates
        if drift_AR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            drift_AR.frameNStart = frameN  # exact frame index
            drift_AR.tStart = t  # local t and not account for scr refresh
            drift_AR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(drift_AR, 'tStartRefresh')  # time at next scr refresh
            drift_AR.setAutoDraw(True)
        if drift_AR.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > drift_AR.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                drift_AR.tStop = t  # not accounting for scr refresh
                drift_AR.frameNStop = frameN  # exact frame index
                win.timeOnFlip(drift_AR, 'tStopRefresh')  # time at next scr refresh
                drift_AR.setAutoDraw(False)
        
        # *press_fixation* updates
        if press_fixation.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            press_fixation.frameNStart = frameN  # exact frame index
            press_fixation.tStart = t  # local t and not account for scr refresh
            press_fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(press_fixation, 'tStartRefresh')  # time at next scr refresh
            press_fixation.setAutoDraw(True)
        
        # *active_press* updates
        waitOnFlip = False
        if active_press.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            active_press.frameNStart = frameN  # exact frame index
            active_press.tStart = t  # local t and not account for scr refresh
            active_press.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(active_press, 'tStartRefresh')  # time at next scr refresh
            active_press.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(active_press.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(active_press.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if active_press.status == STARTED and not waitOnFlip:
            theseKeys = active_press.getKeys(keyList=['space'], waitRelease=False)
            _active_press_allKeys.extend(theseKeys)
            if len(_active_press_allKeys):
                active_press.keys = _active_press_allKeys[-1].name  # just the last key pressed
                active_press.rt = _active_press_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in press_fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "press_fix"-------
    for thisComponent in press_fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    start_AR.stop()  # ensure sound has stopped at end of routine
    trial_AR.addData('press_fixation.started', press_fixation.tStartRefresh)
    trial_AR.addData('press_fixation.stopped', press_fixation.tStopRefresh)
    # the Routine "press_fix" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "first_fixation"-------
    continueRoutine = True
    # update component parameters for each repeat
    first_fix.setText('+')
    # keep track of which components have finished
    first_fixationComponents = [first_fix]
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
        
        # *first_fix* updates
        if first_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            first_fix.frameNStart = frameN  # exact frame index
            first_fix.tStart = t  # local t and not account for scr refresh
            first_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(first_fix, 'tStartRefresh')  # time at next scr refresh
            first_fix.setAutoDraw(True)
        if first_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > first_fix.tStartRefresh + fixation_time_AR-frameTolerance:
                # keep track of stop time/frame for later
                first_fix.tStop = t  # not accounting for scr refresh
                first_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(first_fix, 'tStopRefresh')  # time at next scr refresh
                first_fix.setAutoDraw(False)
        
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
    trial_AR.addData('first_fix.started', first_fix.tStartRefresh)
    trial_AR.addData('first_fix.stopped', first_fix.tStopRefresh)
    # the Routine "first_fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    digitLoop_AR = data.TrialHandler(nReps=digitSpan_AR, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='digitLoop_AR')
    thisExp.addLoop(digitLoop_AR)  # add the loop to the experiment
    thisDigitLoop_AR = digitLoop_AR.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop_AR.rgb)
    if thisDigitLoop_AR != None:
        for paramName in thisDigitLoop_AR:
            exec('{} = thisDigitLoop_AR[paramName]'.format(paramName))
    
    for thisDigitLoop_AR in digitLoop_AR:
        currentLoop = digitLoop_AR
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop_AR.rgb)
        if thisDigitLoop_AR != None:
            for paramName in thisDigitLoop_AR:
                exec('{} = thisDigitLoop_AR[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Presentation"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        pres_text.setText(str(digits_AR)[digitLoop_AR.thisN])
        # keep track of which components have finished
        PresentationComponents = [pres_text]
        for thisComponent in PresentationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PresentationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Presentation"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = PresentationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PresentationClock)
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
            for thisComponent in PresentationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Presentation"-------
        for thisComponent in PresentationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        digitLoop_AR.addData('pres_text.started', pres_text.tStartRefresh)
        digitLoop_AR.addData('pres_text.stopped', pres_text.tStopRefresh)
    # completed digitSpan_AR repeats of 'digitLoop_AR'
    
    
    # ------Prepare to start Routine "Recall"-------
    continueRoutine = True
    # update component parameters for each repeat
    answer_box.reset()
    # keep track of which components have finished
    RecallComponents = [recall_txt, answer_box, button_next]
    for thisComponent in RecallComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RecallClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Recall"-------
    while continueRoutine:
        # get current time
        t = RecallClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RecallClock)
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
        
        # *button_next* updates
        if button_next.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button_next.frameNStart = frameN  # exact frame index
            button_next.tStart = t  # local t and not account for scr refresh
            button_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_next, 'tStartRefresh')  # time at next scr refresh
            button_next.setAutoDraw(True)
        if button_next.status == STARTED:
            # check whether button_next has been pressed
            if button_next.isClicked:
                if not button_next.wasClicked:
                    button_next.timesOn.append(button_next.buttonClock.getTime()) # store time of first click
                    button_next.timesOff.append(button_next.buttonClock.getTime()) # store time clicked until
                else:
                    button_next.timesOff[-1] = button_next.buttonClock.getTime() # update time clicked until
                if not button_next.wasClicked:
                    continueRoutine = False  # end routine when button_next is clicked
                    None
                button_next.wasClicked = True  # if button_next is still clicked next frame, it is not a new click
            else:
                button_next.wasClicked = False  # if button_next is clicked next frame, it is a new click
        else:
            button_next.wasClicked = False  # if button_next is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RecallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Recall"-------
    for thisComponent in RecallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial_AR.addData('recall_txt.started', recall_txt.tStartRefresh)
    trial_AR.addData('recall_txt.stopped', recall_txt.tStopRefresh)
    trial_AR.addData('answer_box.text',answer_box.text)
    trial_AR.addData('answer_box.started', answer_box.tStartRefresh)
    trial_AR.addData('answer_box.stopped', answer_box.tStopRefresh)
    trial_AR.addData('button_next.numClicks', button_next.numClicks)
    if button_next.numClicks:
       trial_AR.addData('button_next.timesOn', button_next.timesOn)
       trial_AR.addData('button_next.timesOff', button_next.timesOff)
    else:
       trial_AR.addData('button_next.timesOn', "")
       trial_AR.addData('button_next.timesOff', "")
    if answer_box.text == str(answer_AR):
        correct = 1
        fbTxt = 'Correct!'
    else:
        correct = 0
        fbTxt = 'Incorrect'
    thisExp.addData('correct', correct)
    # the Routine "Recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trial_AR'


# ------Prepare to start Routine "Lickert"-------
continueRoutine = True
# update component parameters for each repeat
dif_licker.reset()
# keep track of which components have finished
LickertComponents = [Dificultad, dif_licker]
for thisComponent in LickertComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
LickertClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Lickert"-------
while continueRoutine:
    # get current time
    t = LickertClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=LickertClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Dificultad* updates
    if Dificultad.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Dificultad.frameNStart = frameN  # exact frame index
        Dificultad.tStart = t  # local t and not account for scr refresh
        Dificultad.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Dificultad, 'tStartRefresh')  # time at next scr refresh
        Dificultad.setAutoDraw(True)
    
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
    for thisComponent in LickertComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Lickert"-------
for thisComponent in LickertComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Dificultad.started', Dificultad.tStartRefresh)
thisExp.addData('Dificultad.stopped', Dificultad.tStopRefresh)
thisExp.addData('dif_licker.response', dif_licker.getRating())
thisExp.addData('dif_licker.rt', dif_licker.getRT())
thisExp.addData('dif_licker.started', dif_licker.tStartRefresh)
thisExp.addData('dif_licker.stopped', dif_licker.tStopRefresh)
# the Routine "Lickert" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "End"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [thank_you]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thank_you* updates
    if thank_you.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank_you.frameNStart = frameN  # exact frame index
        thank_you.tStart = t  # local t and not account for scr refresh
        thank_you.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank_you, 'tStartRefresh')  # time at next scr refresh
        thank_you.setAutoDraw(True)
    if thank_you.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thank_you.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            thank_you.tStop = t  # not accounting for scr refresh
            thank_you.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thank_you, 'tStopRefresh')  # time at next scr refresh
            thank_you.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

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
