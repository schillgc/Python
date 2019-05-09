""" Income """
# Job Specific Source
company = "APR"
months = 4
job_title = "Computer Technician (Contract -- Philadelphia, PA)"
pay_rate = 29.00
gross_job_specific_base_income = pay_rate * (2080 * (months / 12))


''' Monthly Benefits Fixed Expenses '''
medical_insurance = 0
dental_insurance = 0
vision_insurance = 0
monthly_fixed_benefit_expenses = medical_insurance + dental_insurance + vision_insurance


''' Annual Benefits '''
flex_spending_account = 0
retirement_401K = gross_job_specific_base_income * .04
annual_fixed_benefit_expenses = flex_spending_account + retirement_401K


"""" Taxes """
federal_income_tax = gross_job_specific_base_income * 0.0403
state_income_tax = gross_job_specific_base_income * 0.0307
local_income_tax = gross_job_specific_base_income * 0.0392
income_taxes = federal_income_tax + state_income_tax + local_income_tax

social_security = gross_job_specific_base_income * 0.03825
medicare = gross_job_specific_base_income * 0.03825
fica = social_security + medicare

taxes = income_taxes + fica
