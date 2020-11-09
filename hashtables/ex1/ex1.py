def get_indices_of_item_weights(weights, length, limit):
    """
    Returns two items whose totaled weight equals the limit
    """
    w_dict = dict()
    for i in range(len(weights)):
        current = weights[i]
        if current in w_dict:
            previous = w_dict[current]
            return (i, previous)
        w_dict[limit - current] = i
    return None