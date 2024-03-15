from collections import Counter


def calculate_statistics(values):
    # Find the maximum value
    maximum = max(values)

    # Find the minimum value
    minimum = min(values)

    # Find the mean
    mean = sum(values) / len(values)

    # Find the mode
    counter = Counter(values)
    mode = counter.most_common(1)[0][0]

    return maximum, minimum, mean, mode


if __name__ == "__main__":
    values = []
    while True:
        value = input("Enter a value (or 's' to stop): ")
        if value.lower() == 's':
            break
        values.append(int(value))

    if values:
        maximum, minimum, mean, mode = calculate_statistics(values)
        print(f"The maximum value is: {maximum}")
        print(f"The minimum value is: {minimum}")
        print(f"The mean of the values is: {mean}")
        print(f"The mode of the values is: {mode}")
    else:
        print("No values were entered.")
