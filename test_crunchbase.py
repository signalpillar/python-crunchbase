<<<<<<< HEAD
from crunchbase import CrunchBase
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

investor  = cb.listInvestorPortfolio('Kapor Capital')
for i in investor:
	print i
=======
import doctest
doctest.testfile('README.md', verbose=False)
>>>>>>> 9e524f1f02a9385cbd91979f56c63399c4abecef
