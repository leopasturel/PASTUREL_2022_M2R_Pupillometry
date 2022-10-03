# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 14:20:07 2022

@author: Léo PASTUREL
"""
# Import libraries
import pandas as pd
import os
import inspect

### GET DIRECTORIES ###
# Get full actual file path
actual_file_path = inspect.getframeinfo(inspect.currentframe()).filename
# Get parent folder path
path_QMI = os.path.dirname(os.path.abspath(actual_file_path))
full_path_QMI= os.path.join(path_QMI, 'qmi_results.xlsx')

# Import csv with QMI results
df = pd.read_excel(full_path_QMI)

# Keep only results from my experience
df = df[df['Q00EXPE'] == 'KAY']


# Create list with questions corresponding to senses
visual_qmi = ["QMIQ02[QMI01]", "QMIQ02[QMI02]", "QMIQ02[QMI03]", "QMIQ02[QMI04]", "QMIQ02[QMI05]"]
audio_qmi = ["QMIQ03[QMI06]", "QMIQ03[QMI07]", "QMIQ03[QMI08]", "QMIQ03[QMI09]", "QMIQ03[QMI10]"]
tactile_qmi = ["QMIQ04[QMI11]", "QMIQ04[QMI12]", "QMIQ04[QMI13]", "QMIQ04[QMI14]", "QMIQ04[QMI15]"]
proprioception_qmi = ["QMIQ05[QMI16]", "QMIQ05[QMI17]", "QMIQ05[QMI18]", "QMIQ05[QMI19]", "QMIQ05[QMI20]"]
gustatory_qmi = ["QMIQ06[QMI21]", "QMIQ06[QMI22]", "QMIQ06[QMI23]", "QMIQ06[QMI24]", "QMIQ06[QMI25]"]
olfaction_qmi = ["QMIQ07[QMI26]", "QMIQ07[QMI27]", "QMIQ07[QMI28]", "QMIQ07[QMI29]", "QMIQ07[QMI30]"]
feeling_qmi = ["QMIQ08[QMI31]", "QMIQ08[QMI32]", "QMIQ08[QMI33]", "QMIQ08[QMI34]", "QMIQ08[QMI35]"]
global_qmi = visual_qmi + audio_qmi + tactile_qmi + proprioception_qmi + gustatory_qmi + olfaction_qmi + feeling_qmi

# Create list to store all results per subject
sum_qmi_all = []

# Put results in a dictionnary
for row in df.index:
    # if df.loc[row, 'Q00PARTICIPANT'] != "S005" and df.loc[row, 'Q00PARTICIPANT'] != "S035" and df.loc[row, 'Q00PARTICIPANT'] != "S035":  
    if df[visual_qmi].sum(axis=1)[row] <= 15:
        aphant = 1
    else:
        aphant = 0
        
    sum_qmi_all.append(
        {'subject' : df.loc[row, 'Q00PARTICIPANT'],
        'visual_qmi' : df[visual_qmi].sum(axis=1)[row],
        'audio_qmi' : df[audio_qmi].sum(axis=1)[row],
        'tactile_qmi' : df[tactile_qmi].sum(axis=1)[row],
        'proprioception_qmi' : df[proprioception_qmi].sum(axis=1)[row],
        'gustatory_qmi' : df[gustatory_qmi].sum(axis=1)[row],
        'olfaction_qmi' : df[olfaction_qmi].sum(axis=1)[row],
        'feeling_qmi' : df[feeling_qmi].sum(axis=1)[row],
        'global_qmi' : df[global_qmi].sum(axis=1)[row],
        'self_aphant' : df.loc[row, 'Q05Aphant'],
        'age' : df.loc[row, 'Q02Age'],
        'sex' : df.loc[row, 'Q03Sex'],
        'vision' : df.loc[row, 'Q04Vision'],
        'images_in_dream' : df.loc[row, 'Q07Unvoluntary'],
        'changes_imagery' : df.loc[row, 'Q08Change'],
        'aphant' : aphant
        }
    )
    
    
df_qmi_all = pd.DataFrame(sum_qmi_all)

df_qmi_all.to_csv(path_QMI + '/qmi_results_summary.csv')


#%%

# =============================================================================
# Plot density
# =============================================================================

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize = (10,5))
plt.hist(df_qmi_all.visual_qmi, bins=35, cumulative = False, label = "Repartition per score")
# plt.hist(df_qmi_all.visual_qmi, bins=35, histtype = "step", cumulative = True, label = "Cumulative repartition per score")
plt.title("Visual QMI repartition in our population")
plt.xlabel("Visual QMI results")
plt.ylabel("Number of subjects")
plt.legend(loc = "upper left")


plt.figure(figsize = (10,5))
plt.xlim(4.5,35.5)
sns.histplot(df_qmi_all.visual_qmi, color = "black", kde = True, bins = 35)
plt.title("Visual QMI repartition in our population")
plt.xlabel("Visual QMI results")
plt.ylabel("Number of subjects")
plt.savefig(path_QMI + '/visual_QMI_repartition.png')






