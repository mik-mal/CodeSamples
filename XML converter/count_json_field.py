'''
Reads a json file and outputs the number of occurances of each field name within the json.
To be used with a series of json objects with multiple optional fields to determine which fields are actually used.

'''

import json
from collections import Counter
import csv
from flatten_json import flatten

# Open the file containing the JSON objects
with open('sample.json') as f:
    data = f.read()

# Parse the JSON objects
objects = json.loads(data)
flat = [flatten(obj) for obj in objects]
# Flatten the objects
fields = []
for obj in flat:
    fields.extend(obj.keys())

    
# Count the number of occurrences of each field
count = Counter(fields)

""" Results to csv """

with open('field_count.csv', 'w', newline='') as csvfile:
    fieldnames = ['field', 'occurrences']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for field, occurrences in count.items():
        writer.writerow({'field': field, 'occurrences': occurrences})

