weight_earth = 62
weight_moon=weight_earth*0.165
year=2020
for i in range(0,16):
    year+=1
    weight_earth+=1
    weight_moon+=1
    print("Year", year, "weight on earth", weight_earth, "weight on moon", weight_moon)
