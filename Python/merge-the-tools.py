def merge_the_tools(string, k):
    # your code goes here
    n_k = int(len(string) / k)
    step_length = int(len(string)/n_k)
    for i in range(0, len(string),step_length):
        t = string[i:i+step_length]
        u = list(dict.fromkeys(t))
        str_result = ""
        print(str_result.join(u))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)