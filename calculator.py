def calculate(a: float, operator: str, b: float) -> int | float | None:
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return None
        return a / b


def main() -> None:
    while (first_number := input("First number (or q): ")) != "q":
        operator = input("Operator (+ - * /): ")
        second_number = input("Second number: ")
        result = calculate(float(first_number), operator, float(second_number))
        if result is None:
            print("Cannot calculate that")
        else:
            print(result)


if __name__ == "__main__":
    main()
