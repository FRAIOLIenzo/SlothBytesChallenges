def bridgeShuffle(array1, array2):
    """
    This function takes two arrays and shuffles them together.
    """
    new_array = []
    if len(array1) > len(array2):
        bigger_array = array1
        smaller_array = array2
    else:
        bigger_array = array2
        smaller_array = array1

    for i in range(len(smaller_array)):
        new_array.append(array1[i])
        new_array.append(array2[i])
    new_array.extend(bigger_array[len(smaller_array):])
    return new_array

# Test cases

arrayA = [1, 2, 8, 9]
arrayB = [5, 6, 7]

print(bridgeShuffle(arrayA, arrayB))

