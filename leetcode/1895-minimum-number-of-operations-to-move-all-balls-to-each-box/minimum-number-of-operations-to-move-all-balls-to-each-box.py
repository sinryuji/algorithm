class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        move = right = left = 0

        for idx, ball in enumerate(boxes):
            if ball == '1':
                move += idx
                right += 1

        for ball in boxes:
            result.append(move)
            if ball == '1':
                right -= 1
                left += 1
            move = move - right + left

        return result