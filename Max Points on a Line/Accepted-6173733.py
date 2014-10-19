#Author     : sakura_kyon@hotmail.com
#Question   : Max Points on a Line
#Link       : https://oj.leetcode.com/problems/max-points-on-a-line/
#Language   : python
#Status     : Accepted
#Run Time   : 580 ms
#Description: 
#Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

#Code       : 
def deg(pa, pb):
  if pa.x == pb.x:
    return "NaN"
  else:
    return float(pa.y - pb.y) / (pa.x - pb.x)

def pt(p):
  return p.x, p.y

def eq(pa, pb):
  return pa.x == pb.x and pa.y == pb.y

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
      if not points:
        return 0
      mx = 1
      for i in range(len(points)):
        dic = dict()
        sm = 0
        for j in range(i + 1, len(points)):
          if eq(points[i], points[j]):
            sm += 1
            continue
          d = deg(points[i], points[j])
          if not d in dic:
            dic[d] = set()
          dic[d].add(points[i])
          dic[d].add(points[j])
        vs = dic.values()
        if vs:
          mx = max(mx, max(map(len, vs)) + sm)
        else:
          mx = max(mx, sm + 1)
      return mx