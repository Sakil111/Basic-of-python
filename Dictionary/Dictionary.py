# creating Dictionary
carrier_dictionary={"Python":"Data science","Java script":"web development","java":"app development"}
print(carrier_dictionary)

# Adding value in dictionary
carrier_dictionary["R"]="Statistics"
print(carrier_dictionary)

# Removing key and values from the dictionary
# carrier_dictionary={}
# print(carrier_dictionary)


# changing the value in a dictionary
carrier_dictionary["jave"]="App Development"
print(carrier_dictionary)

# Loop using in the dictionary
for key in carrier_dictionary:
    print(key) # if we want to print key
    print(carrier_dictionary[key]) # to print value corresponding to the key
