import os
import sys

LOWEST_NUMBER = 0
HIGHEST_NUMBER = 9999

FIRST_SERIAL_INPUT_MESSAGE = "Enter the first serial number: "
LAST_SERIAL_INPUT_MESSAGE = "Enter the last serial number: "
INPUT_PARSE_ERROR_MESSAGE = "- BAD INPUT -\n" + "Please enter a whole number"
INPUT_START_RANGE_ERROR_MESSAGE = (
    f"- BAD INPUT -\n"
    + "Please enter a number between {LOWEST_NUMBER} and {HIGHEST_NUMBER} "
)
INPUT_END_RANGE_ERROR_MESSAGE = "- BAD INPUT -\n" + "Please enter a number between "

# Define a cross-platform clear() function for the terminal
if sys.platform == "win32":
    clear = lambda: os.system("cls")
else:
    clear = lambda: os.system("clear")


def opening_statements():  # Clear output and display program information
    clear()
    print("-- Serial Number Generator --\n")
    print(
        "This program generates serial number GCODE files for the Mazak Variaxis i-700."
    )
    print("Allowable generation range for this version of the program is 0000-9999\n")


def get_digit(number, n):
    return number // 10**n % 10


def get_first_serial() -> int:
    try:
        first_serial = int(input(FIRST_SERIAL_INPUT_MESSAGE))

    except ValueError:
        opening_statements()
        print(INPUT_PARSE_ERROR_MESSAGE)  # Give an error message explaining what happened
        return get_first_serial()

    else:
        if (
            LOWEST_NUMBER <= first_serial <= HIGHEST_NUMBER
        ):  # Make sure first_serial is between 0000 and 9999
            return first_serial  # Return it if everything looks good
        else:
            opening_statements()
            print(INPUT_START_RANGE_ERROR_MESSAGE)
            return (
                get_first_serial()
            )  # If not, rerun get_first_serial(), this time with the error message displayed


def get_last_serial(first_serial: int) -> int:
    try:
        last_serial = int(input(LAST_SERIAL_INPUT_MESSAGE))

    except ValueError:
        opening_statements()
        print(f"{FIRST_SERIAL_INPUT_MESSAGE}{first_serial}\n")
        print(INPUT_PARSE_ERROR_MESSAGE)
        return get_last_serial(first_serial)

    else:
        if (
            first_serial <= last_serial <= HIGHEST_NUMBER
        ):  # Make sure the last serial number is greater-than or equal-to the first serial number
            return last_serial  # Return it if everything looks good
        else:
            opening_statements()
            print(f"{FIRST_SERIAL_INPUT_MESSAGE}{first_serial}\n")
            print(
                INPUT_END_RANGE_ERROR_MESSAGE
                + str(first_serial)
                + f" and {HIGHEST_NUMBER}"
            )
            return get_last_serial(first_serial)


def assemble_code_file(serial_number: int) -> str:
    # Get program header & footer
    header = get_header(serial_number=serial_number)
    footer = get_footer()

    # TODO: Change get_###_place_code() function to accept full serial number and to call get_digit() from within
    # Get code chunk based on each digit
    ones_code = get_ones_place_code(serial_number)
    tens_code = get_tens_place_code(serial_number)
    hundreds_code = get_hundreds_place_code(serial_number)
    thousands_code = get_thousands_place_code(serial_number)

    return (
        header
        + "\n"
        + thousands_code
        + "\n"
        + hundreds_code
        + "\n"
        + tens_code
        + "\n"
        + ones_code
        + "\n\n"
        + footer
    )


def get_header(serial_number: int) -> str:
    # Get header
    with open("./data/header") as file:
        header_data = file.readlines()

    # Modify first line of header to match serial number
    header_data[0] = f"O{serial_number:04d} ({f'EMTSERIALSUB-{serial_number:04d}'})\n"

    # Collapse header
    return "".join(header_data)


def get_footer() -> str:
    # Get header
    with open("./data/footer") as file:
        footer_data = file.read()

    return footer_data


def get_ones_place_code(serial_number: int) -> str:
    match get_digit(number=serial_number, n=0):
        case 0:
            with open("./data/1-0") as file:
                return file.read()

        case 1:
            with open("./data/1-1") as file:
                return file.read()

        case 2:
            with open("./data/1-2") as file:
                return file.read()

        case 3:
            with open("./data/1-3") as file:
                return file.read()

        case 4:
            with open("./data/1-4") as file:
                return file.read()

        case 5:
            with open("./data/1-5") as file:
                return file.read()

        case 6:
            with open("./data/1-6") as file:
                return file.read()

        case 7:
            with open("./data/1-7") as file:
                return file.read()

        case 8:
            with open("./data/1-8") as file:
                return file.read()

        case 9:
            with open("./data/1-9") as file:
                return file.read()


def get_tens_place_code(serial_number: int) -> str:
    match get_digit(number=serial_number, n=1):
        case 0:
            with open("./data/10-0") as file:
                return file.read()

        case 1:
            with open("./data/10-1") as file:
                return file.read()

        case 2:
            with open("./data/10-2") as file:
                return file.read()

        case 3:
            with open("./data/10-3") as file:
                return file.read()

        case 4:
            with open("./data/10-4") as file:
                return file.read()

        case 5:
            with open("./data/10-5") as file:
                return file.read()

        case 6:
            with open("./data/10-6") as file:
                return file.read()

        case 7:
            with open("./data/10-7") as file:
                return file.read()

        case 8:
            with open("./data/10-8") as file:
                return file.read()

        case 9:
            with open("./data/10-9") as file:
                return file.read()


def get_hundreds_place_code(serial_number: int) -> str:
    match get_digit(number=serial_number, n=2):
        case 0:
            with open("./data/100-0") as file:
                return file.read()

        case 1:
            with open("./data/100-1") as file:
                return file.read()

        case 2:
            with open("./data/100-2") as file:
                return file.read()

        case 3:
            with open("./data/100-3") as file:
                return file.read()

        case 4:
            with open("./data/100-4") as file:
                return file.read()

        case 5:
            with open("./data/100-5") as file:
                return file.read()

        case 6:
            with open("./data/100-6") as file:
                return file.read()

        case 7:
            with open("./data/100-7") as file:
                return file.read()

        case 8:
            with open("./data/100-8") as file:
                return file.read()

        case 9:
            with open("./data/100-9") as file:
                return file.read()


def get_thousands_place_code(serial_number: int) -> str:
    match get_digit(number=serial_number, n=3):
        case 0:
            with open("./data/1000-0") as file:
                return file.read()

        case 1:
            with open("./data/1000-1") as file:
                return file.read()

        case 2:
            with open("./data/1000-2") as file:
                return file.read()

        case 3:
            with open("./data/1000-3") as file:
                return file.read()

        case 4:
            with open("./data/1000-4") as file:
                return file.read()

        case 5:
            with open("./data/1000-5") as file:
                return file.read()

        case 6:
            with open("./data/1000-6") as file:
                return file.read()

        case 7:
            with open("./data/1000-7") as file:
                return file.read()

        case 8:
            with open("./data/1000-8") as file:
                return file.read()

        case 9:
            with open("./data/1000-9") as file:
                return file.read()


def main():
    opening_statements()  # Clear output and display program information

    start_serial_number = get_first_serial()
    end_serial_number = get_last_serial(start_serial_number)

    print("------------------------\n")

    numbers = [item for item in range(start_serial_number, end_serial_number + 1)]

    for number in numbers:
        filename = f"EMTSERIALSUB-{number:04d}"

        code_file = assemble_code_file(number)

        try:
            with open(f"./NC Files/{filename}.eia", mode="x") as file:
                file.write(code_file)
                print(f"- {filename}.eia created")
        except FileExistsError:
            print(f"Looks like {filename}.eia already exists.")
            continue_command = input("Would you like to overwrite it? (y/n): ")

            if continue_command in ["Y", "y"]:
                os.remove(f"./NC Files/{filename}.eia")
                with open(f"./NC Files/{filename}.eia", mode="x") as file:
                    file.write(code_file)
                print(f"* {filename}.eia was overwritten")
            else:
                print(f"* Creation of {filename}.eia was skipped")


if __name__ == "__main__":
    main()
