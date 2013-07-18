"""
Python library for the CrunchBase api.
Copyright (c) 2010 Apurva Mehta <mehta.apurva@gmail.com> for CrunchBase class

Edits made by Alexander Pease <alexander@usv.com> to...
  * Ensure compliance with 2013 API key requirement
  * Fix namespace conventions (ex: 'Kapor Capital' is sent as 'kapor+capital')
  * Functions requiring parsing of CrunchBase-return JSON (ex. list a company's investors)
  * If HTTP request fails, return None instead of raising Exception
  * Set strict=false for json.loads(). Avoids some errors in the CB API.
  * Sanitize strings used as argument for __webRequest

"""

__author__  = 'Apurva Mehta'
__version__ = '1.0.2'


import urllib2
import simplejson as json
import unicodedata

API_BASE_URL = "http://api.crunchbase.com/"
API_VERSION  = "1"
API_URL      = API_BASE_URL + "v" + "/" + API_VERSION + "/"

class CrunchBase:

  def __init__(self, api_key):
    self.api_key = api_key

  def __webRequest(self, url):
    print 'Making request to:'
    print url
    try:
      response = urllib2.urlopen(url)
      result = response.read()
      return result
    except urllib2.HTTPError as e:
      #raise CrunchBaseError(e)
      print 'HTTPError calling ' + url
      return None

  def __getJsonData(self, namespace, query=""):
    # Replace spaces and non-ASCII chars
    query = query.replace(" ", "+")
    query = unicodedata.normalize('NFKD', query.decode('utf-8')).encode('ascii', 'ignore')
    url = API_URL + namespace + query + ".js?api_key=" + self.api_key
    response = self.__webRequest(url)
    if response is not None:
      response = json.loads(response, strict=False)
    return response

  def getCompanyData(self, name):
    '''This returns the data about a company in JSON format.'''

    result = self.__getJsonData("company", "/%s" % name)
    return result

  def getPersonData(self, *args):
    '''This returns the data about a person in JSON format.'''

    result = self.__getJsonData("person", "/%s" % '-'.join(args).lower().replace(' ','-'))
    return result

  def getFinancialOrgData(self, orgName):
    '''This returns the data about a financial organization in JSON format.'''

    result = self.__getJsonData("financial-organization", "/%s" % orgName)
    return result

  def getProductData(self, name):
    '''This returns the data about a product in JSON format.'''

    result = self.__getJsonData("product", name)
    return result

  def getServiceProviderData(self, name):
    '''This returns the data about a service provider in JSON format.'''

    result = self.__getJsonData("service-provider", "/%s" % name)
    return result

  def listCompanies(self):
    '''This returns the list of companies in JSON format.'''

    result = self.__getJsonData("companies")
    return result

  def listPeople(self):
    '''This returns the list of people in JSON format.'''

    result = self.__getJsonData("people")
    return result

  def listFinancialOrgs(self):
    '''This returns the list of financial organizations in JSON format.'''

    result = self.__getJsonData("financial-organizations")
    return result

  def listProducts(self):
    '''This returns the list of products in JSON format.'''

    result = self.__getJsonData("products")
    return result

  def listServiceProviders(self):
    '''This returns the list of service providers in JSON format.'''

    result = self.__getJsonData("service-providers")
    return result

  '''Below are CrunchBase functions written by Alexander Pease'''
  def listCompanyInvestors(self, name):
    '''Returns the list of financial organizations invested in a given company'''
    
    company = self.getCompanyData(name)
    investors = []
    for rounds in company['funding_rounds']:
      for org in rounds['investments']:
        'CB returns angel investors differently, gives them None financial_org'
        if org['financial_org'] is not None: 
          if org['financial_org']['name'] not in investors:
            investors.append(org['financial_org']['name'])
    return investors
    
  def listInvestorPortfolio(self, orgName):
    '''Returns a list of companies invested in by orgName'''

    investor = self.getFinancialOrgData(orgName)
    portfolio = []
    for investment in investor['investments']:
      portfolio.append(investment['funding_round']['company']['name'])
    return portfolio

class CrunchBaseResponse(object):
  def __init__(self, **kwargs):
    self.__dict__.update(kwargs)

  def __repr__(self):
    return '%s(%r)' % (self.__class__.__name__, self.__dict__)

class CrunchBaseError(Exception):
  pass

