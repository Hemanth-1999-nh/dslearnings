
"""
Code Challenge

# Initialize `fahrenheit` dictionary 
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

1 Get the corresponding `celsius` values in list

2 Create the `celsius` dictionary

3 convert a dictionary of Fahrenheit temperatures into celsius

"""

#step_1 :
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))

#step_2 :
celsius_dict = dict(zip(fahrenheit.keys(), celsius))

print(celsius_dict)


#step_3 :
celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}

print(celsius_dict)

