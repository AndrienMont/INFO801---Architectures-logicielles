import threading
import queue


class LindaSpace:
    def __init__(self):
        self.tuplespace = queue.Queue()
        self.lock = threading.Lock()

    def out(self, tuple_data):
        with self.lock:
            self.tuplespace.put(tuple_data)

    def inp(self, template):
        with self.lock:
            matching_tuples = [t for t in list(self.tuplespace.queue) if self.match(template, t)]
            if matching_tuples:
                selected_tuple = matching_tuples[0]
                self.tuplespace.queue.remove(selected_tuple)
                return selected_tuple
            else:
                return None

    def rd(self, template):
        with self.lock:
            matching_tuples = [t for t in list(self.tuplespace.queue) if self.match(template, t)]
            return matching_tuples

    def match(self, template, tuple_data):
        if len(template) != len(tuple_data):
            return False

        for t, d in zip(template, tuple_data):
            if t is not None and t != d:
                return False

        return True

    def __str__(self):
        with self.lock:
            return str(list(self.tuplespace.queue))