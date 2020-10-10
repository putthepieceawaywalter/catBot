#!/usr/bin/env python3 
import requests
import json




key = {'x-api-key': 'c07bf7e3-f5bc-44f4-8da6-5f4c725e0b09'}
url = 'https://api.thecatapi.com/v1/images/search?category_ids=1' 
#url = 'https://api.thecatapi.com/v1/categories'
r = requests.get(url, key)



for k in r.json():
    print('{}'.format(k['url']))

#json_string = json.dumps(r.json())
#print(json_string.strip('[{"breeds"'))
