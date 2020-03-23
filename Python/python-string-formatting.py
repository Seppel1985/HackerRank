def print_formatted(number):
    # your code goes here
    width = len(bin(number).lstrip("0b").rstrip("L"))
    for i in range (number):
        print(str(i+1).rjust(width) + " "+ (oct(i+1).lstrip("0o").rstrip("L")).rjust(width) + " " + ((hex(i+1).lstrip("0x").rstrip("L")).upper()).rjust(width) + " " + (bin(i+1).lstrip("0b").rstrip("L")).rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)