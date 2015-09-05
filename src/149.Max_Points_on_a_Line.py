from datastructure.point import *

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points)==0:
            return 0
        elif len(points)==1:
            return 1
        elif len(points)==2:
            return 2

        lines = {}
        distinct_points = {}
        for point in points:
            distinct_points[(point.x, point.y)] = distinct_points.get((point.x, point.y),0) + 1

        if len(distinct_points)==1:
            return len(points)

        for i, point in enumerate(distinct_points.keys()):
            for j in range(i+1, len(distinct_points)):
                point2 = distinct_points.keys()[j]
                if point[0] == point2[0]:
                    k = 'inf'
                    b = point[0]
                else:
                    k = (point2[1] - point[1])/(point2[0] - point[0]+0.0)
                    b = point[1] - k * point[0]
#                print point, point2
#                print k, b
#                print '-----------'
                if (k,b) in lines:
                    for p in (point, point2):
                        if p not in lines[(k,b)]['points']:
                            lines[(k,b)]['points'].add(p)
                            lines[(k,b)]['counts'] += distinct_points[p]
                else:
                    lines[(k, b)] = {'points': set([point, point2]),
                                     'counts': distinct_points[point] + distinct_points[point2]}

#        for key in lines:
#            print key, lines[key]
        max_count = 2
        for key in lines:
            max_count = max(lines[key]['counts'], max_count)

        return max_count

s = Solution()




test = [[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]]
# should give 6

print s.maxPoints(listOfPoints(test))





