# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []

    f_dict = dict()

    for i in files:
        a = i.split('/')
        find = a[-1]
        if find not in f_dict:
            f_dict[find] = []
        f_dict[find].append(i)

    for q in queries:
        if q in f_dict:
            result.extend(f_dict[q])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
