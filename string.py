'''
collection of character
upper
lower
index
find
replace
count
removesufix
removeprefix
ends with
starts with
split
strip
lstrip
rstrip
'''
pythonlife="please do"
print(pythonlife.upper())
pythonlife="PLEASE DO"
print(pythonlife.lower())
pythonlife="python language"
print(pythonlife.endswith("language"))
pythonlife="python language"
print(pythonlife.startswith("language"))
pythonlife="python language"
print(pythonlife.replace("language","programming"))
#print(pythonlife.index("kiran"))
pythonlife="python language"
print(pythonlife.find("kiran"))
pythonlife="python language"
print(pythonlife.index("python"))
pythonlife="python language"
print(pythonlife.find("python"))
pythonlife="python language"
#print(pythonlife.count("g"))
print(pythonlife.removeprefix("python"))
print(pythonlife.removesuffix("language"))
pythonlife="python language"
print(pythonlife.split())
#it convert into list
pythonlife="  python language   "
print(pythonlife)
print(len(pythonlife))
#it remove spaces
print(pythonlife.strip())
#it remove right space
print(pythonlife.rstrip())
#it remove left space
print(pythonlife.lstrip())
v=pythonlife.lstrip()
python(len(v))

