COTHROM project
MABS 2023 conference paper
08/Feb/2023

This is the instruction for replication of the results presented in the paper for MABS 2023. 

1. Please be sure to set your own working directory.

2. In this replication folder, there are four datasets and four analysis code files.
    2.1. Three different programms are used: Python, R, and Stata.
    2.2. Python is used to run the simulation model (ABM) and generate the results (saved as .csv files).
    2.3. Stata is used to efficiently open the csv files (the size of each csv file for the result data is about 1gb.) and clean the data to 
    generate figures. 
    2.4. R is used to generate the figures presented in the paper.

3. Replication order is as follows:
    3.1. execute "[AN]01_satisfaction_Feb2023.py"
        3.1.1. Then, you will get six csv files containing the results.
    3.2. execute "[AN]02_data_for_figures_compact.do"   
        3.2.1. This do-file helps you load the large-size csv files efficiently and reshape the data format from wide to long.
    3.3. execute "[AN]03_data_for_figures_compact_cleaning.do"
        3.3.1. This do-file guides you to clean the data and generate the variables for the figures (e.g., satisfaction composite index)
    3.4. Lastly, execute " [AN]04_figures.R "
        3.4.1. This file helps you generate the figures.


