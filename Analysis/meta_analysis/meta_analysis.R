# Import libraries
library(readxl)
library(readr)
library(beanplot)
library(tidyverse)
library(dplyr) #might need plyr for revalue function
library(ggpmisc)
library(patchwork)
library(rstatix)


library(ggpmisc)
# Import datasets 
KR_df <- read_excel("C:/Users/lepas/stuffs/University/Master/M2 sciences co/S2 Stage aphantasie/Experiment/KR_tables/subject_recap_KR_regress.xlsx")
IF_df <- read_excel("C:/Users/lepas/stuffs/University/Master/M2 sciences co/S2 Stage aphantasie/Experiment/IF_tables/subject_recap_IF_regress.xlsx")
QMI_df <- read_csv("C:/Users/lepas/stuffs/University/Master/M2 sciences co/S2 Stage aphantasie/Experiment/pupillometry_M2SCCO/Analysis/QMI/qmi_results_summary.csv")

# Create new columns with n random variables for the beanplots (n = Nbr of phase)
KR_df$phase_KR_random <- sample(1:4,replace=T, size = nrow(KR_df))
IF_df$phase_IF_random <- sample(1:5,replace=T, size = nrow(IF_df))

# Create sub-datasets with only mean ratings > 2 or mean rating > 3
KR_df_2 <- KR_df %>%
  filter(mean_rating > 2)
KR_df_3 <- KR_df %>%
  filter(mean_rating > 3)

IF_df_2 <- IF_df %>%
  filter(mean_rating > 2)
IF_df_3 <- IF_df %>%
  filter(mean_rating > 3)


## Comparing data against themselves ##
# Create a beanplot that compares pupil diameter during of different phases in both conditions for KR
par(mfrow = c(1,1))

# Create the beanplot frame
allplot <- beanplot(mean_pupil_size_perception_1000ms ~ phase_KR_random, data = KR_df_3, 
                    what=c(F,F,F,F), show.names=F, ylim = c(0.45,1.5),
                    main = "Beanplot of mean pupil diameter during\ndifferent phases of KR", 
                    xlab = "Phase", ylab = "Mean pupil diameter (Normalized)")

# Add the baseline phase
beanplot(mean_pupil_size_baseline_500ms ~ stim_color, data = KR_df_3, 
         boxwex = 0.4, at = 1, add = TRUE, names = "baseline",
         what=c(T,T,T,F), side = "b", col = list("grey20", "grey90"),
         bw = allplot$bw, wd = allplot$wd, beanlines = "quantiles")

# Add the perception phase
beanplot(mean_pupil_size_perception_1000ms ~ stim_color, data = KR_df_3, 
         boxwex = 0.4, at = 2, add = TRUE, names = "perception",
         what=c(F,T,T,F), side = "b", col = list("grey20", "grey90"),
         bw = allplot$bw, wd = allplot$wd, beanlines = "quantiles")

# Add the rest phase
beanplot(mean_pupil_size_rest_1000ms ~ stim_color, data = KR_df_3, 
         boxwex = 0.4, at = 3, add = TRUE, names = "rest",
         what=c(F,T,T,F), side = "b", col = list("grey20", "grey90"),
         bw = allplot$bw, wd = allplot$wd, beanlines = "quantiles")

# Add the imagery phase
beanplot(mean_pupil_size_imagery_4000ms ~ stim_color, data = KR_df_3, 
         boxwex = 0.4, at = 4, add = TRUE, names = "imagery",
         what=c(F,T,T,F), side = "b", col = list("grey20", "grey90"),
         bw = allplot$bw, wd = allplot$wd, beanlines = "quantiles")

# Add the legend
legend("bottomleft", bty="n",c("Dark condition", "Bright condition"),
       fill = c("black", "lightgrey"))



# Create a beanplot that compares mean rating and pupil diameter during imagination for KR




# Some random help and more

allplot <- beanplot(len ~ dose+supp, data = ToothGrowth, 
                    what=c(TRUE,FALSE,FALSE,FALSE),show.names=FALSE,ylim=c(-1,40), yaxs = "i")
beanplot(len ~ dose, data = ToothGrowth, add=TRUE,
         boxwex = 0.6, at = 1:3*2 - 0.9,
         subset = supp == "VC", col = "yellow",border="yellow2",
         main = "Guinea Pigs' Tooth Growth",
         xlab = "Vitamin C dose mg",
         ylab = "tooth length", ylim = c(3, 40), yaxs = "i",
         bw = allplot$bw, wd = allplot$wd, what = c(FALSE,TRUE,TRUE,TRUE))
beanplot(len ~ dose, data = ToothGrowth, add = TRUE,
         boxwex = 0.6, at = 1:3*2-0.1,
         subset = supp == "OJ", col = "orange",border="darkorange",
         bw = allplot$bw, wd = allplot$wd, what = c(FALSE,TRUE,TRUE,TRUE))
legend("bottomright", bty="n", c("Ascorbic acid", "Orange juice"),
       fill = c("yellow", "orange"))



#Comparison of mean pupil size during perception
ggplot() +
  geom_point(aes(x = QMI_df$visual_qmi[c(-1, -19)],
                  y = (KR_df %>% filter(stim_color == "black"))$mean_rating, color = "black")) +
  geom_smooth(aes(x = QMI_df$visual_qmi[c(-1, -19)],
                  y = (KR_df %>% filter(stim_color == "black"))$mean_rating, color = "black"),
              formula = 'y~x', method = 'lm', se = F) +
  geom_point(aes(x = QMI_df$visual_qmi[c(-1, -19)],
                  y = (KR_df %>% filter(stim_color == "white"))$mean_rating, color = "white")) +
  geom_smooth(aes(x = QMI_df$visual_qmi[c(-1, -19)],
                  y = (KR_df %>% filter(stim_color == "white"))$mean_rating, color = "white"),
              formula = 'y~x', method = 'lm', se = F) +
  # Add annotations
  stat_poly_eq(aes(x = QMI_df$visual_qmi[c(-1, -19)], y = (KR_df %>% filter(stim_color == "white"))$mean_rating,
                   label = paste(..eq.label.., sep = "~~~")), 
               label.x.npc = "right", label.y.npc = 0.1,
               eq.with.lhs = "italic(y)~`=`~",
               eq.x.rhs = "~italic(x)",
               formula = 'y~x', parse = TRUE, size = 4, color = "grey75") +
  stat_poly_eq(aes(x = QMI_df$visual_qmi[c(-1, -19)], y = (KR_df %>% filter(stim_color == "white"))$mean_rating,
                   label = paste(..rr.label.., sep = "~~~")), 
               label.x.npc = "right", label.y.npc = "bottom",
               formula = 'y~x', parse = TRUE, size = 4, color = "grey75") +
  
  stat_poly_eq(aes(x = QMI_df$visual_qmi[c(-1, -19)], y = (KR_df %>% filter(stim_color == "black"))$mean_rating,
                   label = paste(..eq.label.., sep = "~~~")), 
               label.x.npc = "left", label.y.npc = 0.9,
               eq.with.lhs = "italic(y)~`=`~",
               eq.x.rhs = "~italic(x)",
               formula = 'y~x', parse = TRUE, size = 4, color = "grey20") +
  stat_poly_eq(aes(x = QMI_df$visual_qmi[c(-1, -19)], y = (KR_df %>% filter(stim_color == "black"))$mean_rating,
                   label = paste(..rr.label.., sep = "~~~")), 
               label.x.npc = "left", label.y.npc = 0.85,
               formula = 'y~x', parse = TRUE, size = 4, color = "grey20") +
  
  geom_jitter(width = 0.1) +
  theme_bw() +
  ylim(0.9,4.1) +
  labs(title = "Comparison of rating during experiment and visual QMI", x = "Visual QMI", y = "Mean rating") +
  scale_color_manual(name='Conditions',
                     breaks=c('black', 'white'),
                     values=c('black'='grey20', 'white'='grey75'),
                     labels = c("Black", "White")) + 
  theme(legend.position = "right")
#Correlates with subjects reporting having difficulties to image during the experiment.

################################################################################
# Becoming a draft of the markdown

# Keep only the subjects that rated more than 3 in average in both conditions

keep_double <- function(df){
  previous_subj_id <- ""
  list_double <- list()
  
  for (subject in df$subject_id) {
    
    if (previous_subj_id == subject) {
      list_double <- list_double[-length(list_double)]
      list_double <- append(list_double, "both")
      list_double <- append(list_double, "both")
    }
    else {
      list_double <- append(list_double, "single")
    }
    previous_subj_id <- subject
  }
  print(list_double)
  df$both <- list_double
  
  df_both <- df %>%
    filter(both == "both")
  
  return(df_both)
}

KR_df_3_both = keep_double(KR_df_3)

# Drawing path&dot plot
ggplot(KR_df_3_both, aes(x=stim_color, y=mean_pupil_size_imagery_4000ms)) +
  geom_path(aes(color = subject_id, group = factor(subject_id))) +
  geom_dotplot(aes(fill = subject_id), binaxis="y", binwidth = .01, stackdir = "centerwhole") +
  
  geom_segment(aes(x = "black", y = mean((KR_df_3_both %>% filter(stim_color == "black"))$mean_pupil_size_imagery_4000ms),
                   xend = "white", yend = mean((KR_df_3_both %>% filter(stim_color == "white"))$mean_pupil_size_imagery_4000ms),
                   linetype="Average trend"), color = "red", size = 2) +
  scale_linetype_manual("", values=c("dashed")) +
  theme_bw() +
  labs(title = "Mean pupil diameter during imagery for KR\nRating > 3", x = "Condition", 
       y = "Pupil diameter change\nfrom baseline (mm)") +
  theme(legend.position = "right")





# Repeat graph with standard deviation
# Drawing path&dot plot
ggplot(KR_df_3_both, aes(x=stim_color, y=mean_pupil_size_imagery_4000ms)) +
  geom_path(aes(color = subject_id, group = factor(subject_id))) +
  geom_dotplot(aes(fill = subject_id), binaxis="y", binwidth = .01, stackdir = "centerwhole") +
  
  geom_segment(aes(x = "black", y = mean((KR_df_3_both %>% filter(stim_color == "black"))$mean_pupil_size_imagery_4000ms),
                   xend = "white", yend = mean((KR_df_3_both %>% filter(stim_color == "white"))$mean_pupil_size_imagery_4000ms),
                   linetype="Average trend"), color = "red", size = 2) +
  
  #Add error bars  
  geom_segment(aes(x = "black", y = mean((KR_df_3_both %>% filter(stim_color == "black"))$mean_pupil_size_imagery_4000ms - sd((KR_df_3_both %>% filter(stim_color == "black"))$mean_pupil_size_imagery_4000ms)/sqrt(length((KR_df_3_both %>% filter(stim_color == "black"))$mean_pupil_size_imagery_4000ms))),
                   xend = "black", yend = mean((KR_df_3_both %>% filter(stim_color == "black"))$mean_pupil_size_imagery_4000ms + sd((KR_df_3_both %>% filter(stim_color == "black"))$mean_pupil_size_imagery_4000ms)/sqrt(length((KR_df_3_both %>% filter(stim_color == "black"))$mean_pupil_size_imagery_4000ms)))),
               color = "red", size = 2) +
  
  geom_segment(aes(x = "white", y = mean((KR_df_3_both %>% filter(stim_color == "white"))$mean_pupil_size_imagery_4000ms - sd((KR_df_3_both %>% filter(stim_color == "black"))$mean_pupil_size_imagery_4000ms)/sqrt(length((KR_df_3_both %>% filter(stim_color == "white"))$mean_pupil_size_imagery_4000ms))),
                   xend = "white", yend = mean((KR_df_3_both %>% filter(stim_color == "white"))$mean_pupil_size_imagery_4000ms + sd((KR_df_3_both %>% filter(stim_color == "black"))$mean_pupil_size_imagery_4000ms)/sqrt(length((KR_df_3_both %>% filter(stim_color == "white"))$mean_pupil_size_imagery_4000ms)))),
               color = "red", size = 2) +
  
  geom_segment(aes(x = stim_color, y = mean_pupil_size_imagery_4000ms - std_pupil_size_imagery_4000ms,
                   xend = stim_color, yend = mean_pupil_size_imagery_4000ms + std_pupil_size_imagery_4000ms,
               color = subject_id), lineend = "square") +

  geom_segment(data = KR_df_3_both%>%filter(stim_color=="black"), 
                  aes(x = 1-0.03, y = mean_pupil_size_imagery_4000ms - std_pupil_size_imagery_4000ms,
                  xend = 1+0.03, yend = mean_pupil_size_imagery_4000ms - std_pupil_size_imagery_4000ms,
                  color = subject_id)) +
  geom_segment(data = KR_df_3_both%>%filter(stim_color=="black"), 
               aes(x = 1-0.03, y = mean_pupil_size_imagery_4000ms + std_pupil_size_imagery_4000ms,
                   xend = 1+0.03, yend = mean_pupil_size_imagery_4000ms + std_pupil_size_imagery_4000ms,
                   color = subject_id)) +
  
  geom_segment(data = KR_df_3_both%>%filter(stim_color=="white"), 
                  aes(x = 2-0.03, y = mean_pupil_size_imagery_4000ms - std_pupil_size_imagery_4000ms,
                  xend = 2+0.03, yend = mean_pupil_size_imagery_4000ms - std_pupil_size_imagery_4000ms,
                  color = subject_id)) +
  geom_segment(data = KR_df_3_both%>%filter(stim_color=="white"), 
               aes(x = 2-0.03, y = mean_pupil_size_imagery_4000ms + std_pupil_size_imagery_4000ms,
                   xend = 2+0.03, yend = mean_pupil_size_imagery_4000ms + std_pupil_size_imagery_4000ms,
                   color = subject_id)) +
  
  scale_linetype_manual("", values=c("dashed")) +
  theme_bw() +
  labs(title = "Mean pupil diameter during imagery for KR\nRating > 3", x = "Condition", 
       y = "Pupil diameter change\nfrom baseline (mm)") +
  theme(legend.position = "right")


# Looking at subject 43
ggplot(KR_df %>%filter(subject_id=="KR_S043"), aes(x=stim_color, y=mean_pupil_size_imagery_4000ms)) +
  geom_path(aes(color = subject_id, group = factor(subject_id))) +
  geom_dotplot(aes(fill = subject_id), binaxis="y", binwidth = .01, stackdir = "centerwhole") +
  
  geom_segment(aes(x = stim_color, y = mean_pupil_size_imagery_4000ms - std_pupil_size_imagery_4000ms,
                   xend = stim_color, yend = mean_pupil_size_imagery_4000ms + std_pupil_size_imagery_4000ms,
                   color = subject_id), lineend = "square") +
  
  geom_segment(data = KR_df%>%filter(stim_color=="black", subject_id == "KR_S043"), 
               aes(x = 1-0.03, y = mean_pupil_size_imagery_4000ms - std_pupil_size_imagery_4000ms,
                   xend = 1+0.03, yend = mean_pupil_size_imagery_4000ms - std_pupil_size_imagery_4000ms,
                   color = subject_id)) +
  geom_segment(data = KR_df%>%filter(stim_color=="black", subject_id == "KR_S043"), 
               aes(x = 1-0.03, y = mean_pupil_size_imagery_4000ms + std_pupil_size_imagery_4000ms,
                   xend = 1+0.03, yend = mean_pupil_size_imagery_4000ms + std_pupil_size_imagery_4000ms,
                   color = subject_id)) +
  
  geom_segment(data = KR_df%>%filter(stim_color=="white", subject_id == "KR_S043"), 
               aes(x = 2-0.03, y = mean_pupil_size_imagery_4000ms - std_pupil_size_imagery_4000ms,
                   xend = 2+0.03, yend = mean_pupil_size_imagery_4000ms - std_pupil_size_imagery_4000ms,
                   color = subject_id)) +
  geom_segment(data = KR_df%>%filter(stim_color=="white", subject_id == "KR_S043"), 
               aes(x = 2-0.03, y = mean_pupil_size_imagery_4000ms + std_pupil_size_imagery_4000ms,
                   xend = 2+0.03, yend = mean_pupil_size_imagery_4000ms + std_pupil_size_imagery_4000ms,
                   color = subject_id)) +

  theme_bw() +
  labs(title = "Mean pupil diameter during imagery for KR for subject 43", x = "Condition", y = "Pupil diameter change\nfrom baseline (mm)") +
  theme(legend.position = "right")



# Drawing path&dot plot for perception phase
ggplot(KR_df_3_both, aes(x=stim_color, y=mean_pupil_size_perception_1000ms)) +
  geom_path(aes(color = subject_id, group = factor(subject_id))) +
  geom_dotplot(aes(fill = subject_id), binaxis="y", binwidth = .01, stackdir = "centerwhole") +
  
  geom_segment(aes(x = "black", y = mean((KR_df_3_both %>% filter(stim_color == "black"))$mean_pupil_size_perception_1000ms),
                   xend = "white", yend = mean((KR_df_3_both %>% filter(stim_color == "white"))$mean_pupil_size_perception_1000ms),
                   linetype="Average trend"), color = "red", size = 2) +
  scale_linetype_manual("", values=c("dashed")) +
  theme_bw() +
  labs(title = "Mean pupil diameter during imagery for KR\nRating > 3", x = "Condition", 
       y = "Pupil diameter change\nfrom baseline (mm)") +
  theme(legend.position = "right")



#Define new df
QMI_df_radar_visual = data.frame(Group = c("General population", "Visual aphants"),
                               
                               Visual = c(mean((QMI_df %>% filter(visual_qmi > 15))$visual_qmi),mean((QMI_df %>% filter(visual_qmi <= 15))$visual_qmi)),
                               
                               Auditory = c(mean((QMI_df %>% filter(visual_qmi > 15))$audio_qmi),mean((QMI_df %>% filter(visual_qmi <= 15))$audio_qmi)),
                               
                               Tactile = c(mean((QMI_df %>% filter(visual_qmi > 15))$tactile_qmi),mean((QMI_df %>% filter(visual_qmi <= 15))$tactile_qmi)),
                               
                               Proprioception = c(mean((QMI_df %>% filter(visual_qmi > 15))$proprioception_qmi),mean((QMI_df %>% filter(visual_qmi <= 15))$proprioception_qmi)),
                               
                               Gustatory = c(mean((QMI_df %>% filter(visual_qmi > 15))$gustatory_qmi),mean((QMI_df %>% filter(visual_qmi <= 15))$gustatory_qmi)),
                               
                               Olfaction = c(mean((QMI_df %>% filter(visual_qmi > 15))$olfaction_qmi),mean((QMI_df %>% filter(visual_qmi <= 15))$olfaction_qmi)),
                               
                               Feeling = c(mean((QMI_df %>% filter(visual_qmi > 15))$feeling_qmi),mean((QMI_df %>% filter(visual_qmi <= 15))$feeling_qmi)))


# ggradar
print(ggradar(QMI_df_radar_visual,
        grid.min=5, grid.mid = 20, grid.max=35,
        values.radar = c("5", "20", "35"),
        background.circle.colour = "white",
        group.colours = c("grey80", "black"),
        gridline.min.linetype = 1,
        gridline.mid.linetype = 1,
        gridline.max.linetype = 1,
        gridline.min.colour = "gray60",
        gridline.mid.colour = "gray60",
        gridline.max.colour = "gray60",
        plot.title = "Questionnaire Upon Mental Imagery",
        # legend.title = "Group",
        legend.position = "bottom",
        fill = TRUE, fill.alpha = 0.1,
        grid.label.size = 4,
        group.line.width = 1,
        group.point.size = 4,
        axis.label.size = 5,
        axis.label.offset = 1.08
) +
  theme(
    axis.text.x=element_blank(), #remove x axis labels
    axis.ticks.x=element_blank(), #remove x axis ticks
    axis.text.y=element_blank(),  #remove y axis labels
    axis.ticks.y=element_blank(),
    plot.title = element_text(hjust = 0.5, size = 20),
    legend.text = element_text(hjust = 0.5, size = 15))
)


# Making a nice plot for paper

KR_df_wb <- KR_df
KR_df_wb$stim_color[KR_df_wb$stim_color=="white"] <- 1
KR_df_wb$stim_color[KR_df_wb$stim_color=="black"] <- 2
KR_df_wb$stim_color_j <- jitter(as.numeric(KR_df_wb$stim_color), amount = 0.05)

IF_df_wb <- IF_df
IF_df_wb$stim_color[IF_df_wb$stim_color=="white"] <- 1
IF_df_wb$stim_color[IF_df_wb$stim_color=="black"] <- 2
IF_df_wb$stim_color_j <- jitter(as.numeric(IF_df_wb$stim_color), amount = 0.05)


kr_baseline <- ggplot(KR_df_wb, aes(x = stim_color, y = mean_pupil_size_baseline_500ms)) +
  geom_boxplot(aes(color = stim_color), outlier.alpha = 0) +
  geom_path(aes(x = stim_color_j, group = factor(subject_id)), alpha = 0.7, colour = "grey70") +
  geom_point(aes(x = stim_color_j, color = stim_color), alpha = 0.3) +
  theme_bw() +
  ylim(0.6, 1.31) + 
  scale_color_manual(labels = c("White", "Black"), values = c("mediumblue", "red2")) +
  scale_x_discrete(labels = c("White", "Black")) +
  labs(title = "Baseline", y = "Pupil diameter change\nfrom baseline") +
  theme(legend.position = "NULL")

kr_perception <- ggplot(KR_df_wb, aes(x = stim_color, y = mean_pupil_size_perception_1000ms)) +
  geom_boxplot(aes(color = stim_color), outlier.alpha = 0) +
  geom_path(aes(x = stim_color_j, group = factor(subject_id)), alpha = 0.7, colour = "grey70") +
  geom_point(aes(x = stim_color_j, color = stim_color), alpha = 0.3) +
  theme_bw() +
  ylim(0.6, 1.31) + 
  scale_color_manual(labels = c("White", "Black"), values = c("mediumblue", "red2")) +
  scale_x_discrete(labels = c("White", "Black")) +
  labs(title = "Perception", y = "Pupil diameter change\nfrom baseline") +
  theme(legend.position = "NULL")

kr_imagery <- ggplot(KR_df_wb, aes(x = stim_color, y = mean_pupil_size_imagery_4000ms)) +
  geom_boxplot(aes(color = stim_color), outlier.alpha = 0) +
  geom_path(aes(x = stim_color_j, group = factor(subject_id)), alpha = 0.7, colour = "grey70") +
  geom_point(aes(x = stim_color_j, color = stim_color), alpha = 0.3) +
  theme_bw() +
  ylim(0.6, 1.31) + 
  scale_color_manual(labels = c("White", "Black"), values = c("mediumblue", "red2")) +
  scale_x_discrete(labels = c("White", "Black")) +
  labs(title = "Imagery", y = "Pupil diameter change\nfrom baseline") +
  theme(legend.position = "NULL")

kr_rest <- ggplot(KR_df_wb, aes(x = stim_color, y = mean_pupil_size_rest_1000ms)) +
  geom_boxplot(aes(color = stim_color), outlier.alpha = 0) +
  geom_path(aes(x = stim_color_j, group = factor(subject_id)), alpha = 0.7, colour = "grey70") +
  geom_point(aes(x = stim_color_j, color = stim_color), alpha = 0.3) +
  theme_bw() +
  ylim(0.6, 1.31) + 
  scale_color_manual(labels = c("White", "Black"), values = c("mediumblue", "red2")) +
  scale_x_discrete(labels = c("White", "Black")) +
  labs(title = "Rest", y = "Pupil diameter change\nfrom baseline") +
  theme(legend.position = "NULL")

remove_y <- theme(
  axis.text.y = element_blank(),
  axis.ticks.y = element_blank(),
  axis.title.y = element_blank()
)

remove_x <- theme(axis.title.x = element_blank())

p = list(kr_baseline + remove_x,
         kr_perception + remove_y + remove_x,
         kr_rest + remove_y + remove_x,
         kr_imagery + remove_y + remove_x)

wrap_plots(p, nrow = 1) + plot_layout(guides = "collect")



IF_baseline <- ggplot(IF_df_wb, aes(x = stim_color, y = mean_pupil_size_baseline_500ms)) +
  geom_boxplot(aes(color = stim_color), outlier.alpha = 0) +
  geom_path(aes(x = stim_color_j, group = factor(subject_id)), alpha = 0.7, colour = "grey70") +
  geom_point(aes(x = stim_color_j, color = stim_color), alpha = 0.3) +
  theme_bw() +
  ylim(0.6, 1.31) + 
  scale_color_manual(labels = c("White", "Black"), values = c("mediumblue", "red2")) +
  scale_x_discrete(labels = c("White", "Black")) +
  labs(title = "Baseline", y = "Pupil diameter change\nfrom baseline") +
  theme(legend.position = "NULL")

IF_perception <- ggplot(IF_df_wb, aes(x = stim_color, y = mean_pupil_size_perception_1000ms)) +
  geom_boxplot(aes(color = stim_color), outlier.alpha = 0) +
  geom_path(aes(x = stim_color_j, group = factor(subject_id)), alpha = 0.7, colour = "grey70") +
  geom_point(aes(x = stim_color_j, color = stim_color), alpha = 0.3) +
  theme_bw() +
  ylim(0.6, 1.31) + 
  scale_color_manual(labels = c("White", "Black"), values = c("mediumblue", "red2")) +
  scale_x_discrete(labels = c("White", "Black")) +
  labs(title = "Perception", y = "Pupil diameter change\nfrom baseline") +
  theme(legend.position = "NULL")

IF_imagery <- ggplot(IF_df_wb, aes(x = stim_color, y = mean_pupil_size_imagery_4000ms)) +
  geom_boxplot(aes(color = stim_color), outlier.alpha = 0) +
  geom_path(aes(x = stim_color_j, group = factor(subject_id)), alpha = 0.7, colour = "grey70") +
  geom_point(aes(x = stim_color_j, color = stim_color), alpha = 0.3) +
  theme_bw() +
  ylim(0.6, 1.31) + 
  scale_color_manual(labels = c("White", "Black"), values = c("mediumblue", "red2")) +
  scale_x_discrete(labels = c("White", "Black")) +
  labs(title = "Imagery", y = "Pupil diameter change\nfrom baseline") +
  theme(legend.position = "NULL")

IF_rest1 <- ggplot(IF_df_wb, aes(x = stim_color, y = mean_pupil_size_rest1_1000ms)) +
  geom_boxplot(aes(color = stim_color), outlier.alpha = 0) +
  geom_path(aes(x = stim_color_j, group = factor(subject_id)), alpha = 0.7, colour = "grey70") +
  geom_point(aes(x = stim_color_j, color = stim_color), alpha = 0.3) +
  theme_bw() +
  ylim(0.6, 1.31) + 
  scale_color_manual(labels = c("White", "Black"), values = c("mediumblue", "red2")) +
  scale_x_discrete(labels = c("White", "Black")) +
  labs(title = "Rest 1", y = "Pupil diameter change\nfrom baseline") +
  theme(legend.position = "NULL")

IF_rest2 <- ggplot(IF_df_wb, aes(x = stim_color, y = mean_pupil_size_rest2_1000ms)) +
  geom_boxplot(aes(color = stim_color), outlier.alpha = 0) +
  geom_path(aes(x = stim_color_j, group = factor(subject_id)), alpha = 0.7, colour = "grey70") +
  geom_point(aes(x = stim_color_j, color = stim_color), alpha = 0.3) +
  theme_bw() +
  ylim(0.6, 1.31) + 
  scale_color_manual(labels = c("White", "Black"), values = c("mediumblue", "red2")) +
  scale_x_discrete(labels = c("White", "Black")) +
  labs(title = "Rest 2", y = "Pupil diameter change\nfrom baseline") +
  theme(legend.position = "NULL")

remove_y <- theme(
  axis.text.y = element_blank(),
  axis.ticks.y = element_blank(),
  axis.title.y = element_blank()
)

remove_x <- theme(axis.title.x = element_blank())

p = list(IF_baseline + remove_x,
         IF_imagery + remove_y + remove_x,
         IF_rest1 + remove_y + remove_x,
         IF_perception + remove_y + remove_x,
         IF_rest2 + remove_y + remove_x
)

wrap_plots(p, nrow = 1) + plot_layout(guides = "collect")



# THAT'S DONE

#Let's do some more

KR_df_w <- KR_df %>%
  filter(stim_color == "white")
KR_df_b <- KR_df %>%
  filter(stim_color == "black")
KR_df_dif_imag <- KR_df_b$mean_pupil_size_imagery_4000ms - KR_df_w$mean_pupil_size_imagery_4000ms
KR_df_mean_rating <- (KR_df_w$mean_rating + KR_df_b$mean_rating) /2

IF_df_w <- IF_df %>%
  filter(stim_color == "white")
IF_df_b <- IF_df %>%
  filter(stim_color == "black")
IF_df_dif_imag <- IF_df_b$mean_pupil_size_imagery_4000ms - IF_df_w$mean_pupil_size_imagery_4000ms
IF_df_mean_rating <- (IF_df_w$mean_rating + IF_df_b$mean_rating) /2



ggplot(KR_df, aes(x = mean_rating, y = mean_pupil_size_imagery_4000ms, color = subject_id)) +
  geom_point(aes(shape = stim_color)) +
  geom_path(aes(group = factor(subject_id)), alpha = 0.7) +
  theme_bw() +
  xlim(1,4) +
  labs(title = "Pupil diameter during imagery depending on mean rating during PF", x = "Mean rating",
       y = "Pupil diameter (normalized)") 

# Subjects to remove
visual_QMI_for_KR = QMI_df$visual_qmi[c(-1, -8, -35, -36, -45, -50, -53)]
visual_QMI_for_IF = QMI_df$visual_qmi[c(-1, -8, -25, -35, -36, -45, -50, -53)]

ggplot() +
  geom_point(aes(x = visual_QMI_for_KR, y = KR_df_dif_imag), color = "black") +
  geom_smooth(aes(x = visual_QMI_for_IF, y = IF_df_dif_imag), method = "lm", se = F, color = "black") +
  theme_bw() +
  ylim(-0.10, 0.15) +
  xlim(15,35) +
  labs(title = "Pupil diameter difference during imagery during PF", x = "Visual QMI scores",
       y = "Difference in pupil diameter") 

ggplot() +
  geom_point(aes(x = visual_QMI_for_IF, y = IF_df_dif_imag), color = "black") +
  geom_smooth(aes(x = visual_QMI_for_IF, y = IF_df_dif_imag), method = "lm", se = F, color = "black") +
  theme_bw() +
  ylim(-0.10, 0.15) +
  xlim(15,35) +
  labs(title = "Pupil diameter difference during imagery during IF", x = "Visual QMI scores",
       y = "Difference in pupil diameter")



rq_pf <- ggplot() +
  geom_point(aes(x = visual_QMI_for_KR, y = KR_df_mean_rating, color = KR_df_w$subject_id)) +
  theme_bw() +
  ylim(1,4) +
  xlim(15,35) +
  labs(title = "Self reported visual imagery in PF", x = "Visual QMI", y = "Mean rating")
  
rq_if <- ggplot() +
  geom_point(aes(x = visual_QMI_for_IF, y = IF_df_mean_rating, color = IF_df_w$subject_id)) +
  theme_bw() +
  ylim(1,4) +
  xlim(15,35) +
  labs(title = "Self reported visual imagery in IF", x = "Visual QMI", y = "Mean rating")


p = list(rq_pf ,
         rq_if + remove_y
)

wrap_plots(p, nrow = 1) + plot_layout(guides = "collect")


## Plot mean rating of both experiments against QMI in one plot

# #Remove participant that is in KR but not IF
visual_QMI_for_KR_2 <- QMI_df$visual_qmi[c(-1, -8, -25, -35, -36, -45, -50, -53)]
visual_QMI_for_IF_2 <- QMI_df$visual_qmi[c(-1, -8, -25, -35, -36, -45, -50, -53)]
KR_df_mean_rating_2 <- KR_df_mean_rating[c(-23)]


##Add jitter
#visual_QMI_for_KR_2 <- jitter(as.numeric(visual_QMI_for_KR_2), amount = 0.05)
#visual_QMI_for_IF_2 <- jitter(as.numeric(visual_QMI_for_IF_2), amount = 0.05)

seed <- 42

ggplot() +
  geom_point(aes(x = visual_QMI_for_IF_2, y = IF_df_mean_rating, color = IF_df_w$subject_id, shape = "if"),
             position = position_jitter(seed = seed, width =0.2)) +
  geom_point(aes(x = visual_QMI_for_KR_2, y = KR_df_mean_rating_2, color = IF_df_w$subject_id, shape = "pf"),
             position = position_jitter(seed = seed, width =0.2)) +
  geom_segment(aes(x = visual_QMI_for_KR_2, y = KR_df_mean_rating_2,
               xend = visual_QMI_for_IF, yend = IF_df_mean_rating, color = IF_df_w$subject_id),
               arrow = arrow(), size = 0.5, alpha = 0.3,
               position = position_jitter(seed = seed, width =0.2)) +
  theme_bw() +
  scale_shape_manual(name='Experiment',
                     breaks=c('pf', 'if'),
                     values=c('pf'=16, 'if'=2),
                     labels = c("PF", "IF")) +
  guides(color = "none") +
  #ylim(1,4) +
  #xlim(15,35) +
  labs(title = "Self reported visual imagery depending on experiments", x = "Visual QMI", y = "Mean rating")


# All over again
mean_rating_qmi <- read_excel("C:/Users/lepas/stuffs/University/Master/M2 sciences co/S2 Stage aphantasie/Experiment/mean_rating&qmi.xlsx")



# Repeat with average mean rating every 5 QMI
ggplot(mean_rating_qmi) +
  
  geom_point(aes(x = visual_qmi, y = (rating_if + rating_kr)/2, color = subject_id, shape = stim_color),
             position = position_jitter(seed = seed, width =0.3)) +
  #geom_point(aes(x = visual_qmi, y = rating_kr, color = subject_id, shape = stim_color),
  #           position = position_jitter(seed = seed, width =0.3)) +
  
  #geom_segment(aes(x = visual_qmi, y = rating_kr,
  #                 xend = visual_qmi, yend = rating_if, color = subject_id),
  #             arrow = arrow(), size = 0.5, alpha = 0.3,
  #             position = position_jitter(seed = seed, width =0.2)) +
  
  #geom_segment(aes(x = visual_qmi, y = rating_kr,
  #                 xend = visual_qmi, yend = rating_if, color = subject_id),
  #             arrow = arrow(), size = 0.5, alpha = 0.3,
  #             position = position_jitter(seed = seed, width =0.2)) +

  theme_bw() +
  ylim(0.9,4.1) +
  xlim(15,35.2) +
  labs(title = "Self reported visual imagery", x = "Visual QMI", y = "Mean rating")


# Rating vs pupil dif
ggplot() +
  geom_point(aes(x = KR_df_mean_rating, y = KR_df_dif_imag, color = 'indiv'))+
  geom_point(aes(x = mean(KR_df_mean_rating), y = mean(KR_df_dif_imag), color = 'mean')) +
  theme_bw() +
  xlim(1,4) +
  ylim(-0.10,0.15) +
  scale_color_manual(name='',
                     breaks=c('indiv', 'mean'),
                     values=c('indiv'='black', 'mean'='red'),
                     labels = c("Participants", "Average")) +
  labs(title = "Difference in pupil diameter during imagery during PF", x = "Mean rating", y = "Pupil diameter difference between conditions") 

ggplot() +
  geom_point(aes(x = IF_df_mean_rating, y = IF_df_dif_imag, color = 'indiv')) +
  geom_point(aes(x = mean(IF_df_mean_rating), y = mean(IF_df_dif_imag), color = 'mean')) +
  theme_bw() +
  xlim(1,4) +
  ylim(-0.10,0.15) +
  scale_color_manual(name='',
                     breaks=c('indiv', 'mean'),
                     values=c('indiv'='black', 'mean'='red'),
                     labels = c("Participants", "Average")) +
  labs(title = "Difference in pupil diameter during imagery during IF", x = "Mean rating", y = "Pupil diameter difference between conditions") 



mean_rating_qmi <- read_excel("C:/Users/lepas/stuffs/University/Master/M2 sciences co/S2 Stage aphantasie/Experiment/mean_rating&qmi_wb.xlsx")
seed <- 42


# Repeat with average mean rating every 5 QMI
ggplot(mean_rating_qmi) +
  geom_point(aes(x = visual_qmi, y = rating_pf, color = subject_id, shape = "pf"),
             position = position_jitter(seed = seed, width =0.2)) +
  geom_point(aes(x = visual_qmi, y = rating_if, color = subject_id, shape = "if"),
             position = position_jitter(seed = seed, width =0.2)) +
  
  geom_segment(aes(x = visual_qmi, y = rating_pf,
                 xend = visual_qmi, yend = rating_if, color = subject_id),
             arrow = arrow(), size = 0.5, alpha = 0.3,
             position = position_jitter(seed = seed, width =0.2)) +
  
  
  geom_segment(data = mean_rating_qmi %>% filter (visual_qmi <= 20),
               aes(x = 17.5, y = mean(rating_pf),
                   xend = 17.5, yend = mean(rating_if)),
               arrow = arrow(), size = 0.8, alpha = 0.8, color = "red") +
  
  geom_segment(data = mean_rating_qmi %>% filter (visual_qmi > 20 & visual_qmi <= 25),
               aes(x = 22.5, y = mean(rating_pf),
                   xend = 22.5, yend = mean(rating_if)),
               arrow = arrow(), size = 0.8, alpha = 0.8, color = "red") +
  
  geom_segment(data = mean_rating_qmi %>% filter (visual_qmi > 25 & visual_qmi <= 30),
               aes(x = 27.5, y = mean(rating_pf),
                   xend = 27.5, yend = mean(rating_if)),
               arrow = arrow(), size = 0.8, alpha = 0.8, color = "red") +

  geom_segment(data = mean_rating_qmi %>% filter (visual_qmi > 30 & visual_qmi <= 35),
               aes(x = 32.5, y = mean(rating_pf),
                   xend = 32.5, yend = mean(rating_if)),
               arrow = arrow(), size = 0.8, alpha = 0.8, color = "red") +

  
  scale_shape_manual(name='Experiment',
                     breaks=c('pf', 'if'),
                     values=c('pf'=16, 'if'=2),
                     labels = c("PF", "IF")) +
  guides(color = "none") +
  
  theme_bw() +
  ylim(0.9,4.1) +
  xlim(15,35.2) +
  labs(title = "Self reported visual imagery depending on experiments", x = "Visual QMI", y = "Mean rating")



ggplot() +
  geom_point(aes(x = visual_QMI_for_IF_2, y = IF_df_mean_rating, color = IF_df_w$subject_id, shape = "if"),
             position = position_jitter(seed = seed, width =0.2)) +
  geom_point(aes(x = visual_QMI_for_KR_2, y = KR_df_mean_rating_2, color = IF_df_w$subject_id, shape = "pf"),
             position = position_jitter(seed = seed, width =0.2)) +
  geom_segment(aes(x = visual_QMI_for_KR_2, y = KR_df_mean_rating_2,
                   xend = visual_QMI_for_IF, yend = IF_df_mean_rating, color = IF_df_w$subject_id),
               arrow = arrow(), size = 0.5, alpha = 0.3,
               position = position_jitter(seed = seed, width =0.2)) +
  theme_bw() +
  scale_shape_manual(name='Experiment',
                     breaks=c('pf', 'if'),
                     values=c('pf'=16, 'if'=2),
                     labels = c("PF", "IF")) +
  guides(color = "none") +
  ylim(0.9,4.1) +
  xlim(15,35.2) +
  labs(title = "Self reported visual imagery depending on experiments", x = "Visual QMI", y = "Mean rating")




#Some stats on our data (t-test)

df_dif_rating <- data.frame(
  pf_imag = KR_df_dif_imag[-23],
  pf_rating = KR_df_mean_rating[-23],
  if_imag = IF_df_dif_imag,
  if_rating = IF_df_mean_rating,
  qmi = visual_QMI_for_IF_2
)


write.csv(df_dif_rating,"C:\\Users\\lepas\\stuffs\\University\\Master\\M2 sciences co\\S2 Stage aphantasie\\Experiment\\dif_imag&rating.csv", row.names = TRUE)

ggplot(df_dif_rating) +
  geom_point(aes(x = qmi, y = pf_rating, color = "pf"), alpha = 0.6) +
  geom_smooth(aes(x = qmi, y = pf_rating, color = "pf"), method = "lm", se = FALSE, fill = "darksalmon") +
  geom_point(aes(x = qmi, y = if_rating, color = "if"), alpha = 0.6) +
  geom_smooth(aes(x = qmi, y = if_rating, color = "if"), method = "lm", se = FALSE, fill = "lightblue") +
  theme_bw() +
  scale_color_manual(name='Experiment',
                     breaks=c('pf', 'if'),
                     values=c('pf'="red", 'if'="blue"),
                     labels = c("PF", "IF")) +
  ylim(0.9,4.1) +
  xlim(15,35.2) +
  labs(title = "Self reported visual imagery depending on experiments", x = "Visual QMI", y = "Mean rating")

