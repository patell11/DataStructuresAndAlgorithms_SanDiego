# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def flushes(self,request):
        """ clears the processed element by the arrivals time"""
        while self.finish_time:
            if self.finish_time[0] <= request.arrived_at:
                self.finish_time.pop(0)
            else:
                break

    def is_empty(self):
        """ Return if the buffer is empty"""
        if len(self.finish_time) == 0:
            return True
        else:
            return False

    def is_full(self):
        """ Return true if the buffer is full"""
        if len(self.finish_time) == self.size:
            return True
        else:
            return False

    def last_element(self):
        """ Returns the last element from the buffer"""
        return self.finish_time[-1]

    def process(self, request):
        # write your code here

        self.flushes(request)

        if self.is_empty():
            self.finish_time.append(request.arrived_at + request.time_to_process)
            return Response(False,request.arrived_at)

        if self.is_full():
            return Response(True, -1)

        response = Response(False, self.last_element())
        self.finish_time.append(self.last_element() + request.time_to_process)
        return response




def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
