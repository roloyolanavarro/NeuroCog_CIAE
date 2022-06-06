#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on June 01, 2022, at 19:43
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
psychopyVersion = '2022.1.4'
expName = 'DS_Adapt1L'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
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
    originPath='C:\\Users\\lroci\\Documents\\GitHub\\NeuroCog_CIAE\\TaskTemplates\\PsychoPy_tasks\\digit-span-FwdBack\\DS_Adapt_FB_lastrun.py',
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

# Initialize components for Routine "Instr"
InstrClock = core.Clock()
InstrText = visual.TextStim(win=win, name='InstrText',
    text="Thank you for Participating!\n\nIn this experiment, you will be shown a series of numbers one after the other.\nPlease try to remember the numbers so that afterwards, you can type them into the computer\n\nThere are two short tasks - in the forward task you will type the numbers in the same order you saw them\nIn the backward task, you will type in the numbers backwards\n\nLet's get started!\nPress any key to continue",
    font='Arial',
    pos=(0, 0), height=.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Welcome_resp = keyboard.Keyboard()
TotTrial = 0



# Initialize components for Routine "InstrForward"
InstrForwardClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='We will start with the FORWARD task\n\nA series of numbers will be shown on the screen, please try to remember them.\nYou will then type them into the computer in the same order as they appeared.\n\nIf you get it CORRECT, the following round will be one digit LONGER.\nIf you get it INCORRECT, the following round will be the same length.\nAfter 2 incorrect responses, the following round will be one digit SHORTER.\n\nYou will do this for a total of 14 rounds\n\nIf you are ready, press any key to do one trial round\n\nGood luck!\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "routine_roundTrial"
routine_roundTrialClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='TRIAL ROUND',
    font='Arial',
    pos=(0, .25), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='press "Space"  to continue',
    font='Arial',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "routine_presTrial"
routine_presTrialClock = core.Clock()
Ptrial = 0
seq1_tr = visual.TextStim(win=win, name='seq1_tr',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Seq2_tr = visual.TextStim(win=win, name='Seq2_tr',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Seq3_tr = visual.TextStim(win=win, name='Seq3_tr',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Seq4_tr = visual.TextStim(win=win, name='Seq4_tr',
    text='4',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "routine_RespTrial"
routine_RespTrialClock = core.Clock()
textType = visual.TextStim(win=win, name='textType',
    text='Please type in the numbers as you saw them, followed by the ENTER button:',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textFeedback = visual.TextStim(win=win, name='textFeedback',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "routine_go"
routine_goClock = core.Clock()
text_go = visual.TextStim(win=win, name='text_go',
    text='That\'s it!\n\nLet\'s start doing the actual task.\n\nPress "space" to start',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "routine_round"
routine_roundClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='ROUND',
    font='Arial',
    pos=(0, .25), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='Press "SPACE" to continue',
    font='Arial',
    pos=(0, -.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "routine_Dpres"
routine_DpresClock = core.Clock()
DS_3Corr = 0
DS_3Incorr = 0
DS_4Corr = 0
DS_4Incorr = 0
DS_5Corr = 0
DS_5Incorr = 0
DS_6Corr = 0
DS_6Incorr = 0
DS_7Corr = 0
DS_7Incorr = 0
DS_8Corr = 0
DS_8Incorr = 0
DS_9Corr = 0
DS_9Incorr = 0
DS_10Corr = 0
DS_10Incorr = 0
DS_11Corr = 0
DS_11Incorr = 0
DS_12Corr = 0
DS_12Incorr = 0
DS_13Corr = 0
DS_13Incorr = 0
DS_14Corr = 0
DS_14Incorr = 0
DS_15Corr = 0
DS_15Incorr = 0
DS_16Corr = 0
DS_16Incorr = 0
TotTrial = 0
Seq1 = visual.TextStim(win=win, name='Seq1',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Seq2 = visual.TextStim(win=win, name='Seq2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Seq3 = visual.TextStim(win=win, name='Seq3',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Seq4 = visual.TextStim(win=win, name='Seq4',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
Seq5 = visual.TextStim(win=win, name='Seq5',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
Seq6 = visual.TextStim(win=win, name='Seq6',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
Seq7 = visual.TextStim(win=win, name='Seq7',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
Seq8 = visual.TextStim(win=win, name='Seq8',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
Seq9 = visual.TextStim(win=win, name='Seq9',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
Seq10 = visual.TextStim(win=win, name='Seq10',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
Seq11 = visual.TextStim(win=win, name='Seq11',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
Seq12 = visual.TextStim(win=win, name='Seq12',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
Seq13 = visual.TextStim(win=win, name='Seq13',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
Seq14 = visual.TextStim(win=win, name='Seq14',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
Seq15 = visual.TextStim(win=win, name='Seq15',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
Seq16 = visual.TextStim(win=win, name='Seq16',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);

# Initialize components for Routine "routine_Dresp"
routine_DrespClock = core.Clock()
textType_2 = visual.TextStim(win=win, name='textType_2',
    text='Please type in the numbers as you saw them, followed by the ENTER button:',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textFeedback_2 = visual.TextStim(win=win, name='textFeedback_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp2_2 = keyboard.Keyboard()
wrongAnswer = 0

# Initialize components for Routine "InstrBack"
InstrBackClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Now, you will do the same thing, but type in the number in the REVERSE order.\n\nFor example, if you are presented with \n[1, 2, 3] \nyou would type in \n[3, 2, 1]\n\nPress any key to start the next round',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "routine_round_2"
routine_round_2Clock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text='ROUND',
    font='Arial',
    pos=(0, .25), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_11 = visual.TextStim(win=win, name='text_11',
    text='Press "SPACE" to continue',
    font='Arial',
    pos=(0, -.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "routine_BackPres"
routine_BackPresClock = core.Clock()
B_DS_3Corr = 0
B_DS_3Incorr = 0
B_DS_4Corr = 0
B_DS_4Incorr = 0
B_DS_5Corr = 0
B_DS_5Incorr = 0
B_DS_6Corr = 0
B_DS_6Incorr = 0
B_DS_7Corr = 0
B_DS_7Incorr = 0
B_DS_8Corr = 0
B_DS_8Incorr = 0
B_DS_9Corr = 0
B_DS_9Incorr = 0
B_DS_10Corr = 0
B_DS_10Incorr = 0
B_DS_11Corr = 0
B_DS_11Incorr = 0
B_DS_12Corr = 0
B_DS_12Incorr = 0
B_DS_13Corr = 0
B_DS_13Incorr = 0
B_DS_14Corr = 0
B_DS_14Incorr = 0
B_DS_15Corr = 0
B_DS_15Incorr = 0
B_DS_16Corr = 0
B_DS_16Incorr = 0
B_TotTrial = 0
Seq1_b = visual.TextStim(win=win, name='Seq1_b',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Seq2_b = visual.TextStim(win=win, name='Seq2_b',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Seq3_b = visual.TextStim(win=win, name='Seq3_b',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Seq4_b = visual.TextStim(win=win, name='Seq4_b',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
Seq5_b = visual.TextStim(win=win, name='Seq5_b',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
Seq6_b = visual.TextStim(win=win, name='Seq6_b',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
Seq7_b = visual.TextStim(win=win, name='Seq7_b',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
Seq8_b = visual.TextStim(win=win, name='Seq8_b',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
Seq9_b = visual.TextStim(win=win, name='Seq9_b',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
Seq10_b = visual.TextStim(win=win, name='Seq10_b',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
Seq11_b = visual.TextStim(win=win, name='Seq11_b',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
Seq12_b = visual.TextStim(win=win, name='Seq12_b',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
Seq13_b = visual.TextStim(win=win, name='Seq13_b',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
Seq14_b = visual.TextStim(win=win, name='Seq14_b',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
Seq15_b = visual.TextStim(win=win, name='Seq15_b',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
Seq16_b = visual.TextStim(win=win, name='Seq16_b',
    text='',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);

# Initialize components for Routine "routine_BackResp"
routine_BackRespClock = core.Clock()
textType_2B = visual.TextStim(win=win, name='textType_2B',
    text='Please type in the numbers in the reverse order that you saw them, followed by the ENTER button:',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textFeedback_2B = visual.TextStim(win=win, name='textFeedback_2B',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp2_2B = keyboard.Keyboard()
wrongAnswer = 0

# Initialize components for Routine "Goodbye"
GoodbyeClock = core.Clock()
GB = visual.TextStim(win=win, name='GB',
    text='Thats it!\n\nThanks again for participating! \n\nPlease press escape to leave the experiment',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instr"-------
continueRoutine = True
# update component parameters for each repeat
Welcome_resp.keys = []
Welcome_resp.rt = []
_Welcome_resp_allKeys = []
# keep track of which components have finished
InstrComponents = [InstrText, Welcome_resp]
for thisComponent in InstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr"-------
while continueRoutine:
    # get current time
    t = InstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstrText* updates
    if InstrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstrText.frameNStart = frameN  # exact frame index
        InstrText.tStart = t  # local t and not account for scr refresh
        InstrText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstrText, 'tStartRefresh')  # time at next scr refresh
        InstrText.setAutoDraw(True)
    
    # *Welcome_resp* updates
    waitOnFlip = False
    if Welcome_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome_resp.frameNStart = frameN  # exact frame index
        Welcome_resp.tStart = t  # local t and not account for scr refresh
        Welcome_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome_resp, 'tStartRefresh')  # time at next scr refresh
        Welcome_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Welcome_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Welcome_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Welcome_resp.status == STARTED and not waitOnFlip:
        theseKeys = Welcome_resp.getKeys(keyList=None, waitRelease=False)
        _Welcome_resp_allKeys.extend(theseKeys)
        if len(_Welcome_resp_allKeys):
            Welcome_resp.keys = _Welcome_resp_allKeys[-1].name  # just the last key pressed
            Welcome_resp.rt = _Welcome_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr"-------
for thisComponent in InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstrForward"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
InstrForwardComponents = [text_2, key_resp_2]
for thisComponent in InstrForwardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstrForwardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstrForward"-------
while continueRoutine:
    # get current time
    t = InstrForwardClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstrForwardClock)
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
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=None, waitRelease=False)
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
    for thisComponent in InstrForwardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstrForward"-------
for thisComponent in InstrForwardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "InstrForward" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "routine_roundTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_6.setText(trials_2.thisRepN +1)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    routine_roundTrialComponents = [text_6, text_7, text_8, key_resp_6]
    for thisComponent in routine_roundTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    routine_roundTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "routine_roundTrial"-------
    while continueRoutine:
        # get current time
        t = routine_roundTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routine_roundTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            theseKeys = key_resp_6.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
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
        for thisComponent in routine_roundTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_roundTrial"-------
    for thisComponent in routine_roundTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "routine_roundTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "routine_presTrial"-------
    continueRoutine = True
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    routine_presTrialComponents = [seq1_tr, Seq2_tr, Seq3_tr, Seq4_tr]
    for thisComponent in routine_presTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    routine_presTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "routine_presTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = routine_presTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routine_presTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if Ptrial == 0:
            if t >=3.4:
                continueRoutine = False
                
        
        
        # *seq1_tr* updates
        if seq1_tr.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            seq1_tr.frameNStart = frameN  # exact frame index
            seq1_tr.tStart = t  # local t and not account for scr refresh
            seq1_tr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seq1_tr, 'tStartRefresh')  # time at next scr refresh
            seq1_tr.setAutoDraw(True)
        if seq1_tr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seq1_tr.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                seq1_tr.tStop = t  # not accounting for scr refresh
                seq1_tr.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seq1_tr, 'tStopRefresh')  # time at next scr refresh
                seq1_tr.setAutoDraw(False)
        
        # *Seq2_tr* updates
        if Seq2_tr.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            Seq2_tr.frameNStart = frameN  # exact frame index
            Seq2_tr.tStart = t  # local t and not account for scr refresh
            Seq2_tr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq2_tr, 'tStartRefresh')  # time at next scr refresh
            Seq2_tr.setAutoDraw(True)
        if Seq2_tr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq2_tr.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq2_tr.tStop = t  # not accounting for scr refresh
                Seq2_tr.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq2_tr, 'tStopRefresh')  # time at next scr refresh
                Seq2_tr.setAutoDraw(False)
        
        # *Seq3_tr* updates
        if Seq3_tr.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            Seq3_tr.frameNStart = frameN  # exact frame index
            Seq3_tr.tStart = t  # local t and not account for scr refresh
            Seq3_tr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq3_tr, 'tStartRefresh')  # time at next scr refresh
            Seq3_tr.setAutoDraw(True)
        if Seq3_tr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq3_tr.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq3_tr.tStop = t  # not accounting for scr refresh
                Seq3_tr.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq3_tr, 'tStopRefresh')  # time at next scr refresh
                Seq3_tr.setAutoDraw(False)
        
        # *Seq4_tr* updates
        if Seq4_tr.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            Seq4_tr.frameNStart = frameN  # exact frame index
            Seq4_tr.tStart = t  # local t and not account for scr refresh
            Seq4_tr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq4_tr, 'tStartRefresh')  # time at next scr refresh
            Seq4_tr.setAutoDraw(True)
        if Seq4_tr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq4_tr.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq4_tr.tStop = t  # not accounting for scr refresh
                Seq4_tr.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq4_tr, 'tStopRefresh')  # time at next scr refresh
                Seq4_tr.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_presTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_presTrial"-------
    for thisComponent in routine_presTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "routine_RespTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    screen_text = ''
    # keep track of which components have finished
    routine_RespTrialComponents = [textType, textFeedback, key_resp_4]
    for thisComponent in routine_RespTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    routine_RespTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "routine_RespTrial"-------
    while continueRoutine:
        # get current time
        t = routine_RespTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routine_RespTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textType* updates
        if textType.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            textType.frameNStart = frameN  # exact frame index
            textType.tStart = t  # local t and not account for scr refresh
            textType.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textType, 'tStartRefresh')  # time at next scr refresh
            textType.setAutoDraw(True)
        
        # *textFeedback* updates
        if textFeedback.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            textFeedback.frameNStart = frameN  # exact frame index
            textFeedback.tStart = t  # local t and not account for scr refresh
            textFeedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textFeedback, 'tStartRefresh')  # time at next scr refresh
            textFeedback.setAutoDraw(True)
        if textFeedback.status == STARTED:  # only update if drawing
            textFeedback.setText(screen_text, log=False)
        
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
            theseKeys = key_resp_4.getKeys(keyList=['1','2','3','4','5','6','7','8','9','backspace','return'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = [key.name for key in _key_resp_4_allKeys]  # storing all keys
                key_resp_4.rt = [key.rt for key in _key_resp_4_allKeys]
                # was this correct?
                if (key_resp_4.keys == str('')) or (key_resp_4.keys == ''):
                    key_resp_4.corr = 1
                else:
                    key_resp_4.corr = 0
        if("backspace" in key_resp_4.keys):
            key_resp_4.keys.remove("backspace")
            
            if(len(key_resp_4.keys) > 0):
                key_resp_4.keys.pop()
        elif("return" in key_resp_4.keys):
            key_resp_4.keys.remove("return")
            
            screen_text = ''.join(key_resp_4.keys)
            thisExp.addData("recall_resp", screen_text)
            continueRoutine = False
        
        screen_text = ''.join(key_resp_4.keys)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_RespTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_RespTrial"-------
    for thisComponent in routine_RespTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
        # was no response the correct answer?!
        if str('').lower() == 'none':
           key_resp_4.corr = 1;  # correct non-response
        else:
           key_resp_4.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_4.keys',key_resp_4.keys)
    trials_2.addData('key_resp_4.corr', key_resp_4.corr)
    if key_resp_4.keys != None:  # we had a response
        trials_2.addData('key_resp_4.rt', key_resp_4.rt)
    if screen_text == "123":
        Ptrial = Ptrial + 1
    # the Routine "routine_RespTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 2 repeats of 'trials_2'


# ------Prepare to start Routine "routine_go"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
routine_goComponents = [text_go, key_resp_5]
for thisComponent in routine_goComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
routine_goClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "routine_go"-------
while continueRoutine:
    # get current time
    t = routine_goClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routine_goClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_go* updates
    if text_go.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        text_go.frameNStart = frameN  # exact frame index
        text_go.tStart = t  # local t and not account for scr refresh
        text_go.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_go, 'tStartRefresh')  # time at next scr refresh
        text_go.setAutoDraw(True)
    
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
    for thisComponent in routine_goComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_go"-------
for thisComponent in routine_goComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_go.started', text_go.tStartRefresh)
thisExp.addData('text_go.stopped', text_go.tStopRefresh)
# the Routine "routine_go" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Digit_span.xlsx'),
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
    
    # ------Prepare to start Routine "routine_round"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_3.setText(trials.thisRepN+1)
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    routine_roundComponents = [text_3, text_4, text_5, key_resp_3]
    for thisComponent in routine_roundComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    routine_roundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "routine_round"-------
    while continueRoutine:
        # get current time
        t = routine_roundClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routine_roundClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
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
        for thisComponent in routine_roundComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_round"-------
    for thisComponent in routine_roundComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "routine_round" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "routine_Dpres"-------
    continueRoutine = True
    routineTimer.add(16.500000)
    # update component parameters for each repeat
    
    if TotTrial == 0:
        DS = 3 
    
    
    Seq1.setText(S1)
    Seq2.setText(S2)
    Seq3.setText(S3)
    Seq4.setText(S4)
    Seq5.setText(S5)
    Seq6.setText(S6)
    Seq7.setText(S7)
    Seq8.setText(S8)
    Seq9.setText(S9)
    Seq10.setText(S10)
    Seq11.setText(S11)
    Seq12.setText(S12)
    Seq13.setText(S13)
    Seq14.setText(S14)
    Seq15.setText(S15)
    Seq16.setText(S16)
    # keep track of which components have finished
    routine_DpresComponents = [Seq1, Seq2, Seq3, Seq4, Seq5, Seq6, Seq7, Seq8, Seq9, Seq10, Seq11, Seq12, Seq13, Seq14, Seq15, Seq16]
    for thisComponent in routine_DpresComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    routine_DpresClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "routine_Dpres"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = routine_DpresClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routine_DpresClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if DS == 3:
            if t >=3.5:
                continueRoutine = False
        elif DS == 4:
            if t >= 4.5:
                continueRoutine = False
        elif DS == 5:
            if t >= 5.5:
                continueRoutine = False
        elif DS == 6:
            if t >= 6.5:
                continueRoutine = False
        elif DS == 7:
            if t >= 7.5:
                continueRoutine = False
        elif DS == 8:
            if t >= 8.5:
                continueRoutine = False
        elif DS == 9:
            if t >= 9.5:
                continueRoutine = False 
        elif DS == 10:
            if t >= 10.5:
                continueRoutine = False 
        elif DS == 11:
            if t >= 11.5:
                continueRoutine = False 
        elif DS == 12:
            if t >= 12.5:
                continueRoutine = False 
        elif DS == 13:
            if t >= 13.5:
                continueRoutine = False 
        elif DS == 14:
            if t >= 14.5:
                continueRoutine = False 
        elif DS == 15:
            if t >= 15.5:
                continueRoutine = False 
        elif DS == 16:
            if t >= 16.5:
                continueRoutine = False 
        
        # *Seq1* updates
        if Seq1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Seq1.frameNStart = frameN  # exact frame index
            Seq1.tStart = t  # local t and not account for scr refresh
            Seq1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq1, 'tStartRefresh')  # time at next scr refresh
            Seq1.setAutoDraw(True)
        if Seq1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq1.tStop = t  # not accounting for scr refresh
                Seq1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq1, 'tStopRefresh')  # time at next scr refresh
                Seq1.setAutoDraw(False)
        
        # *Seq2* updates
        if Seq2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            Seq2.frameNStart = frameN  # exact frame index
            Seq2.tStart = t  # local t and not account for scr refresh
            Seq2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq2, 'tStartRefresh')  # time at next scr refresh
            Seq2.setAutoDraw(True)
        if Seq2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq2.tStop = t  # not accounting for scr refresh
                Seq2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq2, 'tStopRefresh')  # time at next scr refresh
                Seq2.setAutoDraw(False)
        
        # *Seq3* updates
        if Seq3.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            Seq3.frameNStart = frameN  # exact frame index
            Seq3.tStart = t  # local t and not account for scr refresh
            Seq3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq3, 'tStartRefresh')  # time at next scr refresh
            Seq3.setAutoDraw(True)
        if Seq3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq3.tStop = t  # not accounting for scr refresh
                Seq3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq3, 'tStopRefresh')  # time at next scr refresh
                Seq3.setAutoDraw(False)
        
        # *Seq4* updates
        if Seq4.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            Seq4.frameNStart = frameN  # exact frame index
            Seq4.tStart = t  # local t and not account for scr refresh
            Seq4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq4, 'tStartRefresh')  # time at next scr refresh
            Seq4.setAutoDraw(True)
        if Seq4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq4.tStop = t  # not accounting for scr refresh
                Seq4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq4, 'tStopRefresh')  # time at next scr refresh
                Seq4.setAutoDraw(False)
        
        # *Seq5* updates
        if Seq5.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
            # keep track of start time/frame for later
            Seq5.frameNStart = frameN  # exact frame index
            Seq5.tStart = t  # local t and not account for scr refresh
            Seq5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq5, 'tStartRefresh')  # time at next scr refresh
            Seq5.setAutoDraw(True)
        if Seq5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq5.tStop = t  # not accounting for scr refresh
                Seq5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq5, 'tStopRefresh')  # time at next scr refresh
                Seq5.setAutoDraw(False)
        
        # *Seq6* updates
        if Seq6.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            Seq6.frameNStart = frameN  # exact frame index
            Seq6.tStart = t  # local t and not account for scr refresh
            Seq6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq6, 'tStartRefresh')  # time at next scr refresh
            Seq6.setAutoDraw(True)
        if Seq6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq6.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq6.tStop = t  # not accounting for scr refresh
                Seq6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq6, 'tStopRefresh')  # time at next scr refresh
                Seq6.setAutoDraw(False)
        
        # *Seq7* updates
        if Seq7.status == NOT_STARTED and tThisFlip >= 6.5-frameTolerance:
            # keep track of start time/frame for later
            Seq7.frameNStart = frameN  # exact frame index
            Seq7.tStart = t  # local t and not account for scr refresh
            Seq7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq7, 'tStartRefresh')  # time at next scr refresh
            Seq7.setAutoDraw(True)
        if Seq7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq7.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq7.tStop = t  # not accounting for scr refresh
                Seq7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq7, 'tStopRefresh')  # time at next scr refresh
                Seq7.setAutoDraw(False)
        
        # *Seq8* updates
        if Seq8.status == NOT_STARTED and tThisFlip >= 7.5-frameTolerance:
            # keep track of start time/frame for later
            Seq8.frameNStart = frameN  # exact frame index
            Seq8.tStart = t  # local t and not account for scr refresh
            Seq8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq8, 'tStartRefresh')  # time at next scr refresh
            Seq8.setAutoDraw(True)
        if Seq8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq8.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq8.tStop = t  # not accounting for scr refresh
                Seq8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq8, 'tStopRefresh')  # time at next scr refresh
                Seq8.setAutoDraw(False)
        
        # *Seq9* updates
        if Seq9.status == NOT_STARTED and tThisFlip >= 8.5-frameTolerance:
            # keep track of start time/frame for later
            Seq9.frameNStart = frameN  # exact frame index
            Seq9.tStart = t  # local t and not account for scr refresh
            Seq9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq9, 'tStartRefresh')  # time at next scr refresh
            Seq9.setAutoDraw(True)
        if Seq9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq9.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq9.tStop = t  # not accounting for scr refresh
                Seq9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq9, 'tStopRefresh')  # time at next scr refresh
                Seq9.setAutoDraw(False)
        
        # *Seq10* updates
        if Seq10.status == NOT_STARTED and tThisFlip >= 9.5-frameTolerance:
            # keep track of start time/frame for later
            Seq10.frameNStart = frameN  # exact frame index
            Seq10.tStart = t  # local t and not account for scr refresh
            Seq10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq10, 'tStartRefresh')  # time at next scr refresh
            Seq10.setAutoDraw(True)
        if Seq10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq10.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq10.tStop = t  # not accounting for scr refresh
                Seq10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq10, 'tStopRefresh')  # time at next scr refresh
                Seq10.setAutoDraw(False)
        
        # *Seq11* updates
        if Seq11.status == NOT_STARTED and tThisFlip >= 10.5-frameTolerance:
            # keep track of start time/frame for later
            Seq11.frameNStart = frameN  # exact frame index
            Seq11.tStart = t  # local t and not account for scr refresh
            Seq11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq11, 'tStartRefresh')  # time at next scr refresh
            Seq11.setAutoDraw(True)
        if Seq11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq11.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq11.tStop = t  # not accounting for scr refresh
                Seq11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq11, 'tStopRefresh')  # time at next scr refresh
                Seq11.setAutoDraw(False)
        
        # *Seq12* updates
        if Seq12.status == NOT_STARTED and tThisFlip >= 11.5-frameTolerance:
            # keep track of start time/frame for later
            Seq12.frameNStart = frameN  # exact frame index
            Seq12.tStart = t  # local t and not account for scr refresh
            Seq12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq12, 'tStartRefresh')  # time at next scr refresh
            Seq12.setAutoDraw(True)
        if Seq12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq12.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq12.tStop = t  # not accounting for scr refresh
                Seq12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq12, 'tStopRefresh')  # time at next scr refresh
                Seq12.setAutoDraw(False)
        
        # *Seq13* updates
        if Seq13.status == NOT_STARTED and tThisFlip >= 12.5-frameTolerance:
            # keep track of start time/frame for later
            Seq13.frameNStart = frameN  # exact frame index
            Seq13.tStart = t  # local t and not account for scr refresh
            Seq13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq13, 'tStartRefresh')  # time at next scr refresh
            Seq13.setAutoDraw(True)
        if Seq13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq13.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq13.tStop = t  # not accounting for scr refresh
                Seq13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq13, 'tStopRefresh')  # time at next scr refresh
                Seq13.setAutoDraw(False)
        
        # *Seq14* updates
        if Seq14.status == NOT_STARTED and tThisFlip >= 13.5-frameTolerance:
            # keep track of start time/frame for later
            Seq14.frameNStart = frameN  # exact frame index
            Seq14.tStart = t  # local t and not account for scr refresh
            Seq14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq14, 'tStartRefresh')  # time at next scr refresh
            Seq14.setAutoDraw(True)
        if Seq14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq14.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq14.tStop = t  # not accounting for scr refresh
                Seq14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq14, 'tStopRefresh')  # time at next scr refresh
                Seq14.setAutoDraw(False)
        
        # *Seq15* updates
        if Seq15.status == NOT_STARTED and tThisFlip >= 14.5-frameTolerance:
            # keep track of start time/frame for later
            Seq15.frameNStart = frameN  # exact frame index
            Seq15.tStart = t  # local t and not account for scr refresh
            Seq15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq15, 'tStartRefresh')  # time at next scr refresh
            Seq15.setAutoDraw(True)
        if Seq15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq15.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq15.tStop = t  # not accounting for scr refresh
                Seq15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq15, 'tStopRefresh')  # time at next scr refresh
                Seq15.setAutoDraw(False)
        
        # *Seq16* updates
        if Seq16.status == NOT_STARTED and tThisFlip >= 15.5-frameTolerance:
            # keep track of start time/frame for later
            Seq16.frameNStart = frameN  # exact frame index
            Seq16.tStart = t  # local t and not account for scr refresh
            Seq16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq16, 'tStartRefresh')  # time at next scr refresh
            Seq16.setAutoDraw(True)
        if Seq16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq16.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq16.tStop = t  # not accounting for scr refresh
                Seq16.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq16, 'tStopRefresh')  # time at next scr refresh
                Seq16.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_DpresComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_Dpres"-------
    for thisComponent in routine_DpresComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData("DS", DS)
    
    # ------Prepare to start Routine "routine_Dresp"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp2_2.keys = []
    key_resp2_2.rt = []
    _key_resp2_2_allKeys = []
    screen_text = ''
    
    
    # keep track of which components have finished
    routine_DrespComponents = [textType_2, textFeedback_2, key_resp2_2]
    for thisComponent in routine_DrespComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    routine_DrespClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "routine_Dresp"-------
    while continueRoutine:
        # get current time
        t = routine_DrespClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routine_DrespClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textType_2* updates
        if textType_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            textType_2.frameNStart = frameN  # exact frame index
            textType_2.tStart = t  # local t and not account for scr refresh
            textType_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textType_2, 'tStartRefresh')  # time at next scr refresh
            textType_2.setAutoDraw(True)
        
        # *textFeedback_2* updates
        if textFeedback_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            textFeedback_2.frameNStart = frameN  # exact frame index
            textFeedback_2.tStart = t  # local t and not account for scr refresh
            textFeedback_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textFeedback_2, 'tStartRefresh')  # time at next scr refresh
            textFeedback_2.setAutoDraw(True)
        if textFeedback_2.status == STARTED:  # only update if drawing
            textFeedback_2.setText(screen_text, log=False)
        
        # *key_resp2_2* updates
        waitOnFlip = False
        if key_resp2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp2_2.frameNStart = frameN  # exact frame index
            key_resp2_2.tStart = t  # local t and not account for scr refresh
            key_resp2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp2_2, 'tStartRefresh')  # time at next scr refresh
            key_resp2_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp2_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp2_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp2_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp2_2.getKeys(keyList=['1','2','3','4','5','6','7','8','9','backspace','return'], waitRelease=False)
            _key_resp2_2_allKeys.extend(theseKeys)
            if len(_key_resp2_2_allKeys):
                key_resp2_2.keys = [key.name for key in _key_resp2_2_allKeys]  # storing all keys
                key_resp2_2.rt = [key.rt for key in _key_resp2_2_allKeys]
                # was this correct?
                if (key_resp2_2.keys == str('')) or (key_resp2_2.keys == ''):
                    key_resp2_2.corr = 1
                else:
                    key_resp2_2.corr = 0
        if("backspace" in key_resp2_2.keys):
            key_resp2_2.keys.remove("backspace")
            
            if(len(key_resp2_2.keys) > 0):
                key_resp2_2.keys.pop()
        elif("return" in key_resp2_2.keys):
            key_resp2_2.keys.remove("return")
            
            screen_text = ''.join(key_resp2_2.keys)
            thisExp.addData("recall_resp", screen_text)
            continueRoutine = False
        
        screen_text = ''.join(key_resp2_2.keys)
        
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_DrespComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_Dresp"-------
    for thisComponent in routine_DrespComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp2_2.keys in ['', [], None]:  # No response was made
        key_resp2_2.keys = None
        # was no response the correct answer?!
        if str('').lower() == 'none':
           key_resp2_2.corr = 1;  # correct non-response
        else:
           key_resp2_2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp2_2.keys',key_resp2_2.keys)
    trials.addData('key_resp2_2.corr', key_resp2_2.corr)
    if key_resp2_2.keys != None:  # we had a response
        trials.addData('key_resp2_2.rt', key_resp2_2.rt)
    if DS == 3:
        if key_resp2_2.keys == CorrAns3:
            thisExp.addData("score", 1)
            DS = DS + 1
            TotTrial = TotTrial + 1
            DS_3Corr += 1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            DS_3Incorr += 1
    elif DS == 4:
        if key_resp2_2.keys == CorrAns4:
            thisExp.addData("score", 1)
            DS = DS + 1
            TotTrial = TotTrial + 1
            DS_4Corr += 1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            DS_4Incorr +=1
            if wrongAnswer == 2:
                DS = DS - 1
                wrongAnswer = 0
    elif DS == 5:
        if key_resp2_2.keys == CorrAns5:
            thisExp.addData("score", 1)
            DS = DS + 1
            TotTrial = TotTrial + 1
            DS_5Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            DS_5Incorr +=1
            if wrongAnswer == 2:
                DS = DS - 1
                wrongAnswer = 0
    elif DS == 6:
        if key_resp2_2.keys == CorrAns6:
            thisExp.addData("score", 1)
            DS = DS + 1
            TotTrial = TotTrial + 1
            DS_6Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            DS_6Incorr +=1
            if wrongAnswer == 2:
                DS = DS -1
                wrongAnswer = 0
    elif DS == 7:
        if key_resp2_2.keys == CorrAns7:
            thisExp.addData("score", 1)
            DS = DS + 1
            TotTrial = TotTrial + 1
            DS_7Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            DS_7Incorr +=1
            if wrongAnswer == 2:
                DS = DS -1
                wrongAnswer = 0
    elif DS == 8:
        if key_resp2_2.keys == CorrAns8:
            thisExp.addData("score", 1)
            DS = DS + 1
            TotTrial = TotTrial + 1
            DS_8Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            DS_8Incorr +=1
            if wrongAnswer == 2:
                DS = DS -1
                wrongAnswer = 0
    elif DS == 9:
        if key_resp2_2.keys == CorrAns9:
            thisExp.addData("score", 1)
            DS = DS + 1
            TotTrial = TotTrial + 1
            DS_9Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            DS_9Incorr +=1
            if wrongAnswer == 2:
                DS = DS -1
                wrongAnswer = 0
    elif DS == 10:
        if key_resp2_2.keys == CorrAns10:
            thisExp.addData("score", 1)
            DS = DS + 1
            TotTrial = TotTrial + 1
            DS_10Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            DS_10Incorr +=1
            if wrongAnswer == 2:
                DS = DS -1
                wrongAnswer = 0
    elif DS == 11:
        if key_resp2_2.keys == CorrAns11:
            thisExp.addData("score", 1)
            DS = DS + 1
            TotTrial = TotTrial + 1
            DS_11Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            DS_11Incorr +=1
            if wrongAnswer == 2:
                DS = DS -1
                wrongAnswer = 0
    elif DS == 12:
        if key_resp2_2.keys == CorrAns12:
            thisExp.addData("score", 1)
            DS = DS + 1
            TotTrial = TotTrial + 1
            DS_12Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            DS_12Incorr +=1
            if wrongAnswer == 2:
                DS = DS -1
                wrongAnswer = 0
    elif DS == 13:
        if key_resp2_2.keys == CorrAns13:
            thisExp.addData("score", 1)
            DS = DS + 1
            TotTrial = TotTrial + 1
            DS_13Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            DS_Incorr +=1
            if wrongAnswer == 2:
                DS = DS -1
                wrongAnswer = 0
    elif DS == 14:
        if key_resp2_2.keys == CorrAns14:
            thisExp.addData("score", 1)
            DS = DS + 1
            TotTrial = TotTrial + 1
            DS_14Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            DS_14Incorr +=1
            if wrongAnswer == 2:
                DS = DS -1
                wrongAnswer = 0
    elif DS == 15:
        if key_resp2_2.keys == CorrAns15:
            thisExp.addData("score", 1)
            DS = DS + 1
            TotTrial = TotTrial + 1
            DS_15Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            DS_15Incorr +=1
            if wrongAnswer == 2:
                DS = DS -1
                wrongAnswer = 0
    elif DS == 16:
        if key_resp2_2.keys == CorrAns16:
            thisExp.addData("score", 1)
            DS = DS + 1
            TotTrial = TotTrial + 1
            DS_16Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            DS_16Incorr +=1
            if wrongAnswer == 2:
                DS = DS -1
                wrongAnswer = 0
                
    print(DS)
    # the Routine "routine_Dresp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "InstrBack"-------
continueRoutine = True
# update component parameters for each repeat
wrongAns = 0

if DS_3Corr + DS_3Incorr != 0:
    Tot3 = DS_3Corr + DS_3Incorr
    HR3 = DS_3Corr / Tot3
else:
    HR3 = 0
    
if DS_4Corr + DS_4Incorr != 0:
    Tot4 = DS_4Corr + DS_4Incorr
    HR4 = DS_4Corr / Tot4
else:
    HR4 = 0
    
if DS_5Corr + DS_5Incorr != 0:
    Tot5 = DS_5Corr + DS_5Incorr
    HR5 = DS_5Corr / Tot5
else:
    HR5 = 0
    
if DS_6Corr + DS_6Incorr != 0:
    Tot6 = DS_6Corr + DS_6Incorr
    HR6 = DS_6Corr / Tot6
else:
    HR6 = 0

if DS_7Corr + DS_7Incorr != 0:
    Tot7 = DS_7Corr + DS_7Incorr
    HR7 = DS_7Corr / Tot7
else:
    HR7 = 0

if DS_8Corr + DS_8Incorr != 0:
    Tot8 = DS_8Corr + DS_8Incorr
    HR8 = DS_8Corr / Tot8
else:
    HR8 = 0

if DS_9Corr + DS_9Incorr != 0:
    Tot9 = DS_9Corr + DS_9Incorr
    HR9 = DS_9Corr / Tot9
else:
    HR9 = 0

if DS_10Corr + DS_10Incorr != 0:
    Tot10 = DS_10Corr + DS_10Incorr
    HR10 = DS_10Corr / Tot10
else:
    HR10 = 0

if DS_11Corr + DS_11Incorr != 0:
    Tot11 = DS_11Corr + DS_11Incorr
    HR11 = DS_11Corr / Tot11
else:
    HR11 = 0

if DS_12Corr + DS_12Incorr != 0:
    Tot12 = DS_12Corr + DS_12Incorr
    HR12 = DS_12Corr / Tot12
else:
    HR12 = 0

if DS_13Corr + DS_13Incorr != 0:
    Tot13 = DS_13Corr + DS_13Incorr
    HR13 = DS_13Corr / Tot13
else:
    HR13 = 0

if DS_14Corr + DS_14Incorr != 0:
    Tot14 = DS_14Corr + DS_14Incorr
    HR14 = DS_14Corr / Tot14
else:
    HR14 = 0

if DS_15Corr + DS_15Incorr != 0:
    Tot15 = DS_15Corr + DS_15Incorr
    HR15 = DS_15Corr / Tot15
else:
    HR15 = 0

if DS_16Corr + DS_16Incorr != 0:
    Tot16 = DS_16Corr + DS_16Incorr
    HR16 = DS_16Corr / Tot16
else:
    HR16 = 0


FDS_score = 2.5+HR3+HR4+HR5+HR6+HR7+HR8+HR9+HR10+HR11+HR12+HR13+HR14+HR15+HR16
thisExp.addData("Forward WM score", FDS_score)
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InstrBackComponents = [text, key_resp]
for thisComponent in InstrBackComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstrBackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstrBack"-------
while continueRoutine:
    # get current time
    t = InstrBackClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstrBackClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
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
        theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
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
    for thisComponent in InstrBackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstrBack"-------
for thisComponent in InstrBackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "InstrBack" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('back_digit_span.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "routine_round_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_9.setText(trials_3.thisTrialN +1)
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    routine_round_2Components = [text_9, text_10, text_11, key_resp_7]
    for thisComponent in routine_round_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    routine_round_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "routine_round_2"-------
    while continueRoutine:
        # get current time
        t = routine_round_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routine_round_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            text_9.setAutoDraw(True)
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        
        # *text_11* updates
        if text_11.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_11.frameNStart = frameN  # exact frame index
            text_11.tStart = t  # local t and not account for scr refresh
            text_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
            text_11.setAutoDraw(True)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_round_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_round_2"-------
    for thisComponent in routine_round_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "routine_round_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "routine_BackPres"-------
    continueRoutine = True
    routineTimer.add(16.500000)
    # update component parameters for each repeat
    if B_TotTrial == 0:
        B_DS = 3 
    Seq1_b.setText(S1)
    Seq2_b.setText(S2)
    Seq3_b.setText(S3)
    Seq4_b.setText(S4)
    Seq5_b.setText(S5)
    Seq6_b.setText(S6)
    Seq7_b.setText(S7)
    Seq8_b.setText(S8)
    Seq9_b.setText(S9)
    Seq10_b.setText(S10)
    Seq11_b.setText(S11)
    Seq12_b.setText(S12)
    Seq13_b.setText(S13)
    Seq14_b.setText(S14)
    Seq15_b.setText(S15)
    Seq16_b.setText(S16)
    # keep track of which components have finished
    routine_BackPresComponents = [Seq1_b, Seq2_b, Seq3_b, Seq4_b, Seq5_b, Seq6_b, Seq7_b, Seq8_b, Seq9_b, Seq10_b, Seq11_b, Seq12_b, Seq13_b, Seq14_b, Seq15_b, Seq16_b]
    for thisComponent in routine_BackPresComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    routine_BackPresClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "routine_BackPres"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = routine_BackPresClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routine_BackPresClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if B_DS == 3:
            if t >=3.5:
                continueRoutine = False
        elif B_DS == 4:
            if t >= 4.5:
                continueRoutine = False
        elif B_DS == 5:
            if t >= 5.5:
                continueRoutine = False
        elif B_DS == 6:
            if t >= 6.5:
                continueRoutine = False
        elif B_DS == 7:
            if t >= 7.5:
                continueRoutine = False
        elif B_DS == 8:
            if t >= 8.5:
                continueRoutine = False
        elif B_DS == 9:
            if t >= 9.5:
                continueRoutine = False 
        elif B_DS == 10:
            if t >= 10.5:
                continueRoutine = False 
        elif B_DS == 11:
            if t >= 11.5:
                continueRoutine = False 
        elif B_DS == 12:
            if t >= 12.5:
                continueRoutine = False 
        elif B_DS == 13:
            if t >= 13.5:
                continueRoutine = False 
        elif B_DS == 14:
            if t >= 14.5:
                continueRoutine = False 
        elif B_DS == 15:
            if t >= 15.5:
                continueRoutine = False 
        elif B_DS == 16:
            if t >= 16.5:
                continueRoutine = False 
        
        # *Seq1_b* updates
        if Seq1_b.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Seq1_b.frameNStart = frameN  # exact frame index
            Seq1_b.tStart = t  # local t and not account for scr refresh
            Seq1_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq1_b, 'tStartRefresh')  # time at next scr refresh
            Seq1_b.setAutoDraw(True)
        if Seq1_b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq1_b.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq1_b.tStop = t  # not accounting for scr refresh
                Seq1_b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq1_b, 'tStopRefresh')  # time at next scr refresh
                Seq1_b.setAutoDraw(False)
        
        # *Seq2_b* updates
        if Seq2_b.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            Seq2_b.frameNStart = frameN  # exact frame index
            Seq2_b.tStart = t  # local t and not account for scr refresh
            Seq2_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq2_b, 'tStartRefresh')  # time at next scr refresh
            Seq2_b.setAutoDraw(True)
        if Seq2_b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq2_b.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq2_b.tStop = t  # not accounting for scr refresh
                Seq2_b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq2_b, 'tStopRefresh')  # time at next scr refresh
                Seq2_b.setAutoDraw(False)
        
        # *Seq3_b* updates
        if Seq3_b.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            Seq3_b.frameNStart = frameN  # exact frame index
            Seq3_b.tStart = t  # local t and not account for scr refresh
            Seq3_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq3_b, 'tStartRefresh')  # time at next scr refresh
            Seq3_b.setAutoDraw(True)
        if Seq3_b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq3_b.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq3_b.tStop = t  # not accounting for scr refresh
                Seq3_b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq3_b, 'tStopRefresh')  # time at next scr refresh
                Seq3_b.setAutoDraw(False)
        
        # *Seq4_b* updates
        if Seq4_b.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            Seq4_b.frameNStart = frameN  # exact frame index
            Seq4_b.tStart = t  # local t and not account for scr refresh
            Seq4_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq4_b, 'tStartRefresh')  # time at next scr refresh
            Seq4_b.setAutoDraw(True)
        if Seq4_b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq4_b.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq4_b.tStop = t  # not accounting for scr refresh
                Seq4_b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq4_b, 'tStopRefresh')  # time at next scr refresh
                Seq4_b.setAutoDraw(False)
        
        # *Seq5_b* updates
        if Seq5_b.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
            # keep track of start time/frame for later
            Seq5_b.frameNStart = frameN  # exact frame index
            Seq5_b.tStart = t  # local t and not account for scr refresh
            Seq5_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq5_b, 'tStartRefresh')  # time at next scr refresh
            Seq5_b.setAutoDraw(True)
        if Seq5_b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq5_b.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq5_b.tStop = t  # not accounting for scr refresh
                Seq5_b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq5_b, 'tStopRefresh')  # time at next scr refresh
                Seq5_b.setAutoDraw(False)
        
        # *Seq6_b* updates
        if Seq6_b.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            Seq6_b.frameNStart = frameN  # exact frame index
            Seq6_b.tStart = t  # local t and not account for scr refresh
            Seq6_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq6_b, 'tStartRefresh')  # time at next scr refresh
            Seq6_b.setAutoDraw(True)
        if Seq6_b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq6_b.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq6_b.tStop = t  # not accounting for scr refresh
                Seq6_b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq6_b, 'tStopRefresh')  # time at next scr refresh
                Seq6_b.setAutoDraw(False)
        
        # *Seq7_b* updates
        if Seq7_b.status == NOT_STARTED and tThisFlip >= 6.5-frameTolerance:
            # keep track of start time/frame for later
            Seq7_b.frameNStart = frameN  # exact frame index
            Seq7_b.tStart = t  # local t and not account for scr refresh
            Seq7_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq7_b, 'tStartRefresh')  # time at next scr refresh
            Seq7_b.setAutoDraw(True)
        if Seq7_b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq7_b.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq7_b.tStop = t  # not accounting for scr refresh
                Seq7_b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq7_b, 'tStopRefresh')  # time at next scr refresh
                Seq7_b.setAutoDraw(False)
        
        # *Seq8_b* updates
        if Seq8_b.status == NOT_STARTED and tThisFlip >= 7.5-frameTolerance:
            # keep track of start time/frame for later
            Seq8_b.frameNStart = frameN  # exact frame index
            Seq8_b.tStart = t  # local t and not account for scr refresh
            Seq8_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq8_b, 'tStartRefresh')  # time at next scr refresh
            Seq8_b.setAutoDraw(True)
        if Seq8_b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq8_b.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq8_b.tStop = t  # not accounting for scr refresh
                Seq8_b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq8_b, 'tStopRefresh')  # time at next scr refresh
                Seq8_b.setAutoDraw(False)
        
        # *Seq9_b* updates
        if Seq9_b.status == NOT_STARTED and tThisFlip >= 8.5-frameTolerance:
            # keep track of start time/frame for later
            Seq9_b.frameNStart = frameN  # exact frame index
            Seq9_b.tStart = t  # local t and not account for scr refresh
            Seq9_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq9_b, 'tStartRefresh')  # time at next scr refresh
            Seq9_b.setAutoDraw(True)
        if Seq9_b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq9_b.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq9_b.tStop = t  # not accounting for scr refresh
                Seq9_b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq9_b, 'tStopRefresh')  # time at next scr refresh
                Seq9_b.setAutoDraw(False)
        
        # *Seq10_b* updates
        if Seq10_b.status == NOT_STARTED and tThisFlip >= 9.5-frameTolerance:
            # keep track of start time/frame for later
            Seq10_b.frameNStart = frameN  # exact frame index
            Seq10_b.tStart = t  # local t and not account for scr refresh
            Seq10_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq10_b, 'tStartRefresh')  # time at next scr refresh
            Seq10_b.setAutoDraw(True)
        if Seq10_b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq10_b.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq10_b.tStop = t  # not accounting for scr refresh
                Seq10_b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq10_b, 'tStopRefresh')  # time at next scr refresh
                Seq10_b.setAutoDraw(False)
        
        # *Seq11_b* updates
        if Seq11_b.status == NOT_STARTED and tThisFlip >= 10.5-frameTolerance:
            # keep track of start time/frame for later
            Seq11_b.frameNStart = frameN  # exact frame index
            Seq11_b.tStart = t  # local t and not account for scr refresh
            Seq11_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq11_b, 'tStartRefresh')  # time at next scr refresh
            Seq11_b.setAutoDraw(True)
        if Seq11_b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq11_b.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq11_b.tStop = t  # not accounting for scr refresh
                Seq11_b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq11_b, 'tStopRefresh')  # time at next scr refresh
                Seq11_b.setAutoDraw(False)
        
        # *Seq12_b* updates
        if Seq12_b.status == NOT_STARTED and tThisFlip >= 11.5-frameTolerance:
            # keep track of start time/frame for later
            Seq12_b.frameNStart = frameN  # exact frame index
            Seq12_b.tStart = t  # local t and not account for scr refresh
            Seq12_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq12_b, 'tStartRefresh')  # time at next scr refresh
            Seq12_b.setAutoDraw(True)
        if Seq12_b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq12_b.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq12_b.tStop = t  # not accounting for scr refresh
                Seq12_b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq12_b, 'tStopRefresh')  # time at next scr refresh
                Seq12_b.setAutoDraw(False)
        
        # *Seq13_b* updates
        if Seq13_b.status == NOT_STARTED and tThisFlip >= 12.5-frameTolerance:
            # keep track of start time/frame for later
            Seq13_b.frameNStart = frameN  # exact frame index
            Seq13_b.tStart = t  # local t and not account for scr refresh
            Seq13_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq13_b, 'tStartRefresh')  # time at next scr refresh
            Seq13_b.setAutoDraw(True)
        if Seq13_b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq13_b.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq13_b.tStop = t  # not accounting for scr refresh
                Seq13_b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq13_b, 'tStopRefresh')  # time at next scr refresh
                Seq13_b.setAutoDraw(False)
        
        # *Seq14_b* updates
        if Seq14_b.status == NOT_STARTED and tThisFlip >= 13.5-frameTolerance:
            # keep track of start time/frame for later
            Seq14_b.frameNStart = frameN  # exact frame index
            Seq14_b.tStart = t  # local t and not account for scr refresh
            Seq14_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq14_b, 'tStartRefresh')  # time at next scr refresh
            Seq14_b.setAutoDraw(True)
        if Seq14_b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq14_b.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq14_b.tStop = t  # not accounting for scr refresh
                Seq14_b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq14_b, 'tStopRefresh')  # time at next scr refresh
                Seq14_b.setAutoDraw(False)
        
        # *Seq15_b* updates
        if Seq15_b.status == NOT_STARTED and tThisFlip >= 14.5-frameTolerance:
            # keep track of start time/frame for later
            Seq15_b.frameNStart = frameN  # exact frame index
            Seq15_b.tStart = t  # local t and not account for scr refresh
            Seq15_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq15_b, 'tStartRefresh')  # time at next scr refresh
            Seq15_b.setAutoDraw(True)
        if Seq15_b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq15_b.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq15_b.tStop = t  # not accounting for scr refresh
                Seq15_b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq15_b, 'tStopRefresh')  # time at next scr refresh
                Seq15_b.setAutoDraw(False)
        
        # *Seq16_b* updates
        if Seq16_b.status == NOT_STARTED and tThisFlip >= 15.5-frameTolerance:
            # keep track of start time/frame for later
            Seq16_b.frameNStart = frameN  # exact frame index
            Seq16_b.tStart = t  # local t and not account for scr refresh
            Seq16_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Seq16_b, 'tStartRefresh')  # time at next scr refresh
            Seq16_b.setAutoDraw(True)
        if Seq16_b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Seq16_b.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Seq16_b.tStop = t  # not accounting for scr refresh
                Seq16_b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Seq16_b, 'tStopRefresh')  # time at next scr refresh
                Seq16_b.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_BackPresComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_BackPres"-------
    for thisComponent in routine_BackPresComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData("B_DS", B_DS)
    
    # ------Prepare to start Routine "routine_BackResp"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp2_2B.keys = []
    key_resp2_2B.rt = []
    _key_resp2_2B_allKeys = []
    screen_text = ''
    
    
    # keep track of which components have finished
    routine_BackRespComponents = [textType_2B, textFeedback_2B, key_resp2_2B]
    for thisComponent in routine_BackRespComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    routine_BackRespClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "routine_BackResp"-------
    while continueRoutine:
        # get current time
        t = routine_BackRespClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routine_BackRespClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textType_2B* updates
        if textType_2B.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            textType_2B.frameNStart = frameN  # exact frame index
            textType_2B.tStart = t  # local t and not account for scr refresh
            textType_2B.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textType_2B, 'tStartRefresh')  # time at next scr refresh
            textType_2B.setAutoDraw(True)
        
        # *textFeedback_2B* updates
        if textFeedback_2B.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            textFeedback_2B.frameNStart = frameN  # exact frame index
            textFeedback_2B.tStart = t  # local t and not account for scr refresh
            textFeedback_2B.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textFeedback_2B, 'tStartRefresh')  # time at next scr refresh
            textFeedback_2B.setAutoDraw(True)
        if textFeedback_2B.status == STARTED:  # only update if drawing
            textFeedback_2B.setText(screen_text, log=False)
        
        # *key_resp2_2B* updates
        waitOnFlip = False
        if key_resp2_2B.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp2_2B.frameNStart = frameN  # exact frame index
            key_resp2_2B.tStart = t  # local t and not account for scr refresh
            key_resp2_2B.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp2_2B, 'tStartRefresh')  # time at next scr refresh
            key_resp2_2B.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp2_2B.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp2_2B.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp2_2B.status == STARTED and not waitOnFlip:
            theseKeys = key_resp2_2B.getKeys(keyList=['1','2','3','4','5','6','7','8','9','backspace','return'], waitRelease=False)
            _key_resp2_2B_allKeys.extend(theseKeys)
            if len(_key_resp2_2B_allKeys):
                key_resp2_2B.keys = [key.name for key in _key_resp2_2B_allKeys]  # storing all keys
                key_resp2_2B.rt = [key.rt for key in _key_resp2_2B_allKeys]
                # was this correct?
                if (key_resp2_2B.keys == str('')) or (key_resp2_2B.keys == ''):
                    key_resp2_2B.corr = 1
                else:
                    key_resp2_2B.corr = 0
        if("backspace" in key_resp2_2B.keys):
            key_resp2_2B.keys.remove("backspace")
            
            if(len(key_resp2_2B.keys) > 0):
                key_resp2_2B.keys.pop()
        elif("return" in key_resp2_2B.keys):
            key_resp2_2B.keys.remove("return")
            
            screen_text = ''.join(key_resp2_2B.keys)
            thisExp.addData("recall_resp", screen_text)
            continueRoutine = False
        
        screen_text = ''.join(key_resp2_2B.keys)
        
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_BackRespComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_BackResp"-------
    for thisComponent in routine_BackRespComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp2_2B.keys in ['', [], None]:  # No response was made
        key_resp2_2B.keys = None
        # was no response the correct answer?!
        if str('').lower() == 'none':
           key_resp2_2B.corr = 1;  # correct non-response
        else:
           key_resp2_2B.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('key_resp2_2B.keys',key_resp2_2B.keys)
    trials_3.addData('key_resp2_2B.corr', key_resp2_2B.corr)
    if key_resp2_2B.keys != None:  # we had a response
        trials_3.addData('key_resp2_2B.rt', key_resp2_2B.rt)
    if B_DS == 3:
        if key_resp2_2B.keys == CorrAns3:
            thisExp.addData("score", 1)
            B_DS = B_DS + 1
            B_TotTrial = B_TotTrial + 1
            B_DS_3Corr += 1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            B_TotTrial = B_TotTrial + 1
            B_DS_3Incorr += 1
                
    elif B_DS == 4:
        if key_resp2_2B.keys == CorrAns4:
            thisExp.addData("score", 1)
            B_DS = B_DS + 1
            B_TotTrial = B_TotTrial + 1
            B_DS_4Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            B_DS_4Incorr += 1
            if wrongAnswer == 2:
                B_DS = B_DS - 1
                wrongAnswer = 0
    elif B_DS == 5:
        if key_resp2_2B.keys == CorrAns5:
            thisExp.addData("score", 1)
            B_DS = B_DS + 1
            TotTrial = TotTrial + 1
            B_DS_5Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            B_DS_5Incorr += 1
            if wrongAnswer == 2:
                B_DS = B_DS - 1
                wrongAnswer = 0
    elif B_DS == 6:
        if key_resp2_2B.keys == CorrAns6:
            thisExp.addData("score", 1)
            B_DS = B_DS + 1
            TotTrial = TotTrial + 1
            B_DS_6Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            B_DS_6Incorr += 1
            if wrongAnswer == 2:
                B_DS = B_DS -1
                wrongAnswer = 0
    elif B_DS == 7:
        if key_resp2_2B.keys == CorrAns7:
            thisExp.addData("score", 1)
            B_DS = B_DS + 1
            TotTrial = TotTrial + 1
            B_DS_7Corr += 1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            B_DS_7Incorr +=1
            if wrongAnswer == 2:
                B_DS = B_DS -1
                wrongAnswer = 0
    elif B_DS == 8:
        if key_resp2_2B.keys == CorrAns8:
            thisExp.addData("score", 1)
            B_DS = B_DS + 1
            TotTrial = TotTrial + 1
            B_DS_8Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            B_DS_8Incorr +=1
            if wrongAnswer == 2:
                B_DS = B_DS -1
                wrongAnswer = 0
    elif B_DS == 9:
        if key_resp2_2B.keys == CorrAns9:
            thisExp.addData("score", 1)
            B_DS = B_DS + 1
            TotTrial = TotTrial + 1
            B_DS_9Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            B_DS_9Incorr += 1
            if wrongAnswer == 2:
                B_DS = B_DS -1
                wrongAnswer = 0
    elif B_DS == 10:
        if key_resp2_2B.keys == CorrAns10:
            thisExp.addData("score", 1)
            B_DS = B_DS + 1
            TotTrial = TotTrial + 1
            B_DS_10Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            B_DS_10Incorr +=1
            if wrongAnswer == 2:
                B_DS = B_DS -1
                wrongAnswer = 0
    elif B_DS == 11:
        if key_resp2_2B.keys == CorrAns11:
            thisExp.addData("score", 1)
            B_DS = B_DS + 1
            TotTrial = TotTrial + 1
            B_DS_11Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            B_DS_11Incorr +=1
            if wrongAnswer == 2:
                B_DS = B_DS -1
                wrongAnswer = 0
    elif B_DS == 12:
        if key_resp2_2B.keys == CorrAns12:
            thisExp.addData("score", 1)
            B_DS = B_DS + 1
            TotTrial = TotTrial + 1
            B_DS_12Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            B_DS_12Incorr +=1
            if wrongAnswer == 2:
                B_DS = B_DS -1
                wrongAnswer = 0
    elif B_DS == 13:
        if key_resp2_2B.keys == CorrAns13:
            thisExp.addData("score", 1)
            B_DS = B_DS + 1
            TotTrial = TotTrial + 1
            B_DS_13Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            B_DS_13Incorr +=1
            if wrongAnswer == 2:
                B_DS = B_DS -1
                wrongAnswer = 0
    elif B_DS == 14:
        if key_resp2_2B.keys == CorrAns14:
            thisExp.addData("score", 1)
            B_DS = B_DS + 1
            TotTrial = TotTrial + 1
            B_DS_14Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            B_DS_14Incorr +=1
            if wrongAnswer == 2:
                B_DS = B_DS -1
                wrongAnswer = 0
    elif B_DS == 15:
        if key_resp2_2B.keys == CorrAns15:
            thisExp.addData("score", 1)
            B_DS = B_DS + 1
            TotTrial = TotTrial + 1
            B_DS_15Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            B_DS_15Incorr +=1
            if wrongAnswer == 2:
                B_DS = B_DS -1
                wrongAnswer = 0
    elif B_DS == 16:
        if key_resp2_2B.keys == CorrAns16:
            thisExp.addData("score", 1)
            B_DS = B_DS + 1
            TotTrial = TotTrial + 1
            B_DS_16Corr +=1
            wrongAnswer = 0
        else:
            thisExp.addData("score", 0)
            wrongAnswer = wrongAnswer + 1
            TotTrial = TotTrial + 1
            B_DS_16Incorr +=1
            if wrongAnswer == 2:
                B_DS = B_DS -1
                wrongAnswer = 0
    # the Routine "routine_BackResp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'

# get names of stimulus parameters
if trials_3.trialList in ([], [None], None):
    params = []
else:
    params = trials_3.trialList[0].keys()
# save data for this loop
trials_3.saveAsText(filename + 'trials_3.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Goodbye"-------
continueRoutine = True
routineTimer.add(6.500000)
# update component parameters for each repeat
if B_DS_3Corr + B_DS_3Incorr != 0:
    B_Tot3 = B_DS_3Corr + B_DS_3Incorr
    BHR3 = B_DS_3Corr / B_Tot3
else:
    BHR3 = 0

if B_DS_4Corr + B_DS_4Incorr != 0:
    B_Tot4 = B_DS_5Corr + B_DS_4Incorr
    BHR4 = B_DS_4Corr / B_Tot4
else:
    BHR4 = 0

if B_DS_5Corr + B_DS_5Incorr != 0:
    B_Tot5 = B_DS_5Corr + B_DS_5Incorr
    BHR5 = B_DS_5Corr / B_Tot5
else:
    BHR5 = 0

if B_DS_6Corr + B_DS_6Incorr != 0:
    B_Tot6 = B_DS_6Corr + B_DS_6Incorr
    BHR6 = B_DS_6Corr / B_Tot6
else:
    BHR6 = 0

if B_DS_7Corr + B_DS_7Incorr != 0:
    B_Tot7 = B_DS_7Corr + B_DS_7Incorr
    BHR7 = B_DS_7Corr / B_Tot7
else:
    BHR7 = 0

if B_DS_8Corr + B_DS_8Incorr != 0:
    B_Tot8 = B_DS_8Corr + B_DS_8Incorr
    BHR8 = B_DS_8Corr / B_Tot8
else:
    BHR8 = 0
    
if B_DS_9Corr + B_DS_9Incorr != 0:
    B_Tot9 = B_DS_9Corr + B_DS_9Incorr
    BHR9 = B_DS_9Corr / B_Tot9
else:
    BHR9 = 0

if B_DS_10Corr + B_DS_10Incorr != 0:
    B_Tot10 = B_DS_10Corr + B_DS_10Incorr
    BHR10 = B_DS_10Corr / B_Tot10
else:
    BHR10 = 0

if B_DS_11Corr + B_DS_11Incorr != 0:
    B_Tot11 = B_DS_11Corr + B_DS_11Incorr
    BHR11 = B_DS_11Corr / B_Tot11
else:
    BHR11 = 0

if B_DS_12Corr + B_DS_12Incorr != 0:
    B_Tot12 = B_DS_12Corr + B_DS_12Incorr
    BHR12 = B_DS_12Corr / B_Tot12
else:
    BHR12 = 0

if B_DS_13Corr + B_DS_13Incorr != 0:
    B_Tot13 = B_DS_13Corr + B_DS_13Incorr
    BHR13 = B_DS_13Corr / B_Tot13
else:
    BHR13 = 0

if B_DS_14Corr + B_DS_14Incorr != 0:
    B_Tot14 = B_DS_14Corr + B_DS_14Incorr
    BHR14 = B_DS_14Corr / B_Tot14
else:
    BHR14 = 0

if B_DS_15Corr + B_DS_15Incorr != 0:
    B_Tot15 = B_DS_15Corr + B_DS_15Incorr
    BHR15 = B_DS_15Corr / B_Tot15
else:
    BHR15 = 0

if B_DS_16Corr + B_DS_16Incorr != 0:
    B_Tot16 = B_DS_16Corr + B_DS_16Incorr
    BHR16 = B_DS_16Corr / B_Tot16
else:
    BHR16 = 0


BDS_score = 2.5+BHR3+BHR4+BHR5+BHR6+BHR7+BHR8+BHR9+BHR10+BHR11+BHR12+BHR13+BHR14+BHR15+BHR16
thisExp.addData("Backward WM score", BDS_score)

# keep track of which components have finished
GoodbyeComponents = [GB]
for thisComponent in GoodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GoodbyeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Goodbye"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = GoodbyeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GoodbyeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GB* updates
    if GB.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        GB.frameNStart = frameN  # exact frame index
        GB.tStart = t  # local t and not account for scr refresh
        GB.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GB, 'tStartRefresh')  # time at next scr refresh
        GB.setAutoDraw(True)
    if GB.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GB.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            GB.tStop = t  # not accounting for scr refresh
            GB.frameNStop = frameN  # exact frame index
            win.timeOnFlip(GB, 'tStopRefresh')  # time at next scr refresh
            GB.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Goodbye"-------
for thisComponent in GoodbyeComponents:
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
