class Point:
    def __init__(self,x=0,y=0):
        self.x=0
	self.y=0

def listOfPoints(input_list):
    result = []
    for point in input_list:
        result.append(Point(point[0],point[1]))
    return result



