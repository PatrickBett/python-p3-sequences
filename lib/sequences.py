#!/usr/bin/env python3

def print_fibonacci(length):
    num_list = list()
    
    if length == 0:
        print(list())
    
    for i in range(length):
        if len(num_list) > 1:
            next_number = num_list[-1] + num_list[-2]
            num_list.append(next_number)
            
        else:
            num_list.append(i)

    print(num_list)
print_fibonacci(9)
          