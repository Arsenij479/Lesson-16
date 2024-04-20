import json
person = {
    'name': 'Max',
    'age': 10,
    'phones': ['9111', '738333']
}
result = json.dumps(person)
print(result)
print(type(result))


result = json.dumps(person)
print(result)
print(type(result))
{
    "person":{
      "name":"Саша",
      "age":37
      "mother":"Оксана",
      "age":35
    },
    "children":[
        "Маша",
        "Никита",
        "Лёша"
    ],

}