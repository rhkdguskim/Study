# https://school.programmers.co.kr/learn/courses/30/lessons/42627?language=python3
import heapq

class DiskController(object):
    def __init__(self, jobs):
        heapq.heapify(jobs)
        self.work_length = len(jobs)
        self.current_time = 0
        self.total_time = 0
        self.jobs = jobs
        self.work_queue = []

    def pop_work(self):
        # 동작한 시간 기준으로 작업큐로 모두 옮긴다.
        # 큐를 옮길때 작업시간이 가장 짧은순으로 저장되어야한다.
        while self.jobs and self.current_time >= self.jobs[0][0]:
            job = heapq.heappop(self.jobs)
            heapq.heappush(self.work_queue, (job[1], job[0])) # 걸리는시간, 시작시간

        # 만약 작업큐가 비어있다면 현재시간을 바꾼다.
        if len(self.work_queue) == 0:
            self.current_time = self.jobs[0][0]
        else:
            work_time, start_time = heapq.heappop(self.work_queue)
            delayed_time = self.current_time - start_time
            
            self.total_time += work_time + delayed_time
            self.current_time += work_time

    def is_empty(self):
        return len(self.jobs) == 0 and len(self.work_queue) == 0

    def get_average(self):
        return self.total_time // self.work_length


def solution(jobs):
    diskcontroler = DiskController(jobs)

    while not diskcontroler.is_empty():
        diskcontroler.pop_work()

    return diskcontroler.get_average()