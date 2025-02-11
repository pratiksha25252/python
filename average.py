def average(array):
    
    m=set(arr)
    t=0
    o=0
    for i in m:
        t=t+i
        o=o+1
    
    return(t/o)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
