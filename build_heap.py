# python3 Elīza Mača RDCP0.grupa

def put_down(data, i, swaps):
    size=len(data)
    minimalais_index = i
    left = 2*i+1   # left child
    right = 2*i+2  # right child
    if left < size and data[left] < data[minimalais_index]:
        minimalais_index = left
    if right < size and data[right] < data[minimalais_index]:
        minimalais_index = right
    # if not minimalais_index == i:
    if minimalais_index != i:
        swaps.append((i, minimalais_index))
        data[i], data[minimalais_index] = data[minimalais_index], data[i]
        put_down(data,minimalais_index,swaps)

def build_heap(data):
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    # n=len(data)
    swaps = []
    for i in range(len(data)//2,-1,-1):
        put_down(data, i, swaps)
    return swaps


def main():
    
    rezultats = input("'F' or 'I':")
    if "I" in rezultats:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n

    elif "F" in rezultats:
         
        myfile=input()
        avots='./tests/'
        # package=os.avots.join(avots,myfile)

        with open(avots+myfile, mode="r") as solis:
            n=int(solis.readline())
            data=list(map(int,solis.readline().split()))
       
    else:
        print("Error")
        return

    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()