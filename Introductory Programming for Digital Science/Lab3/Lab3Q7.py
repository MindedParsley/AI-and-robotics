import math
import statistics

def improved_average(n1,n2,n3,n4,n5):
    '''def improved_average: 
    returns the mean, median and mode of the 5 inputs'''

    #mean
    print(f"mean:{(n1+n2+n3+n4+n5)/5}")

    #median
    n_num = [n1, n2, n3, n4, n5].sort() 
    print(f"Median: {statistics.median(n_num)}")

    #mode
    print(f"mode: {statistics.mode(n_num)}")

improved_average(1,1,8,8,8)
