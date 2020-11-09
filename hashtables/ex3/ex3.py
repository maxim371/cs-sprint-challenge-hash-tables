def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = dict()

    for a in arrays:
        for i in a:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1

    return [info[0] for info in result.items() if info[1] == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
