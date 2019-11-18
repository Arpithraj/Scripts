import shodan

SHODAN_API_KEY = "1RLr3udL7cOjOjVkiMlTjZSkD1lTXVFZ"

api = shodan.Shodan(SHODAN_API_KEY)

try:
	#Search Shodan
	results = api.search('Raspbian')

	#Show results
	for result in results['matches']:
		print '%s' % result['ip_str']
except shodan.APIError, e:
	print 'Error: %s' % e
