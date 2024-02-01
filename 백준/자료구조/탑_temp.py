N = int(input())
towers = list(map(int, input().split()))
stack = [(1, towers[0])] #(인덱스, 타워 높이)
ans = [0]
for i in range(1,N):
    cur_h, cur_idx = towers[i], i+1 #현재 타워 정보
    top_h,top_idx = stack[-1][1], stack[-1][0] #스택 최상단 노드

    if top_h < cur_h: # stack에서 cur_h보 작은 노드들을 빼줘야된다.
        ans_exist = False # h보다 작은 값이 스택 내에 존재 값이 있음
        while stack:
            if stack[-1][1] > cur_h:
                ans_exist = True
                ans.append(stack[-1][0])
                break
            else:
                stack.pop()
        if not ans_exist:
            ans.append(0)

    else:
        ans.append(top_idx)
    stack.append((cur_idx,cur_h))

print(' '.join(map(str, ans)))