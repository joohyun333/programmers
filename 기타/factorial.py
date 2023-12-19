# def factorial(N):
#     start = 1
#     for i in range(1,N+1):
#         start *= i
#     return start

#재귀함수는 자기자신을 호출한다(입력을 줄여가면서)
#재귀함수는 종료조건이 있어야 한다(자기자신을 그만 부를줄 알아야 한다)
def factorial(N):
    if N==1:
        return 1
    return N*factorial(N-1)

if __name__ == "__main__":
    N = int(input())
    print(factorial(N))