class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_day_stack = []
        output_stack = []
        for i in range(len(temperatures)-1,-1,-1):
            while temp_day_stack and temperatures[i] >= temperatures[temp_day_stack[-1]]:
                    temp_day_stack.pop()
            if not temp_day_stack:              
                output_stack.append(0)
            else:
                output_stack.append(temp_day_stack[-1] - i)
            temp_day_stack.append(i)
        return output_stack[::-1]  