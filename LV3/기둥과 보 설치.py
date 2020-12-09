# https://programmers.co.kr/learn/courses/30/lessons/60061
def test(data):
    for i in data:
        if i[2] == 0 : #기둥일 경우
            if i[1] == 0 or [i[0], i[1]-1, 0] in data or [i[0]-1, i[1], 1] in data or [i[0], i[1], 1] in data:
               continue
            else:return False
        elif i[2] == 1: #보일 경우
            if [i[0], i[1]-1, 0] in data or [i[0]+1, i[1]-1, 0] in data or ([i[0]-1, i[1], 1] in data and [i[0]+1, i[1], 1] in data):
                continue
            else:return False
    return True

def solution(n, build_frame):
    build_frame_ = []
    for i in build_frame:
        if i[3] == 1: #설치할때
            build_frame_.append(i[:3])
            if test(build_frame_) == False:
                build_frame_.remove(i[:3])
        elif i[3] == 0 : #제거할때
            build_frame_.remove(i[:3])
            if test(build_frame_) == False:
                build_frame_.append(i[:3])
    return sorted(build_frame_)
if __name__ == "__main__":
    n = 5
    build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    #[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
    build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
     [1, 1, 1, 0], [2, 2, 0, 1]]
    print(solution(n, build_frame))