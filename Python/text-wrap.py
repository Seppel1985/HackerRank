import textwrap

def wrap(string, max_width):
    string_new =""
    for x in range(0, len(string), max_width):
        string_new = string_new + string[x:x+max_width] + "\n"
    return string_new[:-1]

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
