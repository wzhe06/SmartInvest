__author__ = 'Wang Zhe'

loan_years = 30

cash = 50
loan = 100

financial_return_rate = 0.04 / 12
lending_rate = 0.04067 / 12

monthly_income = 1

monthly_repayment = float(loan) * lending_rate * ((1 + lending_rate) ** (12 * loan_years)) / \
    ((1 + lending_rate) ** (12 * loan_years) - 1)

print "Monthly repayment:\t", round(monthly_repayment * 10000, 2), "RMB"



last_month_cash = cash
for this_year in range(1,loan_years):
    for this_month in range(1, 12):
        last_month_cash = last_month_cash * (1 + financial_return_rate) + monthly_income - monthly_repayment

print loan_years, "years later, your cash:\t", last_month_cash, " wan RMB"


