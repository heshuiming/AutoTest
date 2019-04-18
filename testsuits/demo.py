import csv


def get_data():
    data = csv.reader(open("C://Users//DELL//Desktop//test1.csv",'r'))
    dict = {}
    for user in data:
        dict['name'] = user[0]
        dict['pwd'] = user[1]
        print(dict)
        print(dict['name'])
        print(dict['pwd'])


get_data()