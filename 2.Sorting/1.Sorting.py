import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')


def bubbleSort(arr:list[int])->list[int]:
    #move the max element to right end of the array by swapping

    n = len(arr)

    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def bubbleRecursion(arr:list[int],n:int)->list[int]:

    # n = len(arr)

    if n == 1:
        return arr
    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
    
    bubbleRecursion(arr,n-1)

    return arr

def insertionSort(arr:list[int])->list[int]:
    
    n = len(arr)

    for i in range(1,n):
        j = i-1

        while j >=0:
            if arr[j] > arr[j+1]:
                #swap
                arr[j],arr[j+1] = arr[j+1],arr[j]
                j-=1
            else:
                break
    return arr

def insertionSortRecursion(arr:list[int],i)->list[int]:

    if i == len(arr):
        return
    
    j = i-1
    while j >=0:
        if arr[j] > arr[j+1]:
            #swap
            arr[j],arr[j+1] = arr[j+1],arr[j]
            j-=1
        else:
            break
    insertionSortRecursion(arr,i+1)

    return arr


def dutchFlagAlgorithm(arr:list[int]):
    red,white,blue = 0,0,len(arr)-1

    while white <=blue:
        if arr[white] == 0:
            arr[red],arr[white] = arr[white],arr[red]
            white+=1
            red+=1
        elif arr[white] == 1:
            white+=1
        else:
            arr[white],arr[blue] = arr[blue],arr[white]
            blue-=1
    return arr

    

    










        
                 

for line in sys.stdin:
    arr = list(map(int,line.split(",")))
    # print(bubbleSort(arr))
    # print(bubbleRecursion(arr,len(arr)))
    print(dutchFlagAlgorithm(arr))



sys.stdout.close()