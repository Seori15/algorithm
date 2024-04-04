from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ticket_k = tickets[k]
        answer = 0
        
        # [1] for front of k: consider if ticket is bigger than t's
        front = deque(tickets[:k+1])
        while front:
            now = front.popleft()
            if now > ticket_k:
                answer += ticket_k
            else:
                answer += now

				# [2] for back of k: consider if ticket is bigger than t's -1
        back = deque(tickets[k+1:])
        while back:
            now = back.popleft()
            if now >= ticket_k:
                answer += ticket_k - 1 
            else:
                answer += now
        
        return answer