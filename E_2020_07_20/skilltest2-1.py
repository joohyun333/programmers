import math
def solution(nums):
    number = []
    n_number = []
    nums_len = len(nums)
    for i in range(nums_len):
        for j in range(i+1, nums_len):
            for z in range(j+1 , nums_len):
                number.append(nums[i] + nums[j] + nums[z])
                for num in number:
                   if num != 1:
                       for f in range(2, int(math.sqrt(num))+1):
                           if num % f == 0 :
                               n_number.append(num)
                   else:
                       pass
    return len(set(number)-set(n_number))

if __name__ == "__main__":
    nums =[1,2,7,6,4]
    print(solution(nums))