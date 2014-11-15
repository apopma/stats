__author__ = 'Adam'
import stats

intlist = [1,2,3,4,5]
floatlist = [1.0, 2.0, 3.0, 4.0, 5.0]
mixlist = [1, 2.5, 3, 4.5, 6.01]
badlist = [1, '2.816', 'pickle', 4, 6]
goodlist = [1, 2, '3.14159', 4, 5.5]

'''
print (type(goodlist[2]))
goodlist[2] = float(goodlist[2])
print (type(goodlist[2]))
'''

def convertStrToFloat(numbers):
    print ('Running string converter...')
    print (numbers)
    print()

    for x in numbers:
        print (x)
        print (type(x))
        print()

    print ('---------------------------------')

    return None