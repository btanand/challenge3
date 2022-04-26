import json

data_object = json.loads('{"a": { "b" : { "c" : { "d" : "first" } } } , "e" : "second" }')

# Function to get value , passing the object and the key
def retrieve_data(input_key, data_object):
    pos = input_key.rfind('/')
    key = input_key[pos:]
    res = dict(get_vals(data_object, key))
    print(res)


# Flattens the nested object into key value pairs
def get_vals(data, key_list):
        for i,j in data.items():
         if i in key_list:
            yield (i, j)
            print(i)
         yield from [] if not isinstance(j, dict) else get_vals(j, key_list)

# test
input = 'a/b/c/d'
retrieve_data(input, data_object)
