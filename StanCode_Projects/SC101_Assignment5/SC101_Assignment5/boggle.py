"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary666.txt'

# Global
word_bank = []
ans_list = []


def main():
	"""
	TODO:
	"""
	read_dictionary()
	print('Welcome to Boggle game!! ')

	# boggle_list = making_boggle_list()

	# print(boggle_list)
	# print('Len of boggle_list ',len(boggle_list))
	# print(boggle_list[0][0])
	# print(boggle_list[1][1])
	# print(boggle_list[2][2])
	# print(boggle_list[3][3])
	boggle_list = [['f','y','c','l'],['i','o','m','g'],['o','r','i','l'],['h','j','h','u']]
	find_boggle(boggle_list)
	print('There are ' + str(len(ans_list)) + ' words in total.')


def find_boggle(boggle_list):
	find_boggle_helper(boggle_list,'')


def find_boggle_helper(boggle_list, current_ans):
	'''
	Description:
	1.利用 double for loop 對串好的boggle_list[x][y]逐一檢查: choose1
	2.再利用 "另外的" double for loop 檢查 boggle_list[x][y]的九宮格
	3.1 choose1: 開始串
	3.2 choose2: 串完第一個開始 串 9宮格

	:param boggle_list:
	:param current_ans:
	:return:
	'''

	for x in range(len(boggle_list)):
		for y in range(len(boggle_list)):
			word = boggle_list[x][y]
			current_ans += word                                # 先串自己，後面再來檢查自己的九宮格

			for i in range(-1,2,1):							   # 開始檢查九宮格
				for j in range(-1,2,1):
					neighbor_x = x+i                           # 0 <= x <= 3
					neighbor_y = y+j
					if 0 <= neighbor_x < len(boggle_list):     # 0 <= * < 4。 因為上限不包含，所以 = 4 會超出範圍
						if 0 <= neighbor_y < len(boggle_list):
							around_word = boggle_list[neighbor_x][neighbor_y]
							if i != 0 or j != 0:			   					# 避免串到自己
								if boggle_list[neighbor_x][neighbor_y] != ' ':  # 避免來來回回重複串

									# choose
									current_ans += around_word
									boggle_list[x][y] = ' '

									# explore
									if has_prefix(current_ans):
										find_boggle_helper(boggle_list, current_ans)

									# Un choose
									boggle_list[x][y] = word
									current_ans = current_ans[:-1]

			current_ans = current_ans[:-1]


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	if sub_s in word_bank:
		if sub_s not in ans_list:
			print('Found: ', sub_s)
			ans_list.append(sub_s)

	for i in range(len(word_bank)):
		word = str(word_bank[i])  # string is different to string object
		if word.startswith(sub_s):
			return True
	return False


def making_boggle_list():
	boggle_list = []    # 在list裡面放list
	row = 1
	error = 0
	while True:
		if len(boggle_list) == 4 or error != 0:
			break
		else:
			boggle = input(str(row)+' row of letters: ')
			boggle = boggle.lower()				   # case-insensitive
			row += 1
			current_list = []

			for i in range(len(boggle)):
				ele = boggle[i]

				if i % 2 == 1:          			# check odd-index
					if ele != ' ':
						error += 1

				if i % 2 == 0:          			# check even-index
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
