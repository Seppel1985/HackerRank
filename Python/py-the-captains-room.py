if __name__ == '__main__':
    n = int(input())
    room_list = list(map(int, input().split()))
    
    from collections import Counter
    c = Counter(room_list)
    print (c.most_common()[-1][0])