voting_data = []
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})

for county_dict in voting_data:
    for county, voters in voting_data.items():
        print(county + " county has " + str(voters) + " registered voters.")
