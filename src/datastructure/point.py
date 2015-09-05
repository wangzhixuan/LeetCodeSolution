class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return '('+str(self.x)+', '+str(self.y)+')'

def listOfPoints(input_list):
    result = []
    for point in input_list:
        result.append(Point(point[0],point[1]))

    return result



