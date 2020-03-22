# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n1 = int(input())
    integer_list1 = map(int, input().split())
    n2 = int(input())
    integer_list2 = map(int, input().split())
    
    set1 = set(list(integer_list1))
    set2 = set(list(integer_list2))

    diff1 = set1.difference(set2)

    diff_list = []
    for diff_el in diff1:
        diff_list.append(diff_el)

    diff2 = set2.difference(set1)

    for diff_el in diff2:
        diff_list.append(diff_el)
    diff_list.sort()

    for diff_list_el in diff_list:
        print (diff_list_el)

