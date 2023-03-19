# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, swaps)
    return swaps

def heapify(data, n, i, swaps):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] > data[largest]:
        largest = left

    if right < n and data[right] > data[largest]:
        largest = right

    if largest != i:
        swaps.append((i, largest))
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest, swaps)

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
