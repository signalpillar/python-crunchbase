#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python library for the CrunchBase api.
Copyright (c) 2010 Apurva Mehta <mehta.apurva@gmail.com> for CrunchBase class

Edit made by Brian Anglin <brianranglin@gmail.com> to...
  * Update wrapper for API version 2.0 https://developer.crunchbase.com/docs

Edits made by Alexander Pease <alexander@usv.com> to...
  * Ensure compliance with 2013 API key requirement
  * Fix namespace conventions (ex: 'Kapor Capital' is sent as 'kapor+capital')
  * Functions requiring parsing of CrunchBase-return JSON (ex. list investors)
  * If HTTP request fails, return None instead of raising Exception
  * Set strict=false for json.loads(). Avoids some errors in the CB API.
  * Sanitize strings used as argument for __webRequest

"""

__author__ = 'Brian Anglin, Apurva Mehta, Patrick Reilly, Daniel Mendalka'
__version__ = '2.0.1'

import urllib2
import json
import unicodedata

API_BASE_URL = 'http://api.crunchbase.com/'
API_VERSION = '2'
API_URL = API_BASE_URL + 'v' + '/' + API_VERSION + '/'


class CrunchBase:

    def __init__(self, api_key, cache={}):
        self.api_key = api_key
        self.__cache = cache

    def __webRequest(self, url):
        print 'Making request to: ' + url
        try:
            opener = urllib2.build_opener(NotModifiedHandler())
            req = urllib2.Request(url)

            if url in self.__cache:
                if 'etag' in self.__cache[url]:
                    print 'Adding ETag to request header: '\
                        + self.__cache[url]['etag']
                    req.add_header('If-None-Match',
                                   self.__cache[url]['etag'])
                if 'last_modified' in self.__cache[url]:
                    print 'Adding Last-Modified to request header: '\
                        + self.__cache[url]['last_modified']
                    req.add_header('If-Modified-Since',
                                   self.__cache[url]['last_modified'])

            url_handle = opener.open(req)

            if hasattr(url_handle, 'code') and url_handle.code == 304:
                print 'Got 304 response, no body send'
                return self.__cache[url]['response']
            else:
                headers = url_handle.info()
                response = url_handle.read()

                cache_data = {
                    'response': response,
                    'last_modified': headers.getheader('Last-Modified'),
                    'url': url.replace('?api_key=' + self.api_key, '')}

                if headers.getheader('Last-Modified'):
                    cache_data['last_modified'] = \
                        headers.getheader('Last-Modified')

                if headers.getheader('ETag'):
                    cache_data['etag'] = headers \
                        .getheader('ETag').replace('"', '')

                self.__cache[url] = cache_data
                return response
        except urllib2.HTTPError, e:

            print 'HTTPError calling ' + url
            return None

    def createQueryArgs(self, kwargs):
        query_string = ''
        for key, value in kwargs.items():
            query_string = query_string + '&' + key + '=' + value
        return query_string

    def getSingleObjectForPath(self, path, namespace):
        """This returns result of a single path in JSON format"""
        if not path.startswith(namespace+'/'):
            path = namespace+'/'+path
        url = API_URL + path + '/?user_key='+ self.api_key
        return json.loads(self.__webRequest(url))

        return
    def getOrganizations(self, query, **kwargs):
        """This returns result of an organization search query in JSON format. Optional: name, domain_name, organization_types, location_uuids, category_uuids, page, order [created_at DESC/ASC, updated_at DESC/ASC]"""
        extra_args = self.createQueryArgs(dict( {'query':query}.items() + kwargs.items() ))
        url = API_URL + 'organizations/?user_key='+ self.api_key + extra_args
        return json.loads(self.__webRequest(url))

    def getOrganization(self, path):
        """This returns result of a single organization in JSON format"""
        return self.getSingleObjectForPath(path, 'organization')

    def getPeople(self, **kwargs):
        """This returns result of people in JSON format. Optional: page,  order [created_at DESC/ASC, updated_at DESC/ASC]"""
        extra_args = self.createQueryArgs( kwargs.items )
        url = API_URL + 'people/?user_key='+ self.api_key + extra_args
        return json.loads(self.__webRequest(url))

    def getPerson(self, path):
        """This returns result of a single person in JSON format"""
        return self.getSingleObjectForPath(path, 'person')

    def getProducts(self, **kwargs):
        """This returns result of products in JSON format. Optional: page,  order [created_at DESC/ASC, updated_at DESC/ASC]"""
        extra_args = self.createQueryArgs( kwargs )
        url = API_URL + 'products/?user_key='+ self.api_key + extra_args
        return json.loads(self.__webRequest(url))

    def getProduct(self, path):
        """This returns result of a single product in JSON format"""
        return self.getSingleObjectForPath(path, 'product')

    def getFundingRound(self, path):
        """This returns result of a single funding-round in JSON format"""
        return self.getSingleObjectForPath(path, 'funding-round')

    def getAcquisition(self, path):
        """This returns result of a single acquisition in JSON format"""
        return self.getSingleObjectForPath(path, 'acquisition')

    def getIPO(self, path):
        """This returns result of a single product in JSON format"""
        return self.getSingleObjectForPath(path, 'ipo')

    def getFundRaise(self, path):
        """This returns result of a single fund-raise in JSON format"""
      return self.getSingleObjectForPath(path, 'fund-raise')

    def getLocations(self, **kwargs):
        """This returns result of locations in JSON format. Optional: page"""
        extra_args = self.createQueryArgs( kwargs )
        url = API_URL + 'locations/?user_key='+ self.api_key + extra_args
        return json.loads(self.__webRequest(url))

    def getCategories(self, **kwargs):
        """This returns result of categories in JSON format. Optional: page"""
        extra_args = self.createQueryArgs( kwargs )
        url = API_URL + 'categories/?user_key='+ self.api_key + extra_args
        return json.loads(self.__webRequest(url))

# organization/dropbox
class CrunchBaseResponse(object):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.__dict__)


class CrunchBaseError(Exception):

    pass

class NotModifiedHandler(urllib2.BaseHandler):

    def http_error_304(self, req, fp, code, message, headers):
        addinfourl = urllib2.addinfourl(fp, headers, req.get_full_url())
        addinfourl.code = code
        return addinfourl