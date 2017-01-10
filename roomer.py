import csv

def readfile(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    data = list(reader)[1:]

    males = {}
    females = {}
    for d in data:
        if d[1] == "Male":
            males[d[0]] = [d[2], d[3], d[4], d[5]]
        else:
            females[d[0]] = [d[2], d[3], d[4], d[5]]
    return males, females

def make_2d(dict):
    dictionary = {}
    names = list(dict.keys())
    for name in names:
        for nameagain in names:
            if name not in dictionary:
                dictionary[name] = {}
            if name != nameagain:
                dictionary[name][nameagain] = 0
    return dictionary

def add_roommate_positives(dict_2d, data, weight = 1):
    for a in data:
        roommate_info = data[a]
        index = 0
        while index < 3:
            poi = roommate_info[index]
            if poi != "":
                dict_2d[a][poi] = weight
            index += 1
    return dict_2d

m, f = readfile("roominginfo.csv")
male_2d = make_2d(m)
female_2d = make_2d(f)
male_2d = add_roommate_positives(male_2d, m)
female_2d = add_roommate_positives(female_2d, f)