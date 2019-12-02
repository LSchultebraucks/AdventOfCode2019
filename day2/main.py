def main():
    print(part_one())
    print(part_two())


def part_one():
    input_file = open('input.txt', 'r')
    line = input_file.read()
    program = [int(num) for num in line.split((","))]

    program[1] = 12
    program[2] = 2
    address = 0

    while address <= len(program):
        opcode = program[address]
        pos1 = program[address + 1]
        pos2 = program[address + 2]
        pos3 = program[address + 3]
        if opcode == 1:
            program[pos3] = program[pos1] + program[pos2]
        elif opcode == 2:
            program[pos3] = program[pos1] * program[pos2]
        elif opcode == 99:
            break
        address = address + 4

    return program[0]


def part_two():
    input_file = open('input.txt', 'r')
    line = input_file.read()
    source_program = [int(num) for num in line.split((","))]

    for noun in range(100):
        for verb in range(100):
            program = source_program.copy()
            program[1] = noun
            program[2] = verb
            address = 0
            while address <= len(program):
                opcode = program[address]
                pos1 = program[address + 1]
                pos2 = program[address + 2]
                pos3 = program[address + 3]
                if opcode == 1:
                    program[pos3] = program[pos1] + program[pos2]
                elif opcode == 2:
                    program[pos3] = program[pos1] * program[pos2]
                elif opcode == 99:
                    break
                address = address + 4

            if program[0] == 19690720:
                return 100 * noun + verb


if __name__ == '__main__':
    main()
