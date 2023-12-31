from functools import lru_cache
import os
import pathlib
import sys
import time

DEBUG_SHOW_STATS = True
DEBUG_START_TIME = 0
DEBUG_END_TIME = 0

LOWEST_NUMBER = 0
HIGHEST_NUMBER = 99999

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
    print(
        f"Allowable generation range for this version of the program is {LOWEST_NUMBER}-{HIGHEST_NUMBER}\n"
    )


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
        ):  # Make sure first_serial is between 0000 and 99999
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

    ones_code = get_ones_place_code(get_digit(number=serial_number, n=0))
    tens_code = get_tens_place_code(get_digit(number=serial_number, n=1))
    hundreds_code = get_hundreds_place_code(get_digit(number=serial_number, n=2))
    thousands_code = get_thousands_place_code(get_digit(number=serial_number, n=3))
    ten_thousands_code = get_ten_thousands_place_code(
        get_digit(number=serial_number, n=4)
    )

    return (
        header
        + "\n"
        + ten_thousands_code
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
    header_data[0] = f"O{serial_number:05d} (EMTSERIALSUB-{serial_number:05d})\n"

    # Collapse header
    return "".join(header_data)


def get_footer() -> str:
    return pathlib.Path("./data/footer").read_text()  # Get footer data


@lru_cache
def get_ones_place_code(digit: int) -> str:
    match digit:
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


@lru_cache
def get_tens_place_code(digit: int) -> str:
    match digit:
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


@lru_cache
def get_hundreds_place_code(digit: int) -> str:
    match digit:
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


@lru_cache
def get_thousands_place_code(digit: int) -> str:
    match digit:
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


@lru_cache
def get_ten_thousands_place_code(digit: int) -> str:
    match digit:
        case 0:
            with open("./data/10000-0") as file:
                return file.read()

        case 1:
            with open("./data/10000-1") as file:
                return file.read()

        case 2:
            with open("./data/10000-2") as file:
                return file.read()

        case 3:
            with open("./data/10000-3") as file:
                return file.read()

        case 4:
            with open("./data/10000-4") as file:
                return file.read()

        case 5:
            with open("./data/10000-5") as file:
                return file.read()

        case 6:
            with open("./data/10000-6") as file:
                return file.read()

        case 7:
            with open("./data/10000-7") as file:
                return file.read()

        case 8:
            with open("./data/10000-8") as file:
                return file.read()

        case 9:
            with open("./data/10000-9") as file:
                return file.read()


def write_file(code: str, filename: str):
    try:
        with open(f"./NC Files/{filename}.eia", mode="x") as file:
            file.write(code)
            print(f"- {filename}.eia created")

    except FileExistsError:
        print(f"Looks like {filename}.eia already exists.")
        continue_command = input("Would you like to overwrite it? (y/n): ")

        if continue_command in ["Y", "y"]:
            os.remove(f"./NC Files/{filename}.eia")
            with open(f"./NC Files/{filename}.eia", mode="x") as file:
                file.write(code)
            print(f"* {filename}.eia was overwritten")
        else:
            print(f"* Creation of {filename}.eia was skipped")

    except FileNotFoundError:
        os.mkdir("./NC Files/")  # Create the directory if it doesn't exist

        write_file(code, filename)  # Try writing again


def main():
    opening_statements()  # Clear output and display program information

    start_serial_number = get_first_serial()
    end_serial_number = get_last_serial(start_serial_number)

    if DEBUG_SHOW_STATS:
        global DEBUG_START_TIME
        global DEBUG_END_TIME
        DEBUG_START_TIME = time.time()

    print("------------------------\n")

    numbers = [item for item in range(start_serial_number, end_serial_number + 1)]

    for number in numbers:
        filename = f"EMTSERIALSUB-{number:05d}"

        code_file = assemble_code_file(number)

        write_file(code_file, filename)

    DEBUG_END_TIME = time.time()


if __name__ == "__main__":
    main()

    if DEBUG_SHOW_STATS:
        elapsed_seconds = DEBUG_END_TIME - DEBUG_START_TIME
        elapsed_minutes = int(elapsed_seconds // 60)
        elapsed_seconds = elapsed_seconds % 60

        print("\n\nDEBUG STATS\n")
        print(f"Elapsed time: {elapsed_minutes}:{elapsed_seconds:.2f}\n")
        print("Ones Place: " + "\n\t" + str(get_ones_place_code.cache_info()))
        print("Tens Place: " + "\n\t" + str(get_tens_place_code.cache_info()))
        print("Hundreds Place: " + "\n\t" + str(get_hundreds_place_code.cache_info()))
        print("Thousands Place: " + "\n\t" + str(get_thousands_place_code.cache_info()))
        print(
            "Ten-thousands Place: "
            + "\n\t"
            + str(get_ten_thousands_place_code.cache_info())
        )
