if __name__ == '__main__':
    dim = list(map(int, input().split()))
    pattern = ".|."
    width = dim[1]
    for i in range(int((dim[0]/2))):
        print (pattern.center(width,'-'))
        pattern = pattern + ".|..|."
    print ("WELCOME".center(width,'-'))
    pattern = pattern[6:]
    for i in range(int((dim[0]/2))):
        print (pattern.center(width,'-'))
        pattern = pattern[6:]