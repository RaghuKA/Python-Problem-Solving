# Dominator
def solution(A):
    n = len(A)
    #dominator = -1
    index=[]
    for k in range(n):
        candidate=A[k]
        count=0
        for i in range(n):
            if A[i]==candidate:
                count+=1
        if (count>n//2):
            #dominator =candidate
            index.append(k)
    return index
print(solution([3,4,3,2,3,-1,3,3]))    
