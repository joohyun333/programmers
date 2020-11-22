# #https://programmers.co.kr/learn/courses/30/lessons/17676
import datetime
import sys
def solution(lines:datetime)->int:
    start_time = []
    end_time = []
    for i in lines:
        time = i.split(" ")
        time_sec = float(time[2].strip("s"))
        time = ''.join(map(str, time[0]+time[1]))
        day = datetime.datetime.strptime(time, '%Y-%m-%d%H:%M:%S.%f')
        end_time.append(day)
        start_time.append(day - datetime.timedelta(seconds=time_sec)+datetime.timedelta(seconds=0.001))

    answer = -sys.maxsize
    for j in start_time:
        min_point = 0
        for i, e in zip(start_time, end_time):
            if i<=j-datetime.timedelta(seconds=0.999)<=e or i<=j<=e or (j-datetime.timedelta(seconds=0.999)<= i and e <=j):
                min_point+=1
        if answer < min_point:
            answer = min_point
    return answer

if __name__ == "__main__":
    lines = ['2016-09-15 01:00:04.001 2.0s','2016-09-15 01:00:07.000 2s']
    lines = ['2016-09-15 01:00:04.002 2.0s','2016-09-15 01:00:07.000 2s']
    lines =  ['2016-09-15 20:59:57.421 0.351s','2016-09-15 20:59:58.233 1.181s',
              '2016-09-15 20:59:58.299 0.8s','2016-09-15 20:59:58.688 1.041s','2016-09-15 20:59:59.591 1.412s',
              '2016-09-15 21:00:00.464 1.466s','2016-09-15 21:00:00.741 1.581s','2016-09-15 21:00:00.748 2.31s',
              '2016-09-15 21:00:00.966 0.381s','2016-09-15 21:00:02.066 2.62s']
    print(solution(lines))
