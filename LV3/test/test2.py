from collections import defaultdict
def solution(tickets):
    answer = defaultdict(list)
    for s,d in sorted(tickets, reverse=True):
        answer[s].append(d)
    print(answer)
    def DFS(s):
        stack = []
        stack.append(s)
        discovred = []
        while stack:
            node = stack.pop()
            discovred.append(node)
            for i in answer[node]:
                stack.append(i)
            answer[node] = []
        return discovred
    return DFS('ICN')
if __name__ == "__main__":
    tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "I"], ["ATL", "ICN"], ["ATL", "SFO"]]
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ICN"], ["ATL", "ICN"]]
    tickets = [["ICN","BOO"], ["ICN", "COO"], [ "COO", "DOO" ], ["DOO", "COO"], [ "BOO", "DOO"] ,["DOO", "BOO"], ["BOO", "ICN" ], ["COO", "BOO"]]
    #[ICN, ATL, ICN, SFO, ATL, SFO]
    print(solution(tickets))