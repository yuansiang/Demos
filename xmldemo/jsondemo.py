import json

#python data (int. float. unicode .etc etc)
pdata = [ {'a':1, 'b':2, 'c':3} ]
print(pdata)

#encode (python to json)
encoded = json.dumps(pdata)
print(encoded)

#encode with sorting and formatting (python to json)
encoded = json.dumps(pdata,sort_keys=True, indent = 2)
print (encoded)

# JSON data (string) 
jdata = '[ {"a":1, "b":2, "c":3} ]'

# decode (json to python)
decoded = json.loads(jdata)
print (decoded)

# this is a list
print (decoded), type(decoded)
# this is a dictionary
print (decoded[0]), type(decoded[0])
# display key-value pairs
for k, v in decoded[0].items():
    print (k, v)
