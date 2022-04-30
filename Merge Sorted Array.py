class Solution(object):
    def merge(self, arr1, n, arr2, m):
        i = 0
        j = 0
        arr3 = []
        while (i < n and j < m):
            if arr1[i] < arr2[j]:
                arr3.append(arr1[i])
                i += 1
            else:
                arr3.append(arr2[j])
                j += 1
        while (i < n):
            arr3.append(arr1[i])
            i += 1
        while ( j < m):
            arr3.append(arr2[j])
            j += 1
        arr1[:] = arr3[:]    
