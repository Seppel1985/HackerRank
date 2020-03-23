if __name__ == '__main__':
    s = input()
    chk1 = False
    chk2 = False
    chk3 = False
    chk4 = False
    chk5 = False
    for char in s:     
        if(char.isalnum()):
            chk1 = True
        if(char.isalpha()):
            chk2 = True
        if(char.isdigit()):
            chk3 = True
        if(char.islower()):
            chk4 = True
        if(char.isupper()):
            chk5 = True
    print(chk1)
    print(chk2)
    print(chk3)
    print(chk4)
    print(chk5)