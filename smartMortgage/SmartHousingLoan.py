__author__ = 'Wang Zhe'

loan_years = 30
loan = 40
cash = 10
financial_yearly_return_rate = 0.05
lending_yearly_rate = 0.04067
monthly_income = 0.5

financial_monthly_return_rate = financial_yearly_return_rate / 12
lending_monthly_rate = lending_yearly_rate / 12

monthly_repayment = float(loan) * lending_monthly_rate * ((1 + lending_monthly_rate) ** (12 * loan_years)) / \
    ((1 + lending_monthly_rate) ** (12 * loan_years) - 1)

print "Monthly repayment:\t", round(monthly_repayment, 4), "* 10000 RMB"

last_month_cash = cash
for this_month in range(0, 12 * loan_years):
    last_month_cash = last_month_cash * (1 + financial_monthly_return_rate) + monthly_income - monthly_repayment

print loan_years, "years later, your cash:\t", round(last_month_cash, 2), "* 10000 RMB"


