import heapq

class DualPriorityQueue(object):
    def __init__(self):
        self.min_q = []
        self.max_q = []

    def push(self, value):
        heapq.heappush(self.min_q, value)

    def pop_max(self):
        while self.min_q:
            heapq.heappush(self.max_q, heapq.heappop(self.min_q) * -1)

        if self.max_q:
            return heapq.heappop(self.max_q)

    def pop_min(self):
        while self.max_q:
            heapq.heappush(self.min_q, heapq.heappop(self.max_q) * -1)

        if self.min_q:
            heapq.heappop(self.min_q)

    def get_max(self):
        while self.min_q:
            heapq.heappush(self.max_q, heapq.heappop(self.min_q) * -1)

        if self.max_q:
            return self.max_q[0] * -1
        else:
            return 0

    def get_min(self):
        while self.max_q:
            heapq.heappush(self.min_q, heapq.heappop(self.max_q) * -1)

        if self.min_q:
            return self.min_q[0]
        else:
            return 0

def solution(operations):
    dual_priority_queue = DualPriorityQueue()
    for op in operations:
        o, v = op.split(' ')
        if o == 'I':
            dual_priority_queue.push(int(v))
        else:
            if v == '-1':
                dual_priority_queue.pop_min()
            else:
                dual_priority_queue.pop_max()

    return [dual_priority_queue.get_max(), dual_priority_queue.get_min()]