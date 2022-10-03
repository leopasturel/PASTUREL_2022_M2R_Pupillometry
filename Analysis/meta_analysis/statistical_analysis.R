# Import library
library(dplyr)
library(readxl)

# Import datasets
KR_df <- read_excel("C:/Users/lepas/stuffs/University/Master/M2 sciences co/S2 Stage aphantasie/Experiment/KR_tables/subject_recap_KR_ANOVA.xlsx")
IF_df <- read_excel("C:/Users/lepas/stuffs/University/Master/M2 sciences co/S2 Stage aphantasie/Experiment/IF_tables/subject_recap_IF_ANOVA.xlsx")


shapiro.test(KR_df$B_mean_pupil_size_baseline_500ms)
shapiro.test(KR_df$B_mean_pupil_size_perception_1000ms)
shapiro.test(KR_df$B_mean_pupil_size_rest_1000ms)
shapiro.test(KR_df$B_mean_pupil_size_imagery_4000ms)

shapiro.test(IF_df$B_mean_pupil_size_baseline_500ms)
shapiro.test(IF_df$B_mean_pupil_size_imagery_4000ms)
shapiro.test(IF_df$B_mean_pupil_size_rest1_1000ms)
shapiro.test(IF_df$B_mean_pupil_size_perception_1000ms)
shapiro.test(IF_df$B_mean_pupil_size_rest2_1000ms)
