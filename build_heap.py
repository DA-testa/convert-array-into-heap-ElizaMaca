# python3

def put_down(data, i, swaps):
    size=len(data)
    min_index = i
    left = 2*i+1;
    right = 2*i+2;  # right child
    if left < size and data[left] < data[min_index]:
        min_index = left
    if right < size and data[right] < data[min_index]:
        min_index = right
    if min_index != i:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        put_down(data,min_index,swaps)

def build_heap(data):
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    swaps = []
    # n=len(data)
    for i in range(len(data)//2,-1,-1):
        put_down(data, i, swaps)
    return swaps


def main():
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    rezultats = input("'F' or 'I':")
    # input from keyboard
    if "I" in rezultats:
        n = int(input())
        data = list(map(int, input().split()))

    elif "F" in rezultats:
         
        entry=input()
        path= './test/'
        avots=path+entry

        if "a" not in entry:

            with open(avots) as solis:
                n=int(solis.readline())
                data=list(map(int,solis.readline().split()))
            
        else:
            print("Error")
            return
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