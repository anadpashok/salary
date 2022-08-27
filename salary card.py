import pandas as pd
import openpyxl


base_salary=int(input("enter the basic salary"))
basic_salary=base_salary/2
HRA=basic_salary/2
employer_pf=1800*12
employer_ESI=0
Special_Allowance=base_salary-basic_salary-HRA-employer_pf
annual_short_term_bonus=(base_salary/100)*5
other_allowance=6000
total_cost_to_company=base_salary+annual_short_term_bonus+other_allowance



df = pd.DataFrame([[base_salary,base_salary//12],[HRA,HRA//12],[Special_Allowance,Special_Allowance//12],[employer_pf,employer_pf//12],[employer_ESI,employer_ESI//12],[base_salary,base_salary//12],[annual_short_term_bonus,0],[other_allowance,other_allowance/12],[total_cost_to_company,(total_cost_to_company//12)+(other_allowance//12)]],
                  index=['Basic Salary', 'HRA', 'Special Allowance','Employer PF','Employer ESI','Base Salary','Annual Short-Term Bonus','Other Allowance(internet)','Total Cost To Company'], columns=['Annual', 'Monthly'])
print(df)






