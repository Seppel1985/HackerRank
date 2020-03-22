if __name__ == '__main__':
    n_english = int(input())
    s_english = set(map(int, input().split()))
    n_french = int(input())
    s_french = set(map(int, input().split()))
    
    print(len(s_english.union(s_french)))