# 2/4/2023
# COTHROM: satisfaction model
# Generate figures 
# Same as the "[AN]02_figures.R" (only file name slightly changed for consistency with other analysis files.)

# Load the packages
library(haven)
library(ggplot2)
library(dplyr)

library(devtools)
library(grid)
#install.packages("gridExtra")
library(gridExtra)
library(gtable)
#install.packages("cowplot")
library(cowplot) # for combine graph with the same height
# install.packages("RColorBrewer")
library(RColorBrewer)


rm(list=ls())

setwd("C:/Users/Yohan/Dropbox/COTHROM/ABM/satisfaction/overall")


d <- read_dta("results_normal_long_cleaned.dta")

d$wealth_rank2 <- ifelse(d$wealth_rank >= 4, 3, 
                         ifelse(d$wealth_rank==1, 1, 2))


# 1. General (Overall) Satisfaction: Satisfaction Composite Index: Normal vs. Low probation ----



# 1-1. normal condition (reference) ----


d_wr <- d %>%
  group_by(wealth_rank2, day) %>%
  summarize(
    stsf_ratio_mean = mean(stsf_ratio),
    wealth_mean = mean(wealth),
    income_mean = mean(income_mth),
    visa_stsf_mean = mean(visa_stsf),
    house_mean = mean(house),
    houseowner_mean = mean(houseowner),
    rent_mean = mean(rent),
    hsp_stsf_mean = mean(hsp_stsf),
    spouse_hired_num = sum(spouse_hired),
    bc_satisfaction_num = sum(bc_satisfaction),
    child_care_num = sum(child_care),
    marriage_num = sum(marriage)
  )

d_wr$spouse_hired_mean <- d_wr$spouse_hired_num/d_wr$marriage_num ## 3110 = number of married immigrants
d_wr$bc_satisfaction_mean <- d_wr$bc_satisfaction_num/d_wr$marriage_num 
d_wr$child_care_mean <- d_wr$child_care_num/d_wr$marriage_num ## Need to check out the number of immigrants with children & also double-check the python code for ABM 

d_wr$fwealth_rank2 <- factor(d_wr$wealth_rank2 )

# d_wr <- d_wr %>% mutate(wealth_mean = case_when(
#   wealth_rank2==3 & wealth_mean < 0 ~ wealth_mean*(-1),
#   wealth_rank2==3 & wealth_mean >= 0 ~ wealth_mean,
#   wealth_rank2==2  ~ wealth_mean,
#   wealth_rank2==1  ~ wealth_mean,
# ))
# 
# 
# for (i in 1:176) {
# 
#   d_wr$wealth_mean[1447+i] <- 11478.354-(11.123*i)
# 
# }



# 1-2. draw the figures (by rank for total satisfaction ratio) ----


display.brewer.pal(9,"Greys")
brewer.pal(9,"Greys")


# color3 <- brewer.pal(3,"Pastel2")
# names(color3) <- levels(d_wr$fwealth_rank2)
# colScale <- scale_colour_manual(name = "grp",values = myColors)

# Smooth version

d_wr_lo = subset(d_wr, wealth_rank2==1)
d_wr_mid = subset(d_wr, wealth_rank2==2)
d_wr_hi = subset(d_wr, wealth_rank2==3)

d_wr_lo.loess10 <- loess(stsf_ratio_mean ~ day, data=d_wr_lo, span=0.20) # 10% smoothing span
d_wr_mid.loess10 <- loess(stsf_ratio_mean ~ day, data=d_wr_mid, span=0.20) # 10% smoothing span
d_wr_hi.loess10 <- loess(stsf_ratio_mean ~ day, data=d_wr_hi, span=0.20) # 10% smoothing span

d_wr_lo.smoothed10 <- predict(d_wr_lo.loess10) 
d_wr_mid.smoothed10 <- predict(d_wr_mid.loess10)
d_wr_hi.smoothed10 <- predict(d_wr_hi.loess10)


d_wr_lo$stsf_ratio_mean_sm10 <- d_wr_lo.smoothed10
d_wr_mid$stsf_ratio_mean_sm10 <- d_wr_mid.smoothed10
d_wr_hi$stsf_ratio_mean_sm10 <- d_wr_hi.smoothed10

d_wr_sm <- rbind(d_wr_lo, d_wr_mid, d_wr_hi )

p.stsf <- ggplot(d_wr_sm, aes(y=stsf_ratio_mean_sm10, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("High Probation (330 days)") +
  ylab("") + xlab("") +
  scale_x_continuous("", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"), 
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Satisfaction Composite Index (ratio)", 
                     limits = c(0, 1)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-1,0,1), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p.stsf





# 1-3. Low Probation ----



# low_probation



d_prob <- read_dta("results_low_probation_long_cleaned.dta")

d_prob$wealth_rank2 <- ifelse(d_prob$wealth_rank >= 4, 3, 
                            ifelse(d_prob$wealth_rank==1, 1, 2))


# 1. by wealth rank ----


d_prob_wr <- d_prob %>%
  group_by(wealth_rank2, day) %>%
  summarize(
    stsf_ratio_mean = mean(stsf_ratio),
    wealth_mean = mean(wealth, na.rm=TRUE),
    visa_stsf_mean = mean(visa_stsf),
    house_mean = mean(house),
    houseowner_mean = mean(houseowner),
    rent_mean = mean(rent),
    hsp_stsf_mean = mean(hsp_stsf),
    spouse_hired_num = sum(spouse_hired),
    bc_satisfaction_num = sum(bc_satisfaction),
    child_care_num = sum(child_care),
    marriage_num = sum(marriage)
  )

d_prob_wr$spouse_hired_mean <- d_prob_wr$spouse_hired_num/d_prob_wr$marriage_num ## 3110 = number of married immigrants
d_prob_wr$bc_satisfaction_mean <- d_prob_wr$bc_satisfaction_num/d_prob_wr$marriage_num 
d_prob_wr$child_care_mean <- d_prob_wr$child_care_num/d_prob_wr$marriage_num ## Need to check out the number of immigrants with children & also double-check the python code for ABM 





# 1-2. draw the figures (by rank for total satisfaction ratio) ----
d_prob_wr$fwealth_rank2 <- factor(d_prob_wr$wealth_rank2 )




display.brewer.pal(9,"Greys")
brewer.pal(9,"Greys")


# color3 <- brewer.pal(3,"Pastel2")
# names(color3) <- levels(d_wr$fwealth_rank2)
# colScale <- scale_colour_manual(name = "grp",values = myColors)

# 2-3. Smooth version----

d_prob_wr_lo = subset(d_prob_wr, wealth_rank2==1)
d_prob_wr_mid = subset(d_prob_wr, wealth_rank2==2)
d_prob_wr_hi = subset(d_prob_wr, wealth_rank2==3)

d_prob_wr_lo.loess10 <- loess(stsf_ratio_mean ~ day, data=d_prob_wr_lo, span=0.20) # 10% smoothing span
d_prob_wr_mid.loess10 <- loess(stsf_ratio_mean ~ day, data=d_prob_wr_mid, span=0.20) # 10% smoothing span
d_prob_wr_hi.loess10 <- loess(stsf_ratio_mean ~ day, data=d_prob_wr_hi, span=0.20) # 10% smoothing span

d_prob_wr_lo.smoothed10 <- predict(d_prob_wr_lo.loess10) 
d_prob_wr_mid.smoothed10 <- predict(d_prob_wr_mid.loess10)
d_prob_wr_hi.smoothed10 <- predict(d_prob_wr_hi.loess10)


d_prob_wr_lo$stsf_ratio_mean_sm10 <- d_prob_wr_lo.smoothed10
d_prob_wr_mid$stsf_ratio_mean_sm10 <- d_prob_wr_mid.smoothed10
d_prob_wr_hi$stsf_ratio_mean_sm10 <- d_prob_wr_hi.smoothed10

d_prob_wr_sm <- rbind(d_prob_wr_lo, d_prob_wr_mid, d_prob_wr_hi )

p.stsf_prob <- ggplot(d_prob_wr_sm, aes(y=stsf_ratio_mean_sm10, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Low Probation (180 days)") +
  ylab("") + xlab("") +
  scale_x_continuous("", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"), 
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("", 
                     limits = c(0, 1)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,1,0,-1), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p.stsf_prob

















# 1-3. Low GP access ----



d_gp <- read_dta("results_low_gp_long_cleaned.dta")

d_gp$wealth_rank2 <- ifelse(d_gp$wealth_rank >= 4, 3, 
                            ifelse(d_gp$wealth_rank==1, 1, 2))


# 1. by wealth rank ----


d_gp_wr <- d_gp %>%
  group_by(wealth_rank2, day) %>%
  summarize(
    stsf_ratio_mean = mean(stsf_ratio),
    wealth_mean = mean(wealth, na.rm=TRUE),
    visa_stsf_mean = mean(visa_stsf),
    house_mean = mean(house),
    houseowner_mean = mean(houseowner),
    rent_mean = mean(rent),
    hsp_stsf_mean = mean(hsp_stsf),
    spouse_hired_num = sum(spouse_hired),
    bc_satisfaction_num = sum(bc_satisfaction),
    child_care_num = sum(child_care),
    marriage_num = sum(marriage)
  )

d_gp_wr$spouse_hired_mean <- d_gp_wr$spouse_hired_num/d_gp_wr$marriage_num ## 3110 = number of married immigrants
d_gp_wr$bc_satisfaction_mean <- d_gp_wr$bc_satisfaction_num/d_gp_wr$marriage_num 
d_gp_wr$child_care_mean <- d_gp_wr$child_care_num/d_gp_wr$marriage_num ## Need to check out the number of immigrants with children & also double-check the python code for ABM 





# 1-2. draw the figures (by rank for total satisfaction ratio) ----
d_gp_wr$fwealth_rank2 <- factor(d_gp_wr$wealth_rank2 )




display.brewer.pal(9,"Greys")
brewer.pal(9,"Greys")


# color3 <- brewer.pal(3,"Pastel2")
# names(color3) <- levels(d_wr$fwealth_rank2)
# colScale <- scale_colour_manual(name = "grp",values = myColors)

# 1-3. Smooth version----

d_gp_wr_lo = subset(d_gp_wr, wealth_rank2==1)
d_gp_wr_mid = subset(d_gp_wr, wealth_rank2==2)
d_gp_wr_hi = subset(d_gp_wr, wealth_rank2==3)

d_gp_wr_lo.loess10 <- loess(stsf_ratio_mean ~ day, data=d_gp_wr_lo, span=0.20) # 10% smoothing span
d_gp_wr_mid.loess10 <- loess(stsf_ratio_mean ~ day, data=d_gp_wr_mid, span=0.20) # 10% smoothing span
d_gp_wr_hi.loess10 <- loess(stsf_ratio_mean ~ day, data=d_gp_wr_hi, span=0.20) # 10% smoothing span

d_gp_wr_lo.smoothed10 <- predict(d_gp_wr_lo.loess10) 
d_gp_wr_mid.smoothed10 <- predict(d_gp_wr_mid.loess10)
d_gp_wr_hi.smoothed10 <- predict(d_gp_wr_hi.loess10)


d_gp_wr_lo$stsf_ratio_mean_sm10 <- d_gp_wr_lo.smoothed10
d_gp_wr_mid$stsf_ratio_mean_sm10 <- d_gp_wr_mid.smoothed10
d_gp_wr_hi$stsf_ratio_mean_sm10 <- d_gp_wr_hi.smoothed10

d_gp_wr_sm <- rbind(d_gp_wr_lo, d_gp_wr_mid, d_gp_wr_hi )

p.stsf_gp <- ggplot(d_gp_wr_sm, aes(y=stsf_ratio_mean_sm10, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Low GP Access (p = 0.1)") +
  ylab("") + xlab("") +
  scale_x_continuous("Time", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"), 
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("", 
                     limits = c(0, 1)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-1,1,-1), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p.stsf_gp





# wealth
stsf.plots <- list(p.stsf, p.stsf_gp, p.stsf_prob )




# Align left-right margins of all plots
grobs <- lapply(stsf.plots, as_grob)
plot_widths <- lapply(grobs, function(x) {x$widths})
# Aligning the left margins of all plots
aligned_widths <- align_margin(plot_widths, "first")
# Aligning the right margins of all plots as well
aligned_widths <- align_margin(aligned_widths, "last")
# Setting the dimensions of plots to the aligned dimensions
for (i in seq_along(stsf.plots)) {
  grobs[[i]]$widths <- aligned_widths[[i]]
}
stsf_plots <- plot_grid(plotlist = grobs, ncol=3) # Draw aligned plots

stsf_plots

pdf(height = 3, width = 12, "satisfaction_composite.pdf")
# plot_grid(title1, cw, title2, pcw,  ncol = 1, rel_heights = c(0.15, 1))
plot_grid(stsf_plots)
dev.off()













# Part 2. Disaggregated DV:----
# 2-1. Normal Condition
# 2-1-1. Wealth
summary(d_wr$wealth_mean)


d_wr_lo.loess_wealth <- loess(wealth_mean ~ day, data=d_wr_lo, span=0.20) # 10% smoothing span
d_wr_mid.loess_wealth <- loess(wealth_mean ~ day, data=d_wr_mid, span=0.20) # 10% smoothing span
d_wr_hi.loess_wealth <- loess(wealth_mean ~ day, data=d_wr_hi, span=0.20) # 10% smoothing span

d_wr_lo.smoothed_wealth <- predict(d_wr_lo.loess_wealth) 
d_wr_mid.smoothed_wealth <- predict(d_wr_mid.loess_wealth)
d_wr_hi.smoothed_wealth <- predict(d_wr_hi.loess_wealth)


d_wr_lo$wealth_mean_sm10 <- d_wr_lo.smoothed_wealth
d_wr_mid$wealth_mean_sm10 <- d_wr_mid.smoothed_wealth
d_wr_hi$wealth_mean_sm10 <- d_wr_hi.smoothed_wealth

d_wr_sm <- rbind(d_wr_lo, d_wr_mid, d_wr_hi )


p_wr.wealth <- ggplot(d_wr_sm, aes(y=wealth_mean_sm10, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Cumulative Wealth") +
  ylab("") + xlab("") +
  scale_x_continuous("Time", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"), 
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Cum. Wealth (euros)", 
                     limits = c(-25000, 7000)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-1,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p_wr.wealth





# 3-2. Visa ----
summary(d_wr$visa_stsf_mean)

p_wr.visa <- ggplot(d_wr, aes(y=visa_stsf_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Employment") +
  ylab("") + xlab("") +
  scale_x_continuous("Time", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"), 
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Employment (ratio)", 
                     limits = c(0, 1)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), "Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-1,0,-1), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p_wr.visa



# 3-3. Housing ----
summary(d_wr$house_mean)

p_wr.house <- ggplot(d_wr, aes(y=house_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Housing") +
  ylab("") + xlab("") +
  scale_x_continuous("Time", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"), 
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Rent or House Owner (ratio)", 
                     limits = c(0.4, 1)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-1,0,-1), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p_wr.house



# 3-4. Hospital ----
summary(d_wr$hsp_stsf_mean)

p_wr.hsp <- ggplot(d_wr, aes(y=hsp_stsf_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Health Care") +
  ylab("") + xlab("") +
  scale_x_continuous("Time", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"),  
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Health Care Satisfaction (ratio)", 
                     limits = c(0, 0.7)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-1,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p_wr.hsp




# 3-5. Spouse visa ----
summary(d_wr$spouse_hired_mean)

p_wr.spouse <- ggplot(d_wr, aes(y=spouse_hired_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Spouse Employment") +
  ylab("") + xlab("") +
  scale_x_continuous("Time", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"),  
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Spouse Employment (ratio)", 
                     limits = c(0, 0.15)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-1,0,-1), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p_wr.spouse





# 3-6. Maternity care ----
summary(d_wr$bc_satisfaction_mean)

p_wr.bc <- ggplot(d_wr, aes(y=bc_satisfaction_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Maternity Care") +
  ylab("") + xlab("") +
  scale_x_continuous("Time", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"),
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Maternity Care Satisfaction (ratio)", 
                     limits = c(0, 0.7)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-1,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        # legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p_wr.bc



# 3-7 child care ----
summary(d_wr$child_care_mean)

p_wr.cc <- ggplot(d_wr, aes(y=child_care_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Child Care") +
  ylab("") + xlab("") +
  scale_x_continuous("Time", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"),
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Child Care Satisfaction (ratio)", 
                     limits = c(0, 1)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-2,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p_wr.cc



# 3-8 - House Owner ----
summary(d_wr$houseowner)

p_wr.ho <- ggplot(d_wr, aes(y=houseowner_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("House Owner") +
  ylab("") + xlab("") +
  scale_x_continuous("Time", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"),
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("House Owner (ratio)", 
                     limits = c(0, 0.1)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-1,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p_wr.ho










# wealth
stsf.disagg <- list(p_wr.wealth, p_wr.visa, p_wr.house, p_wr.hsp, p_wr.spouse, p_wr.bc, p_wr.cc, p_wr.ho )




# Align left-right margins of all plots
grobs <- lapply(stsf.disagg, as_grob)
plot_widths <- lapply(grobs, function(x) {x$widths})
# Aligning the left margins of all plots
aligned_widths <- align_margin(plot_widths, "first")
# Aligning the right margins of all plots as well
aligned_widths <- align_margin(aligned_widths, "last")
# Setting the dimensions of plots to the aligned dimensions
for (i in seq_along(stsf.disagg)) {
  grobs[[i]]$widths <- aligned_widths[[i]]
}
stsf_disagg <- plot_grid(plotlist = grobs, ncol=3) # Draw aligned plots

stsf_disagg

pdf(height = 12, width = 12, "disaggregate_normal.pdf")
# plot_grid(title1, cw, title2, pcw,  ncol = 1, rel_heights = c(0.15, 1))
plot_grid(stsf_disagg)
dev.off()



# now add the title
title1 <- ggdraw() +   draw_label("High Probation (330 days)",
                                  fontface = 'bold',  x = 0.5,   hjust = 0.5 , size = 20) +
  theme(  # add margin on the left of the drawing canvas,
    # so title is aligned with left edge of first plot
    plot.margin = unit(c(0,0,0,0), "mm"))


pdf(height = 12, width = 12, "disaggregate_normal.pdf")
plot_grid(title1, stsf_disagg, nrow=2, rel_heights = c(0.15, 1))
dev.off()









# 3-1. Low Probation----
# 3-1-1. Wealth
summary(d_prob$wealth_mean)


d_prob_wr_lo = subset(d_prob_wr, wealth_rank2==1)
d_prob_wr_mid = subset(d_prob_wr, wealth_rank2==2)
d_prob_wr_hi = subset(d_prob_wr, wealth_rank2==3)

d_prob_lo.loess_wealth <- loess(wealth_mean ~ day, data=d_prob_wr_lo, span=0.20) # 10% smoothing span
d_prob_mid.loess_wealth <- loess(wealth_mean ~ day, data=d_prob_wr_mid, span=0.20) # 10% smoothing span
d_prob_hi.loess_wealth <- loess(wealth_mean ~ day, data=d_prob_wr_hi, span=0.20) # 10% smoothing span

d_prob_lo.smoothed_wealth <- predict(d_prob_lo.loess_wealth) 
d_prob_mid.smoothed_wealth <- predict(d_prob_mid.loess_wealth)
d_prob_hi.smoothed_wealth <- predict(d_prob_hi.loess_wealth)


d_prob_wr_lo$wealth_mean_sm10 <- d_prob_lo.smoothed_wealth
d_prob_wr_mid$wealth_mean_sm10 <- d_prob_mid.smoothed_wealth
d_prob_wr_hi$wealth_mean_sm10 <- d_prob_hi.smoothed_wealth

d_prob_sm <- rbind(d_prob_wr_lo, d_prob_wr_mid, d_prob_wr_hi )


p_prob.wealth <- ggplot(d_prob_sm, aes(y=wealth_mean_sm10, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Cumulative Wealth") +
  ylab("") + xlab("") +
  scale_x_continuous("Time", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"), 
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Cum. Wealth (euros)", 
                     limits = c(-25000, 7000)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-1,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p_prob.wealth





# 3-2. Visa ----
summary(d_prob$visa_stsf_mean)

p_prob.visa <- ggplot(d_prob_wr, aes(y=visa_stsf_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Employment") +
  ylab("") + xlab("") +
  scale_x_continuous("Time", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"), 
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Employment (ratio)", 
                     limits = c(0, 1)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), "Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-1,0,-1), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p_prob.visa



# 3-3. Housing ----
summary(d_prob$house_mean)

p_prob.house <- ggplot(d_prob_wr, aes(y=house_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Housing") +
  ylab("") + xlab("") +
  scale_x_continuous("Time", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"), 
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Rent or House Owner (ratio)", 
                     limits = c(0.4, 1)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-1,0,-1), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p_prob.house



# 3-4. Hospital ----
summary(d_prob$hsp_stsf_mean)

p_prob.hsp <- ggplot(d_prob_wr, aes(y=hsp_stsf_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Health Care") +
  ylab("") + xlab("") +
  scale_x_continuous("Time", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"),  
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Health Care Satisfaction (ratio)", 
                     limits = c(0, 0.7)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-1,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p_prob.hsp




# 3-5. Spouse visa ----
summary(d_prob$spouse_hired_mean)

p_prob.spouse <- ggplot(d_prob_wr, aes(y=spouse_hired_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Spouse Employment") +
  ylab("") + xlab("") +
  scale_x_continuous("Time", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"),  
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Spouse Employment (ratio)", 
                     limits = c(0, 0.15)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-1,0,-1), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p_prob.spouse





# 3-6. Maternity care ----
summary(d_prob$bc_satisfaction_mean)

p_prob.bc <- ggplot(d_prob_wr, aes(y=bc_satisfaction_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Maternity Care") +
  ylab("") + xlab("") +
  scale_x_continuous("Time", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"),
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Maternity Care Satisfaction (ratio)", 
                     limits = c(0, 0.7)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-1,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        # legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p_prob.bc



# 3-7 child care ----
summary(d_prob$child_care_mean)

p_prob.cc <- ggplot(d_prob_wr, aes(y=child_care_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Child Care") +
  ylab("") + xlab("") +
  scale_x_continuous("Time", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"),
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Child Care Satisfaction (ratio)", 
                     limits = c(0, 1)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-2,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p_prob.cc



# 3-8 - House Owner ----
summary(d_prob$houseowner)

p_prob.ho <- ggplot(d_prob_wr, aes(y=houseowner_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("House Owner") +
  ylab("") + xlab("") +
  scale_x_continuous("Time", 
                     labels = c("1m", "3m", "6m", "1y", "1.5y"),
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("House Owner (ratio)", 
                     limits = c(0, 0.1)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,-1,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        legend.position = "none",
        axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1)
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p_prob.ho










# wealth
stsf.prob.disagg <- list(p_prob.wealth, p_prob.visa, p_prob.house, p_prob.hsp, p_prob.spouse, p_prob.bc, p_prob.cc, p_prob.ho )




# Align left-right margins of all plots
grobs <- lapply(stsf.prob.disagg, as_grob)
plot_widths <- lapply(grobs, function(x) {x$widths})
# Aligning the left margins of all plots
aligned_widths <- align_margin(plot_widths, "first")
# Aligning the right margins of all plots as well
aligned_widths <- align_margin(aligned_widths, "last")
# Setting the dimensions of plots to the aligned dimensions
for (i in seq_along(stsf.disagg)) {
  grobs[[i]]$widths <- aligned_widths[[i]]
}
stsf.prob_disagg <- plot_grid(plotlist = grobs, ncol=3) # Draw aligned plots

stsf.prob_disagg

# pdf(height = 12, width = 12, "disaggregate_low_probation.pdf")
# # plot_grid(title1, cw, title2, pcw,  ncol = 1, rel_heights = c(0.15, 1))
# plot_grid(stsf.prob_disagg)
# dev.off()



# now add the title
title1 <- ggdraw() +   draw_label("Low Probation (180 days)",
                                  fontface = 'bold',  x = 0.5,   hjust = 0.5 , size = 20) +
  theme(  # add margin on the left of the drawing canvas,
    # so title is aligned with left edge of first plot
    plot.margin = unit(c(0,0,0,0), "mm"))


pdf(height = 12, width = 12, "disaggregate_low_probation.pdf")
plot_grid(title1, stsf.prob_disagg, nrow=2, rel_heights = c(0.15, 1))
dev.off()


















# copy------



# 3. Disaggregated DV:----
# 3-1. Wealth ----
summary(d_gp_wr$wealth_mean)

p.gp_wr.wealth <- ggplot(d_gp_wr, aes(y=wealth_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Cumulative Wealth") +
  ylab("") + xlab("") +
  scale_x_continuous("Time (day)", 
                     labels = c("1 month", "3 month", "6 month", "1 year", "1.5 year"), 
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Cum. Wealth (euros)", 
                     limits = c(-25000, 7000)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,2,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p.gp_wr.wealth


# 3-2. Visa ----
summary(d_gp_wr$visa_stsf_mean)

p.gp_wr.visa <- ggplot(d_gp_wr, aes(y=visa_stsf_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Employment") +
  ylab("") + xlab("") +
  scale_x_continuous("Time (day)", 
                     labels = c("1 month", "3 month", "6 month", "1 year", "1.5 year"), 
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Employment (ratio)", 
                     limits = c(0, 1)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,2,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p.gp_wr.visa



# 3-3. Housing ----
summary(d_gp_wr$house_mean)

p.gp_wr.house <- ggplot(d_gp_wr, aes(y=house_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Housing") +
  ylab("") + xlab("") +
  scale_x_continuous("Time (day)", 
                     labels = c("1 month", "3 month", "6 month", "1 year", "1.5 year"), 
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Rent or House Owner (ratio)", 
                     limits = c(0.4, 1)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,2,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p.gp_wr.house



# 3-4. Hospital ----
summary(d_gp_wr$hsp_stsf_mean)

p.gp_wr.hsp <- ggplot(d_gp_wr, aes(y=hsp_stsf_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Health Care") +
  ylab("") + xlab("") +
  scale_x_continuous("Time (day)", 
                     labels = c("1 month", "3 month", "6 month", "1 year", "1.5 year"), 
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Health Care Satisfaction (ratio)", 
                     limits = c(0, 1)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,2,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p.gp_wr.hsp




# 3-6. Spouse visa ----
summary(d_gp_wr$spouse_hired_mean)

p.gp_wr.spouse <- ggplot(d_gp_wr, aes(y=spouse_hired_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Spouse Employment") +
  ylab("") + xlab("") +
  scale_x_continuous("Time (day)", 
                     labels = c("1 month", "3 month", "6 month", "1 year", "1.5 year"), 
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Spouse Employment (ratio)",
                     limits = c(0, 0.2)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,2,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p.gp_wr.spouse





# 3-7. Maternity care ----
summary(d_gp_wr$bc_satisfaction_mean)

p.gp_wr.bc <- ggplot(d_gp_wr, aes(y=bc_satisfaction_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Maternity Care") +
  ylab("") + xlab("") +
  scale_x_continuous("Time (day)", 
                     labels = c("1 month", "3 month", "6 month", "1 year", "1.5 year"), 
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Maternity Care Satisfaction (ratio)", 
                     limits = c(0, 0.7)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,2,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p.gp_wr.bc



# 3-8. child care ----
summary(d_gp_wr$child_care_mean)

p.gp_wr.cc <- ggplot(d_gp_wr, aes(y=child_care_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("Child Care") +
  ylab("") + xlab("") +
  scale_x_continuous("Time (day)", 
                     labels = c("1 month", "3 month", "6 month", "1 year", "1.5 year"), 
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("Child Care Satisfaction (ratio)", 
                     limits = c(0, 1)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,2,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p.gp_wr.cc


# 3-8. house owner ----
summary(d_gp_wr$houseowner_mean)

p.gp_wr.ho <- ggplot(d_gp_wr, aes(y=houseowner_mean, x=day, group=wealth_rank2, col=fwealth_rank2)) +
  geom_line( size=1) + 
  # geom_smooth(alpha=0.1, colour=c("#CB181D", "#F16913" ,"#4292C6"))+
  ggtitle("House Owner") +
  ylab("") + xlab("") +
  scale_x_continuous("Time (day)", 
                     labels = c("1 month", "3 month", "6 month", "1 year", "1.5 year"), 
                     breaks = c(30, 90, 180, 365, 540), limits = c(1, 554), expand = c(0, 0)) +
  scale_y_continuous("House Owner (ratio)", 
                     limits = c(0, 0.1)) +
  scale_color_manual(labels = c("Low", "Mid", "High"), values = c("#EF3B2C", "#74C476" ,"#08519C"), name="Initial Wealth") +
  # scale_colour_manual(name = "Wealth Rank",values = color3) +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
        panel.border = element_blank(),
        panel.grid.major.x = element_line(),
        panel.grid.major.y = element_line(), 
        panel.grid.minor = element_blank(),
        panel.spacing=unit(c(0,0,0,0), "mm"),
        plot.margin = unit(c(1,2,0,0), "mm"),
        plot.title = element_text(size=10, face=NULL, hjust = 0.5),
        # axis.text.x = element_text(size=10,  vjust=0.8),
        # axis.text.y = element_text(size=10),
        # axis.title=element_text(size=10, hjust = 0.1 )
  )


p.gp_wr.ho

































id <- seq(1, 20, by=1)



# wealth
wealth.plots <- list()

for (i in 1:20) {
  dd20 <- d20[d20$id==id[i],]
  dd20 <- dd20[order(dd20$id, dd20$day ) , ]
  
  plot <- ggplot(dd20, aes(y=wealth, x=day)) +
    geom_line(aes(y=wealth), colour="black", size=1) +
    ggtitle(paste(dd20$id)) +
    ylab("") + xlab("") +
    scale_x_continuous("", 
                       labels = c("1 month", "3 month", "6 month", "1 year", "1.5 year", "2 year"), 
                       breaks = c(30, 90, 180, 365, 540, 730), limits = c(1, 731), expand = c(0, 0)) +
    scale_y_continuous("", 
                       limits = c(-30000, 30000)) +
    theme_bw() +
    theme(axis.line = element_line(colour = "black"),
          panel.border = element_blank(),
          panel.grid.major.x = element_blank(),
          panel.grid.major.y = element_line(), 
          panel.grid.minor = element_blank(),
          panel.spacing=unit(c(0,0,0,0), "mm"),
          plot.margin = unit(c(1,2,0,0), "mm"),
          plot.title = element_text(size=7.5, face=NULL, hjust = 0.5),
          axis.text.x = element_text(size=6,  vjust=0.8),
          axis.text.y = element_text(size=7),
          axis.title=element_text(size=4, hjust = 0.1 ))
  wealth.plots[i] <- list(plot)
}

wealth.plots 




# Align left-right margins of all plots
grobs <- lapply(wealth.plots, as_grob)
plot_widths <- lapply(grobs, function(x) {x$widths})
# Aligning the left margins of all plots
aligned_widths <- align_margin(plot_widths, "first")
# Aligning the right margins of all plots as well
aligned_widths <- align_margin(aligned_widths, "last")
# Setting the dimensions of plots to the aligned dimensions
for (i in seq_along(wealth.plots)) {
  grobs[[i]]$widths <- aligned_widths[[i]]
}
wealth_plots <- plot_grid(plotlist = grobs, ncol=5) # Draw aligned plots

wealth_plots

pdf(height = 8, width = 8, "fig_wealth20_prep.pdf")
# plot_grid(title1, cw, title2, pcw,  ncol = 1, rel_heights = c(0.15, 1))
plot_grid(wealth_plots)
dev.off()
