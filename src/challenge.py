# Return the "centered" average of an list of ints, 
# which we'll say is the mean average of the values, 
# except ignoring the largest and smallest values in the list.
# if there are multiple copies of largest or smallest values, ignore only one of min / max values.
# the input list may be unsorted.
# you may assume that the list is length 3 or more

# you can make your own sort or you can use the built in sort function. 

def centered_average(arr):
    sum = 0
    smallest = arr[0]
    largest = arr[0]

    for i in arr:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i

        sum += i

    sum = sum - smallest - largest
    avg = int(sum / (len(arr) - 2))
    return avg


print(centered_average([1, 2, 3, 4, 100])) 
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))

