class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == '+':
                first, second = stack[-1], stack[-2]
                stack.append(first + second)
            elif operation == 'D':
                first = stack[-1]
                stack.append(first * 2)
            elif operation == 'C':
                stack.pop()
            else:
                stack.append(int(operation))
        return sum(stack)