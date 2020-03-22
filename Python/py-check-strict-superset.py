if __name__ == '__main__':
    result = True
    setA = set(map(int, input().split()))
    nSets = int(input())
    for i in range(nSets):
        setOther = set(map(int, input().split()))
        if (not(setA.issuperset(setOther))):
            result = False
    print (result)