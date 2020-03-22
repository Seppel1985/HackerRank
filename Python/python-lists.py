if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        input_line = input()
        input_arr = input_line.split()
        if input_arr[0] == "insert":
            lst.insert(int(input_arr[1]),int(input_arr[2]))
        elif input_arr[0] == "print":
            print(lst)
        elif input_arr[0] == "remove":
            lst.remove(int(input_arr[1]))
        elif input_arr[0] == "append":
            lst.append(int(input_arr[1]))
        elif input_arr[0] == "sort":
            lst.sort()
        elif input_arr[0] == "pop":
            lst.pop()
        elif input_arr[0] == "reverse":
            lst.reverse()
        else :
            print("falsche eingabe")
