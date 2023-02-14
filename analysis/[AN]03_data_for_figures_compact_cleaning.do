* Yohan Park
* 2/5/2023
* COTHROM: satisfaction model
* clean the data: destring & convert types 
* Same as the "[AN]01_data_for_figures_compact_cleaning.do" file (only file name changed for consistency with other analysis files.)

clear all
set maxvar 25000
cd "C:/Users/Yohan/Dropbox/COTHROM/ABM/satisfaction/overall"

*===========================*
* 1. normal condition (reference)
*===========================*

* 1. adjust variables
use "results_normal_long.dta", clear 


// combine variables 
foreach v in wealth_rank nationality child_care com_house com_child income_mth  wealth ///
  bc_satisfaction hospital_satisfaction spouse_hired spouse_rpeaccepted spouse_rpe house rent houseowner {

gen `v' = ""
replace `v' = `v'1 if `v'1 != ""
replace `v' = `v'2 if `v'2 != ""
replace `v' = `v'3 if `v'3 != ""
replace `v' = `v'4 if `v'4 != ""
replace `v' = `v'5 if `v'5 != ""

drop `v'1 - `v'5
}


// destring: non-string variables 

destring gender marriage age rank n_fam  wealth_rank income_mth wealth  com_house com_child ///
   hospital_satisfaction   spouse_rpe   , replace


// destring: string variables 

foreach v in child_care  ///
  bc_satisfaction  spouse_hired spouse_rpeaccepted  house rent houseowner {

replace `v' = "1" if `v'=="True"
replace `v' = "0" if `v'=="False"

destring `v', replace

}

replace nationality = subinstr(nationality, "'", "",.)
replace nationality = "China" if strpos(nationality, "Peoples Republic of China")

compress
save "results_normal_long_cleaned.dta", replace 



* 2. generate variable for satisfaction

// a. wealth 
gen wealth_stsf = ((wealth > income_mth*6) & income_mth>0)

// b. housing 

// c. hospital satisfaction 

gen hsp_stsf = (hospital_satisfaction > 0)

// d. visa_status (hired or not)

gen visa_stsf = (rank!=0)  // next time, use visaperiod


// e. spouse hired (spouse_hired)

// f. bc_satisfaction

// g. child_care


// the number of required categories for satisfaction 
gen stsf_req = 4 if n_fam == 1 
replace stsf_req = 6 if n_fam == 2
replace stsf_req = 7 if n_fam > 2

// the number of categories achieved

gen stsf_ach = wealth_stsf + house + hsp_stsf + visa_stsf + spouse_hired + bc_satisfaction + child_care

// ratio of achieved / required 

gen stsf_ratio = stsf_ach/stsf_req



compress
save "results_normal_long_cleaned.dta", replace 


/*

use "results_normal_long_cleaned.dta", clear
keep if day==1

collapse (count) id , by(nationality) // nationality	id
India	2310
Philippines	437
China	363
Pakistan	263
Zimbabwe	158

gsort -id

dis (2320+437+363)/5000
dis (437+363+263+158)/5000

use "results_normal_long_cleaned.dta", clear
unique id if (nationality=="India" | nationality=="Philippines" | nationality=="China") & n_fam > 1

*/

use "results_normal_long_cleaned.dta", clear 

gen scode =.
gen sname = nationality


do "../data/YP/assign_ccode.do"

rename scode ccode 
order ccode, after(nationality)
drop sname 

replace ccode = 1000 if ccode==.
preserve 
	use "../data/YP/nationality_sector_position.dta", clear 
	duplicates drop ccode, force 
	tempfile temp 
	save `temp'
restore 
merge m:1 ccode using `temp', keepusing(gdppc_2015cnst) keep(match master) nogen


gen wealth_rank_cty = 3 if gdppc_2015cnst >= 13000 
replace wealth_rank_cty = 2 if gdppc_2015cnst > 4000 &  gdppc_2015cnst < 13000
replace wealth_rank_cty = 1 if wealth_rank_cty==.


gen wealth_rank_cty2 = 3 if gdppc_2015cnst >= 6391 
replace wealth_rank_cty2 = 2 if gdppc_2015cnst >= 2000 &  gdppc_2015cnst < 6391
replace wealth_rank_cty2 = 1 if wealth_rank_cty2==.

compress
save "results_normal_long_cleaned.dta", replace 





*===========================*
* 2. low GP 
*===========================*

* 1. adjust variables
use "results_low_gp_long.dta", clear 


// combine variables 
foreach v in marriage age n_fam rank wealth_rank nationality child_care com_house com_child income_mth  wealth ///
  bc_satisfaction hospital_satisfaction spouse_hired spouse_rpeaccepted spouse_rpe house rent houseowner {

gen `v' = ""
replace `v' = `v'1 if `v'1 != ""
replace `v' = `v'2 if `v'2 != ""
replace `v' = `v'3 if `v'3 != ""
replace `v' = `v'4 if `v'4 != ""
replace `v' = `v'5 if `v'5 != ""

drop `v'1 - `v'5
}


// destring: non-string variables 

destring gender marriage age rank n_fam  wealth_rank income_mth wealth  com_house com_child ///
   hospital_satisfaction   spouse_rpe   , replace


// destring: string variables 

foreach v in child_care  ///
  bc_satisfaction  spouse_hired spouse_rpeaccepted  house rent houseowner {

replace `v' = "1" if `v'=="True"
replace `v' = "0" if `v'=="False"

destring `v', replace

}

replace nationality = subinstr(nationality, "'", "",.)
replace nationality = "China" if strpos(nationality, "Peoples Republic of China")

compress
save "results_low_gp_long_cleaned.dta", replace 



* 2. generate variable for satisfaction

// a. wealth 
gen wealth_stsf = ((wealth > income_mth*6) & income_mth>0)

// b. housing 

// c. hospital satisfaction 

gen hsp_stsf = (hospital_satisfaction > 0)

// d. visa_status (hired or not)

gen visa_stsf = (rank!=0)  // next time, use visaperiod


// e. spouse hired (spouse_hired)

// f. bc_satisfaction

// g. child_care


// the number of required categories for satisfaction 
gen stsf_req = 4 if n_fam == 1 
replace stsf_req = 6 if n_fam == 2
replace stsf_req = 7 if n_fam > 2

// the number of categories achieved

gen stsf_ach = wealth_stsf + house + hsp_stsf + visa_stsf + spouse_hired + bc_satisfaction + child_care

// ratio of achieved / required 

gen stsf_ratio = stsf_ach/stsf_req



compress
save "results_low_gp_long_cleaned.dta", replace 





*===========================*
* 3. low visa 
*===========================*

* 1. adjust variables
use "results_low_visa_long.dta", clear 


// combine variables 
foreach v in marriage age n_fam rank wealth_rank nationality child_care com_house com_child income_mth  wealth ///
  bc_satisfaction hospital_satisfaction spouse_hired spouse_rpeaccepted spouse_rpe house rent houseowner {

gen `v' = ""
replace `v' = `v'1 if `v'1 != ""
replace `v' = `v'2 if `v'2 != ""
replace `v' = `v'3 if `v'3 != ""
replace `v' = `v'4 if `v'4 != ""
replace `v' = `v'5 if `v'5 != ""

drop `v'1 - `v'5
}


// destring: non-string variables 

destring gender marriage age rank n_fam  wealth_rank income_mth wealth  com_house com_child ///
   hospital_satisfaction   spouse_rpe   , replace


// destring: string variables 

foreach v in child_care  ///
  bc_satisfaction  spouse_hired spouse_rpeaccepted  house rent houseowner {

replace `v' = "1" if `v'=="True"
replace `v' = "0" if `v'=="False"

destring `v', replace

}

replace nationality = subinstr(nationality, "'", "",.)
replace nationality = "China" if strpos(nationality, "Peoples Republic of China")

compress
save "results_low_visa_long_cleaned.dta", replace 



* 2. generate variable for satisfaction

// a. wealth 
gen wealth_stsf = ((wealth > income_mth*6) & income_mth>0)

// b. housing 

// c. hospital satisfaction 

gen hsp_stsf = (hospital_satisfaction > 0)

// d. visa_status (hired or not)

gen visa_stsf = (rank!=0)  // next time, use visaperiod


// e. spouse hired (spouse_hired)

// f. bc_satisfaction

// g. child_care


// the number of required categories for satisfaction 
gen stsf_req = 4 if n_fam == 1 
replace stsf_req = 6 if n_fam == 2
replace stsf_req = 7 if n_fam > 2

// the number of categories achieved

gen stsf_ach = wealth_stsf + house + hsp_stsf + visa_stsf + spouse_hired + bc_satisfaction + child_care

// ratio of achieved / required 

gen stsf_ratio = stsf_ach/stsf_req



compress
save "results_low_visa_long_cleaned.dta", replace 










*===========================*
* 4. low maternity care 
*===========================*

* 1. adjust variables
use "results_low_bc_long.dta", clear 


// combine variables 
foreach v in marriage age n_fam rank wealth_rank nationality child_care com_house com_child income_mth  wealth ///
  bc_satisfaction hospital_satisfaction spouse_hired spouse_rpeaccepted spouse_rpe house rent houseowner {

gen `v' = ""
replace `v' = `v'1 if `v'1 != ""
replace `v' = `v'2 if `v'2 != ""
replace `v' = `v'3 if `v'3 != ""
replace `v' = `v'4 if `v'4 != ""
replace `v' = `v'5 if `v'5 != ""

drop `v'1 - `v'5
}


// destring: non-string variables 

destring gender marriage age rank n_fam  wealth_rank income_mth wealth  com_house com_child ///
   hospital_satisfaction   spouse_rpe   , replace

destring wealth, replace force  // some obs. have weird values.
list wealth id day if id==4195

foreach v in child_care  ///
  bc_satisfaction  spouse_hired spouse_rpeaccepted  house rent houseowner {

replace `v' = "1" if `v'=="True"
replace `v' = "0" if `v'=="False"

destring `v', replace

}

replace nationality = subinstr(nationality, "'", "",.)
replace nationality = "China" if strpos(nationality, "Peoples Republic of China")

compress
save "results_low_bc_long_cleaned.dta", replace 



* 2. generate variable for satisfaction

// a. wealth 
gen wealth_stsf = ((wealth > income_mth*6) & income_mth>0)

// b. housing 

// c. hospital satisfaction 

gen hsp_stsf = (hospital_satisfaction > 0)

// d. visa_status (hired or not)

gen visa_stsf = (rank!=0)  // next time, use visaperiod


// e. spouse hired (spouse_hired)

// f. bc_satisfaction

// g. child_care


// the number of required categories for satisfaction 
gen stsf_req = 4 if n_fam == 1 
replace stsf_req = 6 if n_fam == 2
replace stsf_req = 7 if n_fam > 2

// the number of categories achieved

gen stsf_ach = wealth_stsf + house + hsp_stsf + visa_stsf + spouse_hired + bc_satisfaction + child_care

// ratio of achieved / required 

gen stsf_ratio = stsf_ach/stsf_req



compress
save "results_low_bc_long_cleaned.dta", replace 









*===========================*
* 5. low probation
*===========================*

* 1. adjust variables
use "results_low_probation_long.dta", clear 


// combine variables 
foreach v in marriage age n_fam rank wealth_rank nationality child_care com_house com_child income_mth  wealth ///
  bc_satisfaction hospital_satisfaction spouse_hired spouse_rpeaccepted spouse_rpe house rent houseowner {

gen `v' = ""
replace `v' = `v'1 if `v'1 != ""
replace `v' = `v'2 if `v'2 != ""
replace `v' = `v'3 if `v'3 != ""
replace `v' = `v'4 if `v'4 != ""
replace `v' = `v'5 if `v'5 != ""

drop `v'1 - `v'5
}


// destring: non-string variables 

destring gender marriage age rank n_fam  wealth_rank income_mth wealth  com_house com_child ///
   hospital_satisfaction   spouse_rpe   , replace


// destring: string variables 

foreach v in child_care  ///
  bc_satisfaction  spouse_hired spouse_rpeaccepted  house rent houseowner {

replace `v' = "1" if `v'=="True"
replace `v' = "0" if `v'=="False"

destring `v', replace

}

replace nationality = subinstr(nationality, "'", "",.)
replace nationality = "China" if strpos(nationality, "Peoples Republic of China")

compress
save "results_low_probation_long_cleaned.dta", replace 



* 2. generate variable for satisfaction

// a. wealth 
gen wealth_stsf = ((wealth > income_mth*6) & income_mth>0)

// b. housing 

// c. hospital satisfaction 

gen hsp_stsf = (hospital_satisfaction > 0)

// d. visa_status (hired or not)

gen visa_stsf = (rank!=0)  // next time, use visaperiod


// e. spouse hired (spouse_hired)

// f. bc_satisfaction

// g. child_care


// the number of required categories for satisfaction 
gen stsf_req = 4 if n_fam == 1 
replace stsf_req = 6 if n_fam == 2
replace stsf_req = 7 if n_fam > 2

// the number of categories achieved

gen stsf_ach = wealth_stsf + house + hsp_stsf + visa_stsf + spouse_hired + bc_satisfaction + child_care

// ratio of achieved / required 

gen stsf_ratio = stsf_ach/stsf_req



compress
save "results_low_probation_long_cleaned.dta", replace 




use "results_low_probation_long_cleaned.dta", clear 

gen scode =.
gen sname = nationality


do "../data/YP/assign_ccode.do"

rename scode ccode 
order ccode, after(nationality)
drop sname 

replace ccode = 1000 if ccode==.
preserve 
	use "../data/YP/nationality_sector_position.dta", clear 
	duplicates drop ccode, force 
	tempfile temp 
	save `temp'
restore 
merge m:1 ccode using `temp', keepusing(gdppc_2015cnst) keep(match master) nogen


gen wealth_rank_cty = 3 if gdppc_2015cnst >= 13000 
replace wealth_rank_cty = 2 if gdppc_2015cnst > 4000 &  gdppc_2015cnst < 13000
replace wealth_rank_cty = 1 if wealth_rank_cty==.


gen wealth_rank_cty2 = 3 if gdppc_2015cnst >= 6391 
replace wealth_rank_cty2 = 2 if gdppc_2015cnst >= 2000 &  gdppc_2015cnst < 6391
replace wealth_rank_cty2 = 1 if wealth_rank_cty2==.

compress
save "results_low_probation_long_cleaned.dta", replace 

