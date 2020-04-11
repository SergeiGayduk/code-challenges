# Reverse Int Explained

To check you can just & the result with the appropriate mask.

So in your case the limits are −2,147,483,648 and 2,147,483,647 the hex values of them are -0x80000000 and 0x7fffffff

Try this in the interpreter.
```
>>> 0x7fffffff
2147483647
>>> 2147483647 & 0x7fffffff   #within limit
2147483647
```
Values exceeding the limit, you can see some other value is displayed.
```
>>> 2147483648 & 0x7fffffff     #Exceeds limit
0
>>> 98989898989898 & 0x7fffffff  #Exceeds limit
1640235338
```
But when the value is within limit. The value is given as output.
```
>>> 1 & 0x7fffffff               #within limit
1
>>> 780 & 0x7fffffff
780
```
For negative values
```
 >>> -0x80000000     #Limit
-2147483648
>>> -2147483648 & -0x80000000
-2147483648
```
When the value is within the range. The limit is given as output.
```
>>> -2147483647 & -0x80000000
-2147483648
>>> -2 & -0x80000000          #within limit
-2147483648
>>> -2323 & -0x80000000
-2147483648
```
However if value is out of range you can see some other value is displayed.
```
>>> -2147483649 & -0x80000000
-4294967296
>>> -999999999999 & -0x80000000
-1000727379968
```
You can make use of this well and good to get what you want!

Here is a program that does what you want.
```
def reverse(x):
    str_x = str(x)
    if x<0:
        str_x = '-'+str_x[::-1][:-1]
        x = int(str_x)
    else:
        str_x = str_x[::-1]
        x = int(str_x)
    neg_limit= -0x80000000
    pos_limit= 0x7fffffff

    if(x<0):
        val=x&neg_limit
        if(val==neg_limit):
            return x
        else:
            return 0
    elif(x==0):
        return x
    else:
        val = x&pos_limit
        if(val==x):
            return x
        else:
            return 0

value = int(input("Enter value: "))
print(reverse(value))
```
The part below just reverses for both negative and positive values.
```
if x<0:
    str_x = '-'+str_x[::-1][:-1]
    x = int(str_x)
    print(x)
else:
    str_x = str_x[::-1]
    x = int(str_x)
    print(x)
```
Set the limits neg_limit= -0x80000000 and pos_limit= 0x7fffffff and check for them according to the explained logic.

Source: https://stackoverflow.com/questions/44581339/reverse-32bit-integer
