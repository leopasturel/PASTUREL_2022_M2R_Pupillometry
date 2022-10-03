import re
import io
import os
import inspect

### GET DIRECTORIES ###
# Get full actual file path
actual_file_path = inspect.getframeinfo(inspect.currentframe()).filename
# Get only filename of the actual file
actual_filename = os.path.basename(actual_file_path)
# Get parent folder path
path = os.path.dirname(os.path.abspath(actual_file_path))
# Write the directory of the file you want to modify
filename = "pupillo_IF_short.py"


file_path = os.path.join(path, filename)
code = io.open(file_path, 'r', encoding = "utf-8-sig")
code = code.read()

# Create the list of the commands following the place where you want your flags to be.
list_of_interest = (
                    "\# Setup eyetracking", # 1. Following command to add def function
                    
                    "instruction.setAutoDraw\(True\)", # 2. Following command to initialize trial_number
                    
                    "imag.setOri\(orientation\)", # 3. Following command to set stimulus sizes
                                        
                    "fix_cross.setAutoDraw\(True\)", # 4. Following commands for the pre-baseline

                    "fix_cross.setAutoDraw\(True\)", # 5. Following commands for the baseline
                    
                    "imag.setAutoDraw\(True\)", # 6. Following commands for beginning of the imagery
                                        
                    "rest_1.setAutoDraw\(True\)", # 7. Following command for end of imagery & beginning of rest_1
                    
                    "stimuli.setAutoDraw\(True\)", # 8. Following commands for end of rest_1 & beginning of stim
                    
                    "rest_2.setAutoDraw\(True\)", # 9 Following commands for end of stim & beginning of rest_2
                    
                    "rest_2.setAutoDraw\(False\)", # 10 Following commands for end rest_2
                    
                    "question_vivid.setAutoDraw\(True\)", "if vivid.getRating\(\) is not None and vivid.status == STARTED:", # 11-12. Following/preceding commands for question phase + remove mouse cursor
                    
                    "\# ------Prepare to start Routine \"Instruction\"-------", # 13. Following command to compute luminances
                    
                    "# ------Prepare to start Routine \"Question_vividness\"-------", # 14. Preceding line to allow mouse cursor
                    
                    "logging.flush\(\)" # 15. Following command to close eyelink 
                    )


# Create the list of commands that you want to add, using the same order as in the previous list.
string_to_add = (
                """
def stim_size():
    \"""Determine the size, in pixel, of the stimuli to display
    In this function, we use the formula sqrt(3)/2*c with c the size of the
    triangles, to calculate the heigth of the equilateral triangles.
    This function is derived from Pythagore theorem\"""
    
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

""", # 1. Def used to set stimulus sizes.
                 
                 """trial_number = 0
        """, # 2. Initialize trial_number variable
                
                """stimuli.size = stim_size()
    imag.size = stim_size()
    """, # 3. Change size of stimuli.
                
                """trial_number += 1
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
            eyetracker.sendMessage(f"var fix_cross__lum_original {fix_cross.fillColor}")
            eyetracker.sendMessage(f"var text_color_original {question_vivid.color}")

            eyetracker.sendMessage('stop_phase info')

            eyetracker.sendMessage('start_phase pre_baseline')
            eyetracker.sendMessage('var imagery_color {imagery_color}')
            
            """, # 4. Messages for info and pre-baseline
                
            """eyetracker.sendMessage('stop_phase pre_baseline')
            eyetracker.sendMessage('start_phase baseline')
            """, # 5. Messages for end of pre-baseline and start of baseline
                            
            """eyetracker.sendMessage('stop_phase baseline')
            eyetracker.sendMessage('start_phase imagery')
            """, # 6. Messages for end of baseline and start of imagery
            
            """eyetracker.sendMessage('stop_phase imagery')
            eyetracker.sendMessage('start_phase rest_1')
            eyetracker.sendMessage(f"var rest_lum_1 [{rest_lum_1},{rest_lum_1},{rest_lum_1}]")
            eyetracker.sendMessage(f"var rest_lum_1_original {rest_1.fillColor}")
            """,  # 7. Message for the resting phase
            
                 """eyetracker.sendMessage('stop_phase rest_1')
            stim_lum = (color_rgb[0] + 1) * 127.5
            border_lum = (border_col[0] + 1) * 127.5 # We add 1 because rest.fillColor[0] goes from -1 to 1.
            eyetracker.sendMessage('start_phase stim')
            eyetracker.sendMessage(f'var stim_color [{stim_lum},{stim_lum},{stim_lum}]')
            eyetracker.sendMessage(f'var stim_color_original {color_rgb}')
            eyetracker.sendMessage(f'var border_color [{border_lum},{border_lum},{border_lum}]')
            eyetracker.sendMessage(f'var border_color_original {border_col}')
            eyetracker.sendMessage(f'var stim_orientation {orientation}')

            """, # 8. Messages for the start of stimuli
             
                 """eyetracker.sendMessage('stop_phase stim')
            eyetracker.sendMessage('start_phase rest_2')
            eyetracker.sendMessage(f"var rest_lum_2 [{rest_lum_2},{rest_lum_2},{rest_lum_2}]")
            eyetracker.sendMessage(f"var rest_lum_2_original {rest_2.fillColor}")
            """, # 9. Messages for the end of stimuli and the resting phase
                
                """eyetracker.sendMessage('stop_phase rest_2')
                """, # 10. End second resting phase
                
                """eyetracker.sendMessage('start_phase rating')
            """, # 11.
            
                 """           eyetracker.sendMessage(f'var rating {vivid.getRating()}')
            eyetracker.sendMessage('stop_phase rating')
            eyetracker.sendMessage('stop_trial')
            win.mouseVisible = False
 """, # 12. Rating of the vividness from the subject + remove mouse cursor

                """
#Compute different luminances
background_lum = (win.color[0] + 1) * 127.5 # We add 1 because win.color[0] goes from -1 to 1.
rest_lum_1 = (rest_1.fillColor[0] + 1) * 127.5 # We add 1 because rest.fillColor[0] goes from -1 to 1.
rest_lum_2 = (rest_2.fillColor[0] + 1) * 127.5 # We add 1 because rest.fillColor[0] goes from -1 to 1.
fix_cross_lum = (fix_cross.fillColor[0] + 1) * 127.5 # We add 1 because win.color[0] goes from -1 to 1.

win.mouseVisible = False
""", # 13. Compute luminances + Disallow mouse cursor at the beginning of the test

            """
    win.mouseVisible = True""", # 14. Allow mouse cursor for the rating phase

            """eyetracker.setConnectionState(False)
""" # 15. Command to close eyelink #Utiliser core.quit()
       )



# Create a loop to go through the code and add the commands of interest.
for index_string, string in enumerate(list_of_interest): # Loop through the strings of interest in the code
    
    # Find all indices of the string of interest
    #print(string) # Print out the command we're looking at.
    indices_object = re.finditer(pattern=string, string=code) # Find all of the occurences that the commands appears in the code.
    indices = [index.start() for index in indices_object]  # Find out the index of the first letter of the command.
    #print(indices) #Print it out.
    if indices == []:
        print("A string has not been found in the code:\n", string, "\n")
        
    i = 0 # Add the length of the command to add to the given index. Used when there are several times the same command to add.
    
    for index_indices, list_index in enumerate(indices):
        if "stop_phase rating" in string_to_add[index_string] or "win.mouseVisible = True" in string_to_add[index_string]:
            code = code[:list_index + i + len(string)] + string_to_add[index_string] + code[list_index + i + len(string):]
            
        else: 
            code = code[:list_index + i] + string_to_add[index_string] + code[list_index + i:]
            
        i += len(string_to_add[index_string])
    



# Save data into a new file
with io.open(path + '/final_' + filename, 'w', encoding = "utf-8") as output:
    output.write(code)
