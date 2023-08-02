def calculate_retirement_plan(current_age, retirement_age, life_expectancy, current_annual_expense, inflation_rate,
                             pre_retirement_ror, post_retirement_ror, annual_increase_in_income,
                             existing_investments, existing_investment_ror):
    years_to_retirement = retirement_age - current_age
    years_in_retirement = life_expectancy - retirement_age
    months_to_retirement = years_to_retirement * 12

    future_value_current_annual_expense = current_annual_expense * (1 + post_retirement_ror - inflation_rate) ** years_in_retirement
    future_value_existing_investments = existing_investments * (1 + existing_investment_ror) ** years_to_retirement
    retirement_corpus_required = future_value_current_annual_expense + future_value_existing_investments

    lumpsum_funding = retirement_corpus_required - existing_investments

    monthly_ror = (1 + pre_retirement_ror) ** (1 / 12) - 1
    monthly_sip_required = lumpsum_funding * monthly_ror / ((1 + monthly_ror) ** months_to_retirement - 1)

    step_up_sip_required = 0
    for year in range(years_to_retirement):
        step_up_sip_required += monthly_sip_required * (1 + annual_increase_in_income) ** year

    return retirement_corpus_required, lumpsum_funding, monthly_sip_required, step_up_sip_required


# Provided Information
current_age = 30
retirement_age = 60
life_expectancy = 95
current_annual_expense = 600000
inflation_rate = 0.07  # 7%
pre_retirement_ror = 0.12  # 12%
post_retirement_ror = 0.08  # 8%
annual_increase_in_income = 0.07  # 7%
existing_investments = 500000
existing_investment_ror = 0.08  # 8%

# Calculate Retirement Plan
retirement_corpus, lumpsum_funding, monthly_sip, step_up_sip = calculate_retirement_plan(
    current_age, retirement_age, life_expectancy, current_annual_expense, inflation_rate,
    pre_retirement_ror, post_retirement_ror, annual_increase_in_income,
    existing_investments, existing_investment_ror
)

print("Retirement corpus required ₹ =", round(retirement_corpus, 2))
print("Lumpsum Funding ₹ =", round(lumpsum_funding, 2))
print("Monthly SIP required ₹ =", round(monthly_sip, 2))
print("Step up SIP required ₹ =", round(step_up_sip, 2))
