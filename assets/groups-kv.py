import os
import json
import requests

if os.path.exists('groups.json'):
    with open('groups.json', 'r') as f:
        groups = json.load(f)
else:
    groups = requests.get('https://dataleak.hopeless99.top//groups').json()
eventdict = []
for group in groups:
    for loc in group['locations']:
        event = group.copy()
        event.pop('locations')
        event.update(loc)
        eventdict.append(event)
        event['host'] = event.pop('fqdn')

with open('assets/groups-kv.json', 'w') as f:
    json.dump(eventdict, indent=2, fp=f)
