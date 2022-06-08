#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on junio 07, 2022, at 23:20
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
expName = 'DigitSpanTask_fwdback'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\INU\\Documents\\GitHub\\NeuroCog_CIAE\\TaskTemplates\\PsychoPy_tasks\\digit-span-fwd\\DigitSpanTask_fwdback_lastrun.py',
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

# Initialize components for Routine "Instrucciones"
InstruccionesClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='instruccion1_pasiva_BACK.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "firs_fixation"
firs_fixationClock = core.Clock()
firs_fix = visual.TextStim(win=win, name='firs_fix',
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
textbox = visual.TextBox2(
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
     name='textbox',
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
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
dif_licker = visual.Slider(win=win, name='dif_licker',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.25), units=None,
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
BienvenidaComponents = [Bienvenida_text, key_bienvenida]
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

# ------Prepare to start Routine "Instrucciones"-------
continueRoutine = True
# update component parameters for each repeat
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

# set up handler to look after randomisation of conditions etc
trial_PF = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Dataset_PF.xlsx'),
    seed=None, name='trial_PF')
thisExp.addLoop(trial_PF)  # add the loop to the experiment
thisTrial_PF = trial_PF.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_PF.rgb)
if thisTrial_PF != None:
    for paramName in thisTrial_PF:
        exec('{} = thisTrial_PF[paramName]'.format(paramName))

for thisTrial_PF in trial_PF:
    currentLoop = trial_PF
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_PF.rgb)
    if thisTrial_PF != None:
        for paramName in thisTrial_PF:
            exec('{} = thisTrial_PF[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "firs_fixation"-------
    continueRoutine = True
    # update component parameters for each repeat
    firs_fix.setText('+')
    # keep track of which components have finished
    firs_fixationComponents = [firs_fix]
    for thisComponent in firs_fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    firs_fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "firs_fixation"-------
    while continueRoutine:
        # get current time
        t = firs_fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=firs_fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *firs_fix* updates
        if firs_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            firs_fix.frameNStart = frameN  # exact frame index
            firs_fix.tStart = t  # local t and not account for scr refresh
            firs_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(firs_fix, 'tStartRefresh')  # time at next scr refresh
            firs_fix.setAutoDraw(True)
        if firs_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > firs_fix.tStartRefresh + fixation_time-frameTolerance:
                # keep track of stop time/frame for later
                firs_fix.tStop = t  # not accounting for scr refresh
                firs_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(firs_fix, 'tStopRefresh')  # time at next scr refresh
                firs_fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in firs_fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "firs_fixation"-------
    for thisComponent in firs_fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial_PF.addData('firs_fix.started', firs_fix.tStartRefresh)
    trial_PF.addData('firs_fix.stopped', firs_fix.tStopRefresh)
    # the Routine "firs_fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    digitLoop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='digitLoop')
    thisExp.addLoop(digitLoop)  # add the loop to the experiment
    thisDigitLoop = digitLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop.rgb)
    if thisDigitLoop != None:
        for paramName in thisDigitLoop:
            exec('{} = thisDigitLoop[paramName]'.format(paramName))
    
    for thisDigitLoop in digitLoop:
        currentLoop = digitLoop
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop.rgb)
        if thisDigitLoop != None:
            for paramName in thisDigitLoop:
                exec('{} = thisDigitLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Presentation"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        pres_text.setText(str(digits)[digitLoop.thisN])
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
        digitLoop.addData('pres_text.started', pres_text.tStartRefresh)
        digitLoop.addData('pres_text.stopped', pres_text.tStopRefresh)
    # completed 1.0 repeats of 'digitLoop'
    
    
    # ------Prepare to start Routine "Recall"-------
    continueRoutine = True
    # update component parameters for each repeat
    textbox.reset()
    # keep track of which components have finished
    RecallComponents = [recall_txt, textbox, button_next]
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
        
        # *textbox* updates
        if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            textbox.setAutoDraw(True)
        
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
    trial_PF.addData('recall_txt.started', recall_txt.tStartRefresh)
    trial_PF.addData('recall_txt.stopped', recall_txt.tStopRefresh)
    trial_PF.addData('textbox.text',textbox.text)
    trial_PF.addData('textbox.started', textbox.tStartRefresh)
    trial_PF.addData('textbox.stopped', textbox.tStopRefresh)
    trial_PF.addData('button_next.numClicks', button_next.numClicks)
    if button_next.numClicks:
       trial_PF.addData('button_next.timesOn', button_next.timesOn)
       trial_PF.addData('button_next.timesOff', button_next.timesOff)
    else:
       trial_PF.addData('button_next.timesOn', "")
       trial_PF.addData('button_next.timesOff', "")
    if textbox.text == str(digits):
        correct = 1
        fbTxt = 'Correct!'
    else:
        correct = 0
        fbTxt = 'Incorrect'
    thisExp.addData('correct', correct)
    # the Routine "Recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trial_PF'


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
