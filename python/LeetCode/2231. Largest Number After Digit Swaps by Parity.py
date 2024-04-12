import heapq
class Solution:
    def largestInteger(self, num: int) -> int:
		# [1] Make 2 heaps odd and even with check_list to check index of each parity.
        num_list = [int(i) for i in str(num)]
        odd, even, check_list = [], [], []
        for number in num_list:
            if number % 2:
                odd.append(-number)
                check_list.append('odd')
            else:
                even.append(-number)
                check_list.append('even')

        heapq.heapify(odd)
        heapq.heapify(even)

		# [2] Reform answer which means sorted num using check_list.
        answer = []
        for check in check_list:
            if check == 'odd':
                answer.append(-heapq.heappop(odd))
            elif check == 'even':
                answer.append(-heapq.heappop(even))

        return int("".join(map(str, answer)))