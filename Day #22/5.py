# List comprenhension

names = ["halo", "search", "polio", "annalia", "Rosa"]
nameswith_o = [item for item in names if (len(item)>4)]
print(nameswith_o)

namesless = [item for item in names if (len(item)<=4)]
print(namesless)