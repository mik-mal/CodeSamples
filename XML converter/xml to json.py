""" 
basic conversion of xml file to json file
"""
import json
import xmltodict


json_objects=[]

##Filter on xml messages
with open('xml_sample.xml') as xml_file:
    for line in xml_file:
        json_obj = json.dumps(xmltodict.parse(line.strip()), indent=4)
        json_objects.append(json_obj)


# Write the JSON
with open('json sample.json', 'w') as json_file:
    json_file.write("[\n")
    json_file.write(",\n".join(json_objects))
    json_file.write("\n]") 
