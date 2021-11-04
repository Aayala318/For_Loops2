# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(num_list):
    for x in range(0,len(num_list)):
        if num_list[x]>0:
            num_list[x]='big'
    return num_list
print(biggie_size([-1, 3, 5, -5]))


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(num_list):
    count = 0
    for x in range(0,len(num_list)):
        if num_list[x]>0:
            count += 1
    last_x = len(num_list) - 1
    num_list[last_x]= count
    return num_list
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))


# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(num_list):
    sum = 0
    for x in range(len(num_list)):
        sum += num_list[x]
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))


# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def average(num_list):
    sum = 0
    for x in range(len(num_list)):
        sum += num_list[x]
    return sum/len(num_list)
print(average([1,2,3,4]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(num_list):
    return len(num_list)
print(length([37,2,1,-9]))
print(length([]))


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(num_list):
    if len(num_list) == 0:
        return False
    else:
        min = num_list[0]
        for x in range(len(num_list)):
            if num_list[x]<min:
                min = num_list[x]
        return min
print(minimum([37,2,1,-9]))
print(minimum([]))


# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(num_list):
    if len(num_list) == 0:
        return False
    else:
        max = num_list[0]
        for x in range(len(num_list)):
            if num_list[x]>max:
                max = num_list[x]
        return max
print(maximum([1,2,37,-9]))
print(maximum([]))


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

# dict {'sum_total': , 'average': , 'minimum': , 'maximim': , 'length': }
def ultimate_analysis(num_list):
    sum = sum_total(num_list)
    avg = average(num_list)
    min = minimum(num_list)
    max = maximum(num_list)
    lth = length(num_list) 
    analysis = {
        'sumTotal': sum,
        'average': avg,
        'minimum': min,
        'maximum': max,
        'length': lth
    }
    return analysis
print(ultimate_analysis([37,2,1,-9]))


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(num_list):
    list_len = len(num_list)
    for x in range(int(list_len/2)):
        temp = num_list[list_len-1-x]
        num_list[list_len-1-x]=num_list[x]
        num_list[x]=temp
    return num_list
print(reverse_list([37,2,1,-9]))
print(reverse_list([3,1,8,10,-5,6]))