class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) // 2

            row = mid // cols 
            col = mid % cols

            if matrix[row][col] == target: 
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid -1
        return False
