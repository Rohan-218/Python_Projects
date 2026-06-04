Dict={
    "name":"Rohan",
    "age":21,
    "is_verified":True
}
Dict["name"]="Nikhil"
Dict["birthdate"]= "sep 30 2003"
# print(Dict["name"])
# print(Dict.get("hgh"))
# print(Dict.get("hgh","hgfdkjg"))
# print(Dict.get("birthdate"))

for key, value in Dict.items():
    print(str(key) + " : " + str(value))