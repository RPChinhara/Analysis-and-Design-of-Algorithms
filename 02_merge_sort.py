def MergeSort(A):
    if len(A) > 1:
        r = len(A) // 2
        L = A[:r]
        M = A[r:]

        MergeSort(L)
        MergeSort(M)

        i = j = k = 0

        while(i < len(L) and j < len(M)):
            if L[i] < M[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = M[j]
                j += 1
            
            k += 1

        while(i < len(L)):
            A[k] = L[i]
            i += 1
            k += 1
        
        while(j < len(M)):
            A[k] = M[j]
            j += 1
            k += 1

array = [6, 5, 12, 10, 9, 1]
MergeSort(array)
print('Sorted array is:', array, sep='\n')