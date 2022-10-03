This is the folder containing the Perception First (PF) experiment. This experiment is also reffered to as "KR" for "Kay Replication since it is inpired by Kay et al. (2022)


# SUBFOLDERS
In the subfolder "conditions", you will find the different excel file required to run the experiment.
In the subfolder "data", data will be recorded as EXPFILES. Use an edf2asc converter (available on the SR-Reseearch website) to convert them in .asc. ASCFILES are required to run analysis.


# THIS EXPERIMENT
In this experiment, participants have to look at the center of the screen. At the beginning, they will have to look at a triangle.
Then, there will be a resting phase where they should keep looking at the center of the screen.
When they hear an auditory cue, they should try visualising the triangle they have seen previously until the second auditory cue. 
At the end of each trial, they will be asked to report on the vividness of their imagery on scale 1-4.

A short version of the experiment with fewer trials is available with the suffix "_short"

The protocol of the experiment is presented in the PowerPoint file and has been used to explain the experiment to our participants.


# CREATE EXPERIMENT
Experiments are created with PsychoPy builder. 
Once done, click on "Compile to Python script". A Python file will be created in this folder with the same name.
Open and run "psyexp_to_py_KR.py". This will add messages in your code to use when analysing data and other important material. The file to modify can be specified in the "filename" variable.
Your final versi on will be compiled with the "final_" prefix.
You can now run it with PsychoPy runner.


# NOTE
The "psyexp_to_py_KR.py" file has been created specifically for the current experiment. It should be checked whenever the PsychoPy file is modified.


# BIBLIOGRAPHY
Kay L, Keogh R, Andrillon T, Pearson J. The pupillary light response as a physiological index of aphantasia, sensory and phenomenological imagery strength. eLife. 2022 Mar; 11:e72484.
https://elifesciences.org/articles/72484, doi: 10.7554/eLife.72484