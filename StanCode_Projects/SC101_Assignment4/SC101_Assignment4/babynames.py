"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import sys


def find_min(a,b):
    if a > b:
        return str(b)
    else:
        return str(a)


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.
    把 filename(list) 裡的 data加到 name_data(dict)!!

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    d_student = {}                              # 先設一個空的dict(第二層)
    if name not in name_data:
        d_student[year] = rank                  # 第二層 d[key] = value
        name_data[name] = d_student             # 第一層 d[name] = value(第二層的dict); 在name_data這個dict裡再創造一個新的dict

    elif name in name_data:
        if year in name_data[name]:
            old_rank = int(name_data[name][year])
            new_rank = find_min(old_rank, int(rank))
            name_data[name][year] = new_rank    # 表示是中性的名字，所以才會在那一年出現兩次排名!!
        else:
            name_data[name][year] = rank        # 把同名但不同年份的data(value)放到該同名的資料夾(key); 沒有再創一個新的dict!!


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    整理 filenames 裡的 filename。在 add_file裡把filename裡的data(year, rank, name)萃取出，再用 add_data_for_name把那些data加到name_data(dict)裡
    ex: 某個 filename是 2010的名次排名，然後先找出 name來當作key -- d[name][year] = rank

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data  # filename是在 filenames這個list裡的其中一個ele

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    with open(filename, 'r') as f:
        # first_line = True
        count = 0
        for line in f:                                  # 對這個filename.txt逐行處裡，並加到name_data(dict)裡
            info_lst = line.split(',')                  # 把各行資訊整理成一個list，這樣才能處理
            # if first_line = True:
            if count == 0:
                year = info_lst[0].strip()              # The first line in all txt is 'year'
                count += 1
                # first_line = False
            else:
                rank = info_lst[0].strip()
                man_name = info_lst[1].strip()          # One filename has two names, so we need to add data twice.
                woman_name = info_lst[2].strip()
                add_data_for_name(name_data,year,rank,man_name)
                add_data_for_name(name_data, year, rank, woman_name)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}

    for filename in filenames:                        # Add all 'filename(str)' from 'filenames(list)' to name_data
        add_file(name_data,filename)                  # For each loop
    return name_data

    # for i in range(len(filenames)):
    #     add_file(name_data, filenames[i])           # Add all 'filename(str)' from 'filenames(list)' to name_data
    # return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    names = []
    for key in name_data:
        key1 = key.lower()                                     # for case-insensitive
        target = target.lower()
        if target in key1:
            names.append(key)
    return names

    # for key, value in name_data.items():                    # 也可用上面的for each loop
    #     key1 = key.lower()                                  # for case-insensitive
    #     target = target.lower()
    #     if target in key1:
    #         # print(key)
    #         names.append(key)
    # return names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]                                     # args 變一個從一開始的list
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args                                        # filenames 變成一個list

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
