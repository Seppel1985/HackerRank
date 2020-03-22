if __name__ == '__main__':
    nA = int(input())
    sA = set(map(int, input().split()))
    n = int(input())
    for i in range(n):
        input_arr = input().split()
        sOther = set(map(int, input().split()))
        if input_arr[0] == "intersection_update":
            sA.intersection_update(sOther)
        elif input_arr[0] == "update":
            sA.update(sOther)
        elif input_arr[0] == "symmetric_difference_update":
            sA.symmetric_difference_update(sOther)
        elif input_arr[0] == "difference_update":
            sA.difference_update(sOther)
        else :
            print("wrong entry")
    print(sum(sA))