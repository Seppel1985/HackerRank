#!/bin/python3

if __name__ == '__main__':
    telbook = {} 
    n = int(input())
    for i in range(n):
        entry = input().split()
        telbook[entry[0]] = entry[1]
while True:
    try:
        name = input()
        try:
            print(name + "="+ telbook[name])
        except:
            print("Not found")
    except:
        break
