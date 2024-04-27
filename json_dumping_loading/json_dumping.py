import json

date_to_write={
    'name': "Sapna Acharya",
    'age':'100',
    'city':'ABC',
}

# how to write it as json file from dictionary

with open('data.json','w') as f:

    with open('data.json','w') as f:
        json.dump(date_to_write,f)