# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    happiness = 0
    n = map(int, input().split())
    integer_list1 = map(int, input().split())
    integer_list2 = map(int, input().split())
    integer_list3 = map(int, input().split())

    lstHappiness = list(integer_list1)
    setA = set(list(integer_list2))
    setB = set(list(integer_list3))

    for el_happiness in lstHappiness:
        if (el_happiness in setA):
                happiness = happiness +1;
        if (el_happiness in setB):
                happiness = happiness -1;
    print(happiness)