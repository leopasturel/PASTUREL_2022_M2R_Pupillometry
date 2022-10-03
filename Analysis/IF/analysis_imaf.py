# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:19:37 2022

@author: Léo PASTUREL

Python version: 3.9
Mathôt's code: https://github.com/open-cogsci/python-datamatrix
PsychoPy version: v2021.2.3
"""

"""
In this version, I use the proper blink reconstruction method that already
applies a Hanning window to smooth the data.
After running the first cell, you will be able to run any other cell independantly.

!!! In cell 1, we are downloading the data. Inspired by Mathôt et al. (2018).
In cell 2, we are plotting a graph with all data.
In cell 3, we are plotting one graph per participant.
In cell 4, we are plotting one graph per rating.
In cell 5, we are plotting one graph per rating and per participant.
!!! In cell 6, we are creating a wide format dataframe and export it to csv.
!!! In cell 7, we create a shorten wide format dataframe, export it to csv.
and plot the results (Results in the paper are from there). Also graph results from
subpopulations (low/high mean_rating and QMI)
In cell 8, we create a new dataframe and export it to excel. It will allow 
us to continue data analysis in R.
In cell 9, we create a new dataframe with 1 line per subject by subtracting 
mean data of one condition to the other and plot the result (1 line per subject)
In cell 10 to 12, we plot gaze position across time
In cell 13, we create histograms of blinks during the whole experiment and imagery.
In cell 14, we plot the distance to center of the gaze over time; Once with one plot
with all participants and one with one plot per participant.
In cell 15, we plot an histogram of pupil size during baseline to see if 
participants should be removed (according to Mathôt et al., 2018)
In cell 16, we compute the correlation matrices and p-values for qmi and mean rating.


In more features are some drafts and other ideas not used. 
"""

#%%

# =============================================================================
# Cell 1 : Read data
# =============================================================================

import numpy as np
from matplotlib import pyplot as plt
from datamatrix import plot, convert, DataMatrix, io
from datamatrix.colors.tango import blue, red
from datamatrix import functional as fnc, series as srs, operations as ops
import datamatrix
from eyelinkparser import parse, defaulttraceprocessor
from scipy.signal import windows, filtfilt
import pandas as pd
import os
import inspect
import time
from datetime import datetime
from datamatrix import SeriesColumn
import matplotlib.colors as colors
import seaborn as sns
import scipy.stats
import matplotlib

# Print out when you started to launch the code
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Start time =", current_time)


# Define values for depth of each cell within columns.
baseline_length_IF = 1600
imagery_length_IF = 6000
rest_1_length_IF = 4000
stim_length_IF = 5000
rest_2_length_IF = 10000

pupil_length_IF = baseline_length_IF + imagery_length_IF + rest_1_length_IF + stim_length_IF + rest_2_length_IF

# Define plot size
FIGSIZE = 10, 5
X_IF = np.linspace(0, pupil_length_IF/1000, pupil_length_IF)
matplotlib.style.use('seaborn-whitegrid')

# Define parameters for the get_data function
smooth_winlen = 51 # Mathôt, 2018, uses 51ms

### GET DIRECTORIES ###
# Get full actual file path
actual_file_path = inspect.getframeinfo(inspect.currentframe()).filename
# Get parent folder path
path_IF = os.path.dirname(os.path.abspath(actual_file_path))
folder_asc = 'data_asc'
full_path_IF = os.path.join(path_IF, folder_asc)

# Create a path out of the git because memoize files are too big for git
out_of_git_path_IF = os.path.dirname(os.path.dirname(os.path.dirname(path_IF)))
fnc.memoize.folder = out_of_git_path_IF + "\\.memoize_IF"# Change the cache folder of the memoize function

# Create functions that will create a simple datamatrix with values of interest.

@fnc.memoize(persistent = True)
def get_data_IF():
    """Create a simple datamatrix with all data of interest."""

    # Get the datafolder that contains all the .asc files
    dm_IF = parse(
        folder = full_path_IF) # Folder with .asc 
    
    # print(dm_IF.ptrace_baseline.depth, dm_IF.ptrace_imagery.depth, dm_IF.ptrace_rest_1.depth,
    #       dm_IF.ptrace_stim.depth, dm_IF.ptrace_rest_2.depth)
    
    # Apply depth to each column
    dm_IF.ptrace_baseline.depth = baseline_length_IF
    dm_IF.ptrace_imagery.depth = imagery_length_IF
    dm_IF.ptrace_rest_1.depth = rest_1_length_IF
    dm_IF.ptrace_stim.depth = stim_length_IF
    dm_IF.ptrace_rest_2.depth = rest_2_length_IF

    # Concatenate pupil size of the whole trial for all trials
    dm_IF.pupil = srs.concatenate(
        dm_IF.ptrace_baseline,
        dm_IF.ptrace_imagery,
        dm_IF.ptrace_rest_1,
        dm_IF.ptrace_stim,
        dm_IF.ptrace_rest_2
    )
    
    # Apply depth to each column for eye gaze in x
    dm_IF.xtrace_baseline.depth = baseline_length_IF
    dm_IF.xtrace_imagery.depth = imagery_length_IF
    dm_IF.xtrace_rest_1.depth = rest_1_length_IF
    dm_IF.xtrace_stim.depth = stim_length_IF
    dm_IF.xtrace_rest_2.depth = rest_2_length_IF
    
    # Apply depth to each column for eye gaze in y
    dm_IF.ytrace_baseline.depth = baseline_length_IF
    dm_IF.ytrace_imagery.depth = imagery_length_IF
    dm_IF.ytrace_rest_1.depth = rest_1_length_IF
    dm_IF.ytrace_stim.depth = stim_length_IF
    dm_IF.ytrace_rest_2.depth = rest_2_length_IF
    
    # Concatenate eye gaze in x of the whole trial for all trials
    dm_IF.xtrace = srs.concatenate(
        dm_IF.xtrace_baseline, 
        dm_IF.xtrace_imagery,
        dm_IF.xtrace_rest_1, 
        dm_IF.xtrace_stim,
        dm_IF.xtrace_rest_2 
    )
    
    # Concatenate eye gaze in y of the whole trial for all trials
    dm_IF.ytrace = srs.concatenate(
        dm_IF.ytrace_baseline, 
        dm_IF.ytrace_imagery,
        dm_IF.ytrace_rest_1, 
        dm_IF.ytrace_stim,
        dm_IF.ytrace_rest_2 
    )
    
    # Reconstruct the signal during blinks. Default parameters are mostly used
    dm_IF.pupil = srs.blinkreconstruct(dm_IF.pupil, vt=5, vt_start=10, vt_end=5, maxdur=500,
                         margin=10, smooth_winlen=smooth_winlen, std_thr=3, gap_margin=20,
                         gap_vt=10, mode='advanced')
    
    # Create list of blinks
    dm_IF.blinkstlist = srs.concatenate(
        dm_IF.blinkstlist_baseline, 
        dm_IF.blinkstlist_imagery,
        dm_IF.blinkstlist_rest_1, 
        dm_IF.blinkstlist_stim,
        dm_IF.blinkstlist_rest_2
    )
    
    # Keep raw pupil evolution
    dm_IF.pupil_raw = dm_IF.pupil
    
    # Remove the baseline from the pupil size
    dm_IF.pupil = srs.baseline(
        dm_IF.pupil,
        dm_IF.ptrace_baseline,
        -500, -1,
        method='divisive' # Should be either divisive or subtractive
    )        
    
    # Remove the baseline from the pupil size during baseline
    dm_IF.baseline = srs.baseline(
        dm_IF.ptrace_baseline,
        dm_IF.ptrace_baseline,
        -500, -1,
        method='divisive' # Should be either divisive or subtractive
    ) 
        
    # Remove the baseline from the pupil size during imagery
    dm_IF.imagery = srs.baseline(
        dm_IF.ptrace_imagery,
        dm_IF.ptrace_baseline,
        -500, -1,
        method='divisive' # Should be either divisive or subtractive
    ) 
    
    # Remove the baseline from the pupil size during rest
    dm_IF.rest_1 = srs.baseline(
        dm_IF.ptrace_rest_1,
        dm_IF.ptrace_baseline,
        -500, -1,
        method='divisive' # Should be either divisive or subtractive
    ) 
        
    # Remove the baseline from the pupil size during perception
    dm_IF.stim = srs.baseline(
        dm_IF.ptrace_stim,
        dm_IF.ptrace_baseline,
        -500, -1,
        method='divisive' # Should be either divisive or subtractive
    ) 
      
    # Remove the baseline from the pupil size during rest
    dm_IF.rest_2 = srs.baseline(
        dm_IF.ptrace_rest_2,
        dm_IF.ptrace_baseline,
        -500, -1,
        method='divisive' # Should be either divisive or subtractive
    ) 
       
    # Define stimuli colors
    dm_IF.stim_color = fnc.map_(
        lambda s: 'white' if '[255.0,255.0,255.0]' in s  else 'black',
        dm_IF.stim_color
    )
    
    # Change name of trial ID variable
    dm_IF.rename('trialid', 'trial_id')    
    
    dm_IF = ops.keep_only(dm_IF, dm_IF.subject_id, dm_IF.trial_id, dm_IF.pupil, dm_IF.imagery, dm_IF.baseline,
                       dm_IF.stim, dm_IF.rest_1, dm_IF.rest_2, dm_IF.stim_color, dm_IF.stim_orientation, 
                       dm_IF.rating, dm_IF.subject_session, dm_IF.exp_date, dm_IF.exp_name, 
                       dm_IF.framerate, dm_IF.screen_size, dm_IF.background_lum, 
                       dm_IF.rest_lum_1, dm_IF.rest_lum_2, dm_IF.fix_cross_lum,
                       dm_IF.text_color_original, dm_IF.stim_color_original, 
                       dm_IF.rest_lum_1_original, dm_IF.rest_lum_2_original,
                       dm_IF.pupil_raw, dm_IF.ptrace_baseline, dm_IF.ptrace_imagery,
                       dm_IF.ptrace_rest_1, dm_IF.ptrace_stim, dm_IF.ptrace_rest_2,
                       dm_IF.xtrace, dm_IF.ytrace, dm_IF.blinkstlist, dm_IF.blinkstlist_baseline, 
                       dm_IF.blinkstlist_imagery, dm_IF.blinkstlist_rest_1, dm_IF.blinkstlist_stim,
                       dm_IF.blinkstlist_rest_2, dm_IF.t_onset_baseline
                       )
    
    return dm_IF


@fnc.memoize(persistent = True)
def remove_wrong_IF(dm_IF, wrong_baseline):
    """Remove trials in which the baseline did not match the expectations"""
    
    wrong_baseline.reverse() # Reverse list items to start removing the ones with a bigger index
    for wrong_trial in wrong_baseline:
        del dm_IF[wrong_trial]
    return dm_IF


@fnc.memoize(persistent = True)
def remove_training_IF(dm_IF):
    """Remove training trials"""
    
    counter = 0
    for index_trial, trial in enumerate(dm_IF.trial_id):
        try:
            if trial < 3:
                del dm_IF[index_trial - counter]
                counter += 1
        except:
            TypeError
            del dm_IF[index_trial - counter]
            counter += 1
    return dm_IF


def trace(series, x=None, color=blue[1], err=True, binomial=False, **kwdict):

    """
    This is a modified version of Mathôt's plot.trace to have proper confidence 
    intervals that take into account the 95% confidence level.
    
    desc:
        Creates an average-trace plot.

    arguments:
        series:
            desc:   The signal.
            type:	SeriesColumn

    keywords:
        x:
            desc:	An array for the X axis with the same length as series, or
                    None for a default axis.
            type:	[ndarray, None]
        color:
            desc:	The color.
            type:	str
        label:
            desc:	A label for the line, or None for no label.
            type:	[str, None]
    """
    
    alpha=0.05
    t=scipy.stats.t.ppf((1-alpha/2),len(series)-1)
    
    y = series.mean
    if x is None:
        x = np.arange(len(y))
    elif type(x) is datamatrix._datamatrix._seriescolumn._SeriesColumn:
        x = series.mean
    if err:
        n = (~np.isnan(series)).sum(axis=0)
        if binomial:
            yerr = np.sqrt((1./n) * y * (1-y))
        else:
            yerr = series.std/np.sqrt(n)
        ymin = y-t*yerr
        ymax = y+t*yerr
        plt.fill_between(x, ymin, ymax, color=color, alpha=.2)
    plt.plot(x, y, color=color, **kwdict)



# Call function
t0 = time.time()
dm_IF = get_data_IF()

# Keep an untouched version of the datamatrix
dm_IF_raw = dm_IF 

# Remove the training trials
dm_IF = remove_training_IF(dm_IF)

# Show participants that had a wrong baseline and the number of baseline they had wrong
dic_subj_IF = {}
counter = 0
# If baseline size < 2mm or > 8mm, remove trial and count it
wrong_baseline = [] # Create list to have a trace of which trials have to be removed. 
for index_baseline, trial in enumerate(dm_IF.ptrace_baseline):
    mean_base = np.nanmean(trial[-500:]) # Only take the last 500ms since we are computing the baseline on them.
    if dm_IF.subject_id[index_baseline] not in dic_subj_IF.keys():
        counter = 0 # Restart counter if you're on a new subject
    # if mean_base < 2000 or mean_base > 8000: # Check if mean pupil size is not in proper range
    if np.isnan(mean_base) == True: # Check if baseline has values
        if index_baseline not in wrong_baseline:
            counter += 1
            dic_subj_IF[dm_IF.subject_id[index_baseline]] = counter
            wrong_baseline.append(index_baseline)
            

dm_IF = remove_wrong_IF(dm_IF, wrong_baseline)
# print(f"There has been {len(wrong_baseline)} trials that have been removed because mean pupil diameter was unrealistic (<2mm or >8mm) during baseline.")
print(f"There has been {len(wrong_baseline)} trials that have been removed because there was no data during baseline.")
print(dic_subj_IF)

t1 = time.time()
print('Full timing IF: %.2f mn' % ((t1-t0)/60))

#%%

# =============================================================================
# Cell 2 : Plot a quick graph with all data (WRONG)
# WARNING: This is just a quick way to plot all data but should not be used as such.
# Refer to cell 7 for a proper graph.
# =============================================================================

plot.new(size=FIGSIZE)
plt.ylim()
plt.xlim(0, pupil_length_IF/1000)


plt.axvline(baseline_length_IF/1000, color='black', linestyle=':') # Add vertical line for end of baseline/start of stim
plt.axvline((baseline_length_IF + imagery_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of rest/start of imagery
plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF + stim_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
plt.axhline(1, color='black', linestyle=':') # Add horizontal line for baseline level


# Split conditions white vs black
for stim_color, _dm_IF in ops.split(dm_IF.stim_color):
    trace(
        _dm_IF.pupil,
        x=X_IF, 
        color=blue[1] if stim_color == 'white' else red[1],
        label='%s condition (N=%d)' % (stim_color, len(_dm_IF))
    )


# Add annotations
plt.annotate('Baseline', rotation=90,
            xy=(68, 265), xycoords='figure points')
plt.annotate('Imagery',
            xy=(120, 300), xycoords='figure points')
plt.annotate('Rest',
            xy=(233, 300), xycoords='figure points')
plt.annotate('Perception',
            xy=(310, 300), xycoords='figure points')
plt.annotate('Rest',
            xy=(480, 300), xycoords='figure points')


  
plt.ylabel('Pupil size (normalized)')
plt.xlabel('Time (s)')
plt.title("Normalized pupil diameter evolution over time in general population")
plt.legend(loc='lower left', frameon=True)
# plt.savefig(path_IF + '\pupil_response_all_subjects.png', bbox_inches='tight')
plt.show()


#%%

# =============================================================================
# Cell 3 : Plot data with one graph per subject
# =============================================================================

subject_list = []
for subject in dm_IF.subject_id:
    if subject not in subject_list:
        subject_list.append(subject)
        subject_nb = subject[-3:]
        dm_IF_subj =  dm_IF.subject_id == {subject}
        
        plot.new(size=FIGSIZE)
        plt.ylim()
        plt.xlim(0, pupil_length_IF/1000)
        
        
        # Split conditions white vs black
        for stim_color, _dm_IF_subj in ops.split(dm_IF_subj.stim_color):
            trace(
                _dm_IF_subj.pupil,
                x=X_IF, 
                color=blue[1] if stim_color == 'white' else red[1],
                label='%s condition (N=%d)' % (stim_color, len(_dm_IF_subj))
            )
        
        # Draw dotted lines on the graph
        plt.axvline(baseline_length_IF/1000, color='black', linestyle=':') # Add vertical line for end of baseline/start of stim
        plt.axvline((baseline_length_IF + imagery_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
        plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of rest/start of imagery
        plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF + stim_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
        plt.axhline(1, color='black', linestyle=':') # Add horizontal line for baseline level


        # Add annotations
        plt.annotate('Baseline', rotation=90,
                    xy=(68, 265), xycoords='figure points')
        plt.annotate('Imagery',
                    xy=(120, 300), xycoords='figure points')
        plt.annotate('Rest',
                    xy=(233, 300), xycoords='figure points')
        plt.annotate('Perception',
                    xy=(310, 300), xycoords='figure points')
        plt.annotate('Rest',
                    xy=(470, 300), xycoords='figure points')
        
        
        plt.ylabel('Pupil size (normalized)')
        plt.xlabel('Time (s)')
        plt.title(f"Normalized pupil diameter evolution over time\nSubject n°{subject_nb}")
        plt.legend(loc='lower left', frameon=True)
        plt.savefig(path_IF + f'\Graphs\per_subject\pupil_response_IF_subject_{subject}.png', 
                    bbox_inches='tight')
        plt.show()
        
        
#%%

# =============================================================================
# Cell 4 : Plot data with one graph per rating
# =============================================================================

rating_list = [1,2,3,4]

for rating in rating_list:

    dm_IF_rating = dm_IF.rating == {rating}
    
    plot.new(size=FIGSIZE)
    plt.ylim()
    plt.xlim(0, pupil_length_IF/1000)
    plt.axvline(baseline_length_IF/1000, color='black', linestyle=':') # Add vertical line for end of baseline/start of stim
    plt.axvline((baseline_length_IF + imagery_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
    plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of rest/start of imagery
    plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF + stim_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
    plt.axhline(1, color='black', linestyle=':') # Add horizontal line for baseline level

    # Split conditions white vs black
    for stim_color, _dm_IF_rating in ops.split(dm_IF_rating.stim_color):
        trace(
            _dm_IF_rating.pupil,
            x=X_IF, 
            color=blue[1] if stim_color == 'white' else red[1],
            label='%s condition (N=%d)' % (stim_color, len(_dm_IF_rating))
        )

    print(rating)
    # Add annotations
    plt.annotate('Baseline', rotation=90,
                xy=(68, 270), xycoords='figure points')
    plt.annotate('Imagery',
                xy=(120, 300), xycoords='figure points')
    plt.annotate('Rest',
                xy=(233, 300), xycoords='figure points')
    plt.annotate('Perception',
                xy=(310, 300), xycoords='figure points')
    plt.annotate('Rest',
                xy=(470, 300), xycoords='figure points')
    
    plt.ylabel('Pupil size (normalized)')
    plt.xlabel('Time (s)')
    plt.title(f"Normalized pupil diameter evolution over time in general population\nRating {rating}")
    plt.legend(loc='lower left', frameon=True)
    plt.savefig(path_IF + f'\Graphs\per_rating\pupil_response_IF_rating_{rating}.png', 
                bbox_inches='tight')
    plt.show()    
    

#%%

# =============================================================================
# Cell 5 : Plot data with one graph per rating and per subject
# =============================================================================

rating_list = [1,2,3,4]
subject_list = []

for subject in dm_IF.subject_id:
    if subject not in subject_list:
        subject_list.append(subject)
        subject_nb = len(subject_list)
        dm_IF_subj =  dm_IF.subject_id == {subject}
        
        for rating in rating_list:
        
            dm_IF_rating = dm_IF_subj.rating == {rating}
            
            plot.new(size=FIGSIZE)
            plt.ylim()
            plt.xlim(0, pupil_length_IF/1000)
        
            # Split conditions white vs black
            for stim_color, _dm_IF_rating in ops.split(dm_IF_rating.stim_color):
                trace(
                    _dm_IF_rating.pupil,
                    x=X_IF, 
                    color=blue[1] if stim_color == 'white' else red[1],
                    label='%s condition (N=%d)' % (stim_color, len(_dm_IF_rating))
                )
        
            # Draw dotted lines on the graph
            plt.axvline(baseline_length_IF/1000, color='black', linestyle=':') # Add vertical line for end of baseline/start of stim
            plt.axvline((baseline_length_IF + imagery_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
            plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of rest/start of imagery
            plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF + stim_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
            plt.axhline(1, color='black', linestyle=':') # Add horizontal line for baseline level

            # Add annotations
            plt.annotate('Baseline', rotation=90,
                        xy=(65, 270), xycoords='figure points')
            plt.annotate('Perception',
                        xy=(120, 300), xycoords='figure points')
            plt.annotate('Rest',
                        xy=(305, 300), xycoords='figure points')
            plt.annotate('Imagery',
                        xy=(490, 300), xycoords='figure points')
            
            plt.ylabel('Pupil size (normalized)')
            plt.xlabel('Time (s)')
            plt.title(f"Normalized pupil diameter evolution over time in general population\nSubject n°{subject} Rating {rating}")
            plt.legend(loc='lower left', frameon=True)
            plt.show()    
                    

#%%

# =============================================================================
# Cell 6: Create a wide mastersheet and export it to csv 
# ============================================================================= 

# Convert datamtrix to pandas
df_IF = convert.to_pandas(dm_IF)

# Keep only columns of interest
df_IF = df_IF[['subject_id', 'trial_id', 'exp_name', 'exp_date', 'stim_color', 
               'stim_orientation', 'rating', 'pupil']]

# Split the column that contains pupil size to have one value per cell
df_IF = df_IF.join(pd.DataFrame(df_IF['pupil'].values.tolist()).add_prefix('ms_'))

# Export to csv
df_IF.to_csv(out_of_git_path_IF + '\\IF_tables\\wide_mastersheet_IF.csv')


#%%

# =============================================================================
# Cell 7: Reduce wide mastersheet to 1 line per subject and per condition
# =============================================================================

# Retreive mastersheet
df_IF = pd.read_csv(out_of_git_path_IF + '\\IF_tables\\wide_mastersheet_IF.csv')

# Compute the mean pupil size at any moment for one subject in one condition
df_IF_short = df_IF.groupby(['subject_id', 'stim_color'], as_index = False).mean()

# Remove unused columns
df_IF_short = df_IF_short.drop(['Unnamed: 0', 'trial_id', 'stim_orientation'], axis=1)

# Get the column headers without the rating
ms_headers = df_IF_short.columns[3:]

# Merge all ms_x columns into one
df_IF_short['pupil_mean'] = df_IF_short[ms_headers].astype(str).agg(', '.join, axis=1)#.tolist()

# Create a secondary table to store the values
df_temp = pd.DataFrame(index = range(len(df_IF_short['pupil_mean'])), columns = ['pupil_mean'])
for index in range(len(df_IF_short['pupil_mean'])):
    df_temp['pupil_mean'][index] = str(list(map(float, df_IF_short['pupil_mean'][index].split(", "))))

# Drop all ms_x columns and replace with the proper one.
df_IF_short = df_IF_short.drop(ms_headers, axis=1)
df_IF_short['pupil_mean'] = df_temp['pupil_mean']

# Re-add the exp name
df_IF_short['exp_name'] = "pupillo_imaf"

# Save dataframe
df_IF_short.to_csv(out_of_git_path_IF + '\\IF_tables\\wide_short_mastersheet_IF.csv')

# Convert back to Datamatrix
dm_IF_short = convert.from_pandas(df_IF_short)

# Create a new colum in the datamatrix to re-inser pupil diameter
dm_IF_short.pupil = SeriesColumn(depth=pupil_length_IF)

# Insert pupil size in the proper column and in the proper format
for index, pupil_size in enumerate(dm_IF_short.pupil_mean):
    k = dm_IF_short.pupil_mean[index]
    k = list(map(float, k[1:-1].split(", ")))
    dm_IF_short.pupil[index] = np.asarray((k))

# Be sure to keep only the right columns in the datamatrix
dm_IF_short = ops.keep_only(dm_IF_short, dm_IF_short.subject_id,
                      dm_IF_short.pupil, dm_IF_short.stim_color,
                      dm_IF_short.rating)



# Plot results with the new, shorter datamatrix. (PLOT IN PAPER)
plot.new(size=FIGSIZE)
plt.ylim()
plt.xlim(0, pupil_length_IF/1000)


plt.axvline(baseline_length_IF/1000, color='black', linestyle=':') # Add vertical line for end of baseline/start of stim
plt.axvline((baseline_length_IF + imagery_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of rest/start of imagery
plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF + stim_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
plt.axhline(1, color='black', linestyle=':') # Add horizontal line for baseline level


# Split conditions white vs black
for stim_color, _dm_IF_short in ops.split(dm_IF_short.stim_color):
    trace(
        _dm_IF_short.pupil,
        x=X_IF, 
        color=blue[1] if stim_color == 'white' else red[1],
        label='%s condition (N=%d)' % (stim_color, len(_dm_IF_short))
    )


# Add annotations
plt.annotate('Baseline', rotation=90,
            xy=(68, 265), xycoords='figure points')
plt.annotate('Imagery',
            xy=(120, 290), xycoords='figure points')
plt.annotate('Rest',
            xy=(233, 290), xycoords='figure points')
plt.annotate('Perception',
            xy=(310, 290), xycoords='figure points')
plt.annotate('Rest',
            xy=(480, 290), xycoords='figure points')


  
plt.ylabel('Pupil size (normalized)')
plt.xlabel('Time (s)')
plt.title("Normalized pupil diameter evolution over time in general population")
plt.legend(loc='lower left', frameon=True)
plt.savefig(path_IF + '\Graphs\pupil_response_IF_all_subjects.png', 
            bbox_inches='tight')
plt.show()


# Graph for mean rating <= 2 and >= 3 

rating_list = [2, 3]

for rating in rating_list:
    
    if rating == 2:
        dm_IF_rating = dm_IF_short.rating <= rating
        
    elif rating == 3:
        dm_IF_rating = dm_IF_short.rating >= rating
    
    plot.new(size=FIGSIZE)
    plt.ylim()
    plt.xlim(0, pupil_length_IF/1000)

    # Split conditions white vs black
    for stim_color, _dm_IF_rating in ops.split(dm_IF_rating.stim_color):
        trace(
            _dm_IF_rating.pupil,
            x=X_IF, 
            color=blue[1] if stim_color == 'white' else red[1],
            label='%s condition (N=%d)' % (stim_color, len(_dm_IF_rating))
        )

    # Draw dotted lines on the graph
    plt.axvline(baseline_length_IF/1000, color='black', linestyle=':') # Add vertical line for end of baseline/start of stim
    plt.axvline((baseline_length_IF + imagery_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
    plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of rest/start of imagery
    plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF + stim_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
    plt.axhline(1, color='black', linestyle=':') # Add horizontal line for baseline level

    # Add annotations
    plt.annotate('Baseline', rotation=90,
                xy=(68, 265), xycoords='figure points')
    plt.annotate('Imagery',
                xy=(120, 290), xycoords='figure points')
    plt.annotate('Rest',
                xy=(233, 290), xycoords='figure points')
    plt.annotate('Perception',
                xy=(310, 290), xycoords='figure points')
    plt.annotate('Rest',
                xy=(480, 290), xycoords='figure points')
    
    plt.ylabel('Pupil size (normalized)')
    plt.xlabel('Time (s)')
    
    if rating == 2:
        plt.title(f"Normalized pupil diameter evolution over time in population\n Mean rating ≤ {rating}")
    elif rating == 3:
        plt.title(f"Normalized pupil diameter evolution over time in population\n Mean rating ≥ {rating}")
    
    plt.legend(loc='lower left', frameon=True)
    plt.show()    




# Graph for low and high QMI

df_qmi = pd.read_csv(out_of_git_path_IF + '\\pupillometry_M2SCCO\\Analysis\\QMI\\qmi_results_summary.csv')

dm_IF_qmi = dm_IF_short
dm_IF_qmi.visual_qmi = ""

subject_list = []

for index, subject in enumerate(dm_IF_qmi.subject_id):
    for index_qmi, subject_qmi in enumerate(df_qmi.subject):
        if subject_qmi == subject[-4:]:
            qmi_value = df_qmi.loc[index_qmi,'visual_qmi']
        
    dm_IF_qmi.visual_qmi[index] = qmi_value
        
    
# Graph for visual QMI <= 15 and >= 30 

qmi_list = [15, 30]

for qmi in qmi_list:
    
    if qmi == 15:
        dm_IF_qmi = dm_IF_short.visual_qmi <= qmi
        
    elif qmi == 30:
        dm_IF_qmi = dm_IF_short.visual_qmi >= qmi
    
    plot.new(size=FIGSIZE)
    plt.ylim()
    plt.xlim(0, pupil_length_IF/1000)

    # Split conditions white vs black
    for stim_color, _dm_IF_qmi in ops.split(dm_IF_qmi.stim_color):
        trace(
            _dm_IF_qmi.pupil,
            x=X_IF, 
            color=blue[1] if stim_color == 'white' else red[1],
            label='%s condition (N=%d)' % (stim_color, len(_dm_IF_qmi))
        )

    # Draw dotted lines on the graph
    plt.axvline(baseline_length_IF/1000, color='black', linestyle=':') # Add vertical line for end of baseline/start of stim
    plt.axvline((baseline_length_IF + imagery_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
    plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of rest/start of imagery
    plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF + stim_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
    plt.axhline(1, color='black', linestyle=':') # Add horizontal line for baseline level

    # Add annotations
    plt.annotate('Baseline', rotation=90,
                xy=(68, 265), xycoords='figure points')
    plt.annotate('Imagery',
                xy=(120, 290), xycoords='figure points')
    plt.annotate('Rest',
                xy=(233, 290), xycoords='figure points')
    plt.annotate('Perception',
                xy=(310, 290), xycoords='figure points')
    plt.annotate('Rest',
                xy=(480, 290), xycoords='figure points')
    
    plt.ylabel('Pupil size (normalized)')
    plt.xlabel('Time (s)')
    
    if qmi == 15:
        plt.title(f"Normalized pupil diameter evolution over time in population\n Visual qmi ≤ {qmi}")
    elif qmi == 30:
        plt.title(f"Normalized pupil diameter evolution over time in population\n Visual qmi ≥ {qmi}")
    
    plt.legend(loc='lower left', frameon=True)
    plt.show() 

#%%

# =============================================================================
# Cell 8: Create a smaller dataframe with mean pupil values (one line/subject)
# =============================================================================

dic_summary = []
subject_list = []

for subject in dm_IF.subject_id:
    if subject not in subject_list:
        subject_list.append(subject)
        subject_nb = len(subject_list)
        dm_IF_subj =  dm_IF.subject_id == {subject}

        for stim_color, _dm_IF_subj in ops.split(dm_IF_subj.stim_color):

            dic_summary.append(
                {'subject_id' : subject,
                'stim_color' : stim_color,
                'exp_name' : "pupillo_imaf",
                'trials' : len(_dm_IF_subj),
                'mean_pupil_size_baseline_500ms' : np.nanmean(_dm_IF_subj.baseline[-500:]),
                'mean_pupil_size_imagery_4000ms' : np.nanmean(list(map(lambda x: x[1500:-500], _dm_IF_subj.imagery))), # Don't take the first 2000ms and last 500ms
                'std_pupil_size_imagery_4000ms' : np.nanstd(list(map(lambda x: x[500:-500], _dm_IF_subj.imagery))), # Don't take the first 2000ms and last 500ms
                'mean_pupil_size_rest1_1000ms' : np.nanmean(list(map(lambda x: x[-1000:], _dm_IF_subj.rest_1))), # Take the last 1000ms
                'mean_pupil_size_perception_1000ms' : np.nanmean(list(map(lambda x: x[-1000:], _dm_IF_subj.stim))), # Take the last 1000ms
                'mean_pupil_size_rest2_1000ms' : np.nanmean(list(map(lambda x: x[-1000:], _dm_IF_subj.rest_2))), # Take the last 1000ms
                'mean_pupil_size_rest2_3000ms' : np.nanmean(list(map(lambda x: x[-4000:-1000], _dm_IF_subj.rest_2))), # Take the last 4000ms without last 1000ms
                'median_rating' : np.median(_dm_IF_subj.rating),
                'mean_rating' : np.mean(_dm_IF_subj.rating)
                }
            )

subject_recap = pd.DataFrame(dic_summary)

print(subject_recap)

subject_recap.to_excel(out_of_git_path_IF + '\\IF_tables\\subject_recap_IF_regress.xlsx')
    

# Create a recap of subject data and segregate conditions
dic_summary = []
subject_list = []

for subject in dm_IF.subject_id:
    if subject not in subject_list:
        subject_list.append(subject)
        subject_nb = len(subject_list)
        dm_IF_subj =  dm_IF.subject_id == {subject}

        for stim_color, _dm_IF_subj in ops.split(dm_IF_subj.stim_color):
            if stim_color == "black":
                dic_summary.append(
                {'subject_id' : subject,
                'exp_name' : "pupillo_imaf",
                'B_mean_pupil_size_baseline_500ms' : np.nanmean(_dm_IF_subj.baseline[-500:]),
                'B_mean_pupil_size_imagery_4000ms' : np.nanmean(list(map(lambda x: x[1500:-500], _dm_IF_subj.imagery))), # Don't take the first 2000ms and last 500ms
                'B_std_pupil_size_imagery_4000ms' : np.nanstd(list(map(lambda x: x[1500:-500], _dm_IF_subj.imagery))), # Don't take the first 2000ms and last 500ms
                'B_mean_pupil_size_rest1_1000ms' : np.nanmean(list(map(lambda x: x[-1000:], _dm_IF_subj.rest_1))), # Take the last 1000ms
                'B_mean_pupil_size_perception_1000ms' : np.nanmean(list(map(lambda x: x[-1000:], _dm_IF_subj.stim))), # Take the last 1000ms
                'B_mean_pupil_size_rest2_1000ms' : np.nanmean(list(map(lambda x: x[-1000:], _dm_IF_subj.rest_2))), # Take the last 1000ms
                'B_mean_pupil_size_rest2_3000ms' : np.nanmean(list(map(lambda x: x[-4000:-1000], _dm_IF_subj.rest_2))), # Take the last 4000ms without last 1000ms
                'B_median_rating' : np.median(_dm_IF_subj.rating),
                'B_mean_rating' : np.mean(_dm_IF_subj.rating)
                    }
                )                
                
            elif stim_color == "white":
                dic_summary.append(
                    {'W_mean_pupil_size_baseline_500ms' : np.nanmean(_dm_IF_subj.baseline[-500:]),
                    'W_mean_pupil_size_imagery_4000ms' : np.nanmean(list(map(lambda x: x[1500:-500], _dm_IF_subj.imagery))), # Don't take the first 2000ms and last 500ms
                    'W_std_pupil_size_imagery_4000ms' : np.nanstd(list(map(lambda x: x[1500:-500], _dm_IF_subj.imagery))), # Don't take the first 2000ms and last 500ms
                    'W_mean_pupil_size_rest1_1000ms' : np.nanmean(list(map(lambda x: x[-1000:], _dm_IF_subj.rest_1))), # Take the last 1000ms
                    'W_mean_pupil_size_perception_1000ms' : np.nanmean(list(map(lambda x: x[-1000:], _dm_IF_subj.stim))), # Take the last 1000ms
                    'W_mean_pupil_size_rest2_1000ms' : np.nanmean(list(map(lambda x: x[-1000:], _dm_IF_subj.rest_2))), # Take the last 1000ms
                    'W_mean_pupil_size_rest2_3000ms' : np.nanmean(list(map(lambda x: x[-4000:-1000], _dm_IF_subj.rest_2))), # Take the last 4000ms without last 1000ms
                    'W_median_rating' : np.median(_dm_IF_subj.rating),
                    'W_mean_rating' : np.mean(_dm_IF_subj.rating)
                    }
                )

subject_recap = pd.DataFrame(dic_summary)
subject_recap = subject_recap.apply(lambda x: pd.Series(x.dropna().values))

print(subject_recap)

subject_recap.to_excel(out_of_git_path_IF + '\\IF_tables\\subject_recap_IF_ANOVA.xlsx')

#%%

# =============================================================================
# Cell 9: Create a datamatrix with one line per subject by subtracting white to black conditions and
# draw graph
# =============================================================================

# Retreive mastersheet
df_IF = pd.read_csv(out_of_git_path_IF + '\\IF_tables\\wide_mastersheet_IF.csv')

# Compute the mean pupil size at any moment for one subject in one condition
df_w_b = df_IF.groupby(['subject_id', 'stim_color'], as_index = False).mean()

# Remove unused columns
df_w_b = df_w_b.drop(['Unnamed: 0', 'trial_id', 'stim_orientation'], axis=1)

# Get the column headers without the rating
ms_headers = df_w_b.columns[3:]

# Creating a new df by subtracting one condition by the other.
df_temp_w_b = pd.DataFrame()
for col in ms_headers:
    df_temp_w_b[col + '_w_b'] = (df_w_b[col].values[1::2] - df_w_b[col].values[::2])

df_temp_w_b['rating'] = (df_w_b.rating.values[1::2] - df_w_b.rating.values[::2])
df_w_b = df_temp_w_b

# Merge all ms_x columns into one
df_w_b['pupil_mean'] = df_w_b[ms_headers + '_w_b'].astype(str).agg(', '.join, axis=1)#.tolist()


df_temp_w_b = pd.DataFrame(index = range(len(df_w_b['pupil_mean'])), columns = ['pupil_mean'])
for index in range(len(df_w_b['pupil_mean'])):
    df_temp_w_b['pupil_mean'][index] = str(list(map(float, df_w_b['pupil_mean'][index].split(", "))))
    

# Drop all ms_x columns and replace with the proper one.
df_w_b['pupil_mean'] = df_temp_w_b['pupil_mean']

# Re-add the exp name
df_w_b['exp_name'] = "pupillo_repli"


# Convert df to csv dataframe
df_w_b.to_csv(out_of_git_path_IF + '\\IF_tables\\wide_short_mastersheet_w_b.csv')

# Convert back to Datamatrix
dm_IF_w_b = convert.from_pandas(df_w_b)

# Create a new colum in the datamatrix to re-inser pupil diameter
dm_IF_w_b.pupil = SeriesColumn(depth=pupil_length_IF)

# Insert pupil size in the proper column and in the proper format
for index, pupil_size in enumerate(dm_IF_w_b.pupil_mean):
    k = dm_IF_w_b.pupil_mean[index]
    k = list(map(float, k[1:-1].split(", ")))
    dm_IF_w_b.pupil[index] = np.asarray((k))

# Retrieve subject_id
subject_list = []
for subject in dm_IF.subject_id:
    if subject not in subject_list:
        subject_list.append(subject)

dm_IF_w_b.subject_id = subject_list

# Be sure to keep only the right columns in the datamatrix
dm_IF_w_b = ops.keep_only(dm_IF_w_b, dm_IF_w_b.exp_name, dm_IF_w_b.pupil, 
                          dm_IF_w_b.rating, dm_IF_w_b.subject_id)




# Plot results per subject.

color_palette = list(colors.cnames.values())

plot.new(size=FIGSIZE)
plt.ylim()
plt.xlim(0, pupil_length_IF/1000)

# Add dotted lines
plt.axvline(baseline_length_IF/1000, color='black', linestyle=':') # Add vertical line for end of baseline/start of stim
plt.axvline((baseline_length_IF + imagery_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of rest/start of imagery
plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF + stim_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
plt.axhline(0, color='black', linestyle=':') # Add horizontal line for baseline level

# Add annotations
plt.annotate('Baseline', rotation=90,
            xy=(68, 270), xycoords='figure points')
plt.annotate('Imagery',
            xy=(120, 300), xycoords='figure points')
plt.annotate('Rest',
            xy=(233, 300), xycoords='figure points')
plt.annotate('Perception',
            xy=(310, 300), xycoords='figure points')
plt.annotate('Rest',
            xy=(480, 300), xycoords='figure points')

# Split per subject
counter = 0
for subject, _dm_IF_w_b in ops.split(dm_IF_w_b.subject_id):
    trace(
        _dm_IF_w_b.pupil,
        x=X_IF,
        color = color_palette[counter],
        label='Subject %s' % (subject[-3:]),
        )
    counter += 1


plt.ylabel('Pupil size (normalized)')
plt.xlabel('Time (s)')
plt.title("Normalized pupil diameter evolution over time in general population")
# plt.legend()
plt.savefig(path_IF + '\Graphs\pupil_response_IF_subtracted_condition.png', 
            bbox_inches='tight')
plt.show()

#%%

# =============================================================================
# Cell 10: Graph average gaze per subject during experiment
# =============================================================================

subject_list = []

for subject in dm_IF.subject_id:
    if subject not in subject_list:
        subject_list.append(subject)
        subject_nb = subject[-3:]
        dm_IF_subj =  dm_IF.subject_id == {subject}
        ms_IF = range(len(dm_IF_subj.xtrace.mean))

        # with sns.color_palette("Oranges", len(dm_IF_subj.xtrace.mean)):
        cmap = plt.set_cmap("cividis")
        plt.figure(figsize = FIGSIZE)
        plt.ylim(0, 1024)
        plt.xlim(0, 1280)
        
        sns.scatterplot(x=dm_IF_subj.xtrace.mean, y=dm_IF_subj.ytrace.mean, 
                      hue = ms_IF, palette="cividis")
        # plt.plot(dm_IF_subj.xtrace.mean, dm_IF_subj.ytrace.mean, 'o-')
  
        plt.ylabel('Pixel in y')
        plt.xlabel('Pixel in x')
        plt.set_cmap("Greys") 
        plt.title(f"Mean gaze of paricipant n°{subject_nb} during the experiment IF")
        plt.savefig(path_IF + f'\Graphs\mean_gaze\Mean gaze of participant n°{subject_nb}.png')
        # plt.show()

#%%

# =============================================================================
# Cell 11: Graph gaze per subject during experiment
# =============================================================================

subject_list = []
for subject in dm_IF.subject_id:
    if subject not in subject_list:
        subject_list.append(subject)
        subject_nb = subject[-3:]
        dm_IF_subj =  dm_IF.subject_id == {subject}
        
        plt.figure(figsize = FIGSIZE)
        plt.ylim(0, 1024)
        plt.xlim(0, 1280)
        
        counter = 0
        for trial in dm_IF_subj:
            plt.plot(trial.xtrace, trial.ytrace, 'o-', label = f"Trial n°{trial.trial_id-2}")
            counter += 1
            
        plt.ylabel('Pixel in y')
        plt.xlabel('Pixel in x')
        plt.title(f"Gaze of paricipant n°{subject_nb} during the experiment IF")
        plt.legend(bbox_to_anchor =(0, -0.5), ncol = 4, loc = "lower left")
        plt.savefig(path_IF + f'\Graphs\gaze\Gaze of participant n°{subject_nb}.png')
        # plt.show()

#%%

# =============================================================================
# Cell 12: Graph gaze per subject during imagery
# =============================================================================

subject_list = []
for subject in dm_IF.subject_id:
    if subject not in subject_list:
        subject_list.append(subject)
        subject_nb = subject[-3:]
        dm_IF_subj =  dm_IF.subject_id == {subject}
        
        plt.figure(figsize = FIGSIZE)
        plt.ylim(0, 1024)
        plt.xlim(0, 1280)
        
        counter = 0
        for trial in dm_IF_subj:
            plt.plot(trial.xtrace[-4500:-500], trial.ytrace[-4500:-500], 'o-', label = f"Trial n°{trial.trial_id-2}")
            counter += 1
            
        plt.ylabel('Pixel in y')
        plt.xlabel('Pixel in x')
        plt.title(f"Gaze of paricipant n°{subject_nb} during imagery for experiment IF")
        plt.legend(bbox_to_anchor =(0, -0.5), ncol = 4, loc = "lower left")
        plt.savefig(path_IF + f'\Graphs\gaze_imagery\Gaze imagery of participant n°{subject_nb}.png')
        # plt.show()
        
        

#%%

# =============================================================================
# Cell 13: Draw histogram of blinks during experiment and during imagery
# =============================================================================

# Blinks during complete experiment 
count_blink = []
sum_blink = []
subject_list = []
for subject in dm_IF.subject_id:
    if subject[-4:] not in subject_list:
        subject_list.append(subject[-4:])
        dm_IF_subj =  dm_IF.subject_id == {subject}
        for index in dm_IF_subj.blinkstlist:
            count_blink.append(sum(1 for _ in index if _ > 0))
        
        sum_blink.append(sum(count_blink))
        count_blink = []

# Create df with blinks and subjects
zipped = list(zip(subject_list, sum_blink))
df_blink_IF = pd.DataFrame(columns = ("subject_id", "blink_count"), data=zipped)
df_blink_IF_sorted = df_blink_IF.sort_values('blink_count')

# Plot results
plt.figure(figsize = FIGSIZE)
plt.bar(df_blink_IF_sorted.subject_id, df_blink_IF_sorted.blink_count)
plt.ylabel("Number of blinks")
plt.xlabel("Subject number")
plt.xticks(rotation = 90)
plt.title("Number of blinks during the experiment IF")
plt.savefig(path_IF + '\\Graphs\\Number of blinks during all experiment.png')
plt.show()


# Blinks during imagery
count_blink = []
sum_blink_imag = []
subject_list = []
for subject in dm_IF.subject_id:
    if subject[-4:] not in subject_list:
        subject_list.append(subject[-4:])
        dm_IF_subj =  dm_IF.subject_id == {subject}
        for index in dm_IF_subj.blinkstlist_imagery:
            count_blink.append(sum(1 for _ in index if _ > 0))
        
        sum_blink_imag.append(sum(count_blink))
        count_blink = []

# Create df with blinks and subjects
zipped = list(zip(subject_list, sum_blink_imag))
df_blink_IF_imag = pd.DataFrame(columns = ("subject_id", "blink_count"), data=zipped)
df_blink_IF_imag_sorted = df_blink_IF_imag.sort_values('blink_count')

# Plot results
plt.figure(figsize = FIGSIZE)
plt.bar(df_blink_IF_imag_sorted.subject_id, df_blink_IF_imag_sorted.blink_count)
plt.ylabel("Number of blinks")
plt.xlabel("Subject number")
plt.xticks(rotation = 90)
plt.title("Number of blinks during imagery of experiment IF")
plt.savefig(path_IF + '\\Graphs\\Number of blinks during imagery.png')
plt.show()


#%%

# =============================================================================
# Cell 14: Plot distance to center of the gaze over time
# =============================================================================

# Make a copy of dm to work on.
dm_IF_x_y = dm_IF

# Normalize distance in x from center 
dm_IF_x_y.xtrace = srs.baseline(
    dm_IF_x_y.xtrace,
    dm_IF_x_y.xtrace,
    0, -1, # Use last 500ms of baseline
    method='subtractive' # Should be either divisive or subtractive
) 

# Normalize distance in y from center 
dm_IF_x_y.ytrace = srs.baseline(
    dm_IF_x_y.ytrace,
    dm_IF_x_y.ytrace,
    0, -1, # Use last 500ms of baseline
    method='subtractive' # Should be either divisive or subtractive
) 


# Compute distance to center.
dm_IF_x_y.distance = np.sqrt(dm_IF_x_y.xtrace*dm_IF_x_y.xtrace + dm_IF_x_y.ytrace*dm_IF_x_y.ytrace)


# Plot results in 1 plot with 1 line per subject.
color_palette = list(colors.cnames.values())

plot.new(size=FIGSIZE)
plt.ylim(0, 500)
plt.xlim(0, pupil_length_IF/1000)

# Add dotted lines
plt.axvline(baseline_length_IF/1000, color='black', linestyle=':') # Add vertical line for end of baseline/start of stim
plt.axvline((baseline_length_IF + imagery_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of rest/start of imagery
plt.axvline((baseline_length_IF + imagery_length_IF + rest_1_length_IF + stim_length_IF)/1000, color='black', linestyle=':') # Add vertical line for end of stim/start of rest
# plt.axhline(0, color='black', linestyle=':') # Add horizontal line for baseline level

# Add annotations
plt.annotate('Baseline', rotation=90,
            xy=(68, 265), xycoords='figure points')
plt.annotate('Imagery',
            xy=(120, 295), xycoords='figure points')
plt.annotate('Rest',
            xy=(233, 295), xycoords='figure points')
plt.annotate('Perception',
            xy=(310, 295), xycoords='figure points')
plt.annotate('Rest',
            xy=(480, 295), xycoords='figure points')

# Split per subject
counter = 0
for subject, _dm_IF_x_y in ops.split(dm_IF_x_y.subject_id):
    trace(
        _dm_IF_x_y.distance,
        x=X_IF,
        color = color_palette[counter],
        label='Subject %s' % (subject[-3:]),
        err = False
        )
    counter += 1


plt.ylabel('Distance from center (in pixel)')
plt.xlabel('Time (s)')
plt.title("Mean distance of gaze from center during IF")
# plt.legend()
plt.savefig(path_IF + '\Graphs\gaze_distance_from_center_IF.png', 
            bbox_inches='tight')
plt.show()    


#%%

# =============================================================================
# Cell 15: Making a quick histogram of pupil size during baseline.
# This is to see if some participants baseline are outliers (see Mathôt et al., 2018)
# =============================================================================

baseline_list = []
subject_list = []
for subject in dm_IF.subject_id:
    if subject not in subject_list:            
        
        subject_list.append(subject)
        dm_IF_subj =  dm_IF.subject_id == {subject}
        
        for index, trial in enumerate(dm_IF_subj.ptrace_baseline):
            baseline_list.append(np.nanmean(trial))

print(len(baseline_list))
plt.hist(baseline_list, bins = (len(dm_IF.subject_id)//2))
plt.axvline(4000, color='black', linestyle=':')
plt.axvline(9000, color='black', linestyle=':')
plt.show()

print(sum(1 for _ in baseline_list if _ > 9000))


#%%

# =============================================================================
# Cell 16: Compute correlation matrix and p-values for qmi and mean rating
# =============================================================================

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

dm_IF_qmi = dm_IF_short
dm_IF_qmi.visual_qmi = ""

subject_list = []

for index, subject in enumerate(dm_IF_qmi.subject_id):
    for index_qmi, subject_qmi in enumerate(df_qmi.subject):
        if subject_qmi == subject[-4:]:
            qmi_value = df_qmi.loc[index_qmi,'visual_qmi']
        
    dm_IF_qmi.visual_qmi[index] = qmi_value
    
df_IF_qmi = convert.to_pandas(dm_IF_qmi)

r, p = stats.pearsonr(df_IF_qmi["rating"],df_IF_qmi["visual_qmi"])
print("r=", r, ", p=",p)

mu = np.mean(df_IF_qmi["rating"])
sd = np.std(df_IF_qmi["rating"])/np.sqrt(len(df_IF_qmi))
print("mu=", mu, ", sd=",sd)


df_IF_qmi.to_excel(out_of_git_path_IF + '\\IF_tables\\qmi_rating_IF.xlsx')

#%%
#%%

# =============================================================================
# More features...  
# ============================================================================= 

#%%
#%%

list_of_blinks = []
dm_IF_blinks = []

for index, blinks in enumerate(dm_IF.blinkstlist):
    new_blinks = blinks - dm_IF.t_onset_baseline[index]
    dm_IF_blinks.append(new_blinks)
    
dm_IF.actual_blinkstlist = list_of_blinks

# Plot results
plt.figure(figsize = FIGSIZE)
plt.hist(dm_IF.actual_blinkstlist)
plt.ylabel("Number of blinks")
plt.xlabel("Time")
plt.title("Blink repartition")
plt.show()

#%%

# Create dataframe with mean pupil size during imagery

dic_imagery = []

for index_pupil, pupil_size in enumerate(dm_IF.imagery):
    dic_imagery.append(
        {'mean_pupil_size' : np.nanmean(pupil_size),
        'stim_color' : dm_IF.stim_color[index_pupil],
        'rating' : dm_IF.rating[index_pupil]
        }
    )

df = pd.DataFrame(dic_imagery)
print(df)
df.to_excel(out_of_git_path_IF + '\\IF_tables\\mean_pupil_imag.xlsx')

    
#%%

# Create mastersheet and export it to csv 
dic_all = []
for index_trial, trial in enumerate(dm_IF.trial_id):
    print(f'{index_trial}/{len(dm_IF.trial_id)}')
    for ms_trial, pupil_size in enumerate(dm_IF.pupil[index_trial]):
        # Determine in which phase we are in
        if ms_trial <= baseline_length_IF:
            phase = "baseline"
        elif ms_trial <= baseline_length_IF + imagery_length_IF:
            phase = "imagery"
        elif ms_trial <= baseline_length_IF + imagery_length_IF + rest_1_length_IF:
            phase = "rest_1"
        elif ms_trial <= baseline_length_IF + imagery_length_IF + rest_1_length_IF + stim_length_IF:
            phase = "perception"
        elif ms_trial <= pupil_length_IF:
            phase = "rest_2"

            
            
        dic_all.append(
            {'subject_id' : dm_IF.subject_id[index_trial],
            'subject_session' : dm_IF.subject_session[index_trial],
            'exp_date' : dm_IF.exp_date[index_trial],
            'exp_name' : dm_IF.exp_name[index_trial],
            'trial_id' : trial,
            'phase' : phase,
            'time' : ms_trial,            
            'pupil_size' : pupil_size,
            'stim_color' : dm_IF.stim_color[index_trial],
            'stim_orientation' : dm_IF.stim_orientation[index_trial],
            'rating' : dm_IF.rating[index_trial],
            'framerate' : dm_IF.framerate[index_trial],
            'screen_size' : dm_IF.screen_size[index_trial],
            'background_lum' : dm_IF.background_lum[index_trial],
            'rest_lum_1' : dm_IF.rest_lum_1[index_trial],
            'rest_lum_2' : dm_IF.rest_lum_2[index_trial],
            'fix_cross_lum' : dm_IF.fix_cross_lum[index_trial]
            }
        )

print("Creating a dataframe with all data...")
mastersheet_IF = pd.DataFrame(dic_all)

print(mastersheet_IF)

mastersheet_IF.to_csv(out_of_git_path_IF + '\\IF_tables\\mastersheet_IF.csv')



#%%

# Create a simplified mastersheet to have 2 rows (one per condition) per subject  
# by computing the mean pupil sizes per phase


dic_summary = []
subject_list = []

for subject in dm_IF.subject_id:
    if subject not in subject_list:
        subject_list.append(subject)
        subject_nb = len(subject_list)
        dm_IF_subj =  dm_IF.subject_id == {subject}

        for stim_color, _dm_IF_subj in ops.split(dm_IF_subj.stim_color):

            dic_summary.append(
                {'subject_id' : subject,
                'mean_pupil_size_baseline' : np.nanmean(_dm_IF_subj.baseline),
                'mean_pupil_size_imagery' : np.nanmean(list(map(lambda x: x[2000:], _dm_IF_subj.imag))), # Don't take the first 2000ms
                'mean_pupil_size_rest_1' : np.nanmean(list(map(lambda x: x[2000:], _dm_IF_subj.rest_1))), # Don't take the first 2000ms
                'mean_pupil_size_perception' : np.nanmean(list(map(lambda x: x[2000:], _dm_IF_subj.stim))), # Don't take the first 2000ms
                'mean_pupil_size_rest_2' : np.nanmean(list(map(lambda x: x[2000:], _dm_IF_subj.rest_2))), # Don't take the first 2000ms
                'stim_color' : stim_color,
                'rating_1' : len(_dm_IF_subj.rating == 1),
                'rating_2' : len(_dm_IF_subj.rating == 2),
                'rating_3' : len(_dm_IF_subj.rating == 3),
                'rating_4' : len(_dm_IF_subj.rating == 4),
                'median_rating' : np.median(_dm_IF_subj.rating)
                }
            )

subject_recap = pd.DataFrame(dic_summary)

print(subject_recap)

subject_recap.to_excel(out_of_git_path_IF + '\\IF_tables\\subject_recap_IF.xlsx')

