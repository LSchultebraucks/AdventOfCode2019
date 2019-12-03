from collections import defaultdict


def main():
    file_input = open('input.txt', 'r')
    data = [line.strip().split(',') for line in file_input]
    file_input.close()
    solve(data)


def map_wires(data):
    wires = ['A', 'B']
    grid = defaultdict(lambda: '.')
    pos_steps = {}
    crossings = []
    crossing_steps = []
    for id, wire in enumerate(wires):
        pos = (0, 0)
        pos_steps[id] = defaultdict(int)
        steps_count = 0
        for path in data[id]:
            positions = []
            direction, steps = path[0], int(path[1:])
            if direction == 'R':
                for i in range(pos[0] + 1, pos[0] + steps + 1):
                    positions.append((i, pos[1]))
            elif direction == 'L':
                for i in range(pos[0] - 1, pos[0] - steps - 1, -1):
                    positions.append((i, pos[1]))
            elif direction == 'U':
                for i in range(pos[1] + 1, pos[1] + steps + 1):
                    positions.append((pos[0], i))
            elif direction == 'D':
                for i in range(pos[1] - 1, pos[1] - steps - 1, -1):
                    positions.append((pos[0], i))
            for pos in positions:
                steps_count += 1
                if grid[pos] == '.':
                    grid[pos] = wire
                    pos_steps[id][pos] = steps_count
                elif grid[pos] != 'x' and grid[pos] != wire:
                    grid[pos] = 'x'
                    crossings.append(abs(pos[0]) + abs(pos[1]))
                    crossing_steps.append(steps_count + pos_steps[0][pos])
    return min(crossings), min(crossing_steps)


def solve(data):
    res = map_wires(data)
    print(res[0])
    print(res[1])
    print()


if __name__ == '__main__':
    main()
