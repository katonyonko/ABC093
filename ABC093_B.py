import io
import sys

_INPUT = """\
6
3 8 2
4 8 3
2 9 100
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B,K=map(int,input().split())
  ans=[]
  for i in range(K):
    if A+i>B or B-i<A: break
    ans.append(A+i)
    ans.append(B-i)
  ans=list(set(ans))
  ans.sort()
  for i in range(len(ans)):
    print(ans[i])