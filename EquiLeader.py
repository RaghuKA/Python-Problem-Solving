#EquiLeader
def solution(A):
    n=len(A)
    firstLeader=-1
    for k in range(n):
        firstCandidate=A[k]
        count = 0
        for i in range(n):
            if (A[i]==firstCandidate):
                count+=1
            if (count>i//2):
                firstLeader=firstCandidate
    return firstCandidate
print(solution([4,3,4,4,4,2]))