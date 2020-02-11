""" You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible. """


class LogStructure:
    def __init__(self, maximum_size):
        self.maximum_size = maximum_size
        self.buffer = [None] * maximum_size
        self.current_id = 0

    def record(self, order_id):
        self.buffer[self.current_id] = order_id
        self.current_id = (self.current_id + 1) % self.maximum_size

    def get_last(self, i):
        return self.buffer[(self.current_id - i + self.maximum_size) % self.maximum_size]

log = LogStructure(5)
log.record(1)
log.record(2)

print(log.get_last(1))