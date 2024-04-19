import csv

exchange_rate = 38.84

with open("test_file.csv") as data:
    csv_data = csv.reader(data)
    data_lines = list(csv_data)
    for line in data_lines[1:]:
        for i in range(1, len(line)):
            line[i] = round(int(line[i]) * exchange_rate)


with open("salaries_uah.csv", mode="w", newline='') as final_data:
    csv_writer = csv.writer(final_data, delimiter=",")
    csv_writer.writerows(data_lines)
