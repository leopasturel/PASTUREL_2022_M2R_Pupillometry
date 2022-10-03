function Jana_PupilContingentNew

clear;

if ~IsOctave
    commandwindow;
else
    more off;
end

%__________________________________________________________________________
%% Dummy mode? yes:1 no:0
dummymode=0; %% Actually, Dummy mode is not available.
%__________________________________________________________________________
%% Settings
numTrial = 3; % number of trials
trialDuration = 30; %duration of the trial

% CHOOSE DOMINANT EYE
eye=0; % left eye = 1; right eye = 0

% CHOOSE COLOR OF STIMULI
stimCol=0 % grey=0, green=1, red=2, blue=3

%biopacTime=5;

%__________________________________________________________________________
%% Display settings - to modify according to stimulation settings
% monWidth =  52.9; %monitor width in cm/in
% monHeight = 29.7; %monitor height in cm/in
% viewDist = 57;  %viewing distance in cm/in
% 
% % Screen BOX 3
% screenSize = [1280 1024]; %width height in pixels
% screenRefreshRate = 75; %Hz

monWidth =  63.7; %monitor width in cm/in
monHeight = 40; %monitor height in cm/in
viewDist = 70;  %viewing distance in cm/in

% Screen BOX 3
screenSize = [1280 1024]; %width height in pixels
screenRefreshRate = 75; %Hz

% Screen PC
% screenSize = [1366 768]; %width height in pixels
% screenRefreshRate = 60; %Hz

%__________________________________________________________________________
%% Load
% Instruction, introduction
instr=imread('Leo_Instruction.jpg');
%__________________________________________________________________________
%% Open port
%s = serial('COM1');
%fopen(s);

%__________________________________________________________________________
%% Exit key
KbName('UnifyKeyNames');
ExitKey=KbName('q');     % define key to exit the experiment
KbQueueCreate;
KbQueueStart;

%__________________________________________________________________________
%% START EXEPERIMENT- from there should not be modified
try
    % STEP 1
    % Add a dialog box to set your own EDF file name before opening
    % experiment graphics.
    if IsOctave
        edfFile = 'DEMO';
    else
        
        prompt = {'Enter tracker EDF file name (1 to 8 letters or numbers)'};
        dlg_title = 'Create EDF file';
        num_lines= 1;
        def     = {'DEMO'};
        answer  = inputdlg(prompt,dlg_title,num_lines,def);
        edfFile = answer{1};
        fprintf('EDFFile: %s\n', edfFile );
        
    end
    
    % STEP 2
    % Open a graphics window on the main screen
    screenNumber=max(Screen('Screens'));
    [windowptr, wRect]=Screen('OpenWindow', screenNumber, 0,[],32,2);
    Screen(windowptr,'BlendFunction',GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    
    %Get screen parameters (resolution, framerate)
    [winWidth, winHeight] = WindowSize(windowptr);
    hz=Screen('FrameRate', windowptr);
    ifi = 1 / hz; %interframe interval
    
    % Hide the mouse cursor;
    if dummymode == 0
        Screen('HideCursorHelper', windowptr);
    end
    
    %Check whether the screen parameters match the ones requested above
    if dummymode~=1
        if not( wRect(3) == screenSize(1) & wRect(4) == screenSize(2))
            sca
            error('Actual screen resolution if %d x %d instead of %d x %d requested',wRect(3), wRect(4), screenSize(2),screenSize(1))
        end
        
        if not( hz >= (screenRefreshRate - 1) & hz <= (screenRefreshRate +1) )
            sca
            error('Refresh rate is of %.2f instead of %d requested',hz, screenRefreshRate)
        end
    end
    
    % STEP 3
    % Provide Eyelink with details about the graphics environment
    % and perform some initializations
    el=EyelinkInitDefaults(windowptr);
    
    % STEP 4
    % Initialization of the connection with the Eyelink Gazetracker
    if ~EyelinkInit(dummymode)
        fprintf('Eyelink Init aborted.\n');
        cleanup;  % cleanup function
        return;
    end
    
    % the following code is used to check the version of the eye tracker
    % and version of the host software
    sw_version = 0;
    
    [~,vs]=Eyelink('GetTrackerVersion');
    fprintf('Running experiment on a ''%s'' tracker.\n', vs );
    
    % open file to record data to
    i = Eyelink('Openfile', edfFile);
    if i~=0
        fprintf('Cannot create EDF file ''%s'' ', edfFile);
        Eyelink( 'Shutdown');
        Screen('CloseAll');
        return;
    end
    
    Eyelink('command', 'add_file_preamble_text ''Recorded by EyelinkToolbox demo-experiment''');
    [width, height]=Screen('WindowSize', screenNumber);
    
    % STEP 5
    % SET UP TRACKER CONFIGURATION
    % Setting the proper recording resolution, proper calibration type,
    % as well as the data file content;
    Eyelink('command','screen_pixel_coords = %ld %ld %ld %ld', 0, 0, width-1, height-1);
    Eyelink('message', 'DISPLAY_COORDS %ld %ld %ld %ld', 0, 0, width-1, height-1);
    % set calibration type.
    Eyelink('command', 'calibration_type = HV5');
    
    % set EDF file contents using the file_sample_data and
    % file-event_filter commands
    % set link data thtough link_sample_data and link_event_filter
    Eyelink('command', 'file_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT');
    Eyelink('command', 'link_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT');
    
    % check the software version
    % add "HTARGET" to record possible target data for EyeLink Remote
    if sw_version >=4
        Eyelink('command', 'file_sample_data  = LEFT,RIGHT,GAZE,HREF,AREA,HTARGET,GAZERES,STATUS,INPUT');
        Eyelink('command', 'link_sample_data  = LEFT,RIGHT,GAZE,GAZERES,AREA,HTARGET,STATUS,INPUT');
    else
        Eyelink('command', 'file_sample_data  = LEFT,RIGHT,GAZE,HREF,AREA,GAZERES,STATUS,INPUT');
        Eyelink('command', 'link_sample_data  = LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS,INPUT');
    end
    
    % allow to use the big button on the eyelink gamepad to accept the
    % calibration/drift correction target
    Eyelink('command', 'button_function 5 "accept_target_fixation"');
    
    % make sure we're still connected.
    if Eyelink('IsConnected')~=1 && dummymode == 0
        fprintf('not connected, clean up\n');
        Eyelink( 'Shutdown');
        Screen('CloseAll');
        return;
    end
    
    % STEP 6
    % Calibrate the eye tracker
    % setup the proper calibration foreground and background colors
    el.backgroundcolour = BlackIndex(windowptr);     %black background
    %el.backgroundcolour =[128 128 128]
    el.calibrationtargetcolour = [100 100 100];
    el.msgfontcolour = [255 255 255];
    
    % parameters are in frequency, volume, and duration
    % set the second value in each line to 0 to turn off the sound
    el.cal_target_beep=[600 0.5 0.05];
    el.drift_correction_target_beep=[600 0.5 0.05];
    el.calibration_failed_beep=[400 0.5 0.25];
    el.calibration_success_beep=[800 0.5 0.25];
    el.drift_correction_failed_beep=[400 0.5 0.25];
    el.drift_correction_success_beep=[800 0.5 0.25];
    % you must call this function to apply the changes from above
    EyelinkUpdateDefaults(el);
    
    % STEP 7
    % Now starts running individual trials;
    % You can keep the rest of the code except for the implementation
    % of graphics and event monitoring
    % Each trial should have a pair of "StartRecording" and "StopRecording"
    % calls as well integration messages to the data file (message to mark
    % the time of critical events and the image/interest area/condition
    % information for the trial)
    
    %calibration
    EyelinkDoTrackerSetup(el);
    [xCenter,yCenter]=RectCenter(wRect);
    % make a base Rect of 400 by 400
    baseRect = [0 0 screenSize(2) screenSize(2)];
    % For cycles we set a maximum diameter up to which it is perfect for
    maxDiameter = max(baseRect)*1.00;
    %Center the rectangle on the center of the screen
    centeredRect =  CenterRectOnPointd(baseRect,xCenter,yCenter);
    
    %Display instruction
    Screen('FillRect', windowptr, el.backgroundcolour);
    Screen('PutImage',windowptr,instr);
    Screen('Flip',windowptr);
    
    %wait for keypress to start - if exit key is pressed
    %abort the experiment
    WaitSecs(0.2);
    [~,keyCode]= KbWait;
    if keyCode(ExitKey)
        sca;
    else
        KbQueueFlush
    end
    while KbCheck; end
    
    
    %% Start trials
    %0. Gray screen
    Screen('FillRect', windowptr, el.backgroundcolour);
    timeflip = Screen('Flip', windowptr);
    Eyelink('Message', 'ISI_DISPLAY %d ms', round(timeflip*1000));
    
    %1 : white cross on gray screen
    Screen('FillRect', windowptr, el.backgroundcolour);
    center = round([width, height]/2);
    Screen('DrawLine', windowptr, [0,0,200], center(1)-15, center(2), center(1)+15, center(2));
    Screen('DrawLine', windowptr, [0,0,200], center(1), center(2)-15, center(1), center(2)+15);
    timeflip = Screen('Flip',windowptr,timeflip+2-ifi/2);
    Eyelink('Message', 'FIXATION_DISPLAY %d ms', round(timeflip*1000));
    
    %
    % %     % MEASURE REAL PUPIL SIZE
    %
    %     Eyelink('StartRecording');
    %     WaitSecs(0.05);
    %     Eyelink('Message','BEGIN REAL PUPIL SIZE RECORDING');
    %
    %     Screen('FillRect', windowptr, el.backgroundcolour);
    %     %Screen('DrawText', windowptr,'Measuring real pupil size of right eye. \nPress any key to continue',width/2-150, height/2,[255 255 255]);
    %     DrawFormattedText(windowptr,'Measuring real pupil size of right eye.\n \nPress any key to continue','center','center',[255 255 255]);
    %     Screen('Flip',windowptr,timeflip+0.2-ifi/2);
    %     KbWait
    %
    %     Screen('FillRect', windowptr, el.backgroundcolour);
    %     center = round([width, height]/2);
    %     Screen('DrawLine', windowptr, [255,255,255], center(1)-15, center(2), center(1)+15, center(2));
    %     Screen('DrawLine', windowptr, [255,255,255], center(1), center(2)-15, center(1), center(2)+15);
    %     timeflip = Screen('Flip',windowptr,timeflip+2-ifi/2);
    %     Eyelink('Message', 'FIXATION_DISPLAY %d ms', round(timeflip*1000));
    %
    %     Screen('FillRect', windowptr, el.backgroundcolour);
    %     DrawFormattedText(windowptr,'Measuring real pupil size of left eye.\n \nPress any key to continue','center','center',[255 255 255]);
    %     Screen('Flip',windowptr,timeflip+3-ifi/2);
    %     KbWait
    %
    %     Screen('FillRect', windowptr, el.backgroundcolour);
    %     center = round([width, height]/2);
    %     Screen('DrawLine', windowptr, [255,255,255], center(1)-15, center(2), center(1)+15, center(2));
    %     Screen('DrawLine', windowptr, [255,255,255], center(1), center(2)-15, center(1), center(2)+15);
    %     timeflip = Screen('Flip',windowptr,timeflip+0.2-ifi/2);
    %     Eyelink('Message', 'FIXATION_DISPLAY %d ms', round(timeflip*1000));
    %     timeflip = Screen('Flip',windowptr,timeflip+3-ifi/2);
    %
    %     Eyelink('StopRecording');
    %     WaitSecs(0.001);
    %     Eyelink('Message', 'END REAL PUPIL SIZE RECORDING');
    % %
    %   %______________________________________________________________________
    
    Eyelink('StartRecording');
    WaitSecs(0.05);
    Eyelink('Message','BEGIN CALIBRATION RECORDING');
    Eyelink('Message','start_phase calibration');
    
    %% CHOOSE EYE FOR GET PUPIL SIZE
    if eye == 1
        usedEye = el.LEFT_EYE; % or el.RIGHT_EYE (eye for get pupil size to change luminance)
    elseif eye == 0
        usedEye = el.RIGHT_EYE;
    end
    
    eye_used = Eyelink('EyeAvailable'); % get eye that's tracked
    if eye_used == el.BINOCULAR % if both eyes are tracked
        eye_used = usedEye;
    end
    
%     a = GetSecs; while (GetSecs-a)<1 fwrite(s,zeros(1,6));end
    
    %% Pupil calibration size
    
    % duree du stim noir qui permet de normaliser la taille de la pupille
    % lum=0 t=12s
    time_maxPup0=8;       
    
    t = datetime('now','TimeZone','local','Format','d-MMM-y HH:mm:ss.SSS');
    t = datestr(t,'yyyy-mm-dd HH:MM:SS.FFF');
    
    Screen('FillOval', windowptr, [0,0,0], centeredRect, maxDiameter);
    Screen('DrawLine', windowptr, [0,0,200], center(1)-15, center(2), center(1)+15, center(2));
    Screen('DrawLine', windowptr, [0,0,200], center(1), center(2)-15, center(1), center(2)+15);
    timeflip = Screen('Flip',windowptr,timeflip+2-ifi/2);
    Eyelink('Message', 'CALIBRATION LUMINANCE: TARGET_DISPLAY %d REAL TIME %s DVlum 0 ',round(timeflip*1000),t);
    
    % Record pupil size for lum = 0
    timeStamp = GetSecs;
    cpt = 1;
    while timeStamp < timeflip+time_maxPup0-ifi/2
        
        if dummymode == 0
            
            if Eyelink('NewFloatSampleAvailable') > 0
                % get the sample in the form of an event structure
                evt = Eyelink( 'NewestFloatSample');
                if eye_used ~= -1 % do we know which eye to use yet?
                    % if we do, get current gaze position and pupil size from sample
                    x = evt.gx(eye_used+1); % +1 as we're accessing MATLAB array
                    y = evt.gy(eye_used+1);
                    area = evt.pa(eye_used+1);
                    % do we have valid data and is the pupil visible?
                    if x~=el.MISSING_DATA && y~=el.MISSING_DATA && evt.pa(eye_used+1)>0
                        mArea1(cpt)=area;
                    end
                end
            end
        else
            % Query current mouse cursor position ("pseudo-eyetracker")
            [area,~]=GetMouse; % x = mArea, y = I1
            mArea1(cpt) = area;
        end
        
        timeStamp = GetSecs;
        WaitSecs(.1)
        cpt = cpt + 1;
        
        % check to see if exit has been called
        [~, ~, keyCode] = KbQueueCheck();
        if keyCode(ExitKey)
            sca;
        else
            KbQueueFlush;
        end
        
    end
    
    maxPup0 = max(mArea1(40:end))
    
    Eyelink('Message', 'Taille Pupille Max stim noir: %d', maxPup0);
    Eyelink('StopRecording');
    WaitSecs(0.001);
    Eyelink('Message', 'END CALIBRATION RECORDING');
    Eyelink('Message', 'stop_phase calibration');
    
    %______________________________________________________________________
    %% %% START OF TRIALS %%
    trialrand=randperm(2);
    for trial=1:numTrial
      
        if trial==1
            Screen('FillRect', windowptr, el.backgroundcolour);
            Screen('DrawText', windowptr,'Pret.e ? Veuillez fixer le centre de l''écran',width/3, height/2,[0 0 128]);
            Screen('DrawText', windowptr,'Appuyez sur espace',width/3, height/2+80,[0 0 128]);
            text='Without'
            Screen('Flip',windowptr,timeflip+0.2-ifi/2);
            KbWait
        else
            if trialrand(trial-1)==2
                Screen('FillRect', windowptr, el.backgroundcolour);
                Screen('DrawText', windowptr,'Pret.e ? Imaginez que l''écran devienne extremement brillant',width/4, height/2,[0 0 128]);
                Screen('DrawText', windowptr,'Appuyez sur espace',width/3, height/2+80,[0 0 128]);
                text='White'
                Screen('Flip',windowptr,timeflip+0.2-ifi/2);
                KbWait
            else
                Screen('FillRect', windowptr, el.backgroundcolour);
                Screen('DrawText', windowptr,'Pret.e ? Imaginez que l''écran devienne d''un noir profond',width/4, height/2,[0 0 128]);
                Screen('DrawText', windowptr,'Appuyez sur espace',width/3, height/2+80,[0 0 128]);
                text='Black'
                Screen('Flip',windowptr,timeflip+0.2-ifi/2);
                KbWait
            end
        end
                              
        %do a final check of calibration using driftcorrection
        beep off;
        EyelinkDoDriftCorrection(el);
        Screen('Flip',windowptr,timeflip+0.2-ifi/2);
        
        % This supplies the title at the bottom of the eyetracker display
        Eyelink('command', 'record_status_message "TRIAL %d "', trial);
        % Eyelink('command', 'record_status_message "TRIAL %d/%d  %s"', i, N, StimList{i,1});
        % Before recording, we place reference graphics on the host display
        % Must be offline to draw to EyeLink screen
        Eyelink('Command', 'set_idle_mode');
        % clear tracker display and draw box at center
        Eyelink('Command', 'clear_screen 0');
        %__________________________________________________________________
        % %% START RECORDING %%
        Eyelink('StartRecording');
        WaitSecs(0.05);
        Eyelink('Message','BEGIN RECORDING TRIALID %d',trial);
        Eyelink('Message','start_trial %d',trial);
        Eyelink('Message','var condition %s',text);
        
        Screen('FillRect', windowptr, el.backgroundcolour);
        Screen('DrawLine', windowptr, [0,0,200], center(1)-15, center(2), center(1)+15, center(2));
        Screen('DrawLine', windowptr, [0,0,200], center(1), center(2)-15, center(1), center(2)+15);
        timeflip = Screen('Flip',windowptr,timeflip+0.2-ifi/2);
        Eyelink('Message','start_phase baseline');
        
        Screen('FillRect', windowptr, el.backgroundcolour);
        Screen('DrawLine', windowptr, [0,0,200], center(1)-15, center(2), center(1)+15, center(2));
        Screen('DrawLine', windowptr, [0,0,200], center(1), center(2)-15, center(1), center(2)+15);
        timeflip = Screen('Flip',windowptr,timeflip+1-ifi/2);
        
        Eyelink('Message','stop_phase baseline');
        
        Eyelink('Message','start_phase cycle');
        % Send a trigger baseline to biopac
%         fwrite(s,ones(1,6))
%         Eyelink('Message','BIOPAC TRIGGER BASELINE START');
%         WaitSecs(biopacTime);
%         fwrite(s,ones(1,6))
%         Eyelink('Message','BIOPAC TRIGGER BASELINE END');
        
        % %% TRIAL NUM X (time=0:ifi:trialDuration)
        
        for time=0:ifi:trialDuration
            %______________________________________________________________
            if dummymode==0 %% DUMMYMODE = 0 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                
                if Eyelink('NewFloatSampleAvailable') > 0
                    % get the sample in the form of an event structure
                    evt = Eyelink( 'NewestFloatSample');
                    if eye_used ~= -1 % do we know which eye to use yet?
                        % if we do, get current gaze position and pupil size from sample
                        x = evt.gx(eye_used+1); % +1 as we're accessing MATLAB array
                        y = evt.gy(eye_used+1);
                        area = evt.pa(eye_used+1);
                        % do we have valid data and is the pupil visible?
                        if x~=el.MISSING_DATA && y~=el.MISSING_DATA && evt.pa(eye_used+1)>0
                            mArea=area;
                        end
                        lumIndex = (mArea/maxPup0)*255;
                        
%                         % Get a time of system
%                         t = datetime('now','TimeZone','local','Format','d-MMM-y HH:mm:ss.SSS');
%                         t = datestr(t,'yyyy-mm-dd HH:MM:SS.FFF');
                    end
                end
                
                %__________________________________________________________
            else %% DUMMYMODE = 1 %%%%% X = "area" %%%%%%%%%%%%%%%%%%%%%%%%
                
                % Query current mouse cursor position ("pseudo-eyetracker")
                [mArea,~]=GetMouse; % x = mArea
                lumIndex = (mArea/maxPup0)*255;
%                 t = datetime('now','TimeZone','local','Format','d-MMM-y HH:mm:ss.SSS');
%                 t = datestr(t,'yyyy-mm-dd HH:MM:SS.FFF'); 
            end
            
            if stimCol==0
                Screen('FillOval', windowptr,lumIndex,centeredRect,maxDiameter);
            elseif stimCol==1
                Screen('FillOval', windowptr,[0,lumIndex,0],centeredRect,maxDiameter);
            elseif stimCol==2
                Screen('FillOval', windowptr,[lumIndex,0,0],centeredRect,maxDiameter);
            elseif stimCol==3
                Screen('FillOval', windowptr,[0,0,lumIndex],centeredRect,maxDiameter);
            end
            Screen('DrawLine', windowptr, [0,0,200], center(1)-15, center(2), center(1)+15, center(2));
            Screen('DrawLine', windowptr, [0,0,200], center(1), center(2)-15, center(1), center(2)+15);
            timeflip = Screen('Flip',windowptr,timeflip-ifi/2);
            Eyelink('Message','TARGET_DISPLAY %d DVlum %d ',round(timeflip*1000),round(lumIndex));
     
            % check to see if exit has been called
            [~, ~, keyCode] = KbQueueCheck();
            if keyCode(ExitKey)
                break;
            else
                KbQueueFlush;
            end
            
        end
        
        % Send a trigger end to biopac
%         fwrite(s,ones(1,6))
%         Eyelink('Message','BIOPAC TRIGGER END');
      
        %__________________________________________________________________
        %% STOP RECORDING
        Eyelink('Message', 'stop_phase cycle');
        
        
    % ---------------------------------------------
    % ---------------------------------------------
    % start rating PHASE

    % number of response allowed
    nRep = 4;
    
    %size of the circle to be clicked
    sizeRep = 100;
    
    % step of color from the backgournd of the circle color
    colorStepResp = 40;
 
    if trial > 1
            Screen('ShowCursorHelper', windowptr);
        repRect = [0 0 sizeRep sizeRep];
        x = [1:nRep]'*winWidth/(nRep+1);
        y = .5*[winHeight winHeight winHeight winHeight]';
        
        newRect = CenterRectOnPoint(repRect,x,y);
        
        Screen('FillRect', windowptr, el.backgroundcolour);
        Screen('FillOval', windowptr, el.backgroundcolour+colorStepResp, newRect');
       DrawFormattedText(windowptr, 'Pas du tout vive\n Aucune luminance n''est apparue pendant l''imagerie', x(1)-sizeRep, y(1)+sizeRep, [0 0 128], 20);
       DrawFormattedText(windowptr,  'Très vive\nPresque comme si elle avait été perçue', x(end)-sizeRep, y(end)+sizeRep, [0 0 128], 20);
        timeflip = Screen('Flip',windowptr);
        Eyelink('Message','start_phase RATING')
        
        clicked = 0;
        while ~clicked
            % get mouse response
            [x_mouse,y_mouse,buttons] = GetMouse;
            while any(buttons) % if already down, wait for release
                [x_mouse,y_mouse,buttons] = GetMouse;
            end
            while ~any(buttons) % wait for press
                [x_mouse,y_mouse,buttons] = GetMouse;
            end
            while any(buttons) % wait for release
                [x_mouse,y_mouse,buttons] = GetMouse;
            end
            
            for iRect = 1 : nRep
                clicked = IsInRect(x_mouse,y_mouse,newRect(iRect,:,:));
                if clicked,fprintf('\n\n rectangle num %d \n\n',iRect);break,
                end
            end
        end
        
        Screen('FillRect', windowptr, el.backgroundcolour);
        timeflip = Screen('Flip',windowptr);
        Eyelink('Message','var RATING %d ',iRect);
        Eyelink('Message','stop_phase RATING')
                Screen('HideCursorHelper', windowptr);

    end
    % ---------------------------------------------
    % ---------------------------------------------        
        WaitSecs(0.001);
        Eyelink('Message','stop_trial');
        Eyelink('StopRecording');
          
        Eyelink('Message', 'END RECORDING');
        
        % for DATAVIEWER
        % Send messages to report trial condition information
        % Each message may be a pair of trial condition variable and its
        % corresponding value follwing the '!V TRIAL_VAR' token message
        % See "Protocol for EyeLink Data to Viewer Integration-> Trial
        % Message Commands" section of the EyeLink Data Viewer User Manual
        WaitSecs(0.001);
        % Eyelink('Message', '!V TRIAL_VAR index %d', gammaCor)
        % Eyelink('Message', '!V TRIAL_VAR imgfile %s', StimList{nTrial})
        % STEP 7.8
        % Sending a 'TRIAL_RESULT' message to mark the end of a trial in
        % Data Viewer. This is different than the end of recording message
        % END that is logged when the trial recording ends. The viewer will
        % not parse any messages, events, or samples that exist in the data
        % file after this message.
        % Eyelink('Message', 'TRIAL_RESULT 0')
                
    end  %end of trials
    % third: Gray screen for 2 sec then clear the display and stop recording
    Screen('FillRect', windowptr, el.backgroundcolour);
    timeflip = Screen('Flip', windowptr, timeflip+2-ifi/2);
    Eyelink('Message','TARGET_END %d ms',round(timeflip*1000));
    
    %%
    Eyelink('Message', 'END ACQUISITION');
    % STEP 8
    % End of Experiment; close the file first
    % close graphics window, close data file and shut down tracker
    
    Eyelink('Command', 'set_idle_mode');
    WaitSecs(0.5);
    Eyelink('CloseFile');
    
    % download data file
    try
        fprintf('Receiving data file ''%s''\n', edfFile );
        status=Eyelink('ReceiveFile');
        if status > 0
            fprintf('ReceiveFile status %d\n', status);
        end
        if 2==exist(edfFile, 'file')
            fprintf('Data file ''%s'' can be found in ''%s''\n', edfFile, pwd );
        end
    catch
        fprintf('Problem receiving data file ''%s''\n', edfFile );
    end
    
    % STEP 9
    % close the eye tracker and window
    Eyelink('ShutDown');
    Screen('CloseAll');
%     
%     fclose(s)
%     delete(s)
%     clear s
catch exception
    %this "catch" section executes in case of an error in the "try" section
    %above.  Importantly, it closes the onscreen window if its open.
    Eyelink('ShutDown');
    %Screen('LoadNormalizedGammaTable',windowptr,oldtable);
%     fclose(s)
%     delete(s)
%     clear s
%     
    Screen('CloseAll');
    commandwindow;
    throw(exception)
end %try..catch.