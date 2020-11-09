def has_negatives(a):
    """
    YOUR CODE HERE
    """
    n_dict = dict()
    result = []

    for i in a:
        n_dict[i] = 1
        if i != 0 and -i in n_dict:
            result.append(abs(i))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
