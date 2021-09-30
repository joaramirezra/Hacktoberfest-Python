import time
class Algo:
    # insertion_sort
    def insertion_sort(self,arr):
        for i in range(1,len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr 

    # arr_merge_sort
    def arr_merge_sort(self,arr1,arr2):
        arr = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                arr.append(arr1[i]) 
                i += 1
            else:
                arr.append(arr2[j])
                j += 1
        while i < len(arr1):
            arr.append(arr1[i])
            i += 1
        while j < len(arr2):
            arr.append(arr2[j])
            j += 1
        return arr

    #merge_sort
    def merge_sort(self,arr):
        if len(arr) == 1:
            return arr
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.arr_merge_sort(left,right)

    #bubble_sort
    def bubble_sort(self,arr):
        size = len(arr)
        sorted = True
        for i in range(size - 1):
            for j in range(size - 1-i):
                if arr[j] > arr[j + 1]:
                    sorted = False
                    arr[j],arr[j+1] = arr[j+1],arr[j]
            if sorted:
                break
        return arr
    
    #binary_search
    def binary_search(self,arr,num,si,ei):
        if si > ei or len(arr) == 0:
            return -1
        
        mid = (si + ei)//2

        if arr[mid - 1] == num:
            return mid
        elif arr[mid -1] > num:
            return self.binary_search(arr,num,si,mid-1)
        elif arr[mid - 1] < num:
            return self.binary_search(arr,num,mid+1,ei)