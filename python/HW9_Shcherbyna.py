# Task 1
def custom_range(start, stop, step=1):
    current = start
    while current < stop if step > 0 else current > stop:
        yield current
        current += step


# Task 2
nums_generator = (x for x in range(1, 11))
