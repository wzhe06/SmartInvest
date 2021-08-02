__author__ = 'Wang Zhe'

property_price = 350
property_yearly_return_rate = 0.03
mortgage_yearly_rate = 0.0465
mortgage_years = 15
down_payment = 200
current_wealth = 200
monthly_income = 3
family_expense = 0.5
financial_yearly_return_rate = 0.03

financial_monthly_return_rate = financial_yearly_return_rate / 12
mortgage_monthly_rate = mortgage_yearly_rate / 12
mortgage = property_price - down_payment

monthly_repayment = float(mortgage) * mortgage_monthly_rate * ((1 + mortgage_monthly_rate) ** (12 * mortgage_years)) / \
    ((1 + mortgage_monthly_rate) ** (12 * mortgage_years) - 1)

print "Monthly Mortgage repayment:\t", round(monthly_repayment, 4), "* 10000 RMB"

wealth_years = 30

cash_wealth = current_wealth - down_payment
for this_month in range(0, 12 * wealth_years):
    cash_wealth = cash_wealth * (1 + financial_monthly_return_rate) + monthly_income - family_expense
    if this_month <= mortgage_years * 12:
        cash_wealth = cash_wealth - monthly_repayment

property_wealth = property_price
for this_year in range(0, wealth_years):
    property_wealth = property_wealth * (1 + property_yearly_return_rate)

print wealth_years, "years later, your cash wealth:\t", round(cash_wealth, 2), "* 10000 RMB"
print wealth_years, "years later, your property wealth:\t", round(property_wealth, 2), "* 10000 RMB"


