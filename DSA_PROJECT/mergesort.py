import time
def merge_sort(data,drawData,timeTick):
    merge_sort_algo(data,drawData,timeTick)
def merge_sort_algo(data,drawData,timeTick):
    if len(data)>1:
        mid =len(data)//2
        left = data[:mid]
        right = data[mid:]
        merge_sort_algo(left,drawData,timeTick)
        merge_sort_algo(right,drawData,timeTick)
        merge(data,left,right,drawData,timeTick)
    else:
        return
def merge(data,left,right,drawData,timeTick):
    drawData(data,colorArray(data,left,right))
    time.sleep(timeTick)
    leftIdx=0
    rightIdx = 0
    dataIdx=0
    while leftIdx<len(left) and rightIdx < len(right):
        if left[leftIdx] <= right[rightIdx]:
            data[dataIdx]=left[leftIdx]
            leftIdx=leftIdx+1
        else:
            data[dataIdx]=right[rightIdx]
            rightIdx=rightIdx+1
        dataIdx=dataIdx+1
    while leftIdx < len(left):
        data[dataIdx]=left[leftIdx]
        leftIdx=leftIdx+1
        dataIdx=dataIdx+1
    while rightIdx < len(right):
        data[dataIdx]=right[rightIdx]
        rightIdx=rightIdx+1
        dataIdx=dataIdx+1
    drawData(data, ['green' for x in range(len(data))])
    time.sleep(timeTick)

def colorArray(data,left,right):
    length=len(data)
    left=0
    right=len(data)-1
    middle=(left+right)//2
    colorArray=[]
    for i in range(length):
        if i >=left and i <=right:
            if i >=left and i <=middle:
                colorArray.append('yellow')
            else:
                colorArray.append('orange')
        else:
            colorArray.append('white')
    return colorArray