import io
import sys

_INPUT = """\
6
2 5 4
2 6 3
31 41 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  X=list(map(int,input().split()))
  X.sort()
  ans=X[2]-X[1]+(-X[0]+X[1])//2
  if (-X[0]+X[1])%2==1: ans+=2
  print(ans)