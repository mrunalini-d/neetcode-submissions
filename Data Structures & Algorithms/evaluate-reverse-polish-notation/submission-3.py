class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                num2 = stack.pop()  # right operand
                num1 = stack.pop()  # left operand
                if token == "+":
                    result = num1 + num2
                elif token == "-":
                    result = num1 - num2
                elif token == "*":
                    result = num1 * num2
                else:
                    result = int(num1 / num2)
                stack.append(result)
        return stack[0]
        