def read(file_name):
    """ File Structure
        1º Number of Test cases
        2º Test cases
        3º Test cases
        ...
        nº Test cases
    """
    file = open(file_name, "r")

    strings = []
    i = 0
    with file as f:
        t = file.readline().split()
        test_case = int(t[0]) # T 

        for line in f:
            words = line.split()

            strings.append([]) 

            for an_word in words:
                strings[i].append(an_word) # Saving the strings in a matrix
            i += 1

    return test_case, strings

def maxswap(S):
    """ 1. find first 'b'
        2. From the next position after 'b', find the continuous sub list with maximum 
        value ('a' = 1, 'b' = -1)
        3. Reverse the first 'b' and the following continuous sub array (if there's one)
    """
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

def replace_words(s, words):
    """ Replace character in a string based in a dictionary"""
    for k, v in words.items():
        s = s.replace(k, v)
    return s    

def main():
    input_file = "data/sample.in"

    T, S = read(input_file)
    print(T)
    
    with open('data/output/res.out', mode='w', encoding='utf-8') as output_file:
        for element in S:
            s = str(element)
            dict1 = {'[' : "", "'" : "", " " : "", "'" : "","]" : ""}
            # First time to remove the characters in dict1
            coord = replace_words(s, dict1)
            # Removing that characters the program results the values correctly
            strings = str(maxswap(coord))
            dict2 = {'[' : "", "'" : "", " " : "", "'" : "","]" : ""}
            # Second time to remove the characters in dict2
            newS = replace_words(strings, dict2)
            # Removing that characters the output is correctly
            output_file.write(newS + '\n')
    
if __name__ == "__main__":
    main()

            

            

    