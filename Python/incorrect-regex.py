import re
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        line = input()
        try:
            re.compile(line)
            print("True")
        except re.error:
            print("False")