import io
import sys

_INPUT = """\
6
bac
bab
abc
aaa
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  if len(set(S))==3: print('Yes')
  else: print('No')