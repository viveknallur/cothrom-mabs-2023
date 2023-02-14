* Yohan Park
* 2/5/2023
* COTHROM: satisfaction model
* convert the wide data to long data: this improves the efficiency of loading the data and generating figures in R. 
* This do-file is the same as "[AN]00_data_for_figures_compact.do" (Only file name changed for consistency with other analysis files.)

clear all
set maxvar 120000
cd "C:/Users/Yohan/Dropbox/COTHROM/ABM/satisfaction/overall"

*===========================*
* 1. normal condition (reference)
*===========================*

import delimited "results_normal.csv", clear
keep  gender - job_competition

save "results_normal.dta", replace

clear all
set maxvar 120000
use "results_normal.dta", replace

// 1. gender 

preserve 
	keep gender
	replace gender = subinstr(gender, "[", "",.) 
	replace gender = subinstr(gender, "]", "",.) 

	split(gender), gen(gender) parse(", ")

	gen day = _n

	drop gender

	reshape long gender, i(day) j(id)
	compress 
	save "results_normal_long.dta", replace
restore

/* 

2. the other variables: reshape first and then destring (marriage age rank  wealth_rank nationality child_care com_house com_child ///
  bc_satisfaction hospital_satisfaction spouse_hired spouse_rpeaccepted spouse_rpe house rent houseowner)


*/
clear all
set maxvar 120000
use "results_normal.dta", replace

foreach v of varlist  marriage age rank  wealth_rank nationality child_care com_house com_child ///
  bc_satisfaction hospital_satisfaction spouse_hired spouse_rpeaccepted spouse_rpe house rent houseowner {

clear all
set maxvar 120000
use "results_normal.dta", replace

	keep `v'
	replace `v' = subinstr(`v', "[", "",.) 
	replace `v' = subinstr(`v', "]", "",.) 

	split(`v'), gen(`v') parse(", ")

	forvalues i = 1/5 {
		local f = (`i'-1)*1000 + 1
		local e = `i'*1000
		preserve 
			keep `v'`f' -  `v'`e'
			
			gen day = _n

			reshape long `v', i(day) j(id)
			rename `v' `v'`i'

			tempfile temp 
			save `temp'
			
			use "results_normal_long.dta", clear 
			merge 1:1 id day using `temp', keepusing(`v'`i') keep(match master) nogen
			compress 
			sleep 500
			save "results_normal_long.dta", replace
		restore 
	}

}


/* 
3. the other variables: shorten the length of characters  (income_mth  wealth)
*/
clear all
set maxvar 120000
use "results_normal.dta", replace

foreach v of varlist  income_mth  wealth {
clear all
set maxvar 120000
use "results_normal.dta", replace

	keep `v'
	replace `v' = subinstr(`v', "[", "",.) 
	replace `v' = subinstr(`v', "]", "",.) 

	split(`v'), gen(`v') parse(", ")
	drop `v'

	// shorten the length of characters

	forvalues i = 1/ 5000{
	replace `v'`i' = substr(`v'`i', 1, 9) 
}

	
	gen day = _n



	forvalues i = 1/5 {
		local f = (`i'-1)*1000 + 1
		local e = `i'*1000
		preserve 
			keep `v'`f' -  `v'`e'
			
			gen day = _n

			reshape long `v', i(day) j(id)
			rename `v' `v'`i'

			tempfile temp 
			save `temp'
			
			use "results_normal_long.dta", clear 
			merge 1:1 id day using `temp', keepusing(`v'`i') keep(match master) nogen
			compress 
			sleep 500
			save "results_normal_long.dta", replace
		restore 
	}

}




*===========================*
* 2. other datasets
*===========================*
//low_gp low_bc low_rpe low_probation
foreach x in low_gp low_bc low_visa low_rpe low_probation  low_childcare     {

clear all
set maxvar 120000

import delimited "results_`x'.csv", clear delimiter(comma) bindquote(strict) 
keep  gender - job_competition

save "results_`x'.dta", replace

clear all
set maxvar 120000
use "results_`x'.dta", replace


// 1. gender 

preserve 
	keep gender
	replace gender = subinstr(gender, "[", "",.) 
	replace gender = subinstr(gender, "]", "",.) 

	split(gender), gen(gender) parse(", ")

	gen day = _n

	drop gender

	reshape long gender, i(day) j(id)
	compress 
	save "results_`x'_long.dta", replace
restore

/* 

2. the other variables: reshape first and then destring (marriage age n_fam rank  wealth_rank nationality child_care ///
  bc_satisfaction hospital_satisfaction spouse_hired spouse_rpeaccepted spouse_rpe house)
*/

clear all
set maxvar 120000
use "results_`x'.dta", replace

foreach v of varlist  marriage age n_fam rank  wealth_rank nationality child_care com_house com_child ///
  bc_satisfaction hospital_satisfaction spouse_hired spouse_rpeaccepted spouse_rpe house  rent houseowner {

clear all
set maxvar 120000
use "results_`x'.dta", replace

	keep `v'
	replace `v' = subinstr(`v', "[", "",.) 
	replace `v' = subinstr(`v', "]", "",.) 

	split(`v'), gen(`v') parse(", ")

	forvalues i = 1/5 {
		local f = (`i'-1)*1000 + 1
		local e = `i'*1000
		preserve 
			keep `v'`f' -  `v'`e'
			
			gen day = _n

			reshape long `v', i(day) j(id)
			rename `v' `v'`i'

			tempfile temp 
			save `temp'
			
			use "results_`x'_long.dta", clear 
			merge 1:1 id day using `temp', keepusing(`v'`i') keep(match master) nogen
			compress 
			sleep 500
			save "results_`x'_long.dta", replace
		restore 
	}

}


/* 
3. the other variables: shorten the length of characters  (income_mth  wealth)
*/

clear all
set maxvar 120000
use "results_`x'.dta", replace

foreach v of varlist  income_mth  wealth {
clear all
set maxvar 120000
use "results_`x'.dta", replace

	keep `v'
	replace `v' = subinstr(`v', "[", "",.) 
	replace `v' = subinstr(`v', "]", "",.) 

	split(`v'), gen(`v') parse(", ")
	drop `v'

	// shorten the length of characters

	forvalues i = 1/ 5000{
	replace `v'`i' = substr(`v'`i', 1, 9) 
}

	
	gen day = _n



	forvalues i = 1/5 {
		local f = (`i'-1)*1000 + 1
		local e = `i'*1000
		preserve 
			keep `v'`f' -  `v'`e'
			
			gen day = _n

			reshape long `v', i(day) j(id)
			rename `v' `v'`i'

			tempfile temp 
			save `temp'
			
			use "results_`x'_long.dta", clear 
			merge 1:1 id day using `temp', keepusing(`v'`i') keep(match master) nogen
			compress 
			sleep 500
			save "results_`x'_long.dta", replace
		restore 
	}

}


}


