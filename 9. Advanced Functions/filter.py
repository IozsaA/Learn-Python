friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']

another_starts_with_r=(f for f in friends if f.startswith('R'))


def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i