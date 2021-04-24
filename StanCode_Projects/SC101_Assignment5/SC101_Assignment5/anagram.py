"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
import time
# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global
ans_list = []                 # The result of anagram
word_bank = []                # All word in dictionary


def main():
    read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        word = input('Find anagrams for: ')
        start = time.time()
        if word == EXIT:
            break
        else:
            print('Searching...')
            find_anagrams(word)
            print(len(ans_list), 'anagrams: ', ans_list)
            ans_list.clear()
        end = time.time()
        print(end-start)


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()                 # 把單字後的 \n 給消掉
            word_bank.append(word)
        print(len(word_bank))


def find_anagrams(s):
    """
    :param s: The word we want to do anagrams
    :return:
    """
    find_anagrams_helper(s, '', len(s))


def find_anagrams_helper(s,current_ans,original_length):

    if len(current_ans) == len(s):                                  # Base case- 字數到達 and 該字在 word_bank裡
        if current_ans not in ans_list:                             # 避免加入重複字彙
            if current_ans in word_bank:
                print('Found: ', current_ans)
                ans_list.append(current_ans)
                print('Searching...')
            else:
                pass
    else:
        for i in range(len(s)):
            word = s[i]                                             # 依序從s配對
            # print(word, i)                                        # s.count(**): **在s裡的總數
            if s.count(word) > current_ans.count(word):             # 用該字母的總數來判斷 ex: contains
                # choose
                current_ans += word

                # explore
                if has_prefix(current_ans):                         # Early stopping

                    find_anagrams_helper(s, current_ans,original_length)

                # Un choose
                current_ans = current_ans[:-1]


def has_prefix(sub_s):

    for i in range(len(word_bank)):
        word = str(word_bank[i])                                    # string is different to string object
        # print(word)
        if word.startswith(sub_s):
            # print(word)
            return True
    return False


if __name__ == '__main__':
    # read_dictionary()
    # has_prefix()
    main()

