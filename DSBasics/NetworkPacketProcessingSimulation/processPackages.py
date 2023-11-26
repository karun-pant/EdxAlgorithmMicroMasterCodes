# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finishTime = []


    @property
    def isFull(self):
        return len(self.finishTime) == self.size
    
    @property
    def isEmpty(self):
        return len(self.finishTime) == 0

    @property
    def lastElement(self):
        return self.finishTime[-1]

    def flushProcessedRequests(self, request):
        while self.finishTime:
            if self.finishTime[0] <= request.arrived_at:
                self.finishTime.pop(0)
            else:
                break

    def process(self, request):
    # Flush the request if it is done
        self.flushProcessedRequests(request)
        if self.isFull:
            # Return a response indicating that the buffer is full
            return Response(True, -1)
        if self.isEmpty:
            # Calculate the finish time and return a response indicating that the request has been processed
            self.finishTime.append(request.arrived_at + request.time_to_process) 
            return Response(False, request.arrived_at)
        # create response for the request
        response = Response(False, self.lastElement)
        # update finish time to array for current request
        self.finishTime.append(self.lastElement + request.time_to_process)
        return response


def process_requests(requests, buffer):
    return [buffer.process(request) for request in requests]


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
