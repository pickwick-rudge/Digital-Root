#This exercise assumes normal numbers as inputs for n

def digital_root(n):
    '''cast n to a string, so I can iterate through it, and initialize total to 0'''
    n = str(n)
    total = 0

    '''Use a list comprehension to separate n into its component digits, then
       iterate through n_list and add to the total counter'''
    n_list = [x for x in n]
    for num in n_list:
        total += int(num)

    '''While the total counter is > 9, set a second counter to 0 and cast total to a string.
       For each num in total, do the same thing as above and increment that onto new_total.
       Then set total equal to new_total, so that the while loop can begin its next iteration
       with new_total's value.  The loop exits when a single-digit value is finally returned.
       '''
    while total > 9:
        new_total = 0
        total = str(total)
        for num in total:
            new_total += int(num)
        total = int(total)
        total = new_total

    return total

print(digital_root(493193))

'''Want to see the snazzy, best practice solution that popped up immediately
   after I submitted this passing solution? -_-'''
            
def d_root_2(n):
    return n if n < 10 else d_root_2(sum(map(int, str(n))))

print(d_root_2(493193))
        

