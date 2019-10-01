# how to define a function

name = "dave"
l = [1, 2, 3, 4]

def cap(n):
    return n.capitalize()
# define a doubling function that passes args by value
def mult(x):
    return x * 2

# define a doubling function that passes args by reference

def mult2(lst):
    for i in range(len(lst)):
        # lst[i] = lst[i] * 2
        lst[i] *= 2

    # no return necessary -
    # passing by reference means that
    # original list is modified

# try out our functions

print(name) # => "dave"
cap(name) # => "Dave" 
print(name) # => "dave"

#mult
n = 12
print(n) # => 12
print(mult(n)) # => 24
print(n) # => 12

#mult2
print(l) #=> [1, 2, 3, 4]
print(mult2(l)) # => None
print(l) # => [2, 4, 6, 8]