#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on julio 01, 2022, at 15:49
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
expName = 'DigitSpanTask_PR2'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\INU\\Documents\\GitHub\\NeuroCog_CIAE\\DigitSpanTask\\PR_PF_AR_AF_lastrun.py',
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

# Initialize components for Routine "InstruccionesPR"
InstruccionesPRClock = core.Clock()
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
first_fix = visual.TextStim(win=win, name='first_fix',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

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
#counters of correct answers
previous_count = 0 
current_count = 0

# Initialize components for Routine "post_recallPR"
post_recallPRClock = core.Clock()
postrecallPR = visual.TextStim(win=win, name='postrecallPR',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

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

# Initialize components for Routine "End1"
End1Clock = core.Clock()
thank_you = visual.TextStim(win=win, name='thank_you',
    text='Esta prueba terminó. \n\nLlevamos 1 de 4 pruebas.\n\nContinuaremos con la siguiente.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Instr_PF"
Instr_PFClock = core.Clock()
image2_2 = visual.ImageStim(
    win=win,
    name='image2_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "firstfix_trainPF"
firstfix_trainPFClock = core.Clock()
drift_trainPR_2 = visual.ImageStim(
    win=win,
    name='drift_trainPR_2', 
    image='datasets/drift.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
start_trainPR_2 = sound.Sound('datasets/trial_init.wav', secs=0.5, stereo=True, hamming=True,
    name='start_trainPR_2')
start_trainPR_2.setVolume(1.0)
firstfixtrain_2 = visual.TextStim(win=win, name='firstfixtrain_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "present_train_PF"
present_train_PFClock = core.Clock()
digitpresentation_training_2 = visual.TextStim(win=win, name='digitpresentation_training_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "recall_trainPF"
recall_trainPFClock = core.Clock()
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

# Initialize components for Routine "post_recall_train_PF"
post_recall_train_PFClock = core.Clock()
post_recall_training_2 = visual.TextStim(win=win, name='post_recall_training_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "start_trialPF"
start_trialPFClock = core.Clock()
end_training_2 = visual.ImageStim(
    win=win,
    name='end_training_2', 
    image='datasets/finpractica.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "first_fixPF"
first_fixPFClock = core.Clock()
driftPR_2 = visual.ImageStim(
    win=win,
    name='driftPR_2', 
    image='datasets/drift.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
startPR_2 = sound.Sound('datasets/trial_init.wav', secs=0.5, stereo=True, hamming=True,
    name='startPR_2')
startPR_2.setVolume(1.0)
first_fix_2 = visual.TextStim(win=win, name='first_fix_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "PresentationPF"
PresentationPFClock = core.Clock()
pres_text_2 = visual.TextStim(win=win, name='pres_text_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "RecallPF"
RecallPFClock = core.Clock()
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
#counters of correct answers
previous_count = 0 
current_count = 0

# Initialize components for Routine "post_recallPF"
post_recallPFClock = core.Clock()
postrecallPR_2 = visual.TextStim(win=win, name='postrecallPR_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "LickertPF"
LickertPFClock = core.Clock()
Dificultad_2 = visual.TextStim(win=win, name='Dificultad_2',
    text='¿Cuán difícil encontraste la tarea en general?',
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

# Initialize components for Routine "End2"
End2Clock = core.Clock()
thank_you_2 = visual.TextStim(win=win, name='thank_you_2',
    text='Esta prueba terminó. \n\nLlevamos 2 de 4 pruebas.\n\nContinuaremos con la siguiente.',
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
PR_task = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='PR_task')
thisExp.addLoop(PR_task)  # add the loop to the experiment
thisPR_task = PR_task.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPR_task.rgb)
if thisPR_task != None:
    for paramName in thisPR_task:
        exec('{} = thisPR_task[paramName]'.format(paramName))

for thisPR_task in PR_task:
    currentLoop = PR_task
    # abbreviate parameter names if possible (e.g. rgb = thisPR_task.rgb)
    if thisPR_task != None:
        for paramName in thisPR_task:
            exec('{} = thisPR_task[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    instrucloop_PR = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('datasets/instructions.xlsx'),
        seed=None, name='instrucloop_PR')
    thisExp.addLoop(instrucloop_PR)  # add the loop to the experiment
    thisInstrucloop_PR = instrucloop_PR.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstrucloop_PR.rgb)
    if thisInstrucloop_PR != None:
        for paramName in thisInstrucloop_PR:
            exec('{} = thisInstrucloop_PR[paramName]'.format(paramName))
    
    for thisInstrucloop_PR in instrucloop_PR:
        currentLoop = instrucloop_PR
        # abbreviate parameter names if possible (e.g. rgb = thisInstrucloop_PR.rgb)
        if thisInstrucloop_PR != None:
            for paramName in thisInstrucloop_PR:
                exec('{} = thisInstrucloop_PR[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "InstruccionesPR"-------
        continueRoutine = True
        # update component parameters for each repeat
        image2.setImage(instrucciones_pasiva)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        InstruccionesPRComponents = [image2, key_resp_2]
        for thisComponent in InstruccionesPRComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        InstruccionesPRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "InstruccionesPR"-------
        while continueRoutine:
            # get current time
            t = InstruccionesPRClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=InstruccionesPRClock)
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
            for thisComponent in InstruccionesPRComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "InstruccionesPR"-------
        for thisComponent in InstruccionesPRComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "InstruccionesPR" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'instrucloop_PR'
    
    
    # set up handler to look after randomisation of conditions etc
    trial_trainingPR = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('datasets/training_pr.xlsx'),
        seed=None, name='trial_trainingPR')
    thisExp.addLoop(trial_trainingPR)  # add the loop to the experiment
    thisTrial_trainingPR = trial_trainingPR.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_trainingPR.rgb)
    if thisTrial_trainingPR != None:
        for paramName in thisTrial_trainingPR:
            exec('{} = thisTrial_trainingPR[paramName]'.format(paramName))
    
    for thisTrial_trainingPR in trial_trainingPR:
        currentLoop = trial_trainingPR
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_trainingPR.rgb)
        if thisTrial_trainingPR != None:
            for paramName in thisTrial_trainingPR:
                exec('{} = thisTrial_trainingPR[paramName]'.format(paramName))
        
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
                if tThisFlipGlobal > firstfixtrain.tStartRefresh + fixation_time_trainPR-frameTolerance:
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
        trial_trainingPR.addData('firstfixtrain.started', firstfixtrain.tStartRefresh)
        trial_trainingPR.addData('firstfixtrain.stopped', firstfixtrain.tStopRefresh)
        # the Routine "firstfix_training" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        train_digitloopPR = data.TrialHandler(nReps=digitSpan_trainPR, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='train_digitloopPR')
        thisExp.addLoop(train_digitloopPR)  # add the loop to the experiment
        thisTrain_digitloopPR = train_digitloopPR.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrain_digitloopPR.rgb)
        if thisTrain_digitloopPR != None:
            for paramName in thisTrain_digitloopPR:
                exec('{} = thisTrain_digitloopPR[paramName]'.format(paramName))
        
        for thisTrain_digitloopPR in train_digitloopPR:
            currentLoop = train_digitloopPR
            # abbreviate parameter names if possible (e.g. rgb = thisTrain_digitloopPR.rgb)
            if thisTrain_digitloopPR != None:
                for paramName in thisTrain_digitloopPR:
                    exec('{} = thisTrain_digitloopPR[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "presentation_training"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            digitpresentation_training.setText(str(digits_trainPR)[train_digitloopPR.thisN])
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
            train_digitloopPR.addData('digitpresentation_training.started', digitpresentation_training.tStartRefresh)
            train_digitloopPR.addData('digitpresentation_training.stopped', digitpresentation_training.tStopRefresh)
            thisExp.nextEntry()
            
        # completed digitSpan_trainPR repeats of 'train_digitloopPR'
        
        
        # ------Prepare to start Routine "recall_training"-------
        continueRoutine = True
        # update component parameters for each repeat
        answ_train.reset()
        answer_trainPR=int(answer_trainPR)
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
                if answ_train.text == str(answer_trainPR):
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
        trial_trainingPR.addData('recall_train.started', recall_train.tStartRefresh)
        trial_trainingPR.addData('recall_train.stopped', recall_train.tStopRefresh)
        trial_trainingPR.addData('answ_train.text',answ_train.text)
        trial_trainingPR.addData('answ_train.started', answ_train.tStartRefresh)
        trial_trainingPR.addData('answ_train.stopped', answ_train.tStopRefresh)
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
        trial_trainingPR.addData('post_recall_training.started', post_recall_training.tStartRefresh)
        trial_trainingPR.addData('post_recall_training.stopped', post_recall_training.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trial_trainingPR'
    
    
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
    PR_task.addData('end_training.started', end_training.tStartRefresh)
    PR_task.addData('end_training.stopped', end_training.tStopRefresh)
    parar_el_trial = False
    # the Routine "start_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trial_PR = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('datasets/Dataset_PR.xlsx'),
        seed=None, name='trial_PR')
    thisExp.addLoop(trial_PR)  # add the loop to the experiment
    thisTrial_PR = trial_PR.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_PR.rgb)
    if thisTrial_PR != None:
        for paramName in thisTrial_PR:
            exec('{} = thisTrial_PR[paramName]'.format(paramName))
    
    for thisTrial_PR in trial_PR:
        currentLoop = trial_PR
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_PR.rgb)
        if thisTrial_PR != None:
            for paramName in thisTrial_PR:
                exec('{} = thisTrial_PR[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "first_fixation"-------
        continueRoutine = True
        # update component parameters for each repeat
        startPR.setSound('datasets/trial_init.wav', secs=0.5, hamming=True)
        startPR.setVolume(1.0, log=False)
        first_fix.setText('+')
        # keep track of which components have finished
        first_fixationComponents = [driftPR, startPR, first_fix]
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
            
            # *first_fix* updates
            if first_fix.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                first_fix.frameNStart = frameN  # exact frame index
                first_fix.tStart = t  # local t and not account for scr refresh
                first_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(first_fix, 'tStartRefresh')  # time at next scr refresh
                first_fix.setAutoDraw(True)
            if first_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > first_fix.tStartRefresh + fixation_time_PR-frameTolerance:
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
        startPR.stop()  # ensure sound has stopped at end of routine
        trial_PR.addData('first_fix.started', first_fix.tStartRefresh)
        trial_PR.addData('first_fix.stopped', first_fix.tStopRefresh)
        # the Routine "first_fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        digitLoop_PR = data.TrialHandler(nReps=digitSpan_PR, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='digitLoop_PR')
        thisExp.addLoop(digitLoop_PR)  # add the loop to the experiment
        thisDigitLoop_PR = digitLoop_PR.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop_PR.rgb)
        if thisDigitLoop_PR != None:
            for paramName in thisDigitLoop_PR:
                exec('{} = thisDigitLoop_PR[paramName]'.format(paramName))
        
        for thisDigitLoop_PR in digitLoop_PR:
            currentLoop = digitLoop_PR
            # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop_PR.rgb)
            if thisDigitLoop_PR != None:
                for paramName in thisDigitLoop_PR:
                    exec('{} = thisDigitLoop_PR[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "Presentation"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            pres_text.setText(str(digits_PR)[digitLoop_PR.thisN])
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
            digitLoop_PR.addData('pres_text.started', pres_text.tStartRefresh)
            digitLoop_PR.addData('pres_text.stopped', pres_text.tStopRefresh)
        # completed digitSpan_PR repeats of 'digitLoop_PR'
        
        
        # ------Prepare to start Routine "Recall"-------
        continueRoutine = True
        # update component parameters for each repeat
        answer_box.reset()
        answer_PR=int(answer_PR)
        
        
        
        # keep track of which components have finished
        RecallComponents = [recall_txt, answer_box]
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
            if defaultKeyboard.getKeys(keyList=["return"]): #end routine when return is typed
                answer_box.text = answer_box.text.rstrip() #deletes return from answer
                if answer_box.text == str(answer_PR): #if correct
                    correct = 1
                else:
                    correct = 0
                trial_trainingPR.addData('correct', correct)
                continueRoutine = False #ends routine
            
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
        trial_PR.addData('recall_txt.started', recall_txt.tStartRefresh)
        trial_PR.addData('recall_txt.stopped', recall_txt.tStopRefresh)
        trial_PR.addData('answer_box.text',answer_box.text)
        trial_PR.addData('answer_box.started', answer_box.tStartRefresh)
        trial_PR.addData('answer_box.stopped', answer_box.tStopRefresh)
        ###trial 1 or 2 (span 3)
        if  trial_PR.thisTrialN == 0 or trial_PR.thisTrialN == 1: 
            if correct == 1: #if trial 1  
                previous_count += 1
                print(f' trial = {trial_PR.thisTrialN} previous_count = {previous_count}')
                
        ###trial 3 or 4 (span 4)
        elif trial_PR.thisTrialN == 2 or trial_PR.thisTrialN == 3: 
            if correct == 1:
                current_count +=1 #else (if incorrect, do nothing)
                print(f' trial = {trial_PR.thisTrialN} current_count = {current_count}')
        if trial_PR.thisTrialN == 3: 
            if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                parar_el_trial = True
                print(f'trial = {trial_PR.thisTrialN} parar_el_trial = {parar_el_trial}')
            else: #if at least one correct, continue routine, and reset counters
                previous_count = current_count #previous count equals corrects at trials 3 and 4
                current_count = 0 
            print(f' trial = {trial_PR.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
                        
        ###trial 5 or 6 (span 5)
        elif trial_PR.thisTrialN == 4 or trial_PR.thisTrialN == 5:
            if correct == 1:
                current_count +=1 #else (if incorrect, do nothing)
                print(f' trial = {trial_PR.thisTrialN} current_count = {current_count}')
        if trial_PR.thisTrialN == 5: 
            if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                parar_el_trial = True
                print(f'parar_el_trial = {parar_el_trial}')
            else: #if at least one correct, continue routine, and reset counters
                previous_count = current_count #previous count equals corrects at trials 3 and 4
                current_count = 0 
            print(f' trial = {trial_PR.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
                        
        ###trial 7 or 8 (span 6)
        elif trial_PR.thisTrialN == 6 or trial_PR.thisTrialN == 7:
            if correct == 1:
                current_count +=1 #else (if incorrect, do nothing)
                print(f' trial = {trial_PR.thisTrialN} current_count = {current_count}')
        if trial_PR.thisTrialN == 7: 
            if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                parar_el_trial = True
                print(f'parar_el_trial = {parar_el_trial}')
            else: #if at least one correct, continue routine, and reset counters
                previous_count = current_count #previous count equals corrects at trials 3 and 4
                current_count = 0 
            print(f' trial = {trial_PR.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
                         
        ###trial 9 or 10 (span 7)
        elif trial_PR.thisTrialN == 8 or trial_PR.thisTrialN == 9:
            if correct == 1:
                current_count +=1 #else (if incorrect, do nothing)
                print(f' trial = {trial_PR.thisTrialN} current_count = {current_count}')
        if trial_PR.thisTrialN == 9: 
            if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                parar_el_trial = True
                print(f'parar_el_trial = {parar_el_trial}')
            else: #if at least one correct, continue routine, and reset counters
                previous_count = current_count #previous count equals corrects at trials 3 and 4
                current_count = 0 
            print(f' trial = {trial_PR.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
             
        ###trial 11 or 12 (span 8)
        elif trial_PR.thisTrialN == 10 or trial_PR.thisTrialN == 11:
            if correct == 1:
                current_count +=1 #else (if incorrect, do nothing)
                print(f' trial = {trial_PR.thisTrialN} current_count = {current_count}')
        if trial_PR.thisTrialN == 11: 
            if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                parar_el_trial = True
                print(f'parar_el_trial = {parar_el_trial}')
            else: #if at least one correct, continue routine, and reset counters
                previous_count = current_count #previous count equals corrects at trials 3 and 4
                current_count = 0 
            print(f' trial = {trial_PR.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
           
        ###trial 13 or 14 (span 9)
        elif trial_PR.thisTrialN == 12 or trial_PR.thisTrialN == 13:
            if correct == 1:
                current_count +=1 #else (if incorrect, do nothing)
                print(f' trial = {trial_PR.thisTrialN} current_count = {current_count}')
        if trial_PR.thisTrialN == 13: 
            if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                parar_el_trial = True
                print(f'parar_el_trial = {parar_el_trial}')
            else: #if at least one correct, continue routine, and reset counters
                previous_count = current_count #previous count equals corrects at trials 3 and 4
                current_count = 0 
            print(f' trial = {trial_PR.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
            
        ###trial 16 (span 10)
        #elif trial_PR.thisTrialN == 15:
        #    continueRoutine = False
        # the Routine "Recall" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "post_recallPR"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        post_recallPRComponents = [postrecallPR]
        for thisComponent in post_recallPRComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        post_recallPRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "post_recallPR"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = post_recallPRClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=post_recallPRClock)
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
            for thisComponent in post_recallPRComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "post_recallPR"-------
        for thisComponent in post_recallPRComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial_PR.addData('postrecallPR.started', postrecallPR.tStartRefresh)
        trial_PR.addData('postrecallPR.stopped', postrecallPR.tStopRefresh)
        if parar_el_trial:
            trial_PR.finished = True
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trial_PR'
    
    
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
    PR_task.addData('Dificultad.started', Dificultad.tStartRefresh)
    PR_task.addData('Dificultad.stopped', Dificultad.tStopRefresh)
    PR_task.addData('dif_licker.response', dif_licker.getRating())
    PR_task.addData('dif_licker.rt', dif_licker.getRT())
    PR_task.addData('dif_licker.started', dif_licker.tStartRefresh)
    PR_task.addData('dif_licker.stopped', dif_licker.tStopRefresh)
    # the Routine "Lickert" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'PR_task'


# ------Prepare to start Routine "End1"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
End1Components = [thank_you]
for thisComponent in End1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
End1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = End1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=End1Clock)
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
    for thisComponent in End1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End1"-------
for thisComponent in End1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
PF_task = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='PF_task')
thisExp.addLoop(PF_task)  # add the loop to the experiment
thisPF_task = PF_task.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPF_task.rgb)
if thisPF_task != None:
    for paramName in thisPF_task:
        exec('{} = thisPF_task[paramName]'.format(paramName))

for thisPF_task in PF_task:
    currentLoop = PF_task
    # abbreviate parameter names if possible (e.g. rgb = thisPF_task.rgb)
    if thisPF_task != None:
        for paramName in thisPF_task:
            exec('{} = thisPF_task[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    intrLoopPF = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('datasets/instructions.xlsx'),
        seed=None, name='intrLoopPF')
    thisExp.addLoop(intrLoopPF)  # add the loop to the experiment
    thisIntrLoopPF = intrLoopPF.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisIntrLoopPF.rgb)
    if thisIntrLoopPF != None:
        for paramName in thisIntrLoopPF:
            exec('{} = thisIntrLoopPF[paramName]'.format(paramName))
    
    for thisIntrLoopPF in intrLoopPF:
        currentLoop = intrLoopPF
        # abbreviate parameter names if possible (e.g. rgb = thisIntrLoopPF.rgb)
        if thisIntrLoopPF != None:
            for paramName in thisIntrLoopPF:
                exec('{} = thisIntrLoopPF[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Instr_PF"-------
        continueRoutine = True
        # update component parameters for each repeat
        image2_2.setImage(instrucciones_pasiva)
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        Instr_PFComponents = [image2_2, key_resp_3]
        for thisComponent in Instr_PFComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Instr_PFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Instr_PF"-------
        while continueRoutine:
            # get current time
            t = Instr_PFClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Instr_PFClock)
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
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            for thisComponent in Instr_PFComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Instr_PF"-------
        for thisComponent in Instr_PFComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "Instr_PF" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'intrLoopPF'
    
    
    # set up handler to look after randomisation of conditions etc
    trial_train_PF = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('datasets/training_pf.xlsx'),
        seed=None, name='trial_train_PF')
    thisExp.addLoop(trial_train_PF)  # add the loop to the experiment
    thisTrial_train_PF = trial_train_PF.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_train_PF.rgb)
    if thisTrial_train_PF != None:
        for paramName in thisTrial_train_PF:
            exec('{} = thisTrial_train_PF[paramName]'.format(paramName))
    
    for thisTrial_train_PF in trial_train_PF:
        currentLoop = trial_train_PF
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_train_PF.rgb)
        if thisTrial_train_PF != None:
            for paramName in thisTrial_train_PF:
                exec('{} = thisTrial_train_PF[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "firstfix_trainPF"-------
        continueRoutine = True
        # update component parameters for each repeat
        start_trainPR_2.setSound('datasets/trial_init.wav', secs=0.5, hamming=True)
        start_trainPR_2.setVolume(1.0, log=False)
        firstfixtrain_2.setText('+')
        # keep track of which components have finished
        firstfix_trainPFComponents = [drift_trainPR_2, start_trainPR_2, firstfixtrain_2]
        for thisComponent in firstfix_trainPFComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        firstfix_trainPFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "firstfix_trainPF"-------
        while continueRoutine:
            # get current time
            t = firstfix_trainPFClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=firstfix_trainPFClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
            
            # *firstfixtrain_2* updates
            if firstfixtrain_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                firstfixtrain_2.frameNStart = frameN  # exact frame index
                firstfixtrain_2.tStart = t  # local t and not account for scr refresh
                firstfixtrain_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(firstfixtrain_2, 'tStartRefresh')  # time at next scr refresh
                firstfixtrain_2.setAutoDraw(True)
            if firstfixtrain_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > firstfixtrain_2.tStartRefresh + fixation_time_trainPR-frameTolerance:
                    # keep track of stop time/frame for later
                    firstfixtrain_2.tStop = t  # not accounting for scr refresh
                    firstfixtrain_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(firstfixtrain_2, 'tStopRefresh')  # time at next scr refresh
                    firstfixtrain_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in firstfix_trainPFComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "firstfix_trainPF"-------
        for thisComponent in firstfix_trainPFComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        start_trainPR_2.stop()  # ensure sound has stopped at end of routine
        trial_train_PF.addData('firstfixtrain_2.started', firstfixtrain_2.tStartRefresh)
        trial_train_PF.addData('firstfixtrain_2.stopped', firstfixtrain_2.tStopRefresh)
        # the Routine "firstfix_trainPF" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        train_digitloop_PR = data.TrialHandler(nReps=digitSpan_trainPF, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='train_digitloop_PR')
        thisExp.addLoop(train_digitloop_PR)  # add the loop to the experiment
        thisTrain_digitloop_PR = train_digitloop_PR.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrain_digitloop_PR.rgb)
        if thisTrain_digitloop_PR != None:
            for paramName in thisTrain_digitloop_PR:
                exec('{} = thisTrain_digitloop_PR[paramName]'.format(paramName))
        
        for thisTrain_digitloop_PR in train_digitloop_PR:
            currentLoop = train_digitloop_PR
            # abbreviate parameter names if possible (e.g. rgb = thisTrain_digitloop_PR.rgb)
            if thisTrain_digitloop_PR != None:
                for paramName in thisTrain_digitloop_PR:
                    exec('{} = thisTrain_digitloop_PR[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "present_train_PF"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            digitpresentation_training_2.setText(str(digits_trainPR)[train_digitloopPR.thisN])
            # keep track of which components have finished
            present_train_PFComponents = [digitpresentation_training_2]
            for thisComponent in present_train_PFComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            present_train_PFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "present_train_PF"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = present_train_PFClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=present_train_PFClock)
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
                for thisComponent in present_train_PFComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "present_train_PF"-------
            for thisComponent in present_train_PFComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            train_digitloop_PR.addData('digitpresentation_training_2.started', digitpresentation_training_2.tStartRefresh)
            train_digitloop_PR.addData('digitpresentation_training_2.stopped', digitpresentation_training_2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed digitSpan_trainPF repeats of 'train_digitloop_PR'
        
        
        # ------Prepare to start Routine "recall_trainPF"-------
        continueRoutine = True
        # update component parameters for each repeat
        answ_train_2.reset()
        answer_trainPR=int(answer_trainPR)
        # keep track of which components have finished
        recall_trainPFComponents = [recall_train_2, answ_train_2]
        for thisComponent in recall_trainPFComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        recall_trainPFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "recall_trainPF"-------
        while continueRoutine:
            # get current time
            t = recall_trainPFClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=recall_trainPFClock)
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
                answ_train.text = answ_train.text.rstrip()
                if answ_train.text == str(answer_trainPR):
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
            for thisComponent in recall_trainPFComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "recall_trainPF"-------
        for thisComponent in recall_trainPFComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial_train_PF.addData('recall_train_2.started', recall_train_2.tStartRefresh)
        trial_train_PF.addData('recall_train_2.stopped', recall_train_2.tStopRefresh)
        trial_train_PF.addData('answ_train_2.text',answ_train_2.text)
        trial_train_PF.addData('answ_train_2.started', answ_train_2.tStartRefresh)
        trial_train_PF.addData('answ_train_2.stopped', answ_train_2.tStopRefresh)
        # the Routine "recall_trainPF" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "post_recall_train_PF"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        post_recall_train_PFComponents = [post_recall_training_2]
        for thisComponent in post_recall_train_PFComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        post_recall_train_PFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "post_recall_train_PF"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = post_recall_train_PFClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=post_recall_train_PFClock)
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
            for thisComponent in post_recall_train_PFComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "post_recall_train_PF"-------
        for thisComponent in post_recall_train_PFComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial_train_PF.addData('post_recall_training_2.started', post_recall_training_2.tStartRefresh)
        trial_train_PF.addData('post_recall_training_2.stopped', post_recall_training_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trial_train_PF'
    
    
    # ------Prepare to start Routine "start_trialPF"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    start_trialPFComponents = [end_training_2, key_resp_4]
    for thisComponent in start_trialPFComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    start_trialPFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "start_trialPF"-------
    while continueRoutine:
        # get current time
        t = start_trialPFClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=start_trialPFClock)
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
        for thisComponent in start_trialPFComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "start_trialPF"-------
    for thisComponent in start_trialPFComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PF_task.addData('end_training_2.started', end_training_2.tStartRefresh)
    PF_task.addData('end_training_2.stopped', end_training_2.tStopRefresh)
    parar_el_trial = False
    # the Routine "start_trialPF" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trialPF = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('datasets/Dataset_PF.xlsx'),
        seed=None, name='trialPF')
    thisExp.addLoop(trialPF)  # add the loop to the experiment
    thisTrialPF = trialPF.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialPF.rgb)
    if thisTrialPF != None:
        for paramName in thisTrialPF:
            exec('{} = thisTrialPF[paramName]'.format(paramName))
    
    for thisTrialPF in trialPF:
        currentLoop = trialPF
        # abbreviate parameter names if possible (e.g. rgb = thisTrialPF.rgb)
        if thisTrialPF != None:
            for paramName in thisTrialPF:
                exec('{} = thisTrialPF[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "first_fixPF"-------
        continueRoutine = True
        # update component parameters for each repeat
        startPR_2.setSound('datasets/trial_init.wav', secs=0.5, hamming=True)
        startPR_2.setVolume(1.0, log=False)
        first_fix_2.setText('+')
        # keep track of which components have finished
        first_fixPFComponents = [driftPR_2, startPR_2, first_fix_2]
        for thisComponent in first_fixPFComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        first_fixPFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "first_fixPF"-------
        while continueRoutine:
            # get current time
            t = first_fixPFClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=first_fixPFClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *driftPR_2* updates
            if driftPR_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                driftPR_2.frameNStart = frameN  # exact frame index
                driftPR_2.tStart = t  # local t and not account for scr refresh
                driftPR_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(driftPR_2, 'tStartRefresh')  # time at next scr refresh
                driftPR_2.setAutoDraw(True)
            if driftPR_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > driftPR_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    driftPR_2.tStop = t  # not accounting for scr refresh
                    driftPR_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(driftPR_2, 'tStopRefresh')  # time at next scr refresh
                    driftPR_2.setAutoDraw(False)
            # start/stop startPR_2
            if startPR_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                startPR_2.frameNStart = frameN  # exact frame index
                startPR_2.tStart = t  # local t and not account for scr refresh
                startPR_2.tStartRefresh = tThisFlipGlobal  # on global time
                startPR_2.play(when=win)  # sync with win flip
            if startPR_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > startPR_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    startPR_2.tStop = t  # not accounting for scr refresh
                    startPR_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(startPR_2, 'tStopRefresh')  # time at next scr refresh
                    startPR_2.stop()
            
            # *first_fix_2* updates
            if first_fix_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                first_fix_2.frameNStart = frameN  # exact frame index
                first_fix_2.tStart = t  # local t and not account for scr refresh
                first_fix_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(first_fix_2, 'tStartRefresh')  # time at next scr refresh
                first_fix_2.setAutoDraw(True)
            if first_fix_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > first_fix_2.tStartRefresh + fixation_time_PR-frameTolerance:
                    # keep track of stop time/frame for later
                    first_fix_2.tStop = t  # not accounting for scr refresh
                    first_fix_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(first_fix_2, 'tStopRefresh')  # time at next scr refresh
                    first_fix_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in first_fixPFComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "first_fixPF"-------
        for thisComponent in first_fixPFComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        startPR_2.stop()  # ensure sound has stopped at end of routine
        trialPF.addData('first_fix_2.started', first_fix_2.tStartRefresh)
        trialPF.addData('first_fix_2.stopped', first_fix_2.tStopRefresh)
        # the Routine "first_fixPF" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        digitLoop_PF = data.TrialHandler(nReps=digitSpan_PF, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='digitLoop_PF')
        thisExp.addLoop(digitLoop_PF)  # add the loop to the experiment
        thisDigitLoop_PF = digitLoop_PF.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop_PF.rgb)
        if thisDigitLoop_PF != None:
            for paramName in thisDigitLoop_PF:
                exec('{} = thisDigitLoop_PF[paramName]'.format(paramName))
        
        for thisDigitLoop_PF in digitLoop_PF:
            currentLoop = digitLoop_PF
            # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop_PF.rgb)
            if thisDigitLoop_PF != None:
                for paramName in thisDigitLoop_PF:
                    exec('{} = thisDigitLoop_PF[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "PresentationPF"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            pres_text_2.setText(str(digits_PR)[digitLoop_PR.thisN])
            # keep track of which components have finished
            PresentationPFComponents = [pres_text_2]
            for thisComponent in PresentationPFComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            PresentationPFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "PresentationPF"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = PresentationPFClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=PresentationPFClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *pres_text_2* updates
                if pres_text_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    pres_text_2.frameNStart = frameN  # exact frame index
                    pres_text_2.tStart = t  # local t and not account for scr refresh
                    pres_text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pres_text_2, 'tStartRefresh')  # time at next scr refresh
                    pres_text_2.setAutoDraw(True)
                if pres_text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > pres_text_2.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        pres_text_2.tStop = t  # not accounting for scr refresh
                        pres_text_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(pres_text_2, 'tStopRefresh')  # time at next scr refresh
                        pres_text_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in PresentationPFComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "PresentationPF"-------
            for thisComponent in PresentationPFComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            digitLoop_PF.addData('pres_text_2.started', pres_text_2.tStartRefresh)
            digitLoop_PF.addData('pres_text_2.stopped', pres_text_2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed digitSpan_PF repeats of 'digitLoop_PF'
        
        
        # ------Prepare to start Routine "RecallPF"-------
        continueRoutine = True
        # update component parameters for each repeat
        answer_box_2.reset()
        answer_PR=int(answer_PR)
        
        
        
        # keep track of which components have finished
        RecallPFComponents = [recall_txt_2, answer_box_2]
        for thisComponent in RecallPFComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        RecallPFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "RecallPF"-------
        while continueRoutine:
            # get current time
            t = RecallPFClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=RecallPFClock)
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
                answer_box.text = answer_box.text.rstrip() #deletes return from answer
                if answer_box.text == str(answer_PR): #if correct
                    correct = 1
                else:
                    correct = 0
                trial_trainingPR.addData('correct', correct)
                continueRoutine = False #ends routine
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RecallPFComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "RecallPF"-------
        for thisComponent in RecallPFComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trialPF.addData('recall_txt_2.started', recall_txt_2.tStartRefresh)
        trialPF.addData('recall_txt_2.stopped', recall_txt_2.tStopRefresh)
        trialPF.addData('answer_box_2.text',answer_box_2.text)
        trialPF.addData('answer_box_2.started', answer_box_2.tStartRefresh)
        trialPF.addData('answer_box_2.stopped', answer_box_2.tStopRefresh)
        ###trial 1 or 2 (span 3)
        if  trial_PR.thisTrialN == 0 or trial_PR.thisTrialN == 1: 
            if correct == 1: #if trial 1  
                previous_count += 1
                print(f' trial = {trial_PR.thisTrialN} previous_count = {previous_count}')
                
        ###trial 3 or 4 (span 4)
        elif trial_PR.thisTrialN == 2 or trial_PR.thisTrialN == 3: 
            if correct == 1:
                current_count +=1 #else (if incorrect, do nothing)
                print(f' trial = {trial_PR.thisTrialN} current_count = {current_count}')
        if trial_PR.thisTrialN == 3: 
            if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                parar_el_trial = True
                print(f'trial = {trial_PR.thisTrialN} parar_el_trial = {parar_el_trial}')
            else: #if at least one correct, continue routine, and reset counters
                previous_count = current_count #previous count equals corrects at trials 3 and 4
                current_count = 0 
            print(f' trial = {trial_PR.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
                        
        ###trial 5 or 6 (span 5)
        elif trial_PR.thisTrialN == 4 or trial_PR.thisTrialN == 5:
            if correct == 1:
                current_count +=1 #else (if incorrect, do nothing)
                print(f' trial = {trial_PR.thisTrialN} current_count = {current_count}')
        if trial_PR.thisTrialN == 5: 
            if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                parar_el_trial = True
                print(f'parar_el_trial = {parar_el_trial}')
            else: #if at least one correct, continue routine, and reset counters
                previous_count = current_count #previous count equals corrects at trials 3 and 4
                current_count = 0 
            print(f' trial = {trial_PR.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
                        
        ###trial 7 or 8 (span 6)
        elif trial_PR.thisTrialN == 6 or trial_PR.thisTrialN == 7:
            if correct == 1:
                current_count +=1 #else (if incorrect, do nothing)
                print(f' trial = {trial_PR.thisTrialN} current_count = {current_count}')
        if trial_PR.thisTrialN == 7: 
            if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                parar_el_trial = True
                print(f'parar_el_trial = {parar_el_trial}')
            else: #if at least one correct, continue routine, and reset counters
                previous_count = current_count #previous count equals corrects at trials 3 and 4
                current_count = 0 
            print(f' trial = {trial_PR.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
                         
        ###trial 9 or 10 (span 7)
        elif trial_PR.thisTrialN == 8 or trial_PR.thisTrialN == 9:
            if correct == 1:
                current_count +=1 #else (if incorrect, do nothing)
                print(f' trial = {trial_PR.thisTrialN} current_count = {current_count}')
        if trial_PR.thisTrialN == 9: 
            if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                parar_el_trial = True
                print(f'parar_el_trial = {parar_el_trial}')
            else: #if at least one correct, continue routine, and reset counters
                previous_count = current_count #previous count equals corrects at trials 3 and 4
                current_count = 0 
            print(f' trial = {trial_PR.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
             
        ###trial 11 or 12 (span 8)
        elif trial_PR.thisTrialN == 10 or trial_PR.thisTrialN == 11:
            if correct == 1:
                current_count +=1 #else (if incorrect, do nothing)
                print(f' trial = {trial_PR.thisTrialN} current_count = {current_count}')
        if trial_PR.thisTrialN == 11: 
            if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                parar_el_trial = True
                print(f'parar_el_trial = {parar_el_trial}')
            else: #if at least one correct, continue routine, and reset counters
                previous_count = current_count #previous count equals corrects at trials 3 and 4
                current_count = 0 
            print(f' trial = {trial_PR.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
           
        ###trial 13 or 14 (span 9)
        elif trial_PR.thisTrialN == 12 or trial_PR.thisTrialN == 13:
            if correct == 1:
                current_count +=1 #else (if incorrect, do nothing)
                print(f' trial = {trial_PR.thisTrialN} current_count = {current_count}')
        if trial_PR.thisTrialN == 13: 
            if current_count == 0 and previous_count == 0: #if 4 mistakes ends routine
                parar_el_trial = True
                print(f'parar_el_trial = {parar_el_trial}')
            else: #if at least one correct, continue routine, and reset counters
                previous_count = current_count #previous count equals corrects at trials 3 and 4
                current_count = 0 
            print(f' trial = {trial_PR.thisTrialN} previous_count = {previous_count} current_count = {current_count} parar_el_trial = {parar_el_trial}')
            
        ###trial 16 (span 10)
        #elif trial_PR.thisTrialN == 15:
        #    continueRoutine = False
        # the Routine "RecallPF" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "post_recallPF"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        post_recallPFComponents = [postrecallPR_2]
        for thisComponent in post_recallPFComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        post_recallPFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "post_recallPF"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = post_recallPFClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=post_recallPFClock)
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
            for thisComponent in post_recallPFComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "post_recallPF"-------
        for thisComponent in post_recallPFComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trialPF.addData('postrecallPR_2.started', postrecallPR_2.tStartRefresh)
        trialPF.addData('postrecallPR_2.stopped', postrecallPR_2.tStopRefresh)
        if parar_el_trial:
            trial_PR.finished = True
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trialPF'
    
    
    # ------Prepare to start Routine "LickertPF"-------
    continueRoutine = True
    # update component parameters for each repeat
    dif_licker_2.reset()
    # keep track of which components have finished
    LickertPFComponents = [Dificultad_2, dif_licker_2]
    for thisComponent in LickertPFComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    LickertPFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "LickertPF"-------
    while continueRoutine:
        # get current time
        t = LickertPFClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=LickertPFClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Dificultad_2* updates
        if Dificultad_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Dificultad_2.frameNStart = frameN  # exact frame index
            Dificultad_2.tStart = t  # local t and not account for scr refresh
            Dificultad_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Dificultad_2, 'tStartRefresh')  # time at next scr refresh
            Dificultad_2.setAutoDraw(True)
        
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
        for thisComponent in LickertPFComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "LickertPF"-------
    for thisComponent in LickertPFComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PF_task.addData('Dificultad_2.started', Dificultad_2.tStartRefresh)
    PF_task.addData('Dificultad_2.stopped', Dificultad_2.tStopRefresh)
    PF_task.addData('dif_licker_2.response', dif_licker_2.getRating())
    PF_task.addData('dif_licker_2.rt', dif_licker_2.getRT())
    PF_task.addData('dif_licker_2.started', dif_licker_2.tStartRefresh)
    PF_task.addData('dif_licker_2.stopped', dif_licker_2.tStopRefresh)
    # the Routine "LickertPF" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'PF_task'


# ------Prepare to start Routine "End2"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
End2Components = [thank_you_2]
for thisComponent in End2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
End2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = End2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=End2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thank_you_2* updates
    if thank_you_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank_you_2.frameNStart = frameN  # exact frame index
        thank_you_2.tStart = t  # local t and not account for scr refresh
        thank_you_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank_you_2, 'tStartRefresh')  # time at next scr refresh
        thank_you_2.setAutoDraw(True)
    if thank_you_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thank_you_2.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            thank_you_2.tStop = t  # not accounting for scr refresh
            thank_you_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thank_you_2, 'tStopRefresh')  # time at next scr refresh
            thank_you_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in End2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End2"-------
for thisComponent in End2Components:
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
