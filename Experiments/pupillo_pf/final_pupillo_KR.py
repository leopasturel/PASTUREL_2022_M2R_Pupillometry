#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on March 28, 2022, at 11:48
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
expName = 'pupillo_repli'  # from the Builder filename that created this script
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
    originPath='D:\\final\\pupillo_repli\\pupillo_KR.py',
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


def stim_size():
    """Determine the size, in pixel, of the stimuli to display
    In this function, we use the formula sqrt(3)/2*c with c the size of the
    triangles, to calculate the heigth of the equilateral triangles.
    This function is derived from Pythagore theorem"""
    
    screen_px_x = win.size[0] # in px
    screen_px_y = win.size[1] # in px
    
    distance_to_screen = 65 # in cm. To be modified if you change distance eye/monitor.
    
    if screen_px_x == 1920:
        screen_x = 34.5 # in cm
        screen_y = 19.4 # in cm
        desired_stim_x = 12.5 * distance_to_screen / 57 # Use distance_to_screen = 57
        desired_stim_y = np.sqrt(3)/2*desired_stim_x
    
    elif screen_px_x == 2560:
        screen_x = 64 # in cm
        screen_y = 40 # in cm
        desired_stim_x = 12.5 * distance_to_screen / 57 # Use distance_to_screen = 70
        desired_stim_y = np.sqrt(3)/2*desired_stim_x
    
    elif screen_px_x == 1280:
        screen_x = 36 # in cm
        screen_y = 27.5 # in cm
        desired_stim_x = 12.5 * distance_to_screen / 57 # Use distance_to_screen = 65
        desired_stim_y = np.sqrt(3)/2*desired_stim_x
    
    stim_x = desired_stim_x * screen_px_x / screen_x
    stim_y = desired_stim_y * screen_px_y / screen_y
    
    return (stim_x, stim_y)

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
ioServer = io.launchHubServer(window=win, experiment_code='pupillo_repli', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
instruction = visual.TextStim(win=win, name='instruction',
    text="Pour rappel, vous allez participer à une expérience d'imagerie. Celle-ci se décompose en 4 phases.\n\n1) Vous allez voir un triangle apparaître au centre de l'écran. \n2) Le triangle va être remplacé par un masque dynamique.\n3) L'écran va redevenir gris. Deux signaux sonores marqueront respectivement le début et la fin de la phase d’imagination. Entre ces deux signaux, vous devrez revisualiser le même triangle en prenant en considération sa taille, son orientation et son intensité lumineuse, et ce tout en gardant les yeux fixés sur la croix centrale.\n4) Vous devrez répondre à une question portant sur la vivacité de votre image mentale.\n\nPendant l’expérience, essayez de limiter les clignements des yeux et ne bougez pas la tête.\n\n(Appuyer sur la barre d'espace pour continuer)",
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=1.0, ori=0.0, 
    color='lightgrey', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instr = keyboard.Keyboard()

# Initialize components for Routine "Start_train"
Start_trainClock = core.Clock()
text_train = visual.TextStim(win=win, name='text_train',
    text="Nous allons commencer par une phase d'entraînement.\n\nPour rappel, concentrez-vous sur le triangle et essayez de mémoriser sa taille, son orientation et sa couleur. \nDès que vous entendrez le signal sonore, imaginez ou revisualisez ce triangle aussi précisément que possible.\n\nVeuillez fixer la croix au centre de l'écran.\n\n(Appuyer sur la barre d'espace pour commencer)",
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='lightgrey', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_train = keyboard.Keyboard()

# Initialize components for Routine "Block_test"
Block_testClock = core.Clock()
rest = visual.NoiseStim(
    win=win, name='rest',units='norm', 
    noiseImage=None, mask=None,
    ori=0.0, pos=(0, 0), size=(2,2), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=None, blendmode='avg', contrast=1.0,
    texRes=256, filter=None,
    noiseType='Uniform', noiseElementSize=[0.005], 
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=10.0, imageComponent='Phase', interpolate=False, depth=0.0)
rest.buildNoise()
fix_cross = visual.ShapeStim(
    win=win, name='fix_cross', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=0.2,     colorSpace='rgb',  lineColor=[-0.2, -0.2, -0.2], fillColor=[-0.2, -0.2, -0.2],
    opacity=None, depth=-1.0, interpolate=True)
stimuli = visual.ShapeStim(
    win=win, name='stimuli',units='pix', 
    size=[695.65, 695.88], vertices='triangle',
    ori=1.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
start_sound_imag = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='start_sound_imag')
start_sound_imag.setVolume(1.0)
end_sound_imag = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='end_sound_imag')
end_sound_imag.setVolume(1.0)
etRecord = hardware.eyetracker.EyetrackerControl(
    server=ioServer,
    tracker=eyetracker
)

# Initialize components for Routine "Question_vividness"
Question_vividnessClock = core.Clock()
question_vivid = visual.TextStim(win=win, name='question_vivid',
    text='Avec quelle vivacité avez-vous imaginé ou revisualisé le triangle ?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='lightgrey', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
vivid = visual.Slider(win=win, name='vivid',
    startValue=None, size=(0.8, 0.1), pos=(0, 0), units=None,
    labels=('Pas du tout vive\nAucune forme n\'est apparue\ndans l\'imagerie', '', '', 'Très vive\nPresque comme si elle\navait été vue'), ticks=(1, 2, 3, 4), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='lightgrey', fillColor='dimgrey', borderColor='lightgrey', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "Start_test"
Start_testClock = core.Clock()
key_resp_start = keyboard.Keyboard()
text_start = visual.TextStim(win=win, name='text_start',
    text="La phase d'entraînement est terminée !\n\nNous allons maintenant passer à la véritable expérience.\n\nPour rappel, concentrez-vous sur le triangle et essayez de mémoriser sa taille, son orientation et sa couleur. \nDès que vous entendrez le signal sonore, imaginez ou revisualisez ce triangle aussi précisément que possible.\n\nVeuillez fixer la croix au centre de l'écran.\n\n(Appuyer sur la barre d'espace pour commencer)",
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='lightgrey', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Block_test"
Block_testClock = core.Clock()
rest = visual.NoiseStim(
    win=win, name='rest',units='norm', 
    noiseImage=None, mask=None,
    ori=0.0, pos=(0, 0), size=(2,2), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=None, blendmode='avg', contrast=1.0,
    texRes=256, filter=None,
    noiseType='Uniform', noiseElementSize=[0.005], 
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=10.0, imageComponent='Phase', interpolate=False, depth=0.0)
rest.buildNoise()
fix_cross = visual.ShapeStim(
    win=win, name='fix_cross', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=0.2,     colorSpace='rgb',  lineColor=[-0.2, -0.2, -0.2], fillColor=[-0.2, -0.2, -0.2],
    opacity=None, depth=-1.0, interpolate=True)
stimuli = visual.ShapeStim(
    win=win, name='stimuli',units='pix', 
    size=[695.65, 695.88], vertices='triangle',
    ori=1.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
start_sound_imag = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='start_sound_imag')
start_sound_imag.setVolume(1.0)
end_sound_imag = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='end_sound_imag')
end_sound_imag.setVolume(1.0)
etRecord = hardware.eyetracker.EyetrackerControl(
    server=ioServer,
    tracker=eyetracker
)

# Initialize components for Routine "Question_vividness"
Question_vividnessClock = core.Clock()
question_vivid = visual.TextStim(win=win, name='question_vivid',
    text='Avec quelle vivacité avez-vous imaginé ou revisualisé le triangle ?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='lightgrey', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
vivid = visual.Slider(win=win, name='vivid',
    startValue=None, size=(0.8, 0.1), pos=(0, 0), units=None,
    labels=('Pas du tout vive\nAucune forme n\'est apparue\ndans l\'imagerie', '', '', 'Très vive\nPresque comme si elle\navait été vue'), ticks=(1, 2, 3, 4), granularity=1.0,
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


#Compute different luminances
background_lum = (win.color[0] + 1) * 127.5 # We add 1 because win.color[0] goes from -1 to 1.
fix_cross_lum = (fix_cross.fillColor[0] + 1) * 127.5 # We add 1 because rest.fillColor[0] goes from -1 to 1.

win.mouseVisible = False
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
        trial_number = 0
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
Start_trainComponents = [text_train, key_resp_train]
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
    
    # *text_train* updates
    if text_train.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_train.frameNStart = frameN  # exact frame index
        text_train.tStart = t  # local t and not account for scr refresh
        text_train.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_train, 'tStartRefresh')  # time at next scr refresh
        text_train.setAutoDraw(True)
    
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
thisExp.addData('text_train.started', text_train.tStartRefresh)
thisExp.addData('text_train.stopped', text_train.tStopRefresh)
# check responses
if key_resp_train.keys in ['', [], None]:  # No response was made
    key_resp_train.keys = None
thisExp.addData('key_resp_train.keys',key_resp_train.keys)
if key_resp_train.keys != None:  # we had a response
    thisExp.addData('key_resp_train.rt', key_resp_train.rt)
thisExp.addData('key_resp_train.started', key_resp_train.tStartRefresh)
thisExp.addData('key_resp_train.stopped', key_resp_train.tStopRefresh)
thisExp.nextEntry()
# the Routine "Start_train" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
train = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/conditions_pupillo_train.xlsx'),
    seed=None, name='train')
thisExp.addLoop(train)  # add the loop to the experiment
thisTrain = train.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrain.rgb)
if thisTrain != None:
    for paramName in thisTrain:
        exec('{} = thisTrain[paramName]'.format(paramName))

for thisTrain in train:
    currentLoop = train
    # abbreviate parameter names if possible (e.g. rgb = thisTrain.rgb)
    if thisTrain != None:
        for paramName in thisTrain:
            exec('{} = thisTrain[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Block_test"-------
    continueRoutine = True
    routineTimer.add(23.500000)
    # update component parameters for each repeat
    stimuli.setFillColor(color_rgb)
    stimuli.size = stim_size()
    stimuli.setOri(orientation)
    stimuli.setLineColor(color_rgb)
    start_sound_imag.setSound('A', secs=0.5, hamming=True)
    start_sound_imag.setVolume(1.0, log=False)
    end_sound_imag.setSound('A', secs=0.5, hamming=True)
    end_sound_imag.setVolume(1.0, log=False)
    # keep track of which components have finished
    Block_testComponents = [rest, fix_cross, stimuli, start_sound_imag, end_sound_imag, etRecord]
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
        
        # *rest* updates
        if rest.status == NOT_STARTED and tThisFlip >= 6.6-frameTolerance:
            # keep track of start time/frame for later
            rest.frameNStart = frameN  # exact frame index
            rest.tStart = t  # local t and not account for scr refresh
            rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest, 'tStartRefresh')  # time at next scr refresh
            eyetracker.sendMessage('stop_phase stim')
            eyetracker.sendMessage('start_phase rest')
            eyetracker.sendMessage(f"var rest_type {rest.noiseType}")
            rest.setAutoDraw(True)
        if rest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                rest.tStop = t  # not accounting for scr refresh
                rest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest, 'tStopRefresh')  # time at next scr refresh
                eyetracker.sendMessage('stop_phase rest')
                eyetracker.sendMessage('start_phase imag')
                rest.setAutoDraw(False)
        if rest.status == STARTED:
            if rest._needBuild:
                rest.buildNoise()
            else:
                if (frameN-rest.frameNStart) %         1==0:
                    rest.updateNoise()
        
        # *fix_cross* updates
        if fix_cross.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
            # keep track of start time/frame for later
            fix_cross.frameNStart = frameN  # exact frame index
            fix_cross.tStart = t  # local t and not account for scr refresh
            fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
            trial_number += 1
            eyetracker.sendMessage(f'start_trial {trial_number}')
            
            eyetracker.sendMessage('start_phase info')
            
            # Subject ID and info about the experiment.
            eyetracker.sendMessage(f"var screen_size {win.size}")
            eyetracker.sendMessage(f"var framerate {expInfo['frameRate']}")
            eyetracker.sendMessage(f"var subject_id {expInfo['participant']}")
            eyetracker.sendMessage(f"var subject_session {expInfo['session']}")
            eyetracker.sendMessage(f"var exp_date {expInfo['date']}")
            eyetracker.sendMessage(f"var exp_name {expInfo['expName']}")
            
            eyetracker.sendMessage(f"var background_lum [{background_lum},{background_lum},{background_lum}]")
            eyetracker.sendMessage(f"var background_lum_original {win.color}")
            eyetracker.sendMessage(f"var fix_cross_lum [{fix_cross_lum},{fix_cross_lum},{fix_cross_lum}]")
            eyetracker.sendMessage(f"var fix_cross_lum_original {fix_cross.fillColor}")
            eyetracker.sendMessage(f"var text_color_original {question_vivid.color}")
            
            eyetracker.sendMessage('stop_phase info')
            
            eyetracker.sendMessage('start_phase baseline')
            fix_cross.setAutoDraw(True)
        if fix_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross.tStartRefresh + 22-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross.tStop = t  # not accounting for scr refresh
                fix_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                eyetracker.sendMessage('stop_phase imag')
                fix_cross.setAutoDraw(False)
        
        # *stimuli* updates
        if stimuli.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            stimuli.frameNStart = frameN  # exact frame index
            stimuli.tStart = t  # local t and not account for scr refresh
            stimuli.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli, 'tStartRefresh')  # time at next scr refresh
            stim_lum = (color_rgb[0] + 1) * 127.5 # We add 1 because rest.fillColor[0] goes from -1 to 1.
            eyetracker.sendMessage('stop_phase baseline')
            eyetracker.sendMessage('start_phase stim')
            eyetracker.sendMessage(f'var stim_color [{stim_lum},{stim_lum},{stim_lum}]')
            eyetracker.sendMessage(f'var stim_color_original {color_rgb}')
            eyetracker.sendMessage(f'var stim_orientation {orientation}')
            
            stimuli.setAutoDraw(True)
        if stimuli.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                stimuli.tStop = t  # not accounting for scr refresh
                stimuli.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli, 'tStopRefresh')  # time at next scr refresh
                stimuli.setAutoDraw(False)
        # start/stop start_sound_imag
        if start_sound_imag.status == NOT_STARTED and tThisFlip >= 17.6-frameTolerance:
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
        if end_sound_imag.status == NOT_STARTED and tThisFlip >= 22.1-frameTolerance:
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
        # *etRecord* updates
        if etRecord.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord.frameNStart = frameN  # exact frame index
            etRecord.tStart = t  # local t and not account for scr refresh
            etRecord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord, 'tStartRefresh')  # time at next scr refresh
            etRecord.status = STARTED
        if etRecord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord.tStartRefresh + 23.5-frameTolerance:
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
    train.addData('rest.started', rest.tStartRefresh)
    train.addData('rest.stopped', rest.tStopRefresh)
    train.addData('fix_cross.started', fix_cross.tStartRefresh)
    train.addData('fix_cross.stopped', fix_cross.tStopRefresh)
    train.addData('stimuli.started', stimuli.tStartRefresh)
    train.addData('stimuli.stopped', stimuli.tStopRefresh)
    start_sound_imag.stop()  # ensure sound has stopped at end of routine
    train.addData('start_sound_imag.started', start_sound_imag.tStartRefresh)
    train.addData('start_sound_imag.stopped', start_sound_imag.tStopRefresh)
    end_sound_imag.stop()  # ensure sound has stopped at end of routine
    train.addData('end_sound_imag.started', end_sound_imag.tStartRefresh)
    train.addData('end_sound_imag.stopped', end_sound_imag.tStopRefresh)
    # make sure the eyetracker recording stops
    if etRecord.status != FINISHED:
        etRecord.status = FINISHED
    
    # ------Prepare to start Routine "Question_vividness"-------
    win.mouseVisible = True
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
            eyetracker.sendMessage('start_phase rating')
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
            eyetracker.sendMessage(f'var rating {vivid.getRating()}')
            eyetracker.sendMessage('stop_phase rating')
            eyetracker.sendMessage('stop_trial')
            win.mouseVisible = False
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
    train.addData('question_vivid.started', question_vivid.tStartRefresh)
    train.addData('question_vivid.stopped', question_vivid.tStopRefresh)
    train.addData('vivid.response', vivid.getRating())
    train.addData('vivid.rt', vivid.getRT())
    train.addData('vivid.started', vivid.tStartRefresh)
    train.addData('vivid.stopped', vivid.tStopRefresh)
    # the Routine "Question_vividness" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'train'

# get names of stimulus parameters
if train.trialList in ([], [None], None):
    params = []
else:
    params = train.trialList[0].keys()
# save data for this loop
train.saveAsExcel(filename + '.xlsx', sheetName='train',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
train.saveAsText(filename + 'train.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

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
test = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/conditions_pupillo.xlsx'),
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
    routineTimer.add(23.500000)
    # update component parameters for each repeat
    stimuli.setFillColor(color_rgb)
    stimuli.size = stim_size()
    stimuli.setOri(orientation)
    stimuli.setLineColor(color_rgb)
    start_sound_imag.setSound('A', secs=0.5, hamming=True)
    start_sound_imag.setVolume(1.0, log=False)
    end_sound_imag.setSound('A', secs=0.5, hamming=True)
    end_sound_imag.setVolume(1.0, log=False)
    # keep track of which components have finished
    Block_testComponents = [rest, fix_cross, stimuli, start_sound_imag, end_sound_imag, etRecord]
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
        
        # *rest* updates
        if rest.status == NOT_STARTED and tThisFlip >= 6.6-frameTolerance:
            # keep track of start time/frame for later
            rest.frameNStart = frameN  # exact frame index
            rest.tStart = t  # local t and not account for scr refresh
            rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest, 'tStartRefresh')  # time at next scr refresh
            eyetracker.sendMessage('stop_phase stim')
            eyetracker.sendMessage('start_phase rest')
            eyetracker.sendMessage(f"var rest_type {rest.noiseType}")
            rest.setAutoDraw(True)
        if rest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                rest.tStop = t  # not accounting for scr refresh
                rest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest, 'tStopRefresh')  # time at next scr refresh
                eyetracker.sendMessage('stop_phase rest')
                eyetracker.sendMessage('start_phase imag')
                rest.setAutoDraw(False)
        if rest.status == STARTED:
            if rest._needBuild:
                rest.buildNoise()
            else:
                if (frameN-rest.frameNStart) %         1==0:
                    rest.updateNoise()
        
        # *fix_cross* updates
        if fix_cross.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
            # keep track of start time/frame for later
            fix_cross.frameNStart = frameN  # exact frame index
            fix_cross.tStart = t  # local t and not account for scr refresh
            fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
            trial_number += 1
            eyetracker.sendMessage(f'start_trial {trial_number}')
            
            eyetracker.sendMessage('start_phase info')
            
            # Subject ID and info about the experiment.
            eyetracker.sendMessage(f"var screen_size {win.size}")
            eyetracker.sendMessage(f"var framerate {expInfo['frameRate']}")
            eyetracker.sendMessage(f"var subject_id {expInfo['participant']}")
            eyetracker.sendMessage(f"var subject_session {expInfo['session']}")
            eyetracker.sendMessage(f"var exp_date {expInfo['date']}")
            eyetracker.sendMessage(f"var exp_name {expInfo['expName']}")
            
            eyetracker.sendMessage(f"var background_lum [{background_lum},{background_lum},{background_lum}]")
            eyetracker.sendMessage(f"var background_lum_original {win.color}")
            eyetracker.sendMessage(f"var fix_cross_lum [{fix_cross_lum},{fix_cross_lum},{fix_cross_lum}]")
            eyetracker.sendMessage(f"var fix_cross_lum_original {fix_cross.fillColor}")
            eyetracker.sendMessage(f"var text_color_original {question_vivid.color}")
            
            eyetracker.sendMessage('stop_phase info')
            
            eyetracker.sendMessage('start_phase baseline')
            fix_cross.setAutoDraw(True)
        if fix_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross.tStartRefresh + 22-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross.tStop = t  # not accounting for scr refresh
                fix_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                eyetracker.sendMessage('stop_phase imag')
                fix_cross.setAutoDraw(False)
        
        # *stimuli* updates
        if stimuli.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            stimuli.frameNStart = frameN  # exact frame index
            stimuli.tStart = t  # local t and not account for scr refresh
            stimuli.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli, 'tStartRefresh')  # time at next scr refresh
            stim_lum = (color_rgb[0] + 1) * 127.5 # We add 1 because rest.fillColor[0] goes from -1 to 1.
            eyetracker.sendMessage('stop_phase baseline')
            eyetracker.sendMessage('start_phase stim')
            eyetracker.sendMessage(f'var stim_color [{stim_lum},{stim_lum},{stim_lum}]')
            eyetracker.sendMessage(f'var stim_color_original {color_rgb}')
            eyetracker.sendMessage(f'var stim_orientation {orientation}')
            
            stimuli.setAutoDraw(True)
        if stimuli.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                stimuli.tStop = t  # not accounting for scr refresh
                stimuli.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli, 'tStopRefresh')  # time at next scr refresh
                stimuli.setAutoDraw(False)
        # start/stop start_sound_imag
        if start_sound_imag.status == NOT_STARTED and tThisFlip >= 17.6-frameTolerance:
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
        if end_sound_imag.status == NOT_STARTED and tThisFlip >= 22.1-frameTolerance:
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
        # *etRecord* updates
        if etRecord.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord.frameNStart = frameN  # exact frame index
            etRecord.tStart = t  # local t and not account for scr refresh
            etRecord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord, 'tStartRefresh')  # time at next scr refresh
            etRecord.status = STARTED
        if etRecord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord.tStartRefresh + 23.5-frameTolerance:
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
    test.addData('rest.started', rest.tStartRefresh)
    test.addData('rest.stopped', rest.tStopRefresh)
    test.addData('fix_cross.started', fix_cross.tStartRefresh)
    test.addData('fix_cross.stopped', fix_cross.tStopRefresh)
    test.addData('stimuli.started', stimuli.tStartRefresh)
    test.addData('stimuli.stopped', stimuli.tStopRefresh)
    start_sound_imag.stop()  # ensure sound has stopped at end of routine
    test.addData('start_sound_imag.started', start_sound_imag.tStartRefresh)
    test.addData('start_sound_imag.stopped', start_sound_imag.tStopRefresh)
    end_sound_imag.stop()  # ensure sound has stopped at end of routine
    test.addData('end_sound_imag.started', end_sound_imag.tStartRefresh)
    test.addData('end_sound_imag.stopped', end_sound_imag.tStopRefresh)
    # make sure the eyetracker recording stops
    if etRecord.status != FINISHED:
        etRecord.status = FINISHED
    
    # ------Prepare to start Routine "Question_vividness"-------
    win.mouseVisible = True
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
            eyetracker.sendMessage('start_phase rating')
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
            eyetracker.sendMessage(f'var rating {vivid.getRating()}')
            eyetracker.sendMessage('stop_phase rating')
            eyetracker.sendMessage('stop_trial')
            win.mouseVisible = False
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
    
# completed 2.0 repeats of 'test'

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
eyetracker.setConnectionState(False)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
