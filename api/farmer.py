import json
from jsonschema import validate
with open("./schemas/farmer.json","r") as f:
    farmerSchema = json.load(f)

#accurate object
farmer1 = {
    "farmer_id":"AK/OT/0008",
    "name":"Lubowa Ahmed"
}
#incorrect id length
farmer2 = {
    "farmer_id":"AK/OT/004",
    "name":"Lubwama Ahmed"
}
#missing name
farmer3 = {
    "farmer_id":"AK/OT/0009"
}

def submit_farmer(farmer):
    try:
        validate(farmer,farmerSchema)
        print(farmer)
    except Exception as e:
        col = list(e.path)[0] if len(e.path) else ""
        print(col+' '+e.message)

list(map(submit_farmer,[farmer1,farmer2,farmer3]))