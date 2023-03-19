# python3


def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(n // 2, -1, -1):
        minHeap(data, n, i, swaps)
    return swaps

def minHeap(data, n, i, swaps):
    lSide = 2 * i + 1
    rSide = 2 * i + 2
    min = i

    if lSide <= n - 1 and data[lSide] < data[min]:
        min = lSide
    if rSide <= n - 1 and data[rSide] < data[min]:
        min = rSide
    if i != min:
        data[i], data[min] = data[min], data[i]
        swaps.append((i, min))
        minHeap(data, n, min, swaps)

    return swaps


def main():
    
   # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    inputs = input()
    if "I" in inputs:
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in inputs:
        inputs2 = input()
        if "a" not in inputs2:
            with open("./tests/"+inputs2, mode='r') as fails:
                n = int(fails.readline())
                data = list(map(int,fails.readline().split()))
    else:
        print("error")
        return

    # input from keyboard
    

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
