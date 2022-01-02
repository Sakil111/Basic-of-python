travel_log={"India":{"city_visited":["Delhi","Mumbai","Kashmir"],"total_visited":10},
            "Germany":{"city_visited":["Berlin","Munich","Dortmund"],"total_visited":15}}

print(travel_log)

# Nesting Dictionary into a list
tranvel_log2=[
    {"Country": "India",
     "city_visited":["Delhi","Mumbai","Kashmir"],
     "total_visited":10},
    {"Country": "Germany",
     "city_visited":["Berlin","Munich","Dortmund"],
     "total_visited":15}
]

print(tranvel_log2)

def add_new_country(country,city,visit):
    new_country={}
    new_country["Country"]=country
    new_country["city_visited"]=city
    new_country["total_visited"]=visit
    tranvel_log2.append(new_country)
add_new_country("Nepal",["katmondu"],2)

add_new_country("Russia",["sait petersberg"],2)
print(tranvel_log2)