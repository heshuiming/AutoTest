
list = []
# dict = {}
def get_data(file_path):
    f = open(file_path,'r').readlines()
    dict = {}
    for line in f:
        line = line.strip('\n')
        # print(line)
        (key,value) = line.split(' ')
        dict[key] = value
    print(dict)

    a = dict['a']
    print(a)

get_data("C://Users//DELL//Desktop//test_data.txt")