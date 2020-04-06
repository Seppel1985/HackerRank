class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = -1
	# Add your code here
    def computeDifference(self):
        for i in range(len(a)):
            for j in range(len(a)):
                if (i != j):
                    abs_difference = abs(a[i] - a[j])
                    if (abs_difference > self.maximumDifference):
                        self.maximumDifference = abs_difference

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()
print(d.maximumDifference)