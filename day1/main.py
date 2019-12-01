def main():
    part_one()
    part_two()


def part_one():
    input_file = open('input.txt', 'r')

    sum_fuel_requirements = 0

    for current in input_file:
        sum_fuel_requirements = sum_fuel_requirements + (int(int(current) / 3) - 2)

    print(sum_fuel_requirements)


def part_two():
    input_file = open('input.txt', 'r')

    sum_fuel_requirements = 0

    for current in input_file:
        current_fuel = (int(int(current) / 3) - 2)
        sum_fuels = current_fuel
        while current_fuel > 0:
            current_fuel = (int(int(current_fuel) / 3) - 2)
            if current_fuel > 0:
                sum_fuels = sum_fuels + current_fuel

        sum_fuel_requirements = sum_fuel_requirements + sum_fuels

    print(sum_fuel_requirements)


if __name__ == '__main__':
    main()
