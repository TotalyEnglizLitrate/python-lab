def flatten(nested_list):
    flattened = []
    for i in nested_list:
        if isinstance(i, list):
            flattened.extend(flatten(i))
        else:
            flattened.append(i)

    return flattened

def map(lst, f):
    for i in lst:
        yield f(i)

def filter(lst, condition_func):
    for i in lst:
        if condition_func(i):
            yield i


if __name__ == "__main__":
    lst = eval(input("Enter a nested list: "))
    flattened = flatten(lst)
    print(flattened)
    print(*map(flattened, lambda x: x ** 2), sep=', ')
    print(*filter(flattened, lambda x: x & 1 == 1), sep=", ")