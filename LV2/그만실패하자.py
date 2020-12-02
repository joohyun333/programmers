# def solution(N, stages):
#     dict1 = {}
#     for i in range(1, N + 1): # 스테이지
#         stages_list1 = [False] * len(stages)  # 분자 - 스테이지에 도달했으나 아직 클리어하지 못한 플페이어 공간
#         stages_list = [False] * len(stages) # 분모 - 스테이지에 도달한 플레이어 수 공간
#         for j in range(len(stages)): # 스테이지에 따라 각 stages 변수들 분모, 분자 만듬
#             if int(i) <= stages[j]:
#                 stages_list[j] = True
#             if int(i) == stages[j]:
#                 stages_list1[j] = True
#
#         a = stages_list.count(True) # 스테이지에 도달한 플레이어
#         b = stages_list1.count(True) # 스테이지에 도달했으나 아직 클리어하지 못한 플페이어
#         c = b/a
#         dict1[i] = c
#
#     sorted_stage = sorted(dict1.items(), key=lambda x: (-x[1], x[0]))
#     return [x[0] for x in sorted_stage]

def solution(N, stages):
    stage_info = {}
    for stage in stages:
        if stage not in stage_info: stage_info[stage] = 1
        else: stage_info[stage] += 1
    N_stage = {}
    total = len(stages)
    for i in range(1, N+1):
        if i in stage_info and total > 0:
            N_stage[i] = stage_info[i]/total
            total -= stage_info[i]
        else: N_stage[i] = 0
    sorted_stage = sorted(N_stage.items(), key=lambda x: (-x[1], x[0]))
    return [x[0] for x in sorted_stage]
if __name__ == "__main__":
    # N = 5
    # stages = [2, 1, 2, 6, 2, 4, 3, 3]

    N = 4
    stages = [4,4,4,4,4]
    print(solution(N, stages))



