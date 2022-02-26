# 3. Working with CSV
# Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions
# from quasi-continuous daily measurements at Mauna Loa, Hawaii dataset,
# obtained from here (https://github.com/datasets/co2-ppm-daily/tree/master/data).
#
# Using Python (csv) calculate the following:
import csv
# Create three lists to use for calculations
year_list, month_list, value_list = [], [], []

with open("co2-ppm-daily.csv") as co2:
    csv_reader = csv.reader(co2, delimiter=',')
    line_count = 0
    header = next(csv_reader)
    print(header)
    for row in csv_reader:
        year, month, day = row[0].split("-")

        if year not in year_list:
            year_list.append(year)
        if month not in month_list:
            month_list.append(month)

        value_list.append(float(row[1]))
        line_count = line_count + 1

# Minimum, maximum and average for the entire dataset.
print("Minimum = " + str(min(value_list)))
print("Maximum = " + str(max(value_list)))
print("Average = " + str(float(sum(value_list) / int(line_count))))

overall_mean = str(float(sum(value_list) / int(line_count)))

# Annual average for each year in the dataset.
print("We have: " + str(len(year_list)) + "years.")
for year_select in year_list:
    ppm_by_year = []
    with open("co2-ppm-daily.csv") as co2:
        csv_reader = csv.reader(co2, delimiter=',')
        line_count = 0
        header = next(csv_reader)
        # print(header)
        for row in csv_reader:
            year, month, day = row[0].split("-")
            if year == year_select:
                ppm_by_year.append(float(row[1]))

    print("Year is:" + str(int(year_select)) + ", ppm is: " + str(float(sum(ppm_by_year) / len(ppm_by_year))))

# Seasonal average if Spring (March, April, May), Summer (June, July, August),
# Autumn (September, October, November) and Winter (December, January, February).
seasons_winter = ['12', '01', '02']
seasons_spring = ['03', '04', '05']
seasons_summer = ['06', '07', '08']
seasons_autumn = ['09', '10', '11']

seasons_winter_ppm = []
seasons_spring_ppm = []
seasons_summer_ppm = []
seasons_autumn_ppm = []


with open("co2-ppm-daily.csv") as co2:
    csv_reader = csv.reader(co2, delimiter=',')
    line_count = 0
    header = next(csv_reader)
    # print(header)
    for row in csv_reader:
        year, month, day = row[0].split("-")

        if month in seasons_winter:
            seasons_winter_ppm.append(float(row[1]))
        if month in seasons_spring:
            seasons_spring_ppm.append(float(row[1]))
        if month in seasons_summer:
            seasons_summer_ppm.append(float(row[1]))
        if month in seasons_autumn:
            seasons_autumn_ppm.append(float(row[1]))

print("Winter is: " + str(float(sum(seasons_winter_ppm) / len(seasons_winter_ppm))))
print("Spring is: " + str(float(sum(seasons_spring_ppm) / len(seasons_spring_ppm))))
print("Summer is: " + str(float(sum(seasons_summer_ppm) / len(seasons_summer_ppm))))
print("Autumn is: " + str(float(sum(seasons_autumn_ppm) / len(seasons_autumn_ppm))))

# Calculate the anomaly for each value in the dataset relative to the mean
# for the entire time series.
print(overall_mean)
with open("co2-ppm-daily.csv") as co2:
    csv_reader = csv.reader(co2, delimiter=',')
    line_count = 0
    header = next(csv_reader)
    # print(header)
    for row in csv_reader:
        print(float(str(row[1])) - float(overall_mean))



