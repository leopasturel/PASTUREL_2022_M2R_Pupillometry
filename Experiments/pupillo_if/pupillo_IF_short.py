#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on March 28, 2022, at 11:54
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')


from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, iohub, hardware
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
psychopyVersion = '2021.2.3'
expName = 'pupillo_imaf'  # from the Builder filename that created this script
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
    originPath='D:\\final\\pupillo_imaf\\pupillo_IF_short.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 1024], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='oculo', color=[0.0000, 0.0000, 0.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = 'eyetracker.hw.sr_research.eyelink.EyeTracker'
ioConfig = {
    ioDevice: {
        'name': 'tracker',
        'model_name': 'EYELINK 1000 DESKTOP',
        'simulation_mode': False,
        'network_settings': '100.1.1.1',
        'default_native_data_file_name': 'EXPFILE',
        'runtime_settings': {
            'sampling_rate': 1000.0,
            'track_eyes': 'RIGHT_EYE',
            'sample_filtering': {
                'sample_filtering': 'FILTER_LEVEL_2',
                'elLiveFiltering': 'FILTER_LEVEL_OFF',
            },
            'vog_settings': {
                'pupil_measure_types': 'PUPIL_DIAMETER',
                'tracking_mode': 'PUPIL_CR_TRACKING',
                'pupil_center_algorithm': 'ELLIPSE_FIT',
            }
        }
    }
}
ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, experiment_code='pupillo_imaf', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
instruction = visual.TextStim(win=win, name='instruction',
    text="Pour rappel, vous allez participer à une expérience d'imagerie. Celle-ci se décompose en 4 phases.\n\n1) Vous allez voir une croix apparaître au centre de l'écran. Un signal auditif vous indiquera la couleur, blanche ou noire, que vous devrez ensuite imaginer.\n2) La croix de fixation va être remplacée par les contours d’un triangle. Vous devrez mentalement imaginer le remplir avec la couleur, blanche ou noire, que vous aurez entendu à l’étape précédente. Deux signaux sonores marqueront respectivement le début et la fin de cette phase d’imagination.\n3) Les contours du triangle vont disparaître et la croix de fixation va réapparaître. Veuillez garder les yeux fixés sur la croix.\n4) Un triangle va apparaître à l’écran. Veuillez garder les yeux fixés sur le triangle.\n5) Le triangle va disparaître et la croix de fixation va réapparaître. Veuillez garder les yeux fixés sur la croix.\n6) Vous devrez répondre à une question portant sur la vivacité de votre image mentale.\n\nPendant l’expérience, essayez de limiter les clignements des yeux et ne bougez pas la tête.\n\n(Appuyer sur la barre d'espace pour continuer)",
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='lightgrey', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instr = keyboard.Keyboard()

# Initialize components for Routine "Start_train"
Start_trainClock = core.Clock()
key_resp_train = keyboard.Keyboard()
text_train = visual.TextStim(win=win, name='text_train',
    text="Nous allons commencer par une phase d'entraînement.\n\nPour rappel, dès que vous entendrez le signal sonore, vous devrez essayer de remplir le triangle mentalement avec la couleur, blanche ou noire, entendue au début de l’essai.\nEnsuite, veuillez garder les yeux au centre de l’écran jusqu’à la fin de l’essai.\n\nVeuillez fixer la croix au centre de l'écran.\n\n(Appuyer sur la barre d'espace pour commencer)",
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='lightgrey', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Block_test"
Block_testClock = core.Clock()
rest_1 = visual.Rect(
    win=win, name='rest_1',
    width=(2,2)[0], height=(2,2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0],
    opacity=None, depth=0.0, interpolate=True)
rest_2 = visual.Rect(
    win=win, name='rest_2',
    width=(2,2)[0], height=(2,2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0],
    opacity=None, depth=-1.0, interpolate=True)
color_sound = sound.Sound('A', secs=0.5, stereo=True, hamming=False,
    name='color_sound')
color_sound.setVolume(5.0)
fix_cross = visual.ShapeStim(
    win=win, name='fix_cross', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=0.2,     colorSpace='rgb',  lineColor=[-0.2, -0.2, -0.2], fillColor=[-0.2, -0.2, -0.2],
    opacity=None, depth=-3.0, interpolate=True)
imag = visual.ShapeStim(
    win=win, name='imag',units='pix', 
    size=[695, 695], vertices='triangle',
    ori=1.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0,0,0],
    opacity=None, depth=-4.0, interpolate=True)
start_sound_imag = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='start_sound_imag')
start_sound_imag.setVolume(1.0)
end_sound_imag = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='end_sound_imag')
end_sound_imag.setVolume(1.0)
stimuli = visual.ShapeStim(
    win=win, name='stimuli',units='pix', 
    size=[695, 695], vertices='triangle',
    ori=1.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
etRecord = hardware.eyetracker.EyetrackerControl(
    server=ioServer,
    tracker=eyetracker
)

# Initialize components for Routine "Question_vividness"
Question_vividnessClock = core.Clock()
question_vivid = visual.TextStim(win=win, name='question_vivid',
    text='Avec quelle vivacité avez-vous imaginé ou visualisé la couleur ?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='lightgrey', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
vivid = visual.Slider(win=win, name='vivid',
    startValue=None, size=(0.8, 0.1), pos=(0, 0), units=None,
    labels=('Pas du tout vive\nAucune couleur n\'est apparue\ndans l\'imagerie', '', '', 'Très vive\nPresque comme si elle\navait été vue'), ticks=(1, 2, 3, 4), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='lightgrey', fillColor='dimgrey', borderColor='lightgrey', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "Start_test"
Start_testClock = core.Clock()
key_resp_start = keyboard.Keyboard()
text_start = visual.TextStim(win=win, name='text_start',
    text="L’entraînement est terminé. Nous allons commencer l’expérience.\n\nPour rappel, dès que vous entendrez le signal sonore, vous devrez essayer de remplir le triangle mentalement avec la couleur, blanche ou noire, entendue au début de l’essai.\nEnsuite, veuillez garder les yeux au centre de l’écran jusqu’à la fin de l’essai.\n\nVeuillez fixer la croix au centre de l'écran.\n\n(Appuyer sur la barre d'espace pour commencer)",
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='lightgrey', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Block_test"
Block_testClock = core.Clock()
rest_1 = visual.Rect(
    win=win, name='rest_1',
    width=(2,2)[0], height=(2,2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0],
    opacity=None, depth=0.0, interpolate=True)
rest_2 = visual.Rect(
    win=win, name='rest_2',
    width=(2,2)[0], height=(2,2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0],
    opacity=None, depth=-1.0, interpolate=True)
color_sound = sound.Sound('A', secs=0.5, stereo=True, hamming=False,
    name='color_sound')
color_sound.setVolume(5.0)
fix_cross = visual.ShapeStim(
    win=win, name='fix_cross', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=0.2,     colorSpace='rgb',  lineColor=[-0.2, -0.2, -0.2], fillColor=[-0.2, -0.2, -0.2],
    opacity=None, depth=-3.0, interpolate=True)
imag = visual.ShapeStim(
    win=win, name='imag',units='pix', 
    size=[695, 695], vertices='triangle',
    ori=1.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0,0,0],
    opacity=None, depth=-4.0, interpolate=True)
start_sound_imag = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='start_sound_imag')
start_sound_imag.setVolume(1.0)
end_sound_imag = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='end_sound_imag')
end_sound_imag.setVolume(1.0)
stimuli = visual.ShapeStim(
    win=win, name='stimuli',units='pix', 
    size=[695, 695], vertices='triangle',
    ori=1.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
etRecord = hardware.eyetracker.EyetrackerControl(
    server=ioServer,
    tracker=eyetracker
)

# Initialize components for Routine "Question_vividness"
Question_vividnessClock = core.Clock()
question_vivid = visual.TextStim(win=win, name='question_vivid',
    text='Avec quelle vivacité avez-vous imaginé ou visualisé la couleur ?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='lightgrey', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
vivid = visual.Slider(win=win, name='vivid',
    startValue=None, size=(0.8, 0.1), pos=(0, 0), units=None,
    labels=('Pas du tout vive\nAucune couleur n\'est apparue\ndans l\'imagerie', '', '', 'Très vive\nPresque comme si elle\navait été vue'), ticks=(1, 2, 3, 4), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='lightgrey', fillColor='dimgrey', borderColor='lightgrey', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "End"
EndClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text='Vos réponses ont bien été enregistrées !\nNous vous remercions pour votre participation !',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='lightgrey', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_end = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# -------Run Routine 'Calibration'-------

# define target for Calibration
CalibrationTarget = visual.TargetStim(win, 
    name='CalibrationTarget',
    radius=0.01, fillColor='', borderColor='black', lineWidth=2.0,
    innerRadius=0.0035, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
    colorSpace='rgb', units=None
)
# define parameters for Calibration
Calibration = hardware.eyetracker.EyetrackerCalibration(win, 
    eyetracker, CalibrationTarget,
    units=None, colorSpace='rgb',
    progressMode='time', targetDur=1.5, expandScale=1.5,
    targetLayout='FIVE_POINTS', randomisePos=True,
    movementAnimation=True, targetDelay=1.0
)
# run calibration
Calibration.run()
# clear any keypresses from during Calibration so they don't interfere with the experiment
defaultKeyboard.clearEvents()
# the Routine "Calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instruction"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_instr.keys = []
key_resp_instr.rt = []
_key_resp_instr_allKeys = []
# keep track of which components have finished
InstructionComponents = [instruction, key_resp_instr]
for thisComponent in InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction"-------
while continueRoutine:
    # get current time
    t = InstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction* updates
    if instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction.frameNStart = frameN  # exact frame index
        instruction.tStart = t  # local t and not account for scr refresh
        instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
        instruction.setAutoDraw(True)
    
    # *key_resp_instr* updates
    waitOnFlip = False
    if key_resp_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instr.frameNStart = frameN  # exact frame index
        key_resp_instr.tStart = t  # local t and not account for scr refresh
        key_resp_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instr, 'tStartRefresh')  # time at next scr refresh
        key_resp_instr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instr.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instr.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_instr_allKeys.extend(theseKeys)
        if len(_key_resp_instr_allKeys):
            key_resp_instr.keys = _key_resp_instr_allKeys[-1].name  # just the last key pressed
            key_resp_instr.rt = _key_resp_instr_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction"-------
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction.started', instruction.tStartRefresh)
thisExp.addData('instruction.stopped', instruction.tStopRefresh)
# check responses
if key_resp_instr.keys in ['', [], None]:  # No response was made
    key_resp_instr.keys = None
thisExp.addData('key_resp_instr.keys',key_resp_instr.keys)
if key_resp_instr.keys != None:  # we had a response
    thisExp.addData('key_resp_instr.rt', key_resp_instr.rt)
thisExp.addData('key_resp_instr.started', key_resp_instr.tStartRefresh)
thisExp.addData('key_resp_instr.stopped', key_resp_instr.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start_train"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_train.keys = []
key_resp_train.rt = []
_key_resp_train_allKeys = []
# keep track of which components have finished
Start_trainComponents = [key_resp_train, text_train]
for thisComponent in Start_trainComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Start_trainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Start_train"-------
while continueRoutine:
    # get current time
    t = Start_trainClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Start_trainClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_train* updates
    waitOnFlip = False
    if key_resp_train.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_train.frameNStart = frameN  # exact frame index
        key_resp_train.tStart = t  # local t and not account for scr refresh
        key_resp_train.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_train, 'tStartRefresh')  # time at next scr refresh
        key_resp_train.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_train.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_train.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_train.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_train.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_train_allKeys.extend(theseKeys)
        if len(_key_resp_train_allKeys):
            key_resp_train.keys = _key_resp_train_allKeys[-1].name  # just the last key pressed
            key_resp_train.rt = _key_resp_train_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_train* updates
    if text_train.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_train.frameNStart = frameN  # exact frame index
        text_train.tStart = t  # local t and not account for scr refresh
        text_train.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_train, 'tStartRefresh')  # time at next scr refresh
        text_train.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_trainComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_train"-------
for thisComponent in Start_trainComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_train.keys in ['', [], None]:  # No response was made
    key_resp_train.keys = None
thisExp.addData('key_resp_train.keys',key_resp_train.keys)
if key_resp_train.keys != None:  # we had a response
    thisExp.addData('key_resp_train.rt', key_resp_train.rt)
thisExp.addData('key_resp_train.started', key_resp_train.tStartRefresh)
thisExp.addData('key_resp_train.stopped', key_resp_train.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_train.started', text_train.tStartRefresh)
thisExp.addData('text_train.stopped', text_train.tStopRefresh)
# the Routine "Start_train" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
training = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/conditions_pupillo_train.xlsx'),
    seed=None, name='training')
thisExp.addLoop(training)  # add the loop to the experiment
thisTraining = training.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
if thisTraining != None:
    for paramName in thisTraining:
        exec('{} = thisTraining[paramName]'.format(paramName))

for thisTraining in training:
    currentLoop = training
    # abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
    if thisTraining != None:
        for paramName in thisTraining:
            exec('{} = thisTraining[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Block_test"-------
    continueRoutine = True
    routineTimer.add(28.000000)
    # update component parameters for each repeat
    color_sound.setSound(sound_color, secs=0.5, hamming=False)
    color_sound.setVolume(5.0, log=False)
    imag.setOri(orientation)
    imag.setLineColor(border_col)
    start_sound_imag.setSound('A', secs=0.5, hamming=True)
    start_sound_imag.setVolume(1.0, log=False)
    end_sound_imag.setSound('A', secs=0.5, hamming=True)
    end_sound_imag.setVolume(1.0, log=False)
    stimuli.setFillColor(color_rgb)
    stimuli.setOri(orientation)
    stimuli.setLineColor(border_col)
    # keep track of which components have finished
    Block_testComponents = [rest_1, rest_2, color_sound, fix_cross, imag, start_sound_imag, end_sound_imag, stimuli, etRecord]
    for thisComponent in Block_testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block_test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Block_testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block_testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest_1* updates
        if rest_1.status == NOT_STARTED and tThisFlip >= 8.2-frameTolerance:
            # keep track of start time/frame for later
            rest_1.frameNStart = frameN  # exact frame index
            rest_1.tStart = t  # local t and not account for scr refresh
            rest_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_1, 'tStartRefresh')  # time at next scr refresh
            rest_1.setAutoDraw(True)
        if rest_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest_1.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                rest_1.tStop = t  # not accounting for scr refresh
                rest_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest_1, 'tStopRefresh')  # time at next scr refresh
                rest_1.setAutoDraw(False)
        
        # *rest_2* updates
        if rest_2.status == NOT_STARTED and tThisFlip >= 17.2-frameTolerance:
            # keep track of start time/frame for later
            rest_2.frameNStart = frameN  # exact frame index
            rest_2.tStart = t  # local t and not account for scr refresh
            rest_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_2, 'tStartRefresh')  # time at next scr refresh
            rest_2.setAutoDraw(True)
        if rest_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest_2.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                rest_2.tStop = t  # not accounting for scr refresh
                rest_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest_2, 'tStopRefresh')  # time at next scr refresh
                rest_2.setAutoDraw(False)
        # start/stop color_sound
        if color_sound.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
            # keep track of start time/frame for later
            color_sound.frameNStart = frameN  # exact frame index
            color_sound.tStart = t  # local t and not account for scr refresh
            color_sound.tStartRefresh = tThisFlipGlobal  # on global time
            color_sound.play(when=win)  # sync with win flip
        if color_sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > color_sound.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                color_sound.tStop = t  # not accounting for scr refresh
                color_sound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(color_sound, 'tStopRefresh')  # time at next scr refresh
                color_sound.stop()
        
        # *fix_cross* updates
        if fix_cross.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
            # keep track of start time/frame for later
            fix_cross.frameNStart = frameN  # exact frame index
            fix_cross.tStart = t  # local t and not account for scr refresh
            fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
            fix_cross.setAutoDraw(True)
        if fix_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross.tStartRefresh + 26.6-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross.tStop = t  # not accounting for scr refresh
                fix_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                fix_cross.setAutoDraw(False)
        
        # *imag* updates
        if imag.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
            # keep track of start time/frame for later
            imag.frameNStart = frameN  # exact frame index
            imag.tStart = t  # local t and not account for scr refresh
            imag.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imag, 'tStartRefresh')  # time at next scr refresh
            imag.setAutoDraw(True)
        if imag.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imag.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                imag.tStop = t  # not accounting for scr refresh
                imag.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imag, 'tStopRefresh')  # time at next scr refresh
                imag.setAutoDraw(False)
        # start/stop start_sound_imag
        if start_sound_imag.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
            # keep track of start time/frame for later
            start_sound_imag.frameNStart = frameN  # exact frame index
            start_sound_imag.tStart = t  # local t and not account for scr refresh
            start_sound_imag.tStartRefresh = tThisFlipGlobal  # on global time
            start_sound_imag.play(when=win)  # sync with win flip
        if start_sound_imag.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_sound_imag.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                start_sound_imag.tStop = t  # not accounting for scr refresh
                start_sound_imag.frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_sound_imag, 'tStopRefresh')  # time at next scr refresh
                start_sound_imag.stop()
        # start/stop end_sound_imag
        if end_sound_imag.status == NOT_STARTED and tThisFlip >= 7.7-frameTolerance:
            # keep track of start time/frame for later
            end_sound_imag.frameNStart = frameN  # exact frame index
            end_sound_imag.tStart = t  # local t and not account for scr refresh
            end_sound_imag.tStartRefresh = tThisFlipGlobal  # on global time
            end_sound_imag.play(when=win)  # sync with win flip
        if end_sound_imag.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_sound_imag.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                end_sound_imag.tStop = t  # not accounting for scr refresh
                end_sound_imag.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_sound_imag, 'tStopRefresh')  # time at next scr refresh
                end_sound_imag.stop()
        
        # *stimuli* updates
        if stimuli.status == NOT_STARTED and tThisFlip >= 12.2-frameTolerance:
            # keep track of start time/frame for later
            stimuli.frameNStart = frameN  # exact frame index
            stimuli.tStart = t  # local t and not account for scr refresh
            stimuli.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli, 'tStartRefresh')  # time at next scr refresh
            stimuli.setAutoDraw(True)
        if stimuli.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                stimuli.tStop = t  # not accounting for scr refresh
                stimuli.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli, 'tStopRefresh')  # time at next scr refresh
                stimuli.setAutoDraw(False)
        # *etRecord* updates
        if etRecord.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            etRecord.frameNStart = frameN  # exact frame index
            etRecord.tStart = t  # local t and not account for scr refresh
            etRecord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord, 'tStartRefresh')  # time at next scr refresh
            etRecord.status = STARTED
        if etRecord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord.tStartRefresh + 28-frameTolerance:
                # keep track of stop time/frame for later
                etRecord.tStop = t  # not accounting for scr refresh
                etRecord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(etRecord, 'tStopRefresh')  # time at next scr refresh
                etRecord.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block_test"-------
    for thisComponent in Block_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    training.addData('rest_1.started', rest_1.tStartRefresh)
    training.addData('rest_1.stopped', rest_1.tStopRefresh)
    training.addData('rest_2.started', rest_2.tStartRefresh)
    training.addData('rest_2.stopped', rest_2.tStopRefresh)
    color_sound.stop()  # ensure sound has stopped at end of routine
    training.addData('color_sound.started', color_sound.tStartRefresh)
    training.addData('color_sound.stopped', color_sound.tStopRefresh)
    training.addData('fix_cross.started', fix_cross.tStartRefresh)
    training.addData('fix_cross.stopped', fix_cross.tStopRefresh)
    training.addData('imag.started', imag.tStartRefresh)
    training.addData('imag.stopped', imag.tStopRefresh)
    start_sound_imag.stop()  # ensure sound has stopped at end of routine
    training.addData('start_sound_imag.started', start_sound_imag.tStartRefresh)
    training.addData('start_sound_imag.stopped', start_sound_imag.tStopRefresh)
    end_sound_imag.stop()  # ensure sound has stopped at end of routine
    training.addData('end_sound_imag.started', end_sound_imag.tStartRefresh)
    training.addData('end_sound_imag.stopped', end_sound_imag.tStopRefresh)
    training.addData('stimuli.started', stimuli.tStartRefresh)
    training.addData('stimuli.stopped', stimuli.tStopRefresh)
    # make sure the eyetracker recording stops
    if etRecord.status != FINISHED:
        etRecord.status = FINISHED
    
    # ------Prepare to start Routine "Question_vividness"-------
    continueRoutine = True
    # update component parameters for each repeat
    vivid.reset()
    # keep track of which components have finished
    Question_vividnessComponents = [question_vivid, vivid]
    for thisComponent in Question_vividnessComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Question_vividnessClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Question_vividness"-------
    while continueRoutine:
        # get current time
        t = Question_vividnessClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Question_vividnessClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *question_vivid* updates
        if question_vivid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_vivid.frameNStart = frameN  # exact frame index
            question_vivid.tStart = t  # local t and not account for scr refresh
            question_vivid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_vivid, 'tStartRefresh')  # time at next scr refresh
            question_vivid.setAutoDraw(True)
        
        # *vivid* updates
        if vivid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vivid.frameNStart = frameN  # exact frame index
            vivid.tStart = t  # local t and not account for scr refresh
            vivid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vivid, 'tStartRefresh')  # time at next scr refresh
            vivid.setAutoDraw(True)
        
        # Check vivid for response to end routine
        if vivid.getRating() is not None and vivid.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Question_vividnessComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Question_vividness"-------
    for thisComponent in Question_vividnessComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    training.addData('question_vivid.started', question_vivid.tStartRefresh)
    training.addData('question_vivid.stopped', question_vivid.tStopRefresh)
    training.addData('vivid.response', vivid.getRating())
    training.addData('vivid.rt', vivid.getRT())
    training.addData('vivid.started', vivid.tStartRefresh)
    training.addData('vivid.stopped', vivid.tStopRefresh)
    # the Routine "Question_vividness" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'training'


# ------Prepare to start Routine "Start_test"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_start.keys = []
key_resp_start.rt = []
_key_resp_start_allKeys = []
# keep track of which components have finished
Start_testComponents = [key_resp_start, text_start]
for thisComponent in Start_testComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Start_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Start_test"-------
while continueRoutine:
    # get current time
    t = Start_testClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Start_testClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_start* updates
    waitOnFlip = False
    if key_resp_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_start.frameNStart = frameN  # exact frame index
        key_resp_start.tStart = t  # local t and not account for scr refresh
        key_resp_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_start, 'tStartRefresh')  # time at next scr refresh
        key_resp_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_start.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_start.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_start_allKeys.extend(theseKeys)
        if len(_key_resp_start_allKeys):
            key_resp_start.keys = _key_resp_start_allKeys[-1].name  # just the last key pressed
            key_resp_start.rt = _key_resp_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_start* updates
    if text_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_start.frameNStart = frameN  # exact frame index
        text_start.tStart = t  # local t and not account for scr refresh
        text_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_start, 'tStartRefresh')  # time at next scr refresh
        text_start.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_testComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_test"-------
for thisComponent in Start_testComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_start.keys in ['', [], None]:  # No response was made
    key_resp_start.keys = None
thisExp.addData('key_resp_start.keys',key_resp_start.keys)
if key_resp_start.keys != None:  # we had a response
    thisExp.addData('key_resp_start.rt', key_resp_start.rt)
thisExp.addData('key_resp_start.started', key_resp_start.tStartRefresh)
thisExp.addData('key_resp_start.stopped', key_resp_start.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_start.started', text_start.tStartRefresh)
thisExp.addData('text_start.stopped', text_start.tStopRefresh)
# the Routine "Start_test" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
test = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/conditions_pupillo_short.xlsx'),
    seed=None, name='test')
thisExp.addLoop(test)  # add the loop to the experiment
thisTest = test.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
if thisTest != None:
    for paramName in thisTest:
        exec('{} = thisTest[paramName]'.format(paramName))

for thisTest in test:
    currentLoop = test
    # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
    if thisTest != None:
        for paramName in thisTest:
            exec('{} = thisTest[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Block_test"-------
    continueRoutine = True
    routineTimer.add(28.000000)
    # update component parameters for each repeat
    color_sound.setSound(sound_color, secs=0.5, hamming=False)
    color_sound.setVolume(5.0, log=False)
    imag.setOri(orientation)
    imag.setLineColor(border_col)
    start_sound_imag.setSound('A', secs=0.5, hamming=True)
    start_sound_imag.setVolume(1.0, log=False)
    end_sound_imag.setSound('A', secs=0.5, hamming=True)
    end_sound_imag.setVolume(1.0, log=False)
    stimuli.setFillColor(color_rgb)
    stimuli.setOri(orientation)
    stimuli.setLineColor(border_col)
    # keep track of which components have finished
    Block_testComponents = [rest_1, rest_2, color_sound, fix_cross, imag, start_sound_imag, end_sound_imag, stimuli, etRecord]
    for thisComponent in Block_testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block_test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Block_testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block_testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest_1* updates
        if rest_1.status == NOT_STARTED and tThisFlip >= 8.2-frameTolerance:
            # keep track of start time/frame for later
            rest_1.frameNStart = frameN  # exact frame index
            rest_1.tStart = t  # local t and not account for scr refresh
            rest_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_1, 'tStartRefresh')  # time at next scr refresh
            rest_1.setAutoDraw(True)
        if rest_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest_1.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                rest_1.tStop = t  # not accounting for scr refresh
                rest_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest_1, 'tStopRefresh')  # time at next scr refresh
                rest_1.setAutoDraw(False)
        
        # *rest_2* updates
        if rest_2.status == NOT_STARTED and tThisFlip >= 17.2-frameTolerance:
            # keep track of start time/frame for later
            rest_2.frameNStart = frameN  # exact frame index
            rest_2.tStart = t  # local t and not account for scr refresh
            rest_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_2, 'tStartRefresh')  # time at next scr refresh
            rest_2.setAutoDraw(True)
        if rest_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest_2.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                rest_2.tStop = t  # not accounting for scr refresh
                rest_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest_2, 'tStopRefresh')  # time at next scr refresh
                rest_2.setAutoDraw(False)
        # start/stop color_sound
        if color_sound.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
            # keep track of start time/frame for later
            color_sound.frameNStart = frameN  # exact frame index
            color_sound.tStart = t  # local t and not account for scr refresh
            color_sound.tStartRefresh = tThisFlipGlobal  # on global time
            color_sound.play(when=win)  # sync with win flip
        if color_sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > color_sound.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                color_sound.tStop = t  # not accounting for scr refresh
                color_sound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(color_sound, 'tStopRefresh')  # time at next scr refresh
                color_sound.stop()
        
        # *fix_cross* updates
        if fix_cross.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
            # keep track of start time/frame for later
            fix_cross.frameNStart = frameN  # exact frame index
            fix_cross.tStart = t  # local t and not account for scr refresh
            fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
            fix_cross.setAutoDraw(True)
        if fix_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross.tStartRefresh + 26.6-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross.tStop = t  # not accounting for scr refresh
                fix_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                fix_cross.setAutoDraw(False)
        
        # *imag* updates
        if imag.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
            # keep track of start time/frame for later
            imag.frameNStart = frameN  # exact frame index
            imag.tStart = t  # local t and not account for scr refresh
            imag.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imag, 'tStartRefresh')  # time at next scr refresh
            imag.setAutoDraw(True)
        if imag.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imag.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                imag.tStop = t  # not accounting for scr refresh
                imag.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imag, 'tStopRefresh')  # time at next scr refresh
                imag.setAutoDraw(False)
        # start/stop start_sound_imag
        if start_sound_imag.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
            # keep track of start time/frame for later
            start_sound_imag.frameNStart = frameN  # exact frame index
            start_sound_imag.tStart = t  # local t and not account for scr refresh
            start_sound_imag.tStartRefresh = tThisFlipGlobal  # on global time
            start_sound_imag.play(when=win)  # sync with win flip
        if start_sound_imag.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_sound_imag.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                start_sound_imag.tStop = t  # not accounting for scr refresh
                start_sound_imag.frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_sound_imag, 'tStopRefresh')  # time at next scr refresh
                start_sound_imag.stop()
        # start/stop end_sound_imag
        if end_sound_imag.status == NOT_STARTED and tThisFlip >= 7.7-frameTolerance:
            # keep track of start time/frame for later
            end_sound_imag.frameNStart = frameN  # exact frame index
            end_sound_imag.tStart = t  # local t and not account for scr refresh
            end_sound_imag.tStartRefresh = tThisFlipGlobal  # on global time
            end_sound_imag.play(when=win)  # sync with win flip
        if end_sound_imag.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_sound_imag.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                end_sound_imag.tStop = t  # not accounting for scr refresh
                end_sound_imag.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_sound_imag, 'tStopRefresh')  # time at next scr refresh
                end_sound_imag.stop()
        
        # *stimuli* updates
        if stimuli.status == NOT_STARTED and tThisFlip >= 12.2-frameTolerance:
            # keep track of start time/frame for later
            stimuli.frameNStart = frameN  # exact frame index
            stimuli.tStart = t  # local t and not account for scr refresh
            stimuli.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli, 'tStartRefresh')  # time at next scr refresh
            stimuli.setAutoDraw(True)
        if stimuli.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                stimuli.tStop = t  # not accounting for scr refresh
                stimuli.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli, 'tStopRefresh')  # time at next scr refresh
                stimuli.setAutoDraw(False)
        # *etRecord* updates
        if etRecord.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            etRecord.frameNStart = frameN  # exact frame index
            etRecord.tStart = t  # local t and not account for scr refresh
            etRecord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord, 'tStartRefresh')  # time at next scr refresh
            etRecord.status = STARTED
        if etRecord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord.tStartRefresh + 28-frameTolerance:
                # keep track of stop time/frame for later
                etRecord.tStop = t  # not accounting for scr refresh
                etRecord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(etRecord, 'tStopRefresh')  # time at next scr refresh
                etRecord.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block_test"-------
    for thisComponent in Block_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    test.addData('rest_1.started', rest_1.tStartRefresh)
    test.addData('rest_1.stopped', rest_1.tStopRefresh)
    test.addData('rest_2.started', rest_2.tStartRefresh)
    test.addData('rest_2.stopped', rest_2.tStopRefresh)
    color_sound.stop()  # ensure sound has stopped at end of routine
    test.addData('color_sound.started', color_sound.tStartRefresh)
    test.addData('color_sound.stopped', color_sound.tStopRefresh)
    test.addData('fix_cross.started', fix_cross.tStartRefresh)
    test.addData('fix_cross.stopped', fix_cross.tStopRefresh)
    test.addData('imag.started', imag.tStartRefresh)
    test.addData('imag.stopped', imag.tStopRefresh)
    start_sound_imag.stop()  # ensure sound has stopped at end of routine
    test.addData('start_sound_imag.started', start_sound_imag.tStartRefresh)
    test.addData('start_sound_imag.stopped', start_sound_imag.tStopRefresh)
    end_sound_imag.stop()  # ensure sound has stopped at end of routine
    test.addData('end_sound_imag.started', end_sound_imag.tStartRefresh)
    test.addData('end_sound_imag.stopped', end_sound_imag.tStopRefresh)
    test.addData('stimuli.started', stimuli.tStartRefresh)
    test.addData('stimuli.stopped', stimuli.tStopRefresh)
    # make sure the eyetracker recording stops
    if etRecord.status != FINISHED:
        etRecord.status = FINISHED
    
    # ------Prepare to start Routine "Question_vividness"-------
    continueRoutine = True
    # update component parameters for each repeat
    vivid.reset()
    # keep track of which components have finished
    Question_vividnessComponents = [question_vivid, vivid]
    for thisComponent in Question_vividnessComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Question_vividnessClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Question_vividness"-------
    while continueRoutine:
        # get current time
        t = Question_vividnessClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Question_vividnessClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *question_vivid* updates
        if question_vivid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_vivid.frameNStart = frameN  # exact frame index
            question_vivid.tStart = t  # local t and not account for scr refresh
            question_vivid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_vivid, 'tStartRefresh')  # time at next scr refresh
            question_vivid.setAutoDraw(True)
        
        # *vivid* updates
        if vivid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vivid.frameNStart = frameN  # exact frame index
            vivid.tStart = t  # local t and not account for scr refresh
            vivid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vivid, 'tStartRefresh')  # time at next scr refresh
            vivid.setAutoDraw(True)
        
        # Check vivid for response to end routine
        if vivid.getRating() is not None and vivid.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Question_vividnessComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Question_vividness"-------
    for thisComponent in Question_vividnessComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    test.addData('question_vivid.started', question_vivid.tStartRefresh)
    test.addData('question_vivid.stopped', question_vivid.tStopRefresh)
    test.addData('vivid.response', vivid.getRating())
    test.addData('vivid.rt', vivid.getRT())
    test.addData('vivid.started', vivid.tStartRefresh)
    test.addData('vivid.stopped', vivid.tStopRefresh)
    # the Routine "Question_vividness" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'test'

# get names of stimulus parameters
if test.trialList in ([], [None], None):
    params = []
else:
    params = test.trialList[0].keys()
# save data for this loop
test.saveAsExcel(filename + '.xlsx', sheetName='test',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
test.saveAsText(filename + 'test.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_end.keys = []
key_resp_end.rt = []
_key_resp_end_allKeys = []
# keep track of which components have finished
EndComponents = [text_end, key_resp_end]
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
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end* updates
    if text_end.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_end.frameNStart = frameN  # exact frame index
        text_end.tStart = t  # local t and not account for scr refresh
        text_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_end, 'tStartRefresh')  # time at next scr refresh
        text_end.setAutoDraw(True)
    if text_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_end.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_end.tStop = t  # not accounting for scr refresh
            text_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_end, 'tStopRefresh')  # time at next scr refresh
            text_end.setAutoDraw(False)
    
    # *key_resp_end* updates
    waitOnFlip = False
    if key_resp_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_end.frameNStart = frameN  # exact frame index
        key_resp_end.tStart = t  # local t and not account for scr refresh
        key_resp_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_end, 'tStartRefresh')  # time at next scr refresh
        key_resp_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_end.clock.reset)  # t=0 on next screen flip
    if key_resp_end.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_end.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_end_allKeys.extend(theseKeys)
        if len(_key_resp_end_allKeys):
            key_resp_end.keys = _key_resp_end_allKeys[-1].name  # just the last key pressed
            key_resp_end.rt = _key_resp_end_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
thisExp.addData('text_end.started', text_end.tStartRefresh)
thisExp.addData('text_end.stopped', text_end.tStopRefresh)
# check responses
if key_resp_end.keys in ['', [], None]:  # No response was made
    key_resp_end.keys = None
thisExp.addData('key_resp_end.keys',key_resp_end.keys)
if key_resp_end.keys != None:  # we had a response
    thisExp.addData('key_resp_end.rt', key_resp_end.rt)
thisExp.addData('key_resp_end.started', key_resp_end.tStartRefresh)
thisExp.addData('key_resp_end.stopped', key_resp_end.tStopRefresh)
thisExp.nextEntry()
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
