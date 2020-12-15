def speak_numbers(numbers, final_turn):
    spoken_numbers = {number: (turn, turn) for turn, number in enumerate(numbers, 1)}
    last_spoken_number = numbers[-1]
    current_turn = len(numbers) + 1

    while current_turn <= final_turn:
        new_number = spoken_numbers[last_spoken_number][1] - spoken_numbers[last_spoken_number][0]

        if new_number not in spoken_numbers:
            spoken_numbers[new_number] = (current_turn, current_turn)
        else:
            spoken_numbers[new_number] = (spoken_numbers[new_number][1], current_turn)
        last_spoken_number = new_number
        current_turn += 1

    return last_spoken_number


if __name__ == '__main__':
    assert speak_numbers([0, 3, 6], 2020) == 436
    assert speak_numbers([1, 3, 2], 2020) == 1
    assert speak_numbers([2, 1, 3], 2020) == 10
    assert speak_numbers([1, 2, 3], 2020) == 27
    assert speak_numbers([2, 3, 1], 2020) == 78
    assert speak_numbers([3, 2, 1], 2020) == 438
    assert speak_numbers([3, 1, 2], 2020) == 1836
    assert speak_numbers([0, 3, 6], 30000000) == 175594

    print(speak_numbers([13, 16, 0, 12, 15, 1], 2020))
    print(speak_numbers([13, 16, 0, 12, 15, 1], 30000000))
