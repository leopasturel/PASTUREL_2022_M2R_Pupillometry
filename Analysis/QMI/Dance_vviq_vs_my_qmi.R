library(haven)
library(readr)

# Import an analyse Dance results
AphantasiaPrevalenceData <- read_sav("C:/Users/lepas/Downloads/AphantasiaPrevalenceData.sav")

summary(AphantasiaPrevalenceData$VVIQ1) # 57.67928 / 80 = 0.720991
sd(AphantasiaPrevalenceData$VVIQ1) # 12.35229 / 80 = 0.1544036
median(AphantasiaPrevalenceData$VVIQ1) # 58 /80 = 0.725

# Import and analyse my results
QMI_df <- read_csv("C:/Users/lepas/stuffs/University/Master/M2 sciences co/S2 Stage aphantasie/Experiment/pupillometry_M2SCCO/Analysis/QMI/qmi_results_summary.csv")

mean(QMI_df$visual_qmi) # 26.33929 / 35 = 0.752551
sd(QMI_df$visual_qmi) # 5.756504 / 35 = 0.1644715
median(QMI_df$visual_qmi) # 27 / 35 = 0.7714286


# Compute skewness and Kurtosis of our data 
# From: https://www.statology.org/skewness-kurtosis-in-r/
library(moments)

#calculate skewness
skewness(QMI_df$visual_qmi) # -1.253454. i.e. it is left-skewed (as expected from the histogram) because it' is less than 0's negative.
skewness(AphantasiaPrevalenceData$VVIQ1) # -0.6482093. i.e. it is left-skewed (as expected from the histogram) because it' is less than 0's negative.


#calculate kurtosis
kurtosis(QMI_df$visual_qmi) # 5.582261. Greater than 3 so more values in the tails than normal distribution
kurtosis(AphantasiaPrevalenceData$VVIQ1) # 3.809917. Greater than 3 so more values in the tails than normal distribution


# Perform Jarque test to see if our data matches a normal distribution with H0: matches; H1: doesn't match
jarque.test(QMI_df$visual_qmi) # JB = 31.302, p-value = 1.595e-07. We can reject the null hypothesis.
jarque.test(AphantasiaPrevalenceData$VVIQ1[1:1004]) # JB = 97.751, p-value < 2.2e-16. We can reject the null hypothesis.

