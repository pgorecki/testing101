def more_negatives(arr):
    """
    :param arr: array of numbers
    :return: True if arr contains more negative numbers than positive
    """
    num_negative = 0
    num_positive = 0
    for number in arr:
        if number < 0:
            num_negative += 1
        else:
            num_positive += 1
    return num_negative > num_positive



