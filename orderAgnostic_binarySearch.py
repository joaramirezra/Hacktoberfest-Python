def orderAgnostic(arr, target):
	start = 0
	end = len(arr)-1

	isAsc = arr[start]<arr[end]

	while start<=end:
		mid = (start+end)//2

		if arr[mid] == target:
			return mid 

		# if sorted in ascending order
		if isAsc:
			if target<arr[mid]:
				end = mid - 1
			else:
				start = mid + 1

		# if sorted in descending order
		else:
			if target>arr[mid]:
				end = mid - 1
			else:
				start = mid + 1

	return -1


arr = [9,8,7,6,5,4,3,2,1]
print(orderAgnostic(arr, 1))
