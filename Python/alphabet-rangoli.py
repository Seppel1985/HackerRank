def print_rangoli(size):
    width = ((size-1)*2) + 1 + ((size-1)*2)
    import string
    var = list(string.ascii_lowercase[0:size])
    var.reverse()
    pattern_left = var[0]
    pattern_right = var[0]
    pattern = var[0]
    print (pattern.center(width,'-'))
    for i in range(1,size):
        middle = var[i];
        pattern = pattern_left +"-"+ middle +"-"+ pattern_right
        print (pattern.center(width,'-'))
        pattern_left = pattern_left + "-" + middle
        pattern_right = middle + "-" + pattern_right
    pattern_right = pattern_right[1:]
    for i in range(size-1):
        pattern_left = pattern_left[0:-2]
        pattern_right = pattern_right[2:]
        pattern = pattern_left+pattern_right
        print (pattern.center(width,'-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)