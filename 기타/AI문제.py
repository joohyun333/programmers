from datetime import timedelta
from datetime import time
import datetime
def solution(P:str, N:int) -> str:
    times = datetime.datetime.strptime(P, "%p %I:%M:%S")
    times += datetime.timedelta(seconds=N)
    return str(times.time())

if __name__ == "__main__":
    P="PM 01:00:00"
    N=10

    P = "PM 11:59:59"
    N = 1
    print(solution(P, N))