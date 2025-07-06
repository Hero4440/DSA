
# https://leetcode.com/problems/search-a-2d-matrix/submissions/1687778173/


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Row, Col = len(matrix) , len(matrix[0])
        top , bottom = 0 , Row - 1
        while top <= bottom:
            currentRow = (top + bottom) // 2
            if target > matrix[currentRow][-1]:
                top = currentRow + 1
            elif target < matrix[currentRow][0]:
                bottom = currentRow - 1
            else:
                break
        if not (top <= bottom):
            return False
        left, right = 0, Col - 1 
        while left <= right: 
            middle = (left + right) // 2
            if target > matrix[currentRow][middle]:
                left = middle + 1
            elif target < matrix[currentRow][middle]:
                right = middle - 1 
            else:
                return True
        return False