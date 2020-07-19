
class Packets:
    def __init__(self, arrived_at, processing_time):
        self.arrived_at = arrived_at
        self.processing_time = processing_time

class Responses:
    def __init__(self, is_processed, started_at):
        self.is_processed = is_processed
        self.started_at = started_at

class Buffer:
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.finish_time = []

    def flush(self, request):
        while self.finish_time:
            if self.finish_time[0] <= request.arrived_at:
                self.finish_time.pop(0)
            else:
                break

    def is_empyt(self):
        if len(self.finish_time) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.finish_time) == self.buffer_size:
            return True
        else:
            return False


    def process(self, request):

        self.flush(request)

        if self.is_empyt():
            self.finish_time.append(request.arrived_at + request.processing_time)
            return Responses(True, request.arrived_at)

        if self.is_full():
            return Responses(False, -1)

        response = Responses(True, self.finish_time[-1])
        self.finish_time.append(self.finish_time[-1] + request.processing_time)
        return response


def main():
    requests = []
    buffer_size, num_packets = map(int, input().split())
    for i in range(num_packets):
        arrived_at, processing_time = map(int, input().split())
        requests.append(Packets(arrived_at, processing_time))

    responses = []
    buffer = Buffer(buffer_size)
    for request in requests:
        responses.append(buffer.process(request))

    for response in responses:
        print(response.started_at if response.is_processed else -1)


if __name__ == '__main__':
    main()