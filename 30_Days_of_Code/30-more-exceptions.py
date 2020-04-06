#Write your code here
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class Calculator:
    def power(self, number_n, number_p):
        if ((number_n < 0) or (number_p < 0)):
            raise Error('n and p should be non-negative')
        else:
            return (pow(number_n,number_p))

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   