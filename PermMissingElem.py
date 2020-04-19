def solution(A):
    if len(A)==1:
        return -1
    A.sort()
    for i in A:
        if A[i+1] !=A[i]+1:
            return A[i+1]-1
print(solution([2,3,1,5]))  