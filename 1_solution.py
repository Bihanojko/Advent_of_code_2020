def main(year):
    with open("1_input.txt", "r") as input_file:
        entries = input_file.read()
        entries = entries.split("\n")
        entries = [int(x) for x in entries]

        # # OPTION #1: Quadratic Time Complexity
        # for i in range(len(entries)):
        #     for j in range(len(entries)):
        #         if i != j:
        #             if entries[i] + entries[j] == year:
        #                 return entries[i] * entries[j]

        # # OPTION #2: Quadratic Time Complexity, slightly improved
        # for i in range(len(entries)):
        #     for j in range(i + 1, len(entries)):
        #         if entries[i] + entries[j] == year:
        #             return entries[i] * entries[j]

        # # OPTION #3: Linear Time Complexity
        found_values = set()

        for i in entries:
            if year - i in entries:
                return i * (year - i)

            found_values.add(i)                


year = 2020
multiplied_value = main(year)
print(multiplied_value)
