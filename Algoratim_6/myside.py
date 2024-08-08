#
# import sys
# from stack import *
# k=sys.maxsize
#
#
# class Stack:
#     pass
#
#
# def DFS(g):
#   st1=Stack()
#   visited=[True,False,False,False,False,False]
#   i=0
#   st1.push(i)
#   while(not(st1.isEmpty())):
#     d=st1.top()
#     st1.pop()
#     print(d+1, end=' ')
#     for j in range(6):
#       if(g[d][j]<k and visited[j]==False):
#         st1.push(j)
#         visited[j]=True
#   print()
# def minMetka(metka,visited):
#   m=k
#   n=0
#   for i in range(len(metka)):
#     if m>metka[i] and visited[i]==False:
#       m=metka[i]
#       n=i
#   return n
# def dijkstra(g,i):
#   i-=1
#   metka=[k,k,k,k,k,k]
#   metka[i]=0
#   visited=[False,False,False,False,False,False]
#   visited[i]=True
#   for j in range(6):
#     q=minMetka(metka,visited)
#     print(q+1)
#     for c in range(6):
#       if g[q][c]<k and visited[c]==False and metka[q]+g[q][c]<metka[c]:
#         metka[c]=metka[q]+g[q][c]
#     visited[q]=True
#   for j in range(len(metka)):
#     print(i+1,'->',j+1,":",metka[j])
#
# g=[[k,7,9,k,k,14],
#    [k,k,10,15,k,k],
#    [k,k,k,11,k,2],
#    [k,k,k,k,6,k],
#    [k,k,k,k,k,9],
#    [k,k,k,k,k,k]]
# DFS(g)
# dijkstra(g,1)
