import math
import matplotlib.pyplot as plt

#Algorithm
myHull = []
hullPoints = set()

def section(start, end, test) :
    det = start[0]*end[1] + test[0]*start[1] + end[0]*test[1] - test[0]*end[1] - end[0]*start[1] - start[0]*test[1]
    if det > 1e-9 :
        return 1
    elif det < -1e-9 :
        return -1
    else :
        return 0

def distance(start, end, test) :
    if end[0] == start[0] :
        return abs(test[0] - end[0])
    else :
        a = (end[1]-start[1])/(end[0]-start[0])
        b = -1
        c = start[1] - start[0]*a
        return abs(a*test[0] + b*test[1] + c)/math.sqrt(a*a + b*b)

def divide(oldArr, start, end, orientation) :
    newArr = []
    for elmt in (oldArr) :
        if section(start, end, elmt) == orientation :
            newArr.append(elmt)
    return newArr

def myConvexHull(oldArr, start, end, orientation) :
    newArr = divide(oldArr, start, end, orientation)
    maxDist = -1
    maxDistPos = []

    if len(newArr) == 0 :
        myHull.append([start[0],start[1],end[0],end[1]])
        hullPoints.add(tuple(start))
        hullPoints.add(tuple(end))
        return

    for elmt in (newArr) :
        dist = distance(start, end, elmt)
        if maxDist < dist :
            maxDist = dist
            maxDistPos = elmt

    myConvexHull(newArr, start, maxDistPos, -section(start, maxDistPos, end))
    myConvexHull(newArr, maxDistPos, end, -section(maxDistPos, end, start)) 
    return


#Show result
def displayConvexHull(df, data, x, y) :
    plt.figure(figsize = (10, 6))
    colors = ['b','r','g']
    plt.title('Convex Hull')
    plt.xlabel(data.feature_names[x-1])
    plt.ylabel(data.feature_names[y-1])
    for i in range(len(data.target_names)):
        myHull.clear()
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[x-1,y-1]].values
        bucket = sorted(bucket, key=lambda x:x[0])
        start = bucket[0]
        end = bucket[len(bucket) - 1]
        myConvexHull(bucket, start, end, 1)
        myConvexHull(bucket, start, end, -1)
        print("Set of hull points : ")
        print(hullPoints)
        for j in range (len(bucket)) :
            plt.scatter(bucket[j][0], bucket[j][1], label=data.target_names[i], color = colors[i])
        for j in range (len(myHull)) :
            plt.plot([myHull[j][0],myHull[j][2]], [myHull[j][1], myHull[j][3]], colors[i])
    plt.show()
