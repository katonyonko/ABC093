import io
import sys

_INPUT = """\
6
9
1 4
10 5
3 3
4 11
8 9
22 40
8 36
314159265 358979323
64 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  Q=int(input())
  for i in range(Q):
    A,B=map(int,input().split())
    if A>B: A,B=B,A
    if A==B: print(2*(A-1))
    else:
      l,r=0,A*B
      while r-l>1:
        mid=(r+l)//2
        if mid**2<A*B: l=mid
        else: r=mid
      ans=2*l-1
      if (A*B-1)//l==l: ans-=1
      print(ans)