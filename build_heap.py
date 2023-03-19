# python3


def build_heap(data):
    
    swaps = []
    n = len(data)

    for i in range(n // 2, -1, -1):
       mHeap(data, n, i, swaps)
                
    return swaps

def mHeap(data, n, i, swaps):
    
    l= 2 * i + 1
    r= 2 * i + 2
    min=i

    if l<=n - 1 and data[l]<data[min]:
        min=l
        
    if r<=n - 1 and data[r]<data[min]:
        min=r
        
    if i != min:
        
        data[i], data[min] = data[min], data[i]
        swaps.append((i, min))
        mHeap(data, n, min, swaps)

    return swaps

def main():
    
    in1=input()
    
    if "I" in in1:
        n = int(input())
        data = list(map(int, input().split()))
        
    elif "F" in in1:
        
        in2=input()
        
        if "a" not in in2:
            
            with open("./tests/" + in2, mode='r') as fails:
                n = int(fails.readline())
                data = list(map(int,fails.readline().split()))
                
    else:
        print("error")
        return
    
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
        
if __name__ == "__main__":
    main()
