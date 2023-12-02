from functools import reduce


def get_solution():
    available_cubes = {
        "red": 12,
        "blue": 14,
        "green": 13
    }
    with open("input.txt") as file:
        input_data = file.read().split("\n")

    real_games = []

    for game_idx in range(len(input_data)):
        is_valid = True
        game_line = input_data[game_idx][input_data[game_idx].find(":") + 1:]
        game_sets = game_line.split(";")
        for game_set in game_sets:
            for cube_info in game_set.split(","):
                if any(color in cube_info and int(
                        cube_info.replace(color, "")) > max_count for
                       color, max_count in available_cubes.items()):
                    is_valid = False
                    break
            if not is_valid:
                break
        if is_valid:
            real_games.append(game_idx + 1)

    print(f"Part 1: {sum(real_games)}")

    cube_powers = []
    for game_idx in range(len(input_data)):
        game_line = input_data[game_idx][input_data[game_idx].find(":") + 1:]
        game_sets = game_line.split(";")
        min_cubes = {
            "red": 0,
            "blue": 0,
            "green": 0
        }
        for game_set in game_sets:
            for cube_info in game_set.split(","):
                for color in available_cubes.keys():
                    if color in cube_info:
                        cube_num = int(cube_info.replace(color, ""))
                        if cube_num > min_cubes[color]:
                            min_cubes[color] = cube_num
        cube_powers.append(reduce(lambda x, y: x * y, min_cubes.values()))

    print(f"Part 2: {sum(cube_powers)}")


if __name__ == "__main__":
    get_solution()

