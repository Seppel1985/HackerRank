def split_and_join(line):
    # write your code here
    line_split = line.split(" ")
    return ("-".join(line_split))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)