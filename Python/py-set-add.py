# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    country_set = set()
    for i in range(n):
        input_country = input()
        country_set.add(input_country)
        #print(input_country)
    print(len(country_set))