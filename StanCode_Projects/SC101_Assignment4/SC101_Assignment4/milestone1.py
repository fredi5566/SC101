"""
File: Milestone1.py
Name: 
-----------------------
This file tests the milestone 1 for
our babyname.py project
"""

import sys


def find_min(a,b):
    if a > b:
        return str(b)
    else:
        return str(a)


def add_data_for_name(name_data, year, rank, name):

    d_student = {}                             # 先設一個空的dict(第二層)
    if name not in name_data:
        d_student[year] = rank                 # 第二層 d[key] = value
        name_data[name] = d_student            # 第一層 d[name] = value(第二層的dict); 在name_data這個dict裡再創造一個新的dict

    elif name in name_data:
        if year in name_data[name]:
            old_rank = int(name_data[name][year])
            new_rank = find_min(old_rank,int(rank))
            name_data[name][year] = new_rank   # 表示是中性的名字，所以才會在那一年出現兩次排名!! 這邊我們取小的
        else:
            name_data[name][year] = rank       # 把同名但不同年份的data(value)放到該同名的資料夾(key); 沒有再創一個新的dict!!

    # name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    # add_data_for_name(name_data, '2010', '208', 'Kate')
    # add_data_for_name(name_data, '2000', '108', 'Kate')
    # add_data_for_name(name_data, '1990', '200', 'Sammy')
    # add_data_for_name(name_data, '1990', '90', 'Sammy')
    # add_data_for_name(name_data, '2000', '104', 'Kylie')

# ------------- DO NOT EDIT THE CODE BELOW THIS LINE ---------------- #


def test1():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    print('--------------------test1----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test2():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test2----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test3():
    name_data = {'Kylie': {'2010': '57'}, 'Sammy': {'1980': '451', '1990': '200'}, 'Kate': {'2000': '100'}}
    add_data_for_name(name_data, '1990', '900', 'Sammy')
    add_data_for_name(name_data, '2010', '400', 'Kylie')
    add_data_for_name(name_data, '2000', '20', 'Kate')
    print('-------------------test3-----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test4():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    add_data_for_name(name_data, '2000', '108', 'Kate')
    add_data_for_name(name_data, '1990', '200', 'Sammy')
    add_data_for_name(name_data, '1990', '90', 'Sammy')
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test4----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def main():
    args = sys.argv[1:]
    if len(args) == 1 and args[0] == 'test1':
        test1()
    elif len(args) == 1 and args[0] == 'test2':
        test2()
    elif len(args) == 1 and args[0] == 'test3':
        test3()
    elif len(args) == 1 and args[0] == 'test4':
        test4()


if __name__ == "__main__":
    main()
