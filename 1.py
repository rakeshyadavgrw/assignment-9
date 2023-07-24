#************Q1*********#
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) -1
        
        while i<j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1 , j + 1]
            
            if s > target:
                j-=1
            else:
               i+=1 
        
        return []
    
    #***********Q2**********#
    # Python program to create a sorted array
# using Binary Search

# Function to create a new sorted array
# using Binary Search
def createSorted(a: list, n: int):

	# Auxiliary Array
	b = []
	for j in range(n):

		# if b is empty any element can be at
		# first place
		if len(b) == 0:
			b.append(a[j])
		else:

			# Perform Binary Search to find the correct
			# position of current element in the
			# new array
			start = 0
			end = len(b) - 1

			# let the element should be at first index
			pos = 0
			while start <= end:
				mid = start + (end - start) // 2

				# if a[j] is already present in the new array
				if b[mid] == a[j]:

					# add a[j] at mid+1. you can add it at mid
					b.insert(max(0, mid + 1), a[j])
					break

				# if a[j] is lesser than b[mid] go right side
				elif b[mid] > a[j]:

					# means pos should be between start and mid-1
					pos = end = mid - 1
				else:

					# else pos should be between mid+1 and end
					pos = start = mid + 1

				# if a[j] is the largest push it at last
				if start > end:
					pos = start
					b.insert(max(0, pos), a[j])

					# here max(0, pos) is used because sometimes
					# pos can be negative as smallest duplicates
					# can be present in the array
					break

	# Print the new generated sorted array
	for i in range(n):
		print(b[i], end=" ")

# Driver Code
if __name__ == "__main__":

	a = [2, 5, 4, 9, 8]
	n = len(a)
	createSorted(a, n)

# This code is contributed by
# sanjeev2552

#*****************Q3**************#
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
                
        return left
    
    #************Q4****************#
    class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return end+1
    
    #**************Q5**************#
    class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
    
    #***************Q6**************#
    class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 0
        last = n
        while first <= last:
            mid = (first+last)//2
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                else:
                    last = mid - 1
            else:
                first = mid + 1
        
        return -1
    
    #**********Q7**********#
    # Python3 program to count
# inversions in an array


def getInvCount(arr, n):

	inv_count = 0
	for i in range(n):
		for j in range(i + 1, n):
			if (arr[i] > arr[j]):
				inv_count += 1

	return inv_count


# Driver Code
arr = [1, 20, 6, 4, 5]
n = len(arr)
print("Number of inversions are",
	getInvCount(arr, n))

#************Q8***********#
# Python function to print common elements in three sorted arrays
def findCommon(ar1, ar2, ar3, n1, n2, n3):

	# Initialize starting indexes for ar1[], ar2[] and ar3[]
	i, j, k = 0, 0, 0

	# Iterate through three arrays while all arrays have elements
	while (i < n1 and j < n2 and k < n3):

		# If x = y and y = z, print any of them and move ahead
		# in all arrays
		if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
			print ar1[i],
			i += 1
			j += 1
			k += 1

		# x < y
		elif ar1[i] < ar2[j]:
			i += 1

		# y < z
		elif ar2[j] < ar3[k]:
			j += 1

		# We reach here when x > y and z < y, i.e., z is smallest
		else:
			k += 1


# Driver program to check above function
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
n1 = len(ar1)
n2 = len(ar2)
n3 = len(ar3)
print "Common elements are",
findCommon(ar1, ar2, ar3, n1, n2, n3)



