if __name__ == "__main__":
    digits_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
    }

    with open("input.txt") as file:
        input_data = file.read().lower().split("\n")

    line_values = []
    for line in input_data:
        first_digit, last_digit = "0", "0"
        for sym in line:
            if sym.isdigit():
                if first_digit == "0":
                    first_digit = sym
                last_digit = sym
        line_values.append(int(first_digit + last_digit))

    print(f"Part 1: {sum(line_values)}")

    line_values = []
    for line in input_data:
        for num_str, num in digits_dict.items():
            line = line.replace(num_str, num_str[0] + num + num_str[-1])
        first_digit, last_digit = "0", "0"
        for sym in line:
            if sym.isdigit():
                if first_digit == "0":
                    first_digit = sym
                last_digit = sym
        line_values.append(int(first_digit + last_digit))

    print(f"Part 2: {sum(line_values)}")



