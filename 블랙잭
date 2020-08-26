N, K= map(int, input().split())
card = list(map(int, input().split()))
sum_list = []
for x in range(N):
    for y in range(1,N):
        if x!=y:
            for z in range(2,N):
                if y!=z and x !=z :
                    sum = card[x]+card[y]+card[z]
                    if sum <= K:
                        sum_list.append(sum)
print(int(max(sum_list)))

