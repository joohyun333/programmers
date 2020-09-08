# import numpy
# def solution(mylist):
#     answer = numpy.array(mylist).T
#     return numpy.array(answer).tolist()
#
# if __name__ == "__main__":
#     mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
#     print(solution(mylist))

mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = list(map(list, zip(*mylist)))
print(new_list)
print(list(zip(mylist[1])))