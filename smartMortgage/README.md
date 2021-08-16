# SmartHousingLoan
一个计算最优化房贷的小项目

# Description
通过输入你的房贷期限、房贷金额、贷款利率、你目前持有的现金、你每月的固定收入、你的理财利率来计算最优的房贷计划

# Input
* 贷款年限(单位:年)
loan_years
* 贷款金额(单位:万元)
loan
* 交完首付后持有的现金(单位:万元)
cash
* 理财年利率
financial_yearly_return_rate
* 贷款年利率
lending_yearly_rate
* 每月净收入(扣除生活开销，但不要扣除房贷)(单位:万元)
monthly_income

# Output
* 每月应还贷款(单位:万元)
Monthly repayment:	0.1444 * 10000 RMB
* X年后，你手中持有的现金(单位:万元)
30 years later, your cash:	179.54 * 10000 RMB

# Example
        输入
        贷款30年
        loan_years = 30
        贷款40万人民币
        loan = 40
        付完首付后，手上还有10万元现金
        cash = 10
        每年的理财收益利率是5%
        financial_yearly_return_rate = 0.05
        每年的房贷利率是4.067%
        lending_yearly_rate = 0.04067
        每个月扣除生活开销，不扣除房贷的收入是0.5万元
        monthly_income = 0.5

        输出
        Monthly repayment:	0.1925 * 10000 RMB
        30 years later, your cash:	300.58 * 10000 RMB

        每月应还贷款 0.1925万元
        30年后，你的现金财富将是300.58万元