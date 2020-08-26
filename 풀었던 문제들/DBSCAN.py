# def DBSCAN(D, eps, MinPts):
#  C = 0
#  for each unvisited point P in dataset D:
#     mark P as visited
#     NeighborPts = regionQuery(P, eps)
#     if sizeof(NeighborPts) < MinPts :
#         mark P as NOISE
#     else:
#         C = next cluster
#         expandCluster(P, NeighborPts, C, eps, MinPts)
# #
# def expandCluster(P, NeighborPts, C, eps, MinPts):
#     add P to cluster C
#     for each point P1 in NeighborPts:
#         if P1 is not visited:
#             mark P1 as visited
#             NeighborPts1 = regionQuery(P1, eps)
#             if sizeof(NeighborPts1) >= MinPts:
#                 NeighborPts = NeighborPts joined with NeighborPts1
#         if P1 is not yet member of any cluster:
#             add P1 to cluster C
#
# def regionQuery(P, eps):
#     return all points within P eps-neighborhood (including P)