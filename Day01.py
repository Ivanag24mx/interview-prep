def average(numbers):
    """Return the average of a list of numbers"""
    total = sum(numbers)
    return total/len(numbers)

scores = [80, 90, 100]
result = average(scores)
print(result)
print(type(result))
help(average)