from urllib import request, parse
from json import loads

# url = 'http://httpbin.org/get'
#
# parms = {
#     'name1': 'value1',
#     'name2': 'value2'
# }
#
# querystring = parse.urlencode(parms)
#
# u = request.urlopen(url + '?' + querystring)
# resp = u.read()
#
# print(resp)

# ------------------------------------------------------------------------------

# Base URL being accessed
url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-005'

# Dictionary of query parameters (if any)
parms = {
   'Authorization': 'CWB-F6F2390F-673B-41C2-AB26-98A36BCB912A',
   'format': 'JSON'
}

# Encode the query string
querystring = parse.urlencode(parms)
print(querystring)

# Make a GET request and read the response
u = request.urlopen(url + '?' + querystring)
resp = dict(loads(u.read()))
print(resp['records'])