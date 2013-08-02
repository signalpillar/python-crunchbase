from crunchbase import CrunchBase
# may be outdated. switched all code to __init__.py
import doctest
doctest.testfile('README.md', verbose=False)

cb = CrunchBase('j4rufy6d4zckdka4cwxhdeda')
#company = cb.getCompanyData('Fundly')
'''
print company
print company['name']
print company['total_money_raised']
print company['funding_rounds'][1]['investments']#['financial_org']
'''
#investors = cb.listCompanyInvestors('Fundly')
#print investors

investor = cb.listInvestorPortfolio('Kapor Capital')
for i in investor:
    print i
