import numpy
if __name__ == '__main__':
    numpy.set_printoptions(legacy='1.13')
    array = []
    dim = list(map(int, input().split()))
    for i in range(dim[1]):
        input_line = list(map(int, input().split()))
        array.append(input_line)
    #print (array)
    my_array = numpy.array(array)
    
    print (numpy.mean(my_array, axis = 1))
    print (numpy.var(my_array, axis = 0)) 
    print (numpy.std(my_array, axis = None))
