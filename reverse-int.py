import sys
def is_int32(number):
    try:
        return not(int(number)>>1534236469)
    except ValueError:
        return False

def reverse(x):
    """
    Given a 32-bit signed integer, reverse digits of an integer.

    Example 1:
    Input: 123
    Output: 321
    
    Example 2:
    Input: -123
    Output: -321

    Example 3:
    Input: 120
    Output: 21

    Note:
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
    [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
    """

    neg_limit =-0x80000000 # hex(-2**31-1),see details in accepted answer above
    pos_limit = 0x7fffffff #hex(2**31-1)
    if x >= 0:
        reverse_num = int(str(x)[::-1])
        if reverse_num & pos_limit==reverse_num: 
            return reverse_num
        else:
            return 0

    elif x <= 0:
        reverse_num = -int(str(abs(x))[::-1])
        if reverse_num&neg_limit == neg_limit:
            return reverse_num
        else:
            return 0
        
    
   

print(reverse(1534236469))
print(reverse(-1534236469))
print(reverse(120))