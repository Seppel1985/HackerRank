# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    #print(n)
    input_string = input()
    numbers = list(map(int, input_string.split()))
    #mean
    numbersum = sum(numbers)
   # print (numbersum)
    mean = numbersum/n
    print (mean)
    #meadian
    numbers.sort()
    #print (numbers)
    if (n %2 ==1):
        median = numbers[int(n/2)-1]
    else:
        middle = [int(n/2)-1,int(n/2)]
        denominator = [numbers[i] for i in middle]
        #print (denominator)
        donominatorsum = sum(denominator)
        #print (donominatorsum)
        median = donominatorsum/2
    print (median)

    from collections import Counter
    c = Counter(numbers)
    print (c.most_common(1)[0][0])