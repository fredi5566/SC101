"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	if n < 0:         					        		# Change negative n to positive n
		n = -n
	else:
		n = n

	return find_largest_digit_helper(n,0)      		 	# 用 0 當作現下的max，所以一定會蓋過去。 int 會受到stack frame的影響!!
	# return find_largest_digit(n,0,0)				    # Original Method


def find_largest_digit_helper(n, current_max):
	if n // 10 < 1:								        # Base case- 當商小於1時，表示已是最後一位數。但要小心只有一位的數(ex: 6)。
		current_max = find_max(n, current_max)
		return current_max
	else:
		if current_max == 9:
			return current_max
		else:
			a = int(n % 10)                              # 從個位數依序檢查
			current_max = find_max(a, current_max)
			return find_largest_digit_helper(n//10,current_max)  # After check: n = n//10


def find_max(a,b):
	if a > b:
		return a
	else:
		return b


if __name__ == '__main__':
	main()

# Original method

# def find_largest_digit_helper(n, current_max, count):
#
# 	if n // 10**count < 1:								 # Base case
# 		return current_max
# 	else:
# 		if current_max == 9:
# 			return current_max
# 		else:
# 			a = int((n/(10**count))) % 10                 # 從個位數依序檢查
# 			current_max = find_max(a, current_max)
# 			return find_largest_digit_helper(n,current_max,count+1)
