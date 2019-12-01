def main():
    print(part_one())
    print(part_two())


def part_one():
    input_file = open('input.txt', 'r')

    sum_fuel_requirements = 0

    for current in input_file:
        sum_fuel_requirements = sum_fuel_requirements + calc_fuel(int(current))

    return sum_fuel_requirements


def part_two():
    input_file = open('input.txt', 'r')

    sum_fuel_requirements = 0

    for current in input_file:
        current_fuel = calc_fuel(int(current))
        sum_fuels = current_fuel
        while current_fuel > 0:
            current_fuel = calc_fuel(current_fuel)
            if current_fuel > 0:
                sum_fuels = sum_fuels + current_fuel

        sum_fuel_requirements = sum_fuel_requirements + sum_fuels

    return sum_fuel_requirements


def calc_fuel(mass):
    return int(mass / 3) - 2


if __name__ == '__main__':
    main()
