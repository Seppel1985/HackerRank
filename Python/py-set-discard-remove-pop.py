if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))

    n = int(input())
    lst = []
    for i in range(n):
        input_line = input()
        input_arr = input_line.split()
        if input_arr[0] == "pop":
            s.pop()
        elif input_arr[0] == "remove":
            s.remove(int(input_arr[1]))
        elif input_arr[0] == "discard":
            s.discard(int(input_arr[1]))
        else :
            print("falsche eingabe")
    print(sum(s))