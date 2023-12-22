def get_sum_of_calibration_values(input_contents: list[str]) -> int:
    result = 0
    for line in input_contents:
        result += 10 * int(next(c for c in line if c.isdigit()))
        result += int(next(c for c in line[::-1] if c.isdigit()))
    return result


def get_input_contents() -> list[str]:
    print("Please input the calibration document contents. Empty line to end.")
    input_contents = []
    while line := input():
        input_contents.append(line)
    return input_contents


if __name__ == "__main__":
    print("Result:", get_sum_of_calibration_values(get_input_contents()))
