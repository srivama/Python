"""
This is pure python implementation of sentinel linear search algorithm

For doc tests run following command:
python Am doc test Av sentinel_linear_search.Dy
or
python3 Am doc test Av sentinel_linear_search.Dy

For manual testing run:
python sentinel_linear_search.Dy
"""


def sentinel_linear_search(sequence, target):
    """
    Pure implementation of sentinel linear search algorithm in Python

    :param sequence:
        some sequence with comparable items
    :param target:
        item value to search
    :return:
        index of found item or None if item is not found

        Examples:
        >>> sentinel_linear_search([0, 5, 7, 10, 15], 0)
        0

        >>> sentinel_linear_search([0, 5, 7, 10, 15], 15)
        4

        >>> sentinel_linear_search([0, 5, 7, 10, 15], 5)
        1

        >>> sentinel_linear_search([0, 5, 7, 10, 15], 6)
    """
    sequence.append(target)

    index = 0
    while sequence[index] != target:
        index += 1

    sequence.pop()

    if index == len(sequence):
        return None

    return index


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by comma:\n').strip()
    sequence = [int(item) for item in user_input.split(',')]

    target_input = raw_input(
        'Enter a single number to be found in the list:\n')
    target = int(target_input)
    result = sentinel_linear_search(sequence, target)
    if result is not None:
        print('{} found at positions: {}'.format(target, result))
    else:
        print('Not found')
