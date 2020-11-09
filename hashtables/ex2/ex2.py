#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Return a list of strings representing the sequence of flights
    """
    route = [None] * length

    r = dict()
    for t in tickets:
        r[t.source] = t.destination
    destine = r['NONE']
    for current in range(0, length):
        route[current] = destine
        destine = r[destine]
    return route
