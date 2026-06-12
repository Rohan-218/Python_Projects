# print(ord('#'))

"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Bradly.html'
count = 7
position = 18

for i in range(count):
    print("Retrieving:", url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all of the anchor tags
    tags = soup('a')
    
    # Get the specific link at position 18 (index 17)
    url = tags[position - 1].get('href', None)

print("Final URL:", url)
"""

"""
import urllib.request
import json

# Prompt for the URL
url = input("Enter location: ")
print("Retrieving", url)

# Retrieve the data
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

# Parse the JSON data
info = json.loads(data)

# Extract the comments list
comments = info['comments']

# Compute the sum
total = 0
for item in comments:
    # Access the 'count' field for each item and add it to the total
    total += int(item['count'])

# Output the final result
print("Count:", len(comments))
print("Sum:", total)
"""

import urllib.request, urllib.parse, urllib.error
import json

# The service URL endpoint
service_url = 'http://py4e-data.dr-chuck.net/opengeo?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    # Use urlencode to properly format the address
    url = service_url + urllib.parse.urlencode({'q': address})

    print('Retrieving', url)
    
    # Open the connection
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        # Load the data into a dictionary
        js = json.loads(data)
    except:
        js = None

    # Check if data exists and is not empty
    if not js or 'features' not in js or len(js['features']) == 0:
        print('==== Failure To Retrieve ====')
        continue

    # Extract the plus_code from the JSON structure
    # You may need to inspect the dictionary to confirm the exact path
    plus_code = js['features'][0]['properties']['plus_code']
    print('Plus code', plus_code)
