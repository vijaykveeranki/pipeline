prefix = "python is an "

sufix = "awesome launguage"

astr = prefix+sufix

print(astr)

astr = astr.replace("launguage", "snake.")

astr = astr*2

print(astr)

astr = astr.replace("snake." ,  "launguage", 1)

print(astr)

print(astr.count("an"))