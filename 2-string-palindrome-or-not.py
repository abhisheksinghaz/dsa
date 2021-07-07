class Solution:
    def isPlaindrome(self, S):
        # code here
        S_len = S.__len__()
        for ptr in range(S_len):
            if S[ptr] != S[S_len - 1 - ptr]:
                return 0
            
        return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.isPlaindrome(S)
        print(answer)

# } Driver Code Ends
