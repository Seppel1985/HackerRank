if __name__ == '__main__':
    nTests = int(input())
    for i in range(nTests):
        input()
        setA = set(map(int, input().split()))
        input()
        setB = set(map(int, input().split()))
        if (setA.issubset(setB)):
            print ("True");
        else:
            print ("False");