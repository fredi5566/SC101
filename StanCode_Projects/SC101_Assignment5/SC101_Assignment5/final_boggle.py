"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global
word_bank = []
ans_list = []


def main():
    """
    Description:
    1. 先讀取出字典
    2. 製造出 boggle checkerboard
    3. 對 boggle checkerboard 逐一檢查 (double for loop)
    4. 進入 boggle(Recursion)-- 應注意 choose 與 un-choose之間的對稱性
    5. Print 出結果
    """
    read_dictionary()
    print('Welcome to Boggle game!! ')

    boggle_list = making_boggle_list()

    for y in range(len(boggle_list)):
        for x in range(len(boggle_list)):
            word = boggle_list[x][y]
            find_boggle(boggle_list, word, x, y, [[x,y]])      # [[x,y]]: 為了避免一樣的字加了兩次

    print('There are ' + str(len(ans_list)) + ' words in total.')
    # boggle_list = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]


def find_boggle(boggle_list, current_ans, x, y, used_list):    # boggle沒有 base-case。就是要把16個字跑完
    '''
    Description:
    1. 對每一個字的九宮格作排列(一個字只能用一次，要設條件來卡住)
    2. 執行 choose- explore- un-choose
    3. un-choose時，記得把 choose時加進去的東西(該字母的index, current_ans)remove掉

    :param boggle_list: 要做boggle的 checkerboard
    :param current_ans: 當前的字串
    :param x:           檢查當下的該字母的 x座標  (絕對座標)
    :param y:           檢查當下的該字母的 y座標  (絕對座標)
    :param used_list    用來儲存當下字母(九宮格的for loop)的座標，以避免同樣的字母and自己被重複使用
    :return:
    '''
    for i in range(-1, 2, 1):                           # 開始檢查九宮格
        for j in range(-1, 2, 1):
            neighbor_x = x + j                          # 0 <= x <= 3
            neighbor_y = y + i
            if 0 <= neighbor_x < len(boggle_list):      # 0 <= * < 4。 因為上限不包含，所以 = 4 會超出範圍
                if 0 <= neighbor_y < len(boggle_list):

                    # chose
                    if [neighbor_x, neighbor_y] not in used_list:   # 避免同位置的字母被重複加到

                        current_ans += boggle_list[neighbor_x][neighbor_y]
                        used_list.append([neighbor_x, neighbor_y])  # 避免同位置的字母被重複加到 (絕對座標~~)

                        # explore
                        if has_prefix(current_ans):
                            find_boggle(boggle_list, current_ans, neighbor_x, neighbor_y, used_list)

                        # Un choose
                        current_ans = current_ans[:-1]
                        # used_list.remove([neighbor_x, neighbor_y])   # 這個寫法也可以
                        used_list.pop()                                # Last in First out


def has_prefix(sub_s):
    """
    Description: 增加boggle的運算速度-- Early Stopping
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    if sub_s in word_bank:
        if sub_s not in ans_list:       # 所以room 與 roomy 都可以印出來
            if len(sub_s) > 3:
                print('Found: ', sub_s)
                ans_list.append(sub_s)

    for i in range(len(word_bank)):
        word = str(word_bank[i])        # string is different to string object
        if word.startswith(sub_s):
            return True
    return False


def making_boggle_list():
    """
    Description: 先把user輸入的legal字串整理成boggle checkerboard
    :return: boggle_list
    """
    boggle_list = []  # 在list裡面放list
    row = 1
    error = 0
    while True:
        if len(boggle_list) == 4 or error != 0:
            break
        else:
            boggle = input(str(row) + ' row of letters: ')
            boggle = boggle.lower()  # case-insensitive
            row += 1
            current_list = []

            for i in range(len(boggle)):
                ele = boggle[i]

                if i % 2 == 1:  # check odd-index
                    if ele != ' ':
                        error += 1

                if i % 2 == 0:  # check even-index
                    if ele.isalpha():
                        current_list.append(ele)
                    # print(current_list)
                    else:
                        error += 1

            boggle_list.append(current_list)

    if error != 0:
        print('Illegal Input')

    else:
        return boggle_list


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()  # 把單字後的 \n 給消掉
            word_bank.append(word)
        print('Length of dictionary: ', len(word_bank))


if __name__ == '__main__':
    main()
