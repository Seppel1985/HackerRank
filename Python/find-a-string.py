def count_substring(string, sub_string):
    counter=0
    for i in range(len(string)):
        string_substr = string[i:len(sub_string)+i]
        if (string_substr == sub_string):
            counter = counter +1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)