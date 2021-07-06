
def rotate( arr, n):
    last_val = arr[n-1]

    for index in range(n -1):
        arr[n -1 - index] = arr[n -2 - index]

    arr[0] = last_val
    
    # for cyclically rotating in the other direction
    # val0 = arr[0]
    # for i in range(n-1):
    #     arr[i]=arr[i+1]
    # arr[n - 1] = val0
    
    return arr


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()

