import os

for file in os.listdir("./data/"):
    # print(file)

    outgoing_file = []

    with open(f"./data/{file}") as current_file:
        data = current_file.readlines()

    for line in data:
        words = line.split()

        words.pop(0)

        modified_line = " ".join(words) + "\n"

        outgoing_file.append(modified_line)

    outgoing_file = "".join(outgoing_file)

    with open(f"./data/clean/{file}", mode="x") as file_out:
        file_out.write(outgoing_file)
