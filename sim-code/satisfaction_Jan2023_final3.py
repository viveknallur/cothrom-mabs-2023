"""
Yohan Park, 27/January/2023
Model for migrants' satisfaction over various categories: housing, spouse work permit, birth care satisfaction, 

"""


import os
os.chdir('C:/Users/Yohan/Dropbox/COTHROM/ABM/satisfaction/overall')

import mesa
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import random


from types import FunctionType
from copy import copy

import pandas as pd
import matplotlib.pyplot as plt

# import the datasets for sampling
df_agent = pd.read_csv(r'../data/YP/agent_sample.csv')  ## immigrants with various characteristics
df_hrent = pd.read_csv(r'../data/YP/hrent_sample.csv') ## housing options (for rent)
df_hbuy = pd.read_csv(r'../data/YP/hbuy_sample.csv')  ## housing options (for buy)
df_job = pd.read_csv(r'../data/YP/job_sample.csv')  ## list of available jobs 

deletelist=['salary','gender']
df_job = df_job.drop(axis='columns', columns = deletelist) ## drop the assigned gender: instead, use the gender_prob

# dapp = pd.DataFrame(np.random.multivariate_normal(mean, cov, 5000))
df_agent.describe()
# df_agent.corr()



# a = df_agent.sample(n = 3)
# a['salary']
# a.loc[1377, 'salary']
# a[1377]['salary']
# a.index[0]

# def compute_spouse_hired(model):
#     spouse_hired = [agent.spouse_hired for agent in model.schedule.agents if isinstance(agent, immigrant)]
#     avg_spouse_hired = np.mean(spouse_hired)
#     return avg_spouse_hired

compute_list = ['unique_id', 'gender', 'marriage', 'age', 'rank', 'n_fam', 'income_mth' , 'income_yr', 'fam_wealth',
                'wealth', 'edu', 'eng', 'nationality', 'child_care', 'ppsn' , 'hp' , 'wealth_rank',
                'com_house', 'com_child', 'visaperiod', 'rentperiod', "hloan_period", 'sickperiod',
                'postbirth', 'prebirth', 'postbirth_period', 'house_seeker', 'job_seeker',
                'bc_satisfaction', 'hospital_satisfaction', 'disease_rate', 'workperiod', 
                'spouse_visaperiod', 'spouse_income_mth',  'spouse_job_seeker', 
                'spouse_rpe', 'spouse_g1', 'spouse_edu', 'spouse_gender',  'spouse_age', 'spouse_rank', 
                'spouse_ppsn', 'spouse_hired', 'spouse_workperiod', 'spouse_rpeaccepted']


compute_fn_list = []
def copy_function(fn, name):
    return FunctionType(copy(fn.__code__), 
                        copy(fn.__globals__), name=name, argdefs=copy(fn.__defaults__),
                        closure=copy(fn.__closure__))

for i in range(len(compute_list)):
    # x = compute_list[i]
    name = 'compute' + '_' + compute_list[i]
    def _compute(model):
        a = compute_list[i]
        x = [agent.a for agent in model.schedule.agents if isinstance(agent, immigrant)]
        return x
    # globals()[name] = copy_function(comp, name)
    globals()[name] = copy_function(_compute, name)
    compute_fn_list.append(name)

# def compute_unique_id(model):
#     unique_id = [agent.unique_id for agent in model.schedule.agents if isinstance(agent, immigrant)]
#     return unique_id

def compute_gender(model):
    gender = [agent.gender for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return gender

def compute_marriage(model):
    marriage = [agent.marriage for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return marriage

def compute_age(model):
    age = [agent.age for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return age

def compute_rank(model):
    rank = [agent.rank for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return rank

def compute_n_fam(model):
    n_fam = [agent.n_fam for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return n_fam

def compute_income_mth(model):
    income_mth = [agent.income_mth for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return income_mth

def compute_income_yr(model):
    income_yr = [agent.income_yr for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return income_yr

def compute_fam_wealth(model):
    fam_wealth = [agent.fam_wealth for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return fam_wealth

def compute_wealth(model):
    wealth = [agent.wealth for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return wealth

def compute_edu(model):
    edu = [agent.edu for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return edu

def compute_eng(model):
    eng = [agent.eng for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return eng

def compute_nationality(model):
    nationality = [agent.nationality for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return nationality

def compute_child_care(model):
    child_care = [agent.child_care for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return child_care

def compute_ppsn(model):
    ppsn = [agent.ppsn for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return ppsn

def compute_hp(model):
    hp = [agent.hp for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return hp

def compute_wealth_rank(model):
    wealth_rank = [agent.wealth_rank for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return wealth_rank

def compute_com_house(model):
    com_house = [agent.com_house for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return com_house

def compute_com_child(model):
    com_child = [agent.com_child for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return com_child

def compute_visaperiod(model):
    visaperiod = [agent.visaperiod for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return visaperiod

def compute_rentperiod(model):
    rentperiod = [agent.rentperiod for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return rentperiod

def compute_hloan_period(model):
    hloan_period = [agent.hloan_period for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return hloan_period

def compute_sickperiod(model):
    sickperiod = [agent.sickperiod for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return sickperiod

def compute_postbirth(model):
    postbirth = [agent.postbirth for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return postbirth

def compute_prebirth(model):
    prebirth = [agent.prebirth for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return prebirth

def compute_postbirth_period(model):
    postbirth_period = [agent.postbirth_period for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return postbirth_period

def compute_house_seeker(model):
    house_seeker = [agent.house_seeker for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return house_seeker

def compute_job_seeker(model):
    job_seeker = [agent.job_seeker for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return job_seeker

def compute_bc_satisfaction(model):
    bc_satisfaction = [agent.bc_satisfaction for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return bc_satisfaction

def compute_hospital_satisfaction(model):
    hospital_satisfaction = [agent.hospital_satisfaction for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return hospital_satisfaction

def compute_disease_rate(model):
    disease_rate = [agent.disease_rate for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return disease_rate

def compute_workperiod(model):
    workperiod = [agent.workperiod for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return workperiod

def compute_spouse_visaperiod(model):
    spouse_visaperiod = [agent.spouse_visaperiod for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return spouse_visaperiod

def compute_spouse_income_mth(model):
    spouse_income_mth = [agent.spouse_income_mth for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return spouse_income_mth

def compute_spouse_job_seeker(model):
    spouse_job_seeker = [agent.spouse_job_seeker for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return spouse_job_seeker

def compute_spouse_rpe(model):
    spouse_rpe = [agent.spouse_rpe for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return spouse_rpe

def compute_spouse_g1(model):
    spouse_g1 = [agent.spouse_g1 for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return spouse_g1

def compute_spouse_edu(model):
    spouse_edu = [agent.spouse_edu for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return spouse_edu

def compute_spouse_gender(model):
    spouse_gender = [agent.spouse_gender for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return spouse_gender

def compute_spouse_age(model):
    spouse_age = [agent.spouse_age for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return spouse_age

def compute_spouse_rank(model):
    spouse_rank = [agent.spouse_rank for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return spouse_rank

def compute_spouse_ppsn(model):
    spouse_ppsn = [agent.spouse_ppsn for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return spouse_ppsn

def compute_spouse_hired(model):
    spouse_hired = [agent.spouse_hired for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return spouse_hired

def compute_spouse_workperiod(model):
    spouse_workperiod = [agent.spouse_workperiod for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return spouse_workperiod

def compute_spouse_rpeaccepted(model):
    spouse_rpeaccepted = [agent.spouse_rpeaccepted for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return spouse_rpeaccepted

def compute_house(model):
    house = [agent.house for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return house

def compute_rent(model):
    rent = [agent.rent for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return rent

def compute_houseowner(model):
    houseowner = [agent.houseowner for agent in model.schedule.agents if isinstance(agent, immigrant)]
    return houseowner

def compute_inflation(model):
    inflation_rate = [agent.inflation_rate for agent in model.schedule.agents if isinstance(agent, econ_status)]
    avg_inflation_rate= np.mean(inflation_rate)
    return avg_inflation_rate

def compute_job_competition(model):
    jobcomp_rate = [agent.jobcomp_rate for agent in model.schedule.agents if isinstance(agent, econ_status)]
    avg_jobcomp_rate= np.mean(jobcomp_rate)
    return avg_jobcomp_rate

# def compute_neighbors(model):
#     neighbors = [agent.neighbors for agent in model.schedule.agents if isinstance(agent, econ_status)]
#     # avg_jobcomp_rate= np.mean(jobcomp_rate)
#     return neighbors

# np.random.uniform(0, 1, 1) = 0.66198459
random.seed(66198459)

class immigrant(mesa.Agent):
    """
    Migrants in Ireland
    """
    def __init__(self, unique_id, model ):

        super().__init__(unique_id, model)
        # self.amount = 50  ## initial level of satisfaction
        mid = int(np.random.uniform(0,9997,1))  ## migrants ID 
        self.gender = df_agent.loc[mid, 'gender']
        self.marriage = df_agent.loc[mid, 'marriage']
        self.age = df_agent.loc[mid, 'age']
        self.rank = df_agent.loc[mid, 'rank']
        self.kid = df_agent.loc[mid, 'kid']
        self.n_fam = df_agent.loc[mid, 'n_fam']
        self.income_mth = df_agent.loc[mid, 'salary_mth']  ## monthly income
        self.income_yr = df_agent.loc[mid, 'salary']  ## annual income
        self.fam_wealth = df_agent.loc[mid, 'fam_wealth'] ## family wealth
        self.wealth_init = df_agent.loc[mid, 'wealth_init'] ## initial wealth
        self.wealth = df_agent.loc[mid, 'fam_wealth']  ## initial money to settle down
        self.edu = df_agent.loc[mid, 'edu']
        self.eng = df_agent.loc[mid, 'eng']
        self.nationality = df_agent.loc[mid, 'nationality']
        self.child_care = False
        self.livcost = df_agent.loc[mid, 'livcost'] ## living cost
        self.wealth_rank = df_agent.loc[mid, 'wealth_rank']  # 1-5 level of initial wealth
        self.com_house = df_agent.loc[mid, 'com_house']  # whether company provides house or not: 1 (no), 2(temp), 3 (permanent)
        self.com_child = df_agent.loc[mid, 'com_child'] # whether company provides chird care or not: 0 (no), 1(yes)
        self.hpref_dist = df_agent.loc[mid, 'hpref_dist'] # housing pref. of distance 1-5; 5 level is the best value.
        self.hpref_safe = df_agent.loc[mid, 'hpref_safe'] # safety
        self.hpref_fq = df_agent.loc[mid, 'hpref_fq']  # facility quality
        self.hpref_loc = df_agent.loc[mid, 'hpref_loc']  # location
        self.hpref_edu = df_agent.loc[mid, 'hpref_edu']  # education: 0 / 1
        self.hpref_nroom = df_agent.loc[mid, 'hpref_nroom'] # number of rooms
        self.hpref_price = df_agent.loc[mid, 'hpref_price'] # maximum price one can afford for rent
        self.hpref_price_buy = (self.income_yr*3) + self.wealth  # maximum price one can afford to buying a house
        self.com_access = df_agent.loc[mid, 'com_size']  # levels of the origin's community access easiness
        self.com_pref = df_agent.loc[mid, 'com']  # prefernce for the origin's community activity
        self.visaperiod = df_agent.loc[mid, 'visaperiod']  # initial visa period for myself (by rank)
        self.spouse_visaperiod = 0
        self.spouse_income_mth = 0
        self.spouse_rpe = df_agent.loc[mid, 'spouse_rpe']  # whether spouse needs recognition of prior experience
        self.spouse_g1 = df_agent.loc[mid, 'CSEP']  # whether spouse can have g1 stamp or not
        self.spouse_edu = df_agent.loc[mid, 'spouse_edu']  
        self.spouse_gender = df_agent.loc[mid, 'spouse_gender'] 
        self.spouse_age = df_agent.loc[mid, 'spouse_age'] 
        self.spouse_ppsnsubmitted = False
        self.spouse_rank = 0
        self.spouse_ppsn = False
        self.spouse_visasubmitted=False
        self.spouse_job_quetime=0
        self.job_quetime = 0 
        self.visasubmitted = False
        self.time = 0 
        self.hired = True
        self.spouse_hired = False
        self.spouse_workperiod = 0
        self.ap = 100 # action point for one day.
        self.hp = int(np.random.uniform(91, 100, 1))  # health point
        self.pregrate = np.random.uniform(0.05, 0.31, 1)
        self.birthrate = np.random.uniform(0.7, 0.95,1)
        self.bc_visit = 0
        self.hospital_satisfaction = 0
        self.disease_rate = (100-self.hp)*0.01
        self.ppsn = False
        self.ppsnsubmitted = False
        self.house = False
        self.residence = False 
        self.residsubmitted = False
        self.rent=False
        self.rentperiod = 0
        self.houseowner = False
        self.hloan_period = 0
        self.sickperiod = 0 
        self.sick = False
        self.postbirth = False
        self.prebirth = False
        self.postbirth_period = False 
        self.visa_queuing_time = 0
        self.preg_period = 0
        self.house_seeker = True
        self.job_seeker = True
        self.spouse_job_seeker = False
        self.bc_satisfaction = False
        self.workperiod = 0
        self.spouse_rpeaccepted = False
        self.spouse_rpesubmitted = False
        self.spouse_offered_income_mth = 0
        self.spouse_offered_rank = 0
        self.offered_income_mth = 0
        self.offered_rank = 0        

        self.unique_id = unique_id
   

    def move(self):                 ## need to limit the area applicants move around (later!)
        possible_steps = self.model.grid.get_neighborhood(
        self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
        self.ap = 100

    def ppsn_work(self):
        if (self.ppsn == False):
            if (self.ppsnsubmitted == False):
                if self.house == True:
                    if self.ap >=50:
                        self.ppsnsubmitted = True
                        self.ppsnquetime = int(np.random.normal(42, 3, 1))
                        self.ap -= 50 
            elif (self.ppsnsubmitted == True):
                if self.ppsnquetime <= 0:
                    self.ppsn = True 
                else:
                    self.ppsnquetime -= 1

    def spouse_ppsn_work(self):
        if self.spouse_hired == True:
            if (self.spouse_ppsn == False):
                if (self.spouse_ppsnsubmitted == False):
                    if self.house == True:
                        if self.ap >=50:
                            self.spouse_ppsnsubmitted = True
                            self.spouse_ppsnquetime = int(np.random.normal(42, 3, 1))
                            self.ap -= 50 
                elif (self.spouse_ppsnsubmitted == True):
                    if self.spouse_ppsnquetime <= 0:
                        self.spouse_ppsn = True 
                    else:
                        self.spouse_ppsnquetime -= 1

    def residence_permit(self):
        if self.residence == False:
            if self.residsubmitted == False:
                if self.ap >=50:
                    self.residsubmitted = True
                    self.residquetime = int(np.random.normal(28, 1, 1))            
                    self.ap -= 50 
                    self.wealth -= 200
            elif self.residsubmitted == True:
                if self.residquetime <=0:
                    self.residence = True 
                else:
                    self.residquetime -= 1   

    def aging(self):
        self.time += 1
        self.age += 1/365
        if self.age > 30:
            self.hp -= 1/365
            self.disease_rate = (100-self.hp)*0.01


    def earning(self):
        if self.hired == True:
            if self.ppsn == True:
                self.wealth += self.income_mth/30
                if self.spouse_hired == True:
                    if self.spouse_ppsn == True:
                        self.wealth += self.spouse_income_mth/30
                    else:
                        self.wealth += self.spouse_income_mth/30*0.6
            else:
                self.wealth += self.income_mth/30*0.6
                if self.spouse_hired == True:
                    if self.spouse_ppsn == True:
                        self.wealth += self.spouse_income_mth/30
                    else:
                        self.wealth += self.spouse_income_mth/30*0.6
    
    # def wealthrank(self):  # redefinition after one year
    #     if self.time > 365:
    #         if (self.income_mth*12) + (self.spouse_income_mth*12) > 110000:
    #             self.wealth_rank = 5
    #         elif ((self.income_mth*12) + (self.spouse_income_mth*12) <= 110000) & (((self.income_mth*12) + (self.spouse_income_mth*12)) > 67000):
    #             self.wealth_rank = 4
    #         elif ((self.income_mth*12) + (self.spouse_income_mth*12) <= 67000) & (((self.income_mth*12) + (self.spouse_income_mth*12)) > 48000):
    #             self.wealth_rank = 3
    #         elif ((self.income_mth*12) + (self.spouse_income_mth*12) <= 48000) & (((self.income_mth*12) + (self.spouse_income_mth*12)) > 39000):
    #             self.wealth_rank = 2  
    #         else:
    #             self.wealth_rank = 1         


    def spending(self):
        if (self.time > 0) & (isinstance(self.time, int)):
            self.wealth -= self.livcost/30
            if self.wealth_rank == 1:            ## tax
                self.wealth -= (self.income_mth + self.spouse_income_mth)/30*0.15
            elif self.wealth_rank == 2:  
                self.wealth -= (self.income_mth + self.spouse_income_mth)/30*0.2
            elif self.wealth_rank == 3:  
                self.wealth -= (self.income_mth + self.spouse_income_mth)/30*0.3
            elif self.wealth_rank == 4:  
                self.wealth -= (self.income_mth + self.spouse_income_mth)/30*0.4
            else:
                self.wealth -= (self.income_mth + self.spouse_income_mth)/30*0.55

    def house_spending(self):
        if (self.com_house == 3):
            if (self.house==False):  # permanently provided; initial point
                self.house = True 
                self.rent = True
                self.rent_price = 0
                self.rentperiod = 365
            else:
                if self.rent == True:
                    if self.rentperiod == 0: 
                        if self.rank == 1:      # short-term contract (1yr)
                            self.rent = False
                            self.house = False 
                            self.com_house = 1
                        elif self.rank == 2:   # long-term contract (3yrs)
                            if (self.time <= 365*2):
                                self.rentperiod = 365
                            else:
                                self.rent = False
                                self.house = False
                                self.com_house = 1 
                        else:
                            self.rentperiod = 365
                    elif self.rentperiod > 0:
                            self.rentperiod -= 1
                elif self.houseowner == True:
                        self.wealth -= self.hloan_price
                        self.hloan_period -= 1
        elif (self.com_house == 2):
            if self.house == False:
                if self.time == 1:  # temporarily provided. initial point
                    self.rent = True 
                    self.house = True
                    self.rentperiod = 60
                    self.rent_price = 0
                else:
                    self.wealth -= 60*math.ceil(self.n_fam/3)  # for hotel or hostel 
            elif (self.house == True):
                if self.rent == True:
                    if self.rentperiod <= 0:
                        self.rent = False
                        self.house = False
                    else:
                        self.rentperiod -= 1
                        self.wealth -= self.rent_price
                elif self.houseowner == True:
                        self.wealth -= self.hloan_price
                        self.hloan_period -= 1       
        elif (self.com_house == 1):   ## no support from company
            if (self.house==False):
                self.wealth -= 60*math.ceil(self.n_fam/3)  # for hotel or hostel
            else:
                if (self.rent == True):
                    if self.rentperiod <= 0:
                        self.rent = False
                        self.house = False 
                    else:
                        self.wealth -= self.rent_price
                        self.rentperiod -= 1
                elif self.houseowner == True:
                        self.wealth -= self.hloan_price
                        self.hloan_period -= 1  


    def house_rent(self):
        if self.com_house < 3:
            if (self.houseowner == False):
                if self.ap >=50:
                    if (self.rentperiod <=30) | (self.house==False):
                        self.ap -= 50
                        self.house_seeker = True
                        cell_agents = self.model.grid.get_cell_list_contents([self.pos])
                        econ = [obj for obj in cell_agents if isinstance(obj, econ_status)][0]
                        if np.random.choice([0,1], p = [econ.inflation_rate, (1-econ.inflation_rate)]) == 1:   # prob. of getting some rent options
                            # n_hopt = int(self.model.N_hopt/(1+econ.inflation_rate))
                            rent_options = np.random.uniform(0, 9999, 2)  ## rent options 
                            rent_options = rent_options.astype(int)
                            # option set
                            rent_optset = df_hrent.iloc[rent_options]
                            rent_optset['price_allowed'] = (rent_optset['hopt_price']*(1+econ.inflation_rate) <= self.hpref_price).astype(int)
                            rent_optset = rent_optset[rent_optset.price_allowed != 0]  # leave only those meeting one's price capacity
                            # compare the options set to one's preference set
                            if len(rent_optset) > 0:                 
                                rent_optset['score_dist'] = (rent_optset['hopt_dist'] >= self.hpref_dist).astype(int)  
                                rent_optset['score_edu'] = (rent_optset['hopt_edu'] >= self.hpref_edu).astype(int)
                                rent_optset['score_safe'] = (rent_optset['hopt_safe'] >= self.hpref_safe).astype(int)
                                rent_optset['score_nroom'] = (rent_optset['hopt_nroom'] >= self.hpref_nroom).astype(int)
                                rent_optset['score_fq'] = (rent_optset['hopt_fq'] >= self.hpref_fq).astype(int)
                                rent_optset['score_loc'] = (rent_optset['hopt_loc'] >= self.hpref_loc).astype(int)
                                # rent_optset['score_all'] = rent_optset.iloc[:, 8:13].sum(axis=1)
                                rent_optset = rent_optset.eval('score_all = score_dist + score_edu + score_safe + score_nroom + score_fq + score_loc')
                                rent_optset = rent_optset[rent_optset.score_all >= self.wealth_rank]  ## leave only those meeting one's preference set
                                if len(rent_optset) > 0:
                                    cell_agents = self.model.grid.get_cell_list_contents([self.pos])
                                    econ = [obj for obj in cell_agents if isinstance(obj, econ_status)][0]
                                    self.rent_price = (rent_optset.loc[rent_optset['hopt_price'].idxmin(axis=0), 'hopt_price'])*(1+econ.inflation_rate)/30  ## choose the cheapest one: monthly rent --> daily rent
                                    # cell_agents = self.model.grid.get_cell_list_contents([self.pos])
                                    # econ = [obj for obj in cell_agents if isinstance(obj, econ_status)][0]
                                    # self.rent_price += self.rent_price*(econ.inflation_rate)
                                    self.rent = True 
                                    self.house = True 
                                    self.rentperiod = 365
                                    self.house_seeker = False


    def house_buy(self):
        if self.visaperiod  > 365*3:
            if (self.rentperiod <= 90) | (self.house==False):
                if self.ap >= 50:
                    self.ap -= 50
                    self.house_seeker = True
                    cell_agents = self.model.grid.get_cell_list_contents([self.pos])
                    econ = [obj for obj in cell_agents if isinstance(obj, econ_status)][0]
                    if np.random.choice([0,1], p = [econ.inflation_rate, (1-econ.inflation_rate)]) == 1:   # prob. of getting some rent options
                        buy_options = np.random.uniform(0,9999, 2)  ## rent options 
                        buy_options = buy_options.astype(int)
                        # option set
                        buy_optset = df_hbuy.iloc[buy_options]
                        buy_optset['price_allowed'] = (buy_optset['hopt_price']*(1+econ.inflation_rate) <= self.hpref_price_buy).astype(int)
                        buy_optset = buy_optset[buy_optset.price_allowed != 0]  # leave only those meeting one's price capacity
                        # compare the options set to one's preference set
                        if len(buy_optset) > 0:                 
                            buy_optset['score_dist'] = (buy_optset['hopt_dist'] >= self.hpref_dist).astype(int)  
                            buy_optset['score_edu'] = (buy_optset['hopt_edu'] >= self.hpref_edu).astype(int)
                            buy_optset['score_safe'] = (buy_optset['hopt_safe'] >= self.hpref_safe).astype(int)
                            buy_optset['score_nroom'] = (buy_optset['hopt_nroom'] >= self.hpref_nroom).astype(int)
                            buy_optset['score_fq'] = (buy_optset['hopt_fq'] >= self.hpref_fq).astype(int)
                            buy_optset['score_loc'] = (buy_optset['hopt_loc'] >= self.hpref_loc).astype(int)
                            # buy_optset['score_all'] = buy_optset.iloc[:, 8:13].sum(axis=1)
                            buy_optset = buy_optset.eval('score_all = score_dist + score_edu + score_safe + score_nroom + score_fq + score_loc')
                            buy_optset = buy_optset[buy_optset.score_all >= self.wealth_rank]  ## leave only those meeting one's preference set
                            if len(buy_optset) > 0:
                                cell_agents = self.model.grid.get_cell_list_contents([self.pos])
                                econ = [obj for obj in cell_agents if isinstance(obj, econ_status)][0]
                                self.hloan_price = (buy_optset.loc[buy_optset['hopt_price'].idxmin(axis=0), 'hopt_price'])/20/365*(1+econ.inflation_rate)  ## choose the cheapest one; assume pay for 20 years
                                    # cell_agents = self.model.grid.get_cell_list_contents([self.pos])
                                    # econ = [obj for obj in cell_agents if isinstance(obj, econ_status)][0]
                                    # self.hloan_price += self.hloan_price*(econ.inflation_rate)
                                self.houseowner = True 
                                self.house = True
                                self.rent = False 
                                self.rentperiod = 0 
                                self.hloan_period = 365*20
                                self.house_seeker = False
    
    def health(self):
        if self.sick == True:
            if self.sickperiod > 1:
                self.ap = 0
                self.sickperiod -= 1
            elif self.sickperiod == 1:
                self.ap = 0
                self.sickperiod = 0
                self.sick = False
        else:
            if (np.random.choice([0,1], p = [(1 - self.disease_rate), self.disease_rate]) == 1):
                self.sick = True 
                self.ap = 0
                self.sickperiod = int(np.random.uniform(3,10,1))


    def hospital(self):
        if self.sick == True:
            if (np.random.choice([0,1], p = [(1-self.model.gp_rate), self.model.gp_rate]) == 1):  ## GP visit success or satisfied with GP  quality 
                self.sickperiod = 0
                self.hospital_satisfaction += 1
            else:
                self.hospital_satisfaction -= 1
                self.wealth -= 10  # cost for buying medicine

    def birth(self):
        if (self.marriage == True):
            if (self.prebirth == False):
                if self.age < 50:
                    # if np.random.choice([0,1], p = [0.8, 0.2]) == 1:   # pregnant rate
                    if np.random.choice([0,1], p = [(1-self.pregrate[0]), self.pregrate[0]]) == 1:   # pregnant rate
                        self.prebirth = True 
                        self.preg_period = int(np.random.normal(280, 3, 1))
            elif self.prebirth == True:
                if self.preg_period > 0:
                    self.preg_period -= 1
                elif self.preg_period == 0:
                    self.prebirth = False
                    if (np.random.choice([0,1], p = [0.1, 0.9]) == 1):  # birth rate
                        self.postbirth = True
                        self.postbirth_period = 0 
                        self.kid += 1
                    else:
                        self.postbirth = False
            elif self.postbirth == True:
                if self.postbirth_period < 180:
                    self.postbirth_period += 1
                else:
                    self.postbirth = False

    def birthcare(self):
        if self.prebirth == True:
            if self.ap >= 50:
                if self.bc_visit == 0:
                    if (np.random.choice([0,1], p = [(1-self.model.bc_quality), self.model.bc_quality]) == 1):  ## satisfaction of quality care
                        self.bc_satisfaction = True
                        self.bc_visit += 1
                        self.ap -= 50
                    else:
                        self.bc_visit += 1
                        self.bc_satisfaction = False
                        self.ap -= 50
                elif self.bc_visit == 1:
                    if self.bc_satisfaction == False:
                        self.birthrate = self.birthrate*0.8        # increase miscarriage rate
                        self.pregrate = self.pregrate*0.6         # decrease pregnancy rate
                        self.hp = self.hp*0.9              # decrease Health Point
                        self.bc_visit += 1
                        self.ap -= 50
                        self.wealth -= 1500         # insurance fee
        elif self.postbirth == True:
            if self.ap >= 50:
                if self.bc_satisfaction == False:
                    if self.bc_visit == 2:
                        self.hp = self.hp*0.9              # decrease Health Point
                        self.bc_visit += 1
                        self.ap -= 50
                        self.wealth -= 900                 # insurance fee     
        elif self.postbirth == False:
            if self.bc_satisfaction == False:
                if self.bc_visit == 3:
                    self.hp =  self.hp*100/81  # recovery when going back to the normal
                    self.bc_visit += 1

    def childcare(self):
        if (self.kid > 0):
            if (self.com_child == 1):
                self.child_care = True 
            else:
                if self.child_care == False:
                    if (np.random.choice([0,1], p = [(1-self.model.childcare_rate), self.model.childcare_rate]) == 1):
                        self.child_care = True
                    else:
                        self.wealth -= 60*self.kid ## on average, 8 euro/hour per kid.
                else: 
                    self.wealth -= 25*self.kid ## on average, when using public child care system, 25 euros per day
    
    def spouse_recognition(self):
        if self.marriage == True:
            if self.spouse_rpe == 1:
                if self.spouse_rpeaccepted == False:
                    if self.spouse_rpesubmitted == False:
                        if self.ap >= 50:
                            self.spouse_rpesubmitted = True 
                            self.spouse_rpequetime = int(np.random.normal(90, 1, 1))
                            self.ap -= 50
                            self.wealth -= 300
                    elif self.spouse_rpesubmitted == True:
                        if self.spouse_rpequetime > 0:
                            self.spouse_rpequetime -= 1
                        else:
                            if np.random.choice([0,1], p = [(1-self.model.spouse_rpe_acceptrate), self.model.spouse_rpe_acceptrate]) == 1:
                                self.spouse_rpeaccepted = True
                                self.spouse_rpefailed = True



    def spouse_permit(self):
        if self.marriage == True:
            if self.spouse_rpe == 0:
                if self.spouse_g1 == 1:         # case 1: G1 stamp & don't need rpe.
                    if self.visaperiod >= 180:          # if the CSEP's visa period is less than 6 months, it is meaningless for the spouse to seek jobs using G1 stamp.
                        if (self.spouse_hired == False) | (self.spouse_workperiod > self.model.probation_period):
                            if self.house == True:
                                if self.ap >= 50:
                                    self.ap -= 50
                                    self.spouse_job_seeker = True
                                    self.spouse_job_quetime = int(np.random.normal(7, 1, 1))
                                    if self.spouse_job_quetime > 0:
                                        self.spouse_job_quetime -= 1
                                    else: 
                                        cell_agents = self.model.grid.get_cell_list_contents([self.pos])
                                        econ = [obj for obj in cell_agents if isinstance(obj, econ_status)][0]
                                        if np.random.choice([0,1], p = [econ.jobcomp_rate, (1-econ.jobcomp_rate)]) == 1:  
                                            job_options = np.random.uniform(0, len(df_job), 2)  ## job options: because of G1 stamp, more opportunities given
                                            job_options = job_options.astype(int)
                                            # option set
                                            job_optset = df_job.iloc[job_options]
                                            job_optset['gender'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['gender_prob']),x["gender_prob"]])[0][0], axis=1)  ## assign target gender
                                            job_optset['salary'] = job_optset.apply(lambda x: np.random.normal(x['salary_mean'], x['salary_sd'], 1)[0], axis=1)  ## assign  salary
                                            job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu) & (job_optset['gender'] == self.spouse_gender) & (job_optset['edu_max']+1 >= self.spouse_edu)).astype(int)
                                            # job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu)).astype(int)
                                            job_optset = job_optset[job_optset.eligible != 0]  # leave only those meeting one's eligibility by education level
                                            # compare the options set to one's preference set
                                            if len(job_optset) > 0:
                                                job_optset['selected'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['hpr']), x["hpr"]])[0][0], axis=1)  ## submit application and see the results!
                                                job_optset = job_optset[job_optset.selected == 1]
                                                if len(job_optset) > 0:
                                                    # job_optset = job_optset.loc[job_optset['salary'].idxmax()]   # Because this spouse has G1 stamp, no need permit.
                                                    job_optset = job_optset[job_optset['salary']==job_optset['salary'].max()]
                                                        # self.spouse_offered_rank = job_optset.loc[job_optset['salary'].idxmax(),'rank'] 
                                                    self.spouse_offered_rank = job_optset['rank'].values[0]
                                                    self.spouse_offered_income_mth = job_optset.loc[job_optset['salary'].idxmax(),'salary']/12            # series often do not work. so try to use as a DF. 
                                                    if self.spouse_rank <= self.spouse_offered_rank:
                                                        if (self.spouse_rank < 3):
                                                            self.spouse_hired = True
                                                            self.spouse_rank = self.spouse_offered_rank
                                                            self.spouse_job_seeker = False
                                                            if (self.spouse_rank == 1):
                                                                self.spouse_income_mth = self.spouse_offered_income_mth*0.9
                                                                self.spouse_visaperiod = min(365, self.visaperiod)      # short-term position
                                                            elif (self.spouse_rank == 2):
                                                                self.spouse_income_mth = self.spouse_offered_income_mth
                                                                self.spouse_visaperiod = min(365*3, self.visaperiod)    # long-term position
                                                        elif self.spouse_rank == 3:
                                                            if ((self.spouse_income_mth) < self.spouse_offered_income_mth*1.2):
                                                                self.spouse_hired = True
                                                                self.spouse_job_seeker = False
                                                                self.spouse_rank = self.spouse_offered_rank
                                                                self.spouse_visaperiod = min((65-self.spouse_age+1)*365, self.visaperiod)
                                                                self.spouse_income_mth = self.spouse_offered_income_mth*1.2
                    elif self.visaperiod < 180:
                        if self.time > self.model.probation_period:
                            if (self.spouse_hired == False) | (self.spouse_workperiod > self.model.probation_period):
                                if self.spouse_visasubmitted == False:
                                    if self.ap >= 50:
                                        self.ap -= 50
                                        self.spouse_job_seeker = True
                                        self.spouse_job_quetime = int(np.random.normal(7, 1, 1))
                                        if self.spouse_job_quetime > 0:
                                            self.spouse_job_quetime -= 1
                                        else: 
                                            cell_agents = self.model.grid.get_cell_list_contents([self.pos])
                                            econ = [obj for obj in cell_agents if isinstance(obj, econ_status)][0]
                                            if np.random.choice([0,1], p = [econ.jobcomp_rate, (1-econ.jobcomp_rate)]) == 1:  
                                                    job_options = np.random.uniform(0, len(df_job), 1)  ## job options: do not have G1, so the possible number of options will decrease.
                                                    job_options = job_options.astype(int)
                                                    # option set
                                                    job_optset = df_job.iloc[job_options]
                                                    job_optset['gender'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['gender_prob']),x["gender_prob"]])[0][0], axis=1)  ## assign target gender
                                                    job_optset['salary'] = job_optset.apply(lambda x: np.random.normal(x['salary_mean'], x['salary_sd'], 1)[0], axis=1)  ## assign  salary
                                                    job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu) & (job_optset['gender'] == self.spouse_gender) & (job_optset['edu_max']+1 >= self.spouse_edu)).astype(int)
                                                    # job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu)).astype(int)
                                                    job_optset = job_optset[job_optset.eligible != 0]  # leave only those meeting one's eligibility by education level
                                                    # compare the options set to one's preference set
                                                    if len(job_optset) > 0:
                                                        job_optset['selected'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['hpr']), x["hpr"]])[0][0], axis=1)  ## submit application and see the results!
                                                        job_optset = job_optset[job_optset.selected == 1]
                                                        if len(job_optset) > 0:
                                                            # job_optset = job_optset.loc[job_optset['salary'].idxmax(axis=0)]   # Because this spouse has no G1 stamp, need to get a permit.
                                                            job_optset = job_optset[job_optset['salary']==job_optset['salary'].max()]
                                                                # self.spouse_offered_rank = job_optset.loc[job_optset['salary'].idxmax(),'rank'] 
                                                            self.spouse_offered_rank = job_optset['rank'].values[0]
                                                            self.spouse_offered_income_mth = job_optset.loc[job_optset['salary'].idxmax(),'salary']/12    
                                                            if (self.spouse_rank <= self.spouse_offered_rank):
                                                                if self.spouse_rank < 3:
                                                                    self.spouse_visasubmitted = True                # apply for the work permit
                                                                    self.spouse_visaquetime = int(np.random.normal(90, 1, 1))
                                                                elif self.spouse_rank == 3:
                                                                    if self.spouse_income_mth < self.spouse_offered_income_mth*1.2:
                                                                        self.spouse_visasubmitted = True                # apply for the work permit
                                                                        self.spouse_visaquetime = int(np.random.normal(90, 1, 1))

                                elif self.spouse_visasubmitted == True:
                                    if self.spouse_visaquetime > 0:
                                        self.spouse_visaquetime -= 1
                                    else:
                                        self.spouse_visasubmitted = False
                                        if self.spouse_offered_rank == 1:
                                            if np.random.choice([0,1], p = [(1-self.model.visa_acceptrate*0.9), self.model.visa_acceptrate*0.9]) == 1:  # work permit decision with a bit lower success rate compared to long-term or permanent position.
                                                self.spouse_hired = True
                                                self.spouse_job_seeker = False
                                                self.spouse_workperiod = 0
                                                self.spouse_rank = self.spouse_offered_rank
                                                self.spouse_visaperiod = 365
                                                self.spouse_income_mth = self.spouse_offered_income_mth*0.9
                                            else:
                                                self.spouse_offered_rank = 0
                                                self.spouse_offered_income_mth = 0
                                        else:
                                            if np.random.choice([0,1], p = [(1-self.model.visa_acceptrate), self.model.visa_acceptrate]) == 1:
                                                self.spouse_hired = True
                                                self.spouse_job_seeker = False
                                                self.spouse_workperiod = 0
                                                self.spouse_rank = self.spouse_offered_rank
                                                if self.spouse_rank == 2:
                                                    self.spouse_visaperiod = 365*3
                                                    self.spouse_income_mth = self.spouse_offered_income_mth
                                                elif self.spouse_rank == 3:
                                                    self.spouse_income_mth = self.spouse_offered_income_mth*1.2
                                                    self.spouse_visaperiod = (65-self.spouse_age+1)*365
                                            else:
                                                self.spouse_offered_rank = 0
                                                self.spouse_offered_income_mth = 0                               
                elif (self.spouse_g1 == 0):                                                   # case 2: without G1 stamp or G1 stamp less than 6 month
                    if self.time > self.model.probation_period:
                        if (self.spouse_hired == False) | (self.spouse_workperiod > self.model.probation_period):
                            if self.spouse_visasubmitted == False:
                                if self.house==True:
                                        if self.ap >= 50:
                                            self.ap -= 50
                                            self.spouse_job_seeker = True
                                            self.spouse_job_quetime = int(np.random.normal(7, 1, 1))
                                            if self.spouse_job_quetime > 0:
                                                self.spouse_job_quetime -= 1
                                            else:                                         
                                                cell_agents = self.model.grid.get_cell_list_contents([self.pos])
                                                econ = [obj for obj in cell_agents if isinstance(obj, econ_status)][0]
                                                if np.random.choice([0,1], p = [econ.jobcomp_rate, (1-econ.jobcomp_rate)]) == 1:  
                                                    job_options = np.random.uniform(0, len(df_job), 1)  ## job options: do not have G1, so the possible number of options will decrease.
                                                    job_options = job_options.astype(int)
                                                    # option set
                                                    job_optset = df_job.iloc[job_options]
                                                    job_optset['gender'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['gender_prob']),x["gender_prob"]])[0][0], axis=1)  ## assign target gender
                                                    job_optset['salary'] = job_optset.apply(lambda x: np.random.normal(x['salary_mean'], x['salary_sd'], 1)[0], axis=1)  ## assign  salary
                                                    job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu) & (job_optset['gender'] == self.spouse_gender) & (job_optset['edu_max']+1 >= self.spouse_edu)).astype(int)
                                                    # job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu)).astype(int)
                                                    job_optset = job_optset[job_optset.eligible != 0]  # leave only those meeting one's eligibility by education level
                                                    # compare the options set to one's preference set
                                                    if len(job_optset) > 0:
                                                        job_optset['selected'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['hpr']), x["hpr"]])[0][0], axis=1)  ## submit application and see the results!
                                                        job_optset = job_optset[job_optset.selected == 1]
                                                        if len(job_optset) > 0:
                                                            # job_optset = job_optset.loc[job_optset['salary'].idxmax(axis=0)]   # Because this spouse has no G1 stamp, need to get a permit.
                                                            job_optset = job_optset[job_optset['salary']==job_optset['salary'].max()]
                                                                # self.spouse_offered_rank = job_optset.loc[job_optset['salary'].idxmax(),'rank'] 
                                                            self.spouse_offered_rank = job_optset['rank'].values[0]
                                                            self.spouse_offered_income_mth = job_optset.loc[job_optset['salary'].idxmax(),'salary']/12  
                                                            if (self.spouse_rank <= self.spouse_offered_rank):
                                                                if self.spouse_rank < 3:
                                                                    self.spouse_visasubmitted = True                # apply for the work permit
                                                                    self.spouse_visaquetime = int(np.random.normal(90, 1, 1))
                                                                elif self.spouse_rank == 3:
                                                                    if self.spouse_income_mth < self.spouse_offered_income_mth*1.2:
                                                                        self.spouse_visasubmitted = True                # apply for the work permit
                                                                        self.spouse_visaquetime = int(np.random.normal(90, 1, 1))

                            elif self.spouse_visasubmitted == True:
                                if self.spouse_visaquetime > 0:
                                    self.spouse_visaquetime -= 1
                                else:
                                    self.spouse_visasubmitted = False
                                    if self.spouse_offered_rank == 1:
                                        if np.random.choice([0,1], p = [(1-self.model.visa_acceptrate*0.9), self.model.visa_acceptrate*0.9]) == 1:  # work permit decision with a bit lower success rate compared to long-term or permanent position.
                                            self.spouse_hired = True
                                            self.spouse_job_seeker = False
                                            self.spouse_workperiod = 0
                                            self.spouse_rank = self.spouse_offered_rank
                                            self.spouse_visaperiod = 365
                                            self.spouse_income_mth = self.spouse_offered_income_mth*0.9    
                                        else: 
                                            self.spouse_offered_rank = 0
                                            self.spouse_offered_income_mth = 0
                                    else:
                                        if np.random.choice([0,1], p = [(1-self.model.visa_acceptrate), self.model.visa_acceptrate]) == 1:
                                            self.spouse_hired = True
                                            self.spouse_job_seeker = False
                                            self.spouse_workperiod = 0
                                            self.spouse_rank = self.spouse_offered_rank
                                            if self.spouse_rank == 2:
                                                self.spouse_visaperiod = 365*3
                                                self.spouse_income_mth = self.spouse_offered_income_mth
                                            elif self.spouse_rank == 3:
                                                    self.spouse_income_mth = self.spouse_offered_income_mth*1.2
                                                    self.spouse_visaperiod = (65-self.spouse_age+1)*365
                                        else:
                                            self.spouse_offered_rank = 0
                                            self.spouse_offered_income_mth = 0   

            elif self.spouse_rpe == 1:                                                ## case 3: those who successfully got RPE & G1 stamp
                if self.spouse_rpeaccepted == True:
                    if self.spouse_g1 == 1:         # case 1: G1 stamp & don't need rpe.
                        if self.visaperiod >= 180:          # if the CSEP's visa period is less than 6 months, it is meaningless for the spouse to seek jobs using G1 stamp.
                            if (self.spouse_hired == False) | (self.spouse_workperiod > self.model.probation_period):
                                if self.house==True:
                                    if self.ap >= 50:
                                        self.ap -= 50
                                        self.spouse_job_seeker = True
                                        self.spouse_job_quetime = int(np.random.normal(7, 1, 1))
                                        if self.spouse_job_quetime > 0:
                                            self.spouse_job_quetime -= 1
                                        else:                                         
                                            cell_agents = self.model.grid.get_cell_list_contents([self.pos])
                                            econ = [obj for obj in cell_agents if isinstance(obj, econ_status)][0]
                                            if np.random.choice([0,1], p = [econ.jobcomp_rate, (1-econ.jobcomp_rate)]) == 1:  
                                                job_options = np.random.uniform(0, len(df_job), 2)  ## job options: because of G1 stamp, more opportunities given
                                                job_options = job_options.astype(int)
                                                # option set
                                                job_optset = df_job.iloc[job_options]
                                                job_optset['gender'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['gender_prob']),x["gender_prob"]])[0][0], axis=1)  ## assign target gender
                                                job_optset['salary'] = job_optset.apply(lambda x: np.random.normal(x['salary_mean'], x['salary_sd'], 1)[0], axis=1)  ## assign  salary
                                                job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu) & (job_optset['gender'] == self.spouse_gender) & (job_optset['edu_max']+1 >= self.spouse_edu)).astype(int)
                                                # job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu)).astype(int)
                                                job_optset = job_optset[job_optset.eligible != 0]  # leave only those meeting one's eligibility by education level
                                                # compare the options set to one's preference set
                                                if len(job_optset) > 0:
                                                    job_optset['selected'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['hpr']), x["hpr"]])[0][0], axis=1)  ## submit application and see the results!
                                                    job_optset = job_optset[job_optset.selected == 1]
                                                    if len(job_optset) > 0:
                                                        # job_optset = job_optset.loc[job_optset['salary'].idxmax(axis=0)]   # Because this spouse has G1 stamp, no need permit.
                                                        job_optset = job_optset[job_optset['salary']==job_optset['salary'].max()]
                                                        # self.spouse_offered_rank = job_optset.loc[job_optset['salary'].idxmax(),'rank'] 
                                                        self.spouse_offered_rank = job_optset['rank'].values[0]
                                                        self.spouse_offered_income_mth = job_optset.loc[job_optset['salary'].idxmax(),'salary']/12  
                                                        if self.spouse_rank <= self.spouse_offered_rank:
                                                            if self.spouse_rank < 3:
                                                                self.spouse_hired = True
                                                                self.spouse_job_seeker = False
                                                                self.spouse_rank = self.spouse_offered_rank
                                                                if self.spouse_rank == 1:
                                                                    self.spouse_income_mth = self.spouse_offered_income_mth*0.9
                                                                    self.spouse_visaperiod = min(365, self.visaperiod)      # short-term position
                                                                elif self.spouse_rank == 2:
                                                                    self.spouse_income_mth = self.spouse_offered_income_mth
                                                                    self.spouse_visaperiod = min(365*3, self.visaperiod)    # long-term position
                                                                else:                                                       
                                                                    self.spouse_income_mth = self.spouse_offered_income_mth*1.2
                                                                    self.spouse_visaperiod = min((65-self.spouse_age+1)*365, self.visaperiod)
                                                            elif self.spouse_rank == 3:
                                                                if (self.spouse_income_mth < self.spouse_offered_income_mth*1.2):
                                                                    self.spouse_hired = True
                                                                    self.spouse_job_seeker = False
                                                                    self.spouse_rank = self.spouse_offered_rank
                                                                    self.spouse_visaperiod = min((65-self.spouse_age+1)*365, self.visaperiod)
                                                                    self.spouse_income_mth = self.spouse_offered_income_mth*1.2
                        else:
                            if self.time > self.model.probation_period:
                                if (self.spouse_hired == False) | (self.spouse_workperiod > self.model.probation_period):
                                    if self.spouse_visasubmitted == False:
                                        if self.house==True:
                                            if self.ap >= 50:
                                                self.ap -= 50
                                                self.spouse_job_seeker = True
                                                cell_agents = self.model.grid.get_cell_list_contents([self.pos])
                                                econ = [obj for obj in cell_agents if isinstance(obj, econ_status)][0]
                                                if np.random.choice([0,1], p = [econ.jobcomp_rate, (1-econ.jobcomp_rate)]) == 1:  
                                                    job_options = np.random.uniform(0, len(df_job), 1)  ## job options: do not have G1, so the possible number of options will decrease.
                                                    job_options = job_options.astype(int)
                                                    # option set
                                                    job_optset = df_job.iloc[job_options]
                                                    job_optset['gender'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['gender_prob']),x["gender_prob"]])[0][0], axis=1)  ## assign target gender
                                                    job_optset['salary'] = job_optset.apply(lambda x: np.random.normal(x['salary_mean'], x['salary_sd'], 1)[0], axis=1)  ## assign  salary
                                                    job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu) & (job_optset['gender'] == self.spouse_gender) & (job_optset['edu_max']+1 >= self.spouse_edu)).astype(int)
                                                    # job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu)).astype(int)
                                                    job_optset = job_optset[job_optset.eligible != 0]  # leave only those meeting one's eligibility by education level
                                                    # compare the options set to one's preference set
                                                    if len(job_optset) > 0:
                                                        job_optset['selected'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['hpr']), x["hpr"]])[0][0], axis=1)  ## submit application and see the results!
                                                        job_optset = job_optset[job_optset.selected == 1]
                                                        if len(job_optset) > 0:
                                                            # job_optset = job_optset.loc[job_optset['salary'].idxmax(axis=0)]   # 
                                                            job_optset = job_optset[job_optset['salary']==job_optset['salary'].max()]
                                                                # self.spouse_offered_rank = job_optset.loc[job_optset['salary'].idxmax(),'rank'] 
                                                            self.spouse_offered_rank = job_optset['rank'].values[0]
                                                            self.spouse_offered_income_mth = job_optset.loc[job_optset['salary'].idxmax(),'salary']/12 
                                                            if (self.spouse_rank <= self.spouse_offered_rank):
                                                                if self.spouse_rank < 3:
                                                                    self.spouse_visasubmitted = True                # apply for the work permit
                                                                    self.spouse_visaquetime = int(np.random.normal(90, 1, 1))
                                                                elif self.spouse_rank == 3:
                                                                    if self.spouse_income_mth < self.spouse_offered_income_mth*1.2:
                                                                        self.spouse_visasubmitted = True                # apply for the work permit
                                                                        self.spouse_visaquetime = int(np.random.normal(90, 1, 1))
                                    elif self.spouse_visasubmitted == True:
                                        if self.spouse_visaquetime > 0:
                                            self.spouse_visaquetime -= 1
                                        else:
                                            self.spouse_visasubmitted = False
                                            if self.spouse_offered_rank == 1:
                                                if np.random.choice([0,1], p = [(1-self.model.visa_acceptrate*0.9), self.model.visa_acceptrate*0.9]) == 1:  # work permit decision with a bit lower success rate compared to long-term or permanent position.
                                                    self.spouse_hired = True
                                                    self.spouse_job_seeker = False
                                                    self.spouse_workperiod = 0
                                                    self.spouse_rank = self.spouse_offered_rank
                                                    self.spouse_visaperiod = 365
                                                    self.spouse_income_mth = self.spouse_offered_income_mth*0.9
                                                    
                                                else:
                                                    self.spouse_offered_rank = 0
                                                    self.spouse_offered_income_mth = 0
                                            else:
                                                if np.random.choice([0,1], p = [(1-self.model.visa_acceptrate), self.model.visa_acceptrate]) == 1:
                                                    self.spouse_hired = True
                                                    self.spouse_job_seeker = False
                                                    self.spouse_workperiod = 0
                                                    self.spouse_rank = self.spouse_offered_rank
                                                    if self.spouse_rank == 2:
                                                        self.spouse_visaperiod = 365*3
                                                        self.spouse_income_mth = self.spouse_offered_income_mth
                                                    elif self.spouse_rank == 3:
                                                            self.spouse_income_mth = self.spouse_offered_income_mth*1.2
                                                            self.spouse_visaperiod = (65-self.spouse_age+1)*365
                                                else:
                                                    self.spouse_offered_rank = 0
                                                    self.spouse_offered_income_mth = 0   
                    elif (self.spouse_g1 == 0) :                                                   # case 4: those who successfully got RPE but no G1 stamp
                        if self.time > self.model.probation_period:
                            if (self.spouse_hired == False) | (self.spouse_workperiod > self.model.probation_period):
                                if self.spouse_visasubmitted == False:
                                    if self.house==True:
                                        if self.ap >= 50:
                                            self.ap -= 50
                                            self.spouse_job_seeker = True
                                            self.spouse_job_quetime = int(np.random.normal(7, 1, 1))
                                            if self.spouse_job_quetime > 0:
                                                self.spouse_job_quetime -= 1
                                            else:                                             
                                                cell_agents = self.model.grid.get_cell_list_contents([self.pos])
                                                econ = [obj for obj in cell_agents if isinstance(obj, econ_status)][0]
                                                if np.random.choice([0,1], p = [econ.jobcomp_rate, (1-econ.jobcomp_rate)]) == 1:  
                                                    job_options = np.random.uniform(0, len(df_job), 1)  ## job options: do not have G1, so the possible number of options will decrease.
                                                    job_options = job_options.astype(int)
                                                    # option set
                                                    job_optset = df_job.iloc[job_options]
                                                    job_optset['gender'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['gender_prob']),x["gender_prob"]])[0][0], axis=1)  ## assign target gender
                                                    job_optset['salary'] = job_optset.apply(lambda x: np.random.normal(x['salary_mean'], x['salary_sd'], 1)[0], axis=1)  ## assign  salary
                                                    job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu) & (job_optset['gender'] == self.spouse_gender) & (job_optset['edu_max']+1 >= self.spouse_edu)).astype(int)
                                                    # job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu)).astype(int)
                                                    job_optset = job_optset[job_optset.eligible != 0]  # leave only those meeting one's eligibility by education level
                                                    # compare the options set to one's preference set
                                                    if len(job_optset) > 0:
                                                        job_optset['selected'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['hpr']), x["hpr"]])[0][0], axis=1)  ## submit application and see the results!
                                                        job_optset = job_optset[job_optset.selected == 1]
                                                        if len(job_optset) > 0:
                                                            # job_optset = job_optset.loc[job_optset['salary'].idxmax(axis=0)]   # Because this spouse has no G1 stamp, need to get a permit.
                                                            job_optset = job_optset[job_optset['salary']==job_optset['salary'].max()]
                                                                # self.spouse_offered_rank = job_optset.loc[job_optset['salary'].idxmax(),'rank'] 
                                                            self.spouse_offered_rank = job_optset['rank'].values[0]
                                                            self.spouse_offered_income_mth = job_optset.loc[job_optset['salary'].idxmax(),'salary']/12 
                                                            if (self.spouse_rank <= self.spouse_offered_rank):
                                                                if self.spouse_rank < 3:
                                                                        self.spouse_visasubmitted = True                # apply for the work permit
                                                                        self.spouse_visaquetime = int(np.random.normal(90, 1, 1))
                                                                elif self.spouse_rank == 3:
                                                                    if self.spouse_income_mth < self.spouse_offered_income_mth*1.2:
                                                                        self.spouse_visasubmitted = True                # apply for the work permit
                                                                        self.spouse_visaquetime = int(np.random.normal(90, 1, 1))

                                elif self.spouse_visasubmitted == True:
                                    if self.spouse_visaquetime > 0:
                                        self.spouse_visaquetime -= 1
                                    else:
                                        self.spouse_visasubmitted = False 
                                        if self.spouse_offered_rank == 1:
                                            if np.random.choice([0,1], p = [(1-self.model.visa_acceptrate*0.9), self.model.visa_acceptrate*0.9]) == 1:  # work permit decision with a bit lower success rate compared to long-term or permanent position.
                                                self.spouse_hired = True
                                                self.spouse_job_seeker = False
                                                self.spouse_workperiod = 0
                                                self.spouse_rank = self.spouse_offered_rank
                                                self.spouse_visaperiod = 365
                                                self.spouse_income_mth = self.spouse_offered_income_mth*0.9
                                            else:
                                                self.spouse_offered_rank = 0
                                                self.spouse_offered_income_mth = 0
                                        else:
                                            if np.random.choice([0,1], p = [(1-self.model.visa_acceptrate), self.model.visa_acceptrate]) == 1:
                                                self.spouse_hired = True
                                                self.spouse_job_seeker = False
                                                self.spouse_workperiod = 0
                                                self.spouse_rank = self.spouse_offered_rank
                                                if self.spouse_rank == 2:
                                                    self.spouse_visaperiod = 365*3
                                                    self.spouse_income_mth = self.spouse_offered_income_mth
                                                elif self.spouse_rank == 3:
                                                        self.spouse_income_mth = self.spouse_offered_income_mth*1.2
                                                        self.spouse_visaperiod = (65-self.spouse_age+1)*365
                                            else:
                                                
                                                self.spouse_offered_rank = 0
                                                self.spouse_offered_income_mth = 0   

                elif self.spouse_rpeaccepted == False:                                          # Case 5: RPE needed but failed getting RPE; with G1
                    if self.spouse_g1 == 1:         # case 1: G1 stamp & don't need rpe.
                        if self.visaperiod >= 180:          # if the CSEP's visa period is less than 6 months, it is meaningless for the spouse to seek jobs using G1 stamp.
                            if (self.spouse_hired == False) | (self.spouse_workperiod > self.model.probation_period):
                                if self.house==True:
                                    if self.ap >= 50:
                                        self.ap -= 50
                                        self.spouse_job_seeker = True
                                        self.spouse_job_quetime = int(np.random.normal(7, 1, 1))
                                        if self.spouse_job_quetime > 0:
                                            self.spouse_job_quetime -= 1
                                        else:                                         
                                            cell_agents = self.model.grid.get_cell_list_contents([self.pos])
                                            econ = [obj for obj in cell_agents if isinstance(obj, econ_status)][0]
                                            if np.random.choice([0,1], p = [econ.jobcomp_rate, (1-econ.jobcomp_rate)]) == 1:  
                                                job_options = np.random.uniform(0, len(df_job), 2)  ## job options: because of G1 stamp, more opportunities given
                                                job_options = job_options.astype(int)
                                                # option set
                                                job_optset = df_job.iloc[job_options]
                                                job_optset = job_optset[job_optset.rpe_needed == 0]  # leave only those not requiring RPE
                                                if len(job_optset) > 0:
                                                    job_optset['gender'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['gender_prob']),x["gender_prob"]])[0][0], axis=1)  ## assign target gender
                                                    job_optset['salary'] = job_optset.apply(lambda x: np.random.normal(x['salary_mean'], x['salary_sd'], 1)[0], axis=1)  ## assign  salary
                                                    job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu) & (job_optset['gender'] == self.spouse_gender) & (job_optset['edu_max']+1 >= self.spouse_edu)).astype(int)
                                                    # job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu)).astype(int)
                                                    job_optset = job_optset[job_optset.eligible != 0]  # leave only those meeting one's eligibility by education level
                                                    # compare the options set to one's preference set
                                                    if len(job_optset) > 0:
                                                        job_optset['selected'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['hpr']), x["hpr"]])[0][0], axis=1)  ## submit application and see the results!
                                                        job_optset = job_optset[job_optset.selected == 1]
                                                        if len(job_optset) > 0:
                                                            # job_optset = job_optset.loc[job_optset['salary'].idxmax(axis=0)]   # Because this spouse has G1 stamp, no need permit.
                                                            job_optset = job_optset[job_optset['salary']==job_optset['salary'].max()]
                                                                # self.spouse_offered_rank = job_optset.loc[job_optset['salary'].idxmax(),'rank'] 
                                                            self.spouse_offered_rank = job_optset['rank'].values[0] 
                                                            self.spouse_offered_income_mth = job_optset.loc[job_optset['salary'].idxmax(),'salary']/12 
                                                            if (self.spouse_rank <= self.spouse_offered_rank) :
                                                                if self.spouse_rank < 3:
                                                                    self.spouse_hired = True
                                                                    self.spouse_job_seeker = False
                                                                    self.spouse_rank = self.spouse_offered_rank
                                                                    if (self.spouse_rank == 1):
                                                                        self.spouse_income_mth = self.spouse_offered_income_mth*0.9
                                                                        self.spouse_visaperiod = min(365, self.visaperiod)      # short-term position
                                                                    elif (self.spouse_rank == 2):
                                                                        self.spouse_income_mth = self.spouse_offered_income_mth
                                                                        self.spouse_visaperiod = min(365*3, self.visaperiod)    # long-term position
                                                                elif self.spouse_rank == 3:
                                                                    if self.spouse_income_mth < self.spouse_offered_income_mth*1.2:
                                                                        self.spouse_hired = True
                                                                        self.spouse_job_seeker = False
                                                                        self.spouse_rank = self.spouse_offered_rank
                                                                        self.spouse_visaperiod = min((65-self.spouse_age+1)*365, self.visaperiod)
                                                                        self.spouse_income_mth = self.spouse_offered_income_mth*1.2
                        elif  (self.visaperiod < 180):
                            if self.time > self.model.probation_period:
                                if (self.spouse_hired == False) | (self.spouse_workperiod > self.model.probation_period):
                                    if self.spouse_visasubmitted == False:
                                        if self.house==True:
                                            if self.ap >= 50:
                                                self.ap -= 50
                                                self.spouse_job_seeker = True
                                                cell_agents = self.model.grid.get_cell_list_contents([self.pos])
                                                econ = [obj for obj in cell_agents if isinstance(obj, econ_status)][0]
                                                if np.random.choice([0,1], p = [econ.jobcomp_rate, (1-econ.jobcomp_rate)]) == 1:  
                                                    job_options = np.random.uniform(0, len(df_job), 1)  ## job options: do not have G1, so the possible number of options will decrease.
                                                    job_options = job_options.astype(int)
                                                    # option set
                                                    job_optset = df_job.iloc[job_options]
                                                    job_optset = job_optset[job_optset.rpe_needed == 0]  # leave only those not requiring RPE
                                                    job_optset['gender'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['gender_prob']),x["gender_prob"]])[0][0], axis=1)  ## assign target gender
                                                    job_optset['salary'] = job_optset.apply(lambda x: np.random.normal(x['salary_mean'], x['salary_sd'], 1)[0], axis=1)  ## assign  salary
                                                    job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu) & (job_optset['gender'] == self.spouse_gender) & (job_optset['edu_max']+1 >= self.spouse_edu)).astype(int)
                                                    # job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu)).astype(int)
                                                    job_optset = job_optset[job_optset.eligible != 0]  # leave only those meeting one's eligibility by education level
                                                    # compare the options set to one's preference set
                                                    if len(job_optset) > 0:
                                                        job_optset['selected'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['hpr']), x["hpr"]])[0][0], axis=1)  ## submit application and see the results!
                                                        job_optset = job_optset[job_optset.selected == 1]
                                                        if len(job_optset) > 0:
                                                            # job_optset = job_optset.loc[job_optset['salary'].idxmax(axis=0)]   # Because this spouse has no G1 stamp, need to get a permit.
                                                            job_optset = job_optset[job_optset['salary']==job_optset['salary'].max()]
                                                                # self.spouse_offered_rank = job_optset.loc[job_optset['salary'].idxmax(),'rank'] 
                                                            self.spouse_offered_rank = job_optset['rank'].values[0]
                                                            self.spouse_offered_income_mth = job_optset.loc[job_optset['salary'].idxmax(),'salary']/12 
                                                            if (self.spouse_rank <= self.spouse_offered_rank):
                                                                if self.spouse_rank < 3:
                                                                    self.spouse_visasubmitted = True                # apply for the work permit
                                                                    self.spouse_visaquetime = int(np.random.normal(90, 1, 1))
                                                                elif self.spouse_rank == 3:
                                                                    if self.spouse_income_mth < self.spouse_offered_income_mth*1.2:
                                                                        self.spouse_visasubmitted = True                # apply for the work permit
                                                                        self.spouse_visaquetime = int(np.random.normal(90, 1, 1))

                                    elif self.spouse_visasubmitted == True:
                                        if self.spouse_visaquetime > 0:
                                            self.spouse_visaquetime -= 1
                                        else:
                                            self.spouse_visasubmitted = False
                                            if self.spouse_offered_rank == 1:
                                                if np.random.choice([0,1], p = [(1-self.model.visa_acceptrate*0.9), self.model.visa_acceptrate*0.9]) == 1:  # work permit decision with a bit lower success rate compared to long-term or permanent position.
                                                    self.spouse_hired = True
                                                    self.spouse_job_seeker = False
                                                    self.spouse_workperiod = 0
                                                    self.spouse_rank = self.spouse_offered_rank
                                                    self.spouse_visaperiod = 365
                                                    self.spouse_income_mth = self.spouse_offered_income_mth*0.9   
                                                else:
                                                    self.spouse_offered_rank = 0
                                                    self.spouse_offered_income_mth = 0
                                            else:
                                                if np.random.choice([0,1], p = [(1-self.model.visa_acceptrate), self.model.visa_acceptrate]) == 1:
                                                    self.spouse_hired = True
                                                    self.spouse_job_seeker = False
                                                    self.spouse_workperiod = 0
                                                    self.spouse_rank = self.spouse_offered_rank
                                                    if self.spouse_rank == 2:
                                                        self.spouse_visaperiod = 365*3
                                                        self.spouse_income_mth = self.spouse_offered_income_mth
                                                    elif self.spouse_rank == 3:
                                                            self.spouse_income_mth = self.spouse_offered_income_mth*1.2
                                                            self.spouse_visaperiod = (65-self.spouse_age+1)*365
                                                else:
                                                    self.spouse_offered_rank = 0
                                                    self.spouse_offered_income_mth = 0   


                    elif (self.spouse_g1 == 0):                                                   # Case 6: RPE needed but failed getting RPE; without G1
                        if self.time > self.model.probation_period:
                            if (self.spouse_hired == False) | (self.spouse_workperiod > self.model.probation_period):
                                if self.spouse_visasubmitted == False:
                                    if self.house==True:
                                        if self.ap >= 50:
                                            self.ap -= 50
                                            self.spouse_job_seeker = True
                                            self.spouse_job_quetime = int(np.random.normal(7, 1, 1))
                                            if self.spouse_job_quetime > 0:
                                                self.spouse_job_quetime -= 1
                                            else:                                             
                                                cell_agents = self.model.grid.get_cell_list_contents([self.pos])
                                                econ = [obj for obj in cell_agents if isinstance(obj, econ_status)][0]
                                                if np.random.choice([0,1], p = [econ.jobcomp_rate, (1-econ.jobcomp_rate)]) == 1:  
                                                    job_options = np.random.uniform(0, len(df_job), 1)  ## job options: do not have G1, so the possible number of options will decrease.
                                                    job_options = job_options.astype(int)
                                                    # option set
                                                    job_optset = df_job.iloc[job_options]
                                                    job_optset = job_optset[job_optset.rpe_needed == 0]  # leave only those not requiring RPE
                                                    job_optset['gender'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['gender_prob']),x["gender_prob"]])[0][0], axis=1)  ## assign target gender
                                                    job_optset['salary'] = job_optset.apply(lambda x: np.random.normal(x['salary_mean'], x['salary_sd'], 1)[0], axis=1)  ## assign  salary
                                                    job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu) & (job_optset['gender'] == self.spouse_gender) & (job_optset['edu_max']+1 >= self.spouse_edu)).astype(int)
                                                    # job_optset['eligible'] = ((job_optset['edu_min'] <= self.spouse_edu)).astype(int)
                                                    job_optset = job_optset[job_optset.eligible != 0]  # leave only those meeting one's eligibility by education level
                                                    # compare the options set to one's preference set
                                                    if len(job_optset) > 0:
                                                        job_optset['selected'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['hpr']), x["hpr"]])[0][0], axis=1)  ## submit application and see the results!
                                                        job_optset = job_optset[job_optset.selected == 1]
                                                        if len(job_optset) > 0:
                                                            # job_optset = job_optset.loc[job_optset['salary'].idxmax(axis=0)]   # Because this spouse has no G1 stamp, need to get a permit.
                                                            job_optset = job_optset[job_optset['salary']==job_optset['salary'].max()]
                                                                # self.spouse_offered_rank = job_optset.loc[job_optset['salary'].idxmax(),'rank'] 
                                                            self.spouse_offered_rank = job_optset['rank'].values[0] 
                                                            self.spouse_offered_income_mth = job_optset.loc[job_optset['salary'].idxmax(),'salary']/12 
                                                            if (self.spouse_rank <= self.spouse_offered_rank):
                                                                if self.spouse_rank < 3:
                                                                    self.spouse_visasubmitted = True                # apply for the work permit
                                                                    self.spouse_visaquetime = int(np.random.normal(90, 1, 1))
                                                                elif self.spouse_rank == 3:
                                                                    if self.spouse_income_mth < self.spouse_offered_income_mth*1.2:
                                                                        self.spouse_visasubmitted = True                # apply for the work permit
                                                                        self.spouse_visaquetime = int(np.random.normal(90, 1, 1))

                                elif self.spouse_visasubmitted == True:
                                    if self.spouse_visaquetime > 0:
                                        self.spouse_visaquetime -= 1
                                    else:
                                        self.spouse_visasubmitted = False
                                        if self.spouse_offered_rank == 1:
                                            if np.random.choice([0,1], p = [(1-self.model.visa_acceptrate*0.9), self.model.visa_acceptrate*0.9]) == 1:  # work permit decision with a bit lower success rate compared to long-term or permanent position.
                                                self.spouse_hired = True
                                                self.spouse_job_seeker = False
                                                self.spouse_workperiod = 0
                                                self.spouse_rank = self.spouse_offered_rank
                                                self.spouse_visaperiod = 365
                                                self.spouse_income_mth = self.spouse_offered_income_mth*0.9
                                            else:
                                                self.spouse_offered_rank = 0
                                                self.spouse_offered_income_mth = 0
                                        else:
                                            if np.random.choice([0,1], p = [(1-self.model.visa_acceptrate), self.model.visa_acceptrate]) == 1:
                                                self.spouse_hired = True
                                                self.spouse_job_seeker = False
                                                self.spouse_workperiod = 0
                                                self.spouse_rank = self.spouse_offered_rank
                                                if self.spouse_rank == 2:
                                                    self.spouse_visaperiod = 365*3
                                                    self.spouse_income_mth = self.spouse_offered_income_mth
                                                elif self.spouse_rank == 3:
                                                        self.spouse_income_mth = self.spouse_offered_income_mth*1.2
                                                        self.spouse_visaperiod = (65-self.spouse_age+1)*365
                                            else: 
                                                self.spouse_offered_rank = 0
                                                self.spouse_offered_income_mth = 0                                            

    def permit_renewal(self):
        if self.hired == True:
            self.workperiod += 1
            if self.visaperiod > 0:
                self.visaperiod -= 1
                if self.time > 365:
                    self.wealth -= 350/365  ## renewal fee
            else:
                self.hired = False
                self.income_mth = 0
                self.rank = 0
    

    def spouse_permit_renewal(self):
        if self.spouse_hired == True:
            self.spouse_workperiod += 1
            if self.spouse_visaperiod > 0:
                if self.spouse_workperiod > 365:
                    self.wealth -= 350/365  ## renewal fee
            else:
                self.spouse_hired = False
                self.spouse_income_mth  = 0
                self.spouse_rank = 0




    def job_application(self):
        if self.hired == False:
            if self.time > self.model.probation_period:
                if self.spouse_hired == True:
                    if self.visasubmitted == False:
                        if self.ap >= 50:
                            self.ap -= 50
                            self.job_seeker = True
                            self.job_quetime = int(np.random.normal(7, 1, 1))
                            if self.job_quetime > 0:
                                self.job_quetime -= 1
                            else:                             
                                cell_agents = self.model.grid.get_cell_list_contents([self.pos])
                                econ = [obj for obj in cell_agents if isinstance(obj, econ_status)][0]
                                if np.random.choice([0,1], p = [econ.jobcomp_rate, (1-econ.jobcomp_rate)]) == 1:  
                                    job_options = np.random.uniform(0, len(df_job), 1)
                                    job_options = job_options.astype(int)
                                    # option set
                                    job_optset = df_job.iloc[job_options]
                                    job_optset['gender'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['gender_prob']),x["gender_prob"]])[0][0], axis=1)  ## assign target gender
                                    job_optset['salary'] = job_optset.apply(lambda x: np.random.normal(x['salary_mean'], x['salary_sd'], 1)[0], axis=1)  ## assign  salary
                                    job_optset['eligible'] = ((job_optset['edu_min'] <= self.edu) & (job_optset['gender'] == self.gender) & (job_optset['edu_max']+1 >= self.edu)).astype(int)
                                    # job_optset['eligible'] = ((job_optset['edu_min'] <= self.edu)).astype(int)
                                    job_optset = job_optset[job_optset.eligible != 0]  # leave only those meeting one's eligibility by education level
                                    # compare the options set to one's preference set
                                    if len(job_optset) > 0:
                                        job_optset['selected'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['hpr']), x["hpr"]])[0][0], axis=1)  ## submit application and see the results!
                                        job_optset = job_optset[job_optset.selected == 1]
                                        if len(job_optset) > 0:
                                            # job_optset = job_optset.loc[job_optset['salary'].idxmax(axis=0)]
                                            job_optset = job_optset[job_optset['salary']==job_optset['salary'].max()]
                                                # self.spouse_offered_rank = job_optset.loc[job_optset['salary'].idxmax(),'rank'] 
                                            self.offered_rank = job_optset['rank'].values[0]
                                            self.offered_income_mth = job_optset.loc[job_optset['salary'].idxmax(),'salary']/12*(1-econ.jobcomp_rate)    
                                            self.visasubmitted = True                # apply for the work permit
                                            self.visaquetime = int(np.random.normal(90, 1, 1))

                    elif self.visasubmitted == True:
                        if self.visaquetime > 0:
                            self.visaquetime -= 1
                        else:
                            self.visasubmitted = False
                            if self.offered_rank == 1:
                                if np.random.choice([0,1], p = [(1-self.model.visa_acceptrate*0.9), self.model.visa_acceptrate*0.9]) == 1:  # work permit decision with a bit lower success rate compared to long-term or permanent position.
                                    self.hired = True
                                    self.rank = self.offered_rank
                                    self.visaperiod = 365
                                    self.income_mth = self.offered_income_mth*0.9
                                    self.job_seeker = False
                                else:
                                    self.offered_rank = 0
                                    self.offered_income_mth = 0
                            else:
                                if np.random.choice([0,1], p = [(1-self.model.visa_acceptrate), self.model.visa_acceptrate]) == 1:
                                    self.hired = True
                                    self.rank = self.offered_rank
                                    self.job_seeker = False
                                    if self.rank == 2:
                                        self.visaperiod = 365*3
                                        self.income_mth = self.offered_income_mth
                                    elif self.rank == 3:
                                            self.income_mth = self.offered_income_mth*1.2
                                            self.visaperiod = (65-self.age+1)*365
                                else:
                                    self.offered_rank = 0
                                    self.offered_income_mth = 0

        elif self.hired == True:
            if self.workperiod > self.model.probation_period:
                if self.visasubmitted == False:
                    if self.ap >= 50:
                        self.ap -= 50
                        self.job_seeker = True
                        self.job_quetime = int(np.random.normal(7, 1, 1))
                        if self.job_quetime > 0:
                            self.job_quetime -= 1
                        else:                         
                            cell_agents = self.model.grid.get_cell_list_contents([self.pos])
                            econ = [obj for obj in cell_agents if isinstance(obj, econ_status)][0]
                            if np.random.choice([0,1], p = [econ.jobcomp_rate, (1-econ.jobcomp_rate)]) == 1:  
                                job_options = np.random.uniform(0, len(df_job), 1)
                                job_options = job_options.astype(int)
                                # option set
                                job_optset = df_job.iloc[job_options]
                                job_optset['gender'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['gender_prob']),x["gender_prob"]])[0][0], axis=1)  ## assign target gender
                                job_optset['salary'] = job_optset.apply(lambda x: np.random.normal(x['salary_mean'], x['salary_sd'], 1)[0], axis=1)  ## assign  salary
                                job_optset['eligible'] = ((job_optset['edu_min'] <= self.edu) & (job_optset['gender'] == self.gender) & (job_optset['edu_max']+1 >= self.edu)).astype(int)
                                # job_optset['eligible'] = ((job_optset['edu_min'] <= self.edu)).astype(int)
                                job_optset = job_optset[job_optset.eligible != 0]  # leave only those meeting one's eligibility by education level
                                # compare the options set to one's preference set
                                if len(job_optset) > 0:
                                    job_optset['selected'] = job_optset.apply(lambda x: np.random.choice([0,1], size=(1, 1), p=[(1-x['hpr']), x["hpr"]])[0][0], axis=1)  ## submit application and see the results!
                                    job_optset = job_optset[job_optset.selected == 1]
                                    if len(job_optset) > 0:
                                        # job_optset = job_optset.loc[job_optset['salary'].idxmax()]   
                                        job_optset = job_optset[job_optset['salary']==job_optset['salary'].max()]
                                            # self.spouse_offered_rank = job_optset.loc[job_optset['salary'].idxmax(),'rank'] 
                                        self.offered_rank = job_optset['rank'].values[0]
                                        self.offered_income_mth = job_optset.loc[job_optset['salary'].idxmax(),'salary']/12*(1-econ.jobcomp_rate)    
                                        if (self.rank <= self.offered_rank):
                                            if self.rank < 3:
                                                self.visasubmitted = True                # apply for the work permit
                                                self.visaquetime = int(np.random.normal(90, 1, 1))
                                            elif self.rank == 3:
                                                if self.income_mth < self.offered_income_mth*1.2:
                                                    self.visasubmitted = True                # apply for the work permit
                                                    self.visaquetime = int(np.random.normal(90, 1, 1))

                elif self.visasubmitted == True:
                    if self.visaquetime > 0:
                        self.visaquetime -= 1
                    else:
                        self.visasubmitted = False 
                        if (self.offered_rank == 1):
                            if np.random.choice([0,1], p = [(1-self.model.visa_acceptrate*0.9), self.model.visa_acceptrate*0.9]) == 1:  # work permit decision with a bit lower success rate compared to long-term or permanent position.
                                self.hired = True
                                self.workperiod = 0
                                self.rank = self.offered_rank
                                self.visaperiod = 365
                                self.income_mth = self.offered_income_mth*0.9
                            else:
                                self.offered_rank = 0
                                self.offered_income_mth = 0
                                self.job_seeker = False
                        else:
                            
                            if np.random.choice([0,1], p = [(1-self.model.visa_acceptrate), self.model.visa_acceptrate]) == 1:
                                self.hired = True
                                self.rank = self.offered_rank
                                if self.rank == 2:
                                    self.visaperiod = 365*3
                                    self.income_mth = self.offered_income_mth
                                elif self.rank == 3:
                                        self.income_mth = self.offered_income_mth*1.2
                                        self.visaperiod = (65-self.age+1)*365
                            else:
                                self.offered_rank = 0
                                self.offered_income_mth = 0  
                                self.job_seeker = False 




    # def wealth_eval(self):
    #     if self.wealth > self.wealth_init:
    #         if (self.time > 365):
    #             self.wealth_satisfaction = True
               

    def step(self):
        self.move()
        self.ppsn_work()
        self.spouse_ppsn_work()
        self.residence_permit()
        self.aging()
        self.house_spending()
        self.house_rent()
        self.house_buy()
        self.health()
        self.hospital()
        self.birth()
        self.birthcare()
        self.childcare()
        self.job_application()
        self.spouse_recognition()
        self.spouse_permit()
        self.permit_renewal()
        self.spouse_permit_renewal()
        self.earning()
        self.spending()
        # self.wealthrank()
        # self.wealth_eval()


class econ_status(mesa.Agent):
    """
    A cell representing economic status: inflation (housing market & living cost) and job market
    """

    def __init__(self, unique_id,  model):
        super().__init__(unique_id, model)
        self.inflation = False 
        self.inflation_rate = 0
        self.jobcomp_rate = 0
        self.hseeker_num = 0
        self.jobcomp_num = 0
        self.econ_shock = False
        self.econ_shock_quetime = 0
        self.n_ppl = 0
        self.neighbors = 0 

    
    def inflation_move(self):
        self.hseeker_num -= int(self.hseeker_num/3)
        self.neighbors = len(self.model.grid.get_neighbors(self.pos, moore=True, include_center=False))
        # neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
        cell_agents = self.model.grid.get_cell_list_contents([self.pos])
        self.n_ppl = self.neighbors + len(cell_agents)
        for agent in cell_agents:
            if isinstance(agent, immigrant):
                if agent.house_seeker:
                    # self.inflation_rate += 1/self.model.N_imm
                    self.hseeker_num += 1
                # for n in neighbors:
                #     n.inflation_rate +=0.001

    def job_competition(self):
        self.jobcomp_num -= int(self.jobcomp_num/2)
        # neighbors = self.model.grid.get_neighbors(self.pos, True)
        cell_agents = self.model.grid.get_cell_list_contents([self.pos])
        for agent in cell_agents:
            if isinstance(agent, immigrant):
                if agent.job_seeker:
                    # self.jobcomp_rate += 1/self.model.N_imm
                    if agent.spouse_job_seeker == True:
                        self.jobcomp_num += 2
                    else: 
                        self.jobcomp_num += 1
                else:
                    if agent.spouse_job_seeker == True:
                        self.jobcomp_num += 1

    def shock(self):
        if self.econ_shock == False:
            if np.random.choice([0,1], p = [0.99, (0.01)]) == 1:
                self.econ_shock = True
                self.econ_shock_quetime = int(np.random.normal(90, 3, 1))
        else:
            if self.econ_shock_quetime > 0:
                self.econ_shock_quetime -= 1
            else:
                self.econ_shock = False
        

    def step(self):
        self.inflation_move()
        if self.econ_shock == False:
            # self.inflation_rate = self.hseeker_num / self.model.N_imm
            self.inflation_rate = self.hseeker_num / self.n_ppl
            if self.inflation_rate >= 1:
                self.inflation_rate = 0.99            
        else: 
            # self.inflation_rate = self.hseeker_num*5 / self.model.N_imm
            self.inflation_rate = self.hseeker_num*2 / self.n_ppl
            if self.inflation_rate >= 1:
                self.inflation_rate = 0.99   
        self.job_competition()
        if self.econ_shock == False:
            # self.jobcomp_rate = self.jobcomp_num / (self.model.N_imm*1.5)
            self.jobcomp_rate = self.jobcomp_num / self.n_ppl
            if self.jobcomp_rate >= 1:
                self.jobcomp_rate = 0.99
        else: 
            # self.jobcomp_rate = self.jobcomp_num*3 / (self.model.N_imm*1.5)
            self.jobcomp_rate = self.jobcomp_num*2 / self.n_ppl
            if self.jobcomp_rate >= 1:
                self.jobcomp_rate = 0.99

        



class satisfactionmodel(mesa.Model):
    

    def __init__(self, width, height, N_imm,  gp_rate, bc_quality, childcare_rate, spouse_rpe_acceptrate, visa_acceptrate, probation_period ):

        super().__init__()
        self.N_imm = N_imm   # Number of immigrants
        # self.N_hopt = N_hopt  # avg. number of housing option
        # self.N_jopt = N_jopt
        self.probation_period = probation_period
        # self.hprice_rate = hprice_rate  # avg. price rate
        self.gp_rate = gp_rate  # avg. GP registration rate
        self.bc_quality = bc_quality
        self.childcare_rate = childcare_rate
        self.spouse_rpe_acceptrate = spouse_rpe_acceptrate
        self.visa_acceptrate = visa_acceptrate

        # self.preprate = preprate 
        
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivationByType(self)
        
        self.running = True
        # Create agents 1: Immigrant
        for i in range(self.N_imm):
         # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            a = immigrant(self.next_id(), self)
            self.schedule.add(a)
            self.grid.place_agent(a, (x, y))
        
        # Create agents 2: Econ status
        for (cell_content, x, y) in self.grid.coord_iter():
            cell = econ_status((x, y), self)
            self.grid.place_agent(cell, (x, y))
            self.schedule.add(cell)

        # self.datacollector = mesa.DataCollector(
        #     {"Spouse hired": compute_spouse_hired,
        #      "Birth Satisfaction": compute_birth_satisfaction,
        #      "Wealth": compute_wealth,
        #      "inflation" : compute_inflation,
        #      "House" : compute_house,
        #      "Job competition": compute_job_competition}
        # )
        # self.datacollector = mesa.DataCollector(
        #     {str(compute_list[0]): str(compute_fn_list[0]), str(compute_list[1]): compute_fn_list[1], str(compute_list[2]): compute_fn_list[2],
        #     str(compute_list[3]): compute_fn_list[3], str(compute_list[4]): compute_fn_list[4], str(compute_list[5]): compute_fn_list[5],
        #     str(compute_list[6]): compute_fn_list[6], str(compute_list[7]): compute_fn_list[7], str(compute_list[8]): compute_fn_list[8],
        #     str(compute_list[9]): compute_fn_list[9], str(compute_list[10]): compute_fn_list[10], str(compute_list[11]): compute_fn_list[11],
        #     str(compute_list[12]): compute_fn_list[12], str(compute_list[13]): compute_fn_list[13], str(compute_list[14]): compute_fn_list[14],
        #     str(compute_list[15]): compute_fn_list[15], str(compute_list[16]): compute_fn_list[16], str(compute_list[17]): compute_fn_list[17],
        #     str(compute_list[18]): compute_fn_list[18], str(compute_list[19]): compute_fn_list[19], str(compute_list[20]): compute_fn_list[20],
        #     str(compute_list[21]): compute_fn_list[21], str(compute_list[22]): compute_fn_list[22], str(compute_list[23]): compute_fn_list[23],
        #     str(compute_list[24]): compute_fn_list[24], str(compute_list[25]): compute_fn_list[25], str(compute_list[26]): compute_fn_list[26],
        #     str(compute_list[27]): compute_fn_list[27], str(compute_list[28]): compute_fn_list[28], str(compute_list[29]): compute_fn_list[29],
        #     str(compute_list[30]): compute_fn_list[30], str(compute_list[31]): compute_fn_list[31], str(compute_list[32]): compute_fn_list[32],
        #     str(compute_list[33]): compute_fn_list[33], str(compute_list[34]): compute_fn_list[34], str(compute_list[35]): compute_fn_list[35],
        #     str(compute_list[36]): compute_fn_list[36], str(compute_list[37]): compute_fn_list[37], str(compute_list[38]): compute_fn_list[38],
        #     str(compute_list[39]): compute_fn_list[39], str(compute_list[40]): compute_fn_list[40], str(compute_list[41]): compute_fn_list[41],
        #     str(compute_list[42]): compute_fn_list[42], str(compute_list[43]): compute_fn_list[43], str(compute_list[44]): compute_fn_list[44]}
        # )
        # self.datacollector = mesa.DataCollector(
        #     {"wealth" :  compute_wealth, "gender" : compute_gender }

        # )
        self.datacollector = mesa.DataCollector(
            {compute_list[1]: compute_gender, compute_list[2]: compute_marriage, compute_list[3]: compute_age,
            compute_list[4]: compute_rank, compute_list[5]: compute_n_fam, compute_list[6]: compute_income_mth, compute_list[7]: compute_income_yr,
            compute_list[8]: compute_fam_wealth, compute_list[9]: compute_wealth, compute_list[10]: compute_edu, compute_list[11]: compute_eng,
            compute_list[12]: compute_nationality, compute_list[13]: compute_child_care, compute_list[14]: compute_ppsn, compute_list[15]: compute_hp,
            compute_list[16]: compute_wealth_rank, compute_list[17]: compute_com_house, compute_list[18]: compute_com_child, compute_list[19]: compute_visaperiod,
            compute_list[20]: compute_rentperiod, compute_list[21]: compute_hloan_period, compute_list[22]: compute_sickperiod, compute_list[23]: compute_postbirth,
            compute_list[24]: compute_prebirth, compute_list[25]: compute_postbirth_period, compute_list[26]: compute_house_seeker, compute_list[27]: compute_job_seeker,
            compute_list[28]: compute_bc_satisfaction, compute_list[29]: compute_hospital_satisfaction, compute_list[30]: compute_disease_rate, compute_list[31]: compute_workperiod,
            compute_list[32]: compute_spouse_visaperiod, compute_list[33]: compute_spouse_income_mth, compute_list[34]: compute_spouse_job_seeker, compute_list[35]: compute_spouse_rpe,
            compute_list[36]: compute_spouse_g1, compute_list[37]: compute_spouse_edu, compute_list[38]: compute_spouse_gender, compute_list[39]: compute_spouse_age,
            compute_list[40]: compute_spouse_rank, compute_list[41]: compute_spouse_ppsn, compute_list[42]: compute_spouse_hired, compute_list[43]: compute_spouse_workperiod,
            compute_list[44]: compute_spouse_rpeaccepted, "house": compute_house, "rent" : compute_rent, "houseowner" : compute_houseowner ,
            "inflation": compute_inflation, "job_competition": compute_job_competition}
        )

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
        # if self.schedule.get_type_count(applicant)==0:
        #     self.running = False
        # else:
        #     self.running = True

# params = {"width": 10, "height": 10, "Napp": 10, 
# "dojcapavg" : 100, "dojcapsd" : 2, "dojresavg" : 30, "dojressd" : 3, "preprate": 0.1}



# params = {"width": 100, "height": 100, "N_imm": 200, 
# "N_hopt" : 2, "N_jopt"  : 2, "hprice_rate" : 2, "gp_rate" : 0.1, "bc_quality": 0.2,  "childcare_rate" : 0.1,
# "spouse_rpe_acceptrate" : 0.8, "visa_acceptrate" : 0.5, "probation_period" : 330}

params = {"width": 40, "height": 40, "N_imm": 5000, 
"gp_rate" : 0.5, "bc_quality": 0.5,  "childcare_rate" : 0.5,
"spouse_rpe_acceptrate" : 0.5, "visa_acceptrate" : 0.5, "probation_period" : 330}

results = mesa.batch_run(
    satisfactionmodel,
    parameters=params,
    iterations=1,
    max_steps=540,
    number_processes=1,
    data_collection_period=1,
    display_progress=True,
)



# results_df.max(axis='rows')
# max(results_df.loc[,'job_competition'])
# results_df.loc[730, 'job_competition']

results_df = pd.DataFrame(results)
results_df


# cc = results_df["job_competition"]
# cc.max(axis='rows')
# max(cc.max(axis='rows'))

results_df.to_csv('results_normal.csv')


params = {"width": 40, "height": 40, "N_imm": 5000, 
"gp_rate" : 0.1, "bc_quality": 0.5,  "childcare_rate" : 0.5,
"spouse_rpe_acceptrate" : 0.5, "visa_acceptrate" : 0.5, "probation_period" : 330}

results = mesa.batch_run(
    satisfactionmodel,
    parameters=params,
    iterations=1,
    max_steps=540,
    number_processes=1,
    data_collection_period=1,
    display_progress=True,
)




results_df = pd.DataFrame(results)
results_df

results_df.to_csv('results_low_gp.csv')



params = {"width": 40, "height": 40, "N_imm": 5000, 
"gp_rate" : 0.5, "bc_quality": 0.1,  "childcare_rate" : 0.5,
"spouse_rpe_acceptrate" : 0.5, "visa_acceptrate" : 0.5, "probation_period" : 330}

results = mesa.batch_run(
    satisfactionmodel,
    parameters=params,
    iterations=1,
    max_steps=540,
    number_processes=1,
    data_collection_period=1,
    display_progress=True,
)




results_df = pd.DataFrame(results)
results_df

results_df.to_csv('results_low_bc.csv')



params = {"width": 40, "height": 40, "N_imm": 5000, 
"gp_rate" : 0.5, "bc_quality": 0.5,  "childcare_rate" : 0.1,
"spouse_rpe_acceptrate" : 0.5, "visa_acceptrate" : 0.5, "probation_period" : 330}

results = mesa.batch_run(
    satisfactionmodel,
    parameters=params,
    iterations=1,
    max_steps=540,
    number_processes=1,
    data_collection_period=1,
    display_progress=True,
)




results_df = pd.DataFrame(results)
results_df

results_df.to_csv('results_low_childcare.csv')

params = {"width": 40, "height": 40, "N_imm": 5000, 
"gp_rate" : 0.5, "bc_quality": 0.5,  "childcare_rate" : 0.1,
"spouse_rpe_acceptrate" : 0.1, "visa_acceptrate" : 0.5, "probation_period" : 330}

results = mesa.batch_run(
    satisfactionmodel,
    parameters=params,
    iterations=1,
    max_steps=540,
    number_processes=1,
    data_collection_period=1,
    display_progress=True,
)




results_df = pd.DataFrame(results)
results_df

results_df.to_csv('results_low_rpe.csv')




params = {"width": 40, "height": 40, "N_imm": 5000, 
"gp_rate" : 0.5, "bc_quality": 0.5,  "childcare_rate" : 0.1,
"spouse_rpe_acceptrate" : 0.5, "visa_acceptrate" : 0.1, "probation_period" : 330}

results = mesa.batch_run(
    satisfactionmodel,
    parameters=params,
    iterations=1,
    max_steps=540,
    number_processes=1,
    data_collection_period=1,
    display_progress=True,
)




results_df = pd.DataFrame(results)
results_df

results_df.to_csv('results_low_visa.csv')



params = {"width": 40, "height": 40, "N_imm": 5000, 
"gp_rate" : 0.5, "bc_quality": 0.5,  "childcare_rate" : 0.1,
"spouse_rpe_acceptrate" : 0.5, "visa_acceptrate" : 0.5, "probation_period" : 180}

results = mesa.batch_run(
    satisfactionmodel,
    parameters=params,
    iterations=1,
    max_steps=540,
    number_processes=1,
    data_collection_period=1,
    display_progress=True,
)




results_df = pd.DataFrame(results)
results_df

results_df.to_csv('results_low_probation.csv')






# low vs. high rpe acceptrate 
# low vs. high visa acceptrate
# low vs. child care rate



results_df.loc[60, 'com_house']
results_df.loc[500, 'spouse_hired']
# print(results_df.keys())

# df_graph = results_df[["Spouse hired", "Birth Satisfaction", "Wealth", "inflation", "House"]]
# color_dict = dict({"Spouse hired":'red', "Birth Satisfaction":"green", "Wealth":"blue", "inflation":'orange', "House":"black"})

df_graph = results_df[["Spouse hired", "Birth Satisfaction", "House", "inflation"]]
color_dict = dict({'Spouse hired':'red', "Birth Satisfaction":"green", "House":"blue", "inflation":'orange'})

df_graph = results_df[["Job competition", "inflation"]]
color_dict = dict({'Job competition':'red', "inflation":'orange'})

df_graph = results_df[["Wealth"]]
color_dict = dict({'Wealth':'red'})

# df_graph = results_df[["Population", "Tree", "Pollution"]]
# color_dict = dict({'Population':'dodgerblue',
#                   'Tree':'green',
#                   'Pollution': 'orange'})

df_graph.plot(color=color_dict)
plt.show()




# results_df.to_csv('results_200n_800t.csv')
