def main():
    print(part_one())


def part_one():
    lower_bound = 353096
    higher_bound = 843212
    diff_password_count = 0
    for potential_password in range(lower_bound, higher_bound):
        has_double = False
        is_increasing = True
        previous_digit = -1
        for digit in map(int, str(potential_password)):
            if digit == previous_digit:
                has_double = True
            if digit < previous_digit:
                is_increasing = False
            previous_digit = digit
        if is_increasing and has_double:
            diff_password_count += 1
    return diff_password_count


if __name__ == '__main__':
    main()