from functools import reduce
from operator import xor

s_box = [3,13,10,2,1,7,11,5,12,14,15,6,9,8,0,4]
def enlarge_to_4_bits(binary_value):
    # Check if the input binary value has more than 4 bits
    if len(binary_value) > 4:
        return binary_value
    result = format(int(binary_value, 2), '04b')
    return result
def dotbitproduct(a,b):
    # a and b to two arrays and each num of a with each num of b and then xor each result
    xora = []
    x = enlarge_to_4_bits(bin(a).removeprefix("0b"))
    y = enlarge_to_4_bits(bin(b).removeprefix("0b"))
    for i in range(4):
        xora.append(int(x[i]) & int(y[i]))
    result = reduce(xor, xora)
    return result
def calculatelat(inmask,outmask,sbox):
    count = 0
    for i in range(16):
        a = dotbitproduct(inmask,i)
        b = dotbitproduct(outmask,sbox[i])
        if(a == b):
            count = count+1
    return count
def lattable(sbox,degree):
    table = [[0 for _ in range(16)] for _ in range(16)]
    for i in range(16):
        for j in range(16):
            table[i][j] = calculatelat(i,j,sbox) - 2**(degree-1)
    return table
print("0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15")
count = 0
for row in lattable(s_box,4):

    formatted_result = '[' + ', '.join(str(num) + ' ' if num < 0 else str(num) for num in row) + ']'
    print(str(count) +' '+ formatted_result)
    count=count+1
