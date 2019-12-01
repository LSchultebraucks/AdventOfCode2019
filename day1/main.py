def main():
    part_one()


def part_one():
    input_file = open('input.txt', 'r')

    sum_fuel_requirements = 0

    for current in input_file:
        sum_fuel_requirements = sum_fuel_requirements + (int(int(current) / 3) - 2)

    print(sum_fuel_requirements)


if __name__ == '__main__':
    main()