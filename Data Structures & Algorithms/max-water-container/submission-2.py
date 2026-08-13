#Two Pointers
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first = 0
        last = len(heights)-1
        area = 0
        while first < last:
            area = max(area,min(heights[first],heights[last])*(last-first))
            if heights[first] >= heights[last]:
                last -=1
            else:
                first +=1
        
        return area