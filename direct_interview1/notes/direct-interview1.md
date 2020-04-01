# Direct Interview number #1

You are given a string S. Each character of S is either 'a' or 'b'. You wish to reverse exactly one sub-string of S such that the new string is **lexicographically** smaller than all the other strings that you can get by reversing exactly one sub-string.
For example, given 'abab', you may choose to reverse the substring 'ab' that starts from index 2 (O-based). This gives you the string 'abba'. 
But, if you choose the reverse the substring 'ba' starting from index 1, you will get 'aabb'. There is no way of getting a smaller string, hence reversing the substringin the range [1, 2] is optimal.

<h1>Input</h1>

First line contains a number T, the number of test cases. 
Each test case contains a single string S. The characters of the string will be from the se {a, b}.

<h1>Output</h1>

For each test case, print two numbers separated by comma; for example “x,y” (without the quotes and without any additional whitespace). “x,y” describe the starting index (0-based) and ending index respectively of the substring that must be reversed in order to achieve the smallest lexicographical string. If there are multiple possible answers, print the one with the smallest ‘x’. If there are still multiple answers possible, print the one with the smallest ‘y’.

<h1>Constraints</h1>

1 <= **T** <= 100

1 <= **length of S** <= 1000

<h1>Solution</h1>

To solve this challenge, it was used Big O notation, in which is a mathematical notation
that describes the limiting behavior of a function whe the argument tends to towards a particular value or infinity, it is a member of a family of notations invented by Paul Bachmann, Edmund Landau, and others, collectively called **Bachmann-Landau notation** or **asymptotic notation**.

In computer science, big O notation is used to **classify algorithms** according to how their running time or space requirements grow as the input size grows. In analytic number theory, big O notation is often used to express a bound on the difference between an arithmetical function and a better understood approximation; a famous example of such a difference is the remaider term in the prime number theorem. (source: [Wikipedia](https://en.wikipedia.org/wiki/Big_O_notation))

```
def maxswap(S):
    slen = len(S)
    i, j = 0, 0
    while i < slen:
        if S[i] == 'b':
            break
        i += 1
    
    if i == slen:
        return [0, 0]
    
    val = -(slen - i - 1)
    rj = i
    sval = 0
    for j in range(i + 1, slen):
        if S[j] == 'a':
            sval += 1
        else:
            sval -= 1
        
        if sval > val:
            rj = j
            val = sval
    
    if rj == i:
        return [0, 0]
    
    return [i, rj]
```
The function above it was written in **python**. And it is the best piece of code of the  **o(n^2)**.