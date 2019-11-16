# You have to create a function that takes a positive integer number
# and returns the next bigger number formed by the same digits
# If no bigger number can be composed using those digits, return -1

def next_bigger_number(num):
    # Turn a single number into single digits Python using list comprehension
    list_digits = [int(d) for d in str(num)]

    n = len(list_digits)

    # Traverse the given list of digits from right to left
    for i in range(2, n + 1):

        # keep traversing till you find a digit which is smaller than the previously digit
        if list_digits[n - i] < list_digits[n - i + 1]:

            # Search the right side of above found digit d for the smallest digit greater than d
            right = list_digits[n - i + 1:n]
            right.sort()

            for j in range(len(right)):
                if right[j] > list_digits[n - i]:
                    next_num = right[j]
                    right[j] = list_digits[n - i]

                    break

            middle = [next_num]

            left = list_digits[0:n - i]

            # combine all lists into one
            final = left + middle + right

            list_strings = map(str, final)

            s = ''.join(list_strings)

            next_bigger_num = int(s)

            if int(s) > num:
                return next_bigger_num

    return -1


# Test cases

# 12 ==> 21
print(next_bigger_number(12))

# 513 ==> 531
print(next_bigger_number(513))

# 2017 ==> 2071
print(next_bigger_number(2017))

# 9 ==> -1
print(next_bigger_number(9))

# 111 ==> -1
print(next_bigger_number(111))

# 531 ==> -1
print(next_bigger_number(531))

# 218765 ==> 251678
print(next_bigger_number(218765))

# 1234 ==> 1243
print(next_bigger_number(1234))

# 4321 ==> -1
print(next_bigger_number(4321))

# 534976 ==> 536479
print(next_bigger_number(534976))

# 9 ==> -1
print(next_bigger_number(9))

# 1111 ==> -1
print(next_bigger_number(1111))

# 1432 ==> 2134
print(next_bigger_number(1432))

# 1430 ==> 3014
print(next_bigger_number(1430))







