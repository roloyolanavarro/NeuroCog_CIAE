#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on mayo 20, 2022, at 20:31
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
expName = 'MyTestTask'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\INU\\Documents\\GitHub\\NeuroCog_CIAE\\TaskTemplates\\PsychoPy_tasks\\MyTestTask.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
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

# Initialize components for Routine "IntroText"
IntroTextClock = core.Clock()
Introtext = visual.TextStim(win=win, name='Introtext',
    text='Bienvenid@s \n\nPresiona la barra espaciadora para avanzar a la siguiente página',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
avanzar_intro = keyboard.Keyboard()

# Initialize components for Routine "Encoding"
EncodingClock = core.Clock()
encodingimage = visual.ImageStim(
    win=win,
    name='encodingimage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
encodingaudio = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='encodingaudio')
encodingaudio.setVolume(1.0)
text = visual.TextStim(win=win, name='text',
    text='',
    font='Arial',
    pos=(0, 0.3), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "FactTest"
FactTestClock = core.Clock()
fact_test_image = visual.ImageStim(
    win=win,
    name='fact_test_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.2), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
question_test = visual.TextStim(win=win, name='question_test',
    text='',
    font='Arial',
    pos=(0, -0.1), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Alternativas = visual.TextStim(win=win, name='Alternativas',
    text='',
    font='Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
fact_response = keyboard.Keyboard()

# Initialize components for Routine "SourceTest"
SourceTestClock = core.Clock()
sourcetext = visual.TextStim(win=win, name='sourcetext',
    text='',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sourceresponse = keyboard.Keyboard()

# Initialize components for Routine "QuitExperiment"
QuitExperimentClock = core.Clock()
quit_text = visual.TextStim(win=win, name='quit_text',
    text='Thank you for participating!\n\nPress the space bar to quit',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
quit_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "IntroText"-------
continueRoutine = True
# update component parameters for each repeat
avanzar_intro.keys = []
avanzar_intro.rt = []
_avanzar_intro_allKeys = []
# keep track of which components have finished
IntroTextComponents = [Introtext, avanzar_intro]
for thisComponent in IntroTextComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroTextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "IntroText"-------
while continueRoutine:
    # get current time
    t = IntroTextClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroTextClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Introtext* updates
    if Introtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Introtext.frameNStart = frameN  # exact frame index
        Introtext.tStart = t  # local t and not account for scr refresh
        Introtext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Introtext, 'tStartRefresh')  # time at next scr refresh
        Introtext.setAutoDraw(True)
    
    # *avanzar_intro* updates
    waitOnFlip = False
    if avanzar_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        avanzar_intro.frameNStart = frameN  # exact frame index
        avanzar_intro.tStart = t  # local t and not account for scr refresh
        avanzar_intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(avanzar_intro, 'tStartRefresh')  # time at next scr refresh
        avanzar_intro.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(avanzar_intro.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(avanzar_intro.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if avanzar_intro.status == STARTED and not waitOnFlip:
        theseKeys = avanzar_intro.getKeys(keyList=['space'], waitRelease=False)
        _avanzar_intro_allKeys.extend(theseKeys)
        if len(_avanzar_intro_allKeys):
            avanzar_intro.keys = _avanzar_intro_allKeys[-1].name  # just the last key pressed
            avanzar_intro.rt = _avanzar_intro_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroTextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "IntroText"-------
for thisComponent in IntroTextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "IntroText" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('semepistim.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Encoding"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    encodingimage.setImage(animalimage)
    encodingaudio.setSound(questionaudio, secs=6.0, hamming=True)
    encodingaudio.setVolume(1.0, log=False)
    text.setText(animalname)
    # keep track of which components have finished
    EncodingComponents = [encodingimage, encodingaudio, text]
    for thisComponent in EncodingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    EncodingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Encoding"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EncodingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=EncodingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *encodingimage* updates
        if encodingimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encodingimage.frameNStart = frameN  # exact frame index
            encodingimage.tStart = t  # local t and not account for scr refresh
            encodingimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encodingimage, 'tStartRefresh')  # time at next scr refresh
            encodingimage.setAutoDraw(True)
        if encodingimage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encodingimage.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                encodingimage.tStop = t  # not accounting for scr refresh
                encodingimage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encodingimage, 'tStopRefresh')  # time at next scr refresh
                encodingimage.setAutoDraw(False)
        # start/stop encodingaudio
        if encodingaudio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encodingaudio.frameNStart = frameN  # exact frame index
            encodingaudio.tStart = t  # local t and not account for scr refresh
            encodingaudio.tStartRefresh = tThisFlipGlobal  # on global time
            encodingaudio.play(when=win)  # sync with win flip
        if encodingaudio.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encodingaudio.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                encodingaudio.tStop = t  # not accounting for scr refresh
                encodingaudio.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encodingaudio, 'tStopRefresh')  # time at next scr refresh
                encodingaudio.stop()
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EncodingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Encoding"-------
    for thisComponent in EncodingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    encodingaudio.stop()  # ensure sound has stopped at end of routine
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('semepistim.csv'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "FactTest"-------
    continueRoutine = True
    # update component parameters for each repeat
    fact_test_image.setImage(animalimage)
    question_test.setText(question)
    Alternativas.setText(lettera + choicea + '\n' + letterb + choiceb)
    fact_response.keys = []
    fact_response.rt = []
    _fact_response_allKeys = []
    # keep track of which components have finished
    FactTestComponents = [fact_test_image, question_test, Alternativas, fact_response]
    for thisComponent in FactTestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FactTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FactTest"-------
    while continueRoutine:
        # get current time
        t = FactTestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FactTestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fact_test_image* updates
        if fact_test_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fact_test_image.frameNStart = frameN  # exact frame index
            fact_test_image.tStart = t  # local t and not account for scr refresh
            fact_test_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fact_test_image, 'tStartRefresh')  # time at next scr refresh
            fact_test_image.setAutoDraw(True)
        
        # *question_test* updates
        if question_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_test.frameNStart = frameN  # exact frame index
            question_test.tStart = t  # local t and not account for scr refresh
            question_test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_test, 'tStartRefresh')  # time at next scr refresh
            question_test.setAutoDraw(True)
        
        # *Alternativas* updates
        if Alternativas.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Alternativas.frameNStart = frameN  # exact frame index
            Alternativas.tStart = t  # local t and not account for scr refresh
            Alternativas.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Alternativas, 'tStartRefresh')  # time at next scr refresh
            Alternativas.setAutoDraw(True)
        
        # *fact_response* updates
        waitOnFlip = False
        if fact_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fact_response.frameNStart = frameN  # exact frame index
            fact_response.tStart = t  # local t and not account for scr refresh
            fact_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fact_response, 'tStartRefresh')  # time at next scr refresh
            fact_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fact_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fact_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fact_response.status == STARTED and not waitOnFlip:
            theseKeys = fact_response.getKeys(keyList=['a','b'], waitRelease=False)
            _fact_response_allKeys.extend(theseKeys)
            if len(_fact_response_allKeys):
                fact_response.keys = _fact_response_allKeys[-1].name  # just the last key pressed
                fact_response.rt = _fact_response_allKeys[-1].rt
                # was this correct?
                if (fact_response.keys == str(correctanswer)) or (fact_response.keys == correctanswer):
                    fact_response.corr = 1
                else:
                    fact_response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FactTestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FactTest"-------
    for thisComponent in FactTestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('Alternativas.started', Alternativas.tStartRefresh)
    trials_2.addData('Alternativas.stopped', Alternativas.tStopRefresh)
    # check responses
    if fact_response.keys in ['', [], None]:  # No response was made
        fact_response.keys = None
        # was no response the correct answer?!
        if str(correctanswer).lower() == 'none':
           fact_response.corr = 1;  # correct non-response
        else:
           fact_response.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('fact_response.keys',fact_response.keys)
    trials_2.addData('fact_response.corr', fact_response.corr)
    if fact_response.keys != None:  # we had a response
        trials_2.addData('fact_response.rt', fact_response.rt)
    trials_2.addData('fact_response.started', fact_response.tStartRefresh)
    trials_2.addData('fact_response.stopped', fact_response.tStopRefresh)
    # the Routine "FactTest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "SourceTest"-------
    continueRoutine = True
    # update component parameters for each repeat
    sourcetext.setText('Did a male or female voice tell you this fact?\n\na. Male\nb. Female')
    sourceresponse.keys = []
    sourceresponse.rt = []
    _sourceresponse_allKeys = []
    # keep track of which components have finished
    SourceTestComponents = [sourcetext, sourceresponse]
    for thisComponent in SourceTestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SourceTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SourceTest"-------
    while continueRoutine:
        # get current time
        t = SourceTestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SourceTestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sourcetext* updates
        if sourcetext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sourcetext.frameNStart = frameN  # exact frame index
            sourcetext.tStart = t  # local t and not account for scr refresh
            sourcetext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sourcetext, 'tStartRefresh')  # time at next scr refresh
            sourcetext.setAutoDraw(True)
        
        # *sourceresponse* updates
        waitOnFlip = False
        if sourceresponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sourceresponse.frameNStart = frameN  # exact frame index
            sourceresponse.tStart = t  # local t and not account for scr refresh
            sourceresponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sourceresponse, 'tStartRefresh')  # time at next scr refresh
            sourceresponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(sourceresponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(sourceresponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if sourceresponse.status == STARTED and not waitOnFlip:
            theseKeys = sourceresponse.getKeys(keyList=['a','b'], waitRelease=False)
            _sourceresponse_allKeys.extend(theseKeys)
            if len(_sourceresponse_allKeys):
                sourceresponse.keys = _sourceresponse_allKeys[-1].name  # just the last key pressed
                sourceresponse.rt = _sourceresponse_allKeys[-1].rt
                # was this correct?
                if (sourceresponse.keys == str(sourceanswer)) or (sourceresponse.keys == sourceanswer):
                    sourceresponse.corr = 1
                else:
                    sourceresponse.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SourceTestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SourceTest"-------
    for thisComponent in SourceTestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('sourcetext.started', sourcetext.tStartRefresh)
    trials_2.addData('sourcetext.stopped', sourcetext.tStopRefresh)
    # check responses
    if sourceresponse.keys in ['', [], None]:  # No response was made
        sourceresponse.keys = None
        # was no response the correct answer?!
        if str(sourceanswer).lower() == 'none':
           sourceresponse.corr = 1;  # correct non-response
        else:
           sourceresponse.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('sourceresponse.keys',sourceresponse.keys)
    trials_2.addData('sourceresponse.corr', sourceresponse.corr)
    if sourceresponse.keys != None:  # we had a response
        trials_2.addData('sourceresponse.rt', sourceresponse.rt)
    trials_2.addData('sourceresponse.started', sourceresponse.tStartRefresh)
    trials_2.addData('sourceresponse.stopped', sourceresponse.tStopRefresh)
    # the Routine "SourceTest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# ------Prepare to start Routine "QuitExperiment"-------
continueRoutine = True
# update component parameters for each repeat
quit_resp.keys = []
quit_resp.rt = []
_quit_resp_allKeys = []
# keep track of which components have finished
QuitExperimentComponents = [quit_text, quit_resp]
for thisComponent in QuitExperimentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
QuitExperimentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "QuitExperiment"-------
while continueRoutine:
    # get current time
    t = QuitExperimentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=QuitExperimentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *quit_text* updates
    if quit_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        quit_text.frameNStart = frameN  # exact frame index
        quit_text.tStart = t  # local t and not account for scr refresh
        quit_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(quit_text, 'tStartRefresh')  # time at next scr refresh
        quit_text.setAutoDraw(True)
    
    # *quit_resp* updates
    waitOnFlip = False
    if quit_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        quit_resp.frameNStart = frameN  # exact frame index
        quit_resp.tStart = t  # local t and not account for scr refresh
        quit_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(quit_resp, 'tStartRefresh')  # time at next scr refresh
        quit_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(quit_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(quit_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if quit_resp.status == STARTED and not waitOnFlip:
        theseKeys = quit_resp.getKeys(keyList=['space'], waitRelease=False)
        _quit_resp_allKeys.extend(theseKeys)
        if len(_quit_resp_allKeys):
            quit_resp.keys = _quit_resp_allKeys[-1].name  # just the last key pressed
            quit_resp.rt = _quit_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in QuitExperimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "QuitExperiment"-------
for thisComponent in QuitExperimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('quit_text.started', quit_text.tStartRefresh)
thisExp.addData('quit_text.stopped', quit_text.tStopRefresh)
# the Routine "QuitExperiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
