#!/usr/bin/python3
import random
import csv

IN_FILE_NAME = "../data/SC-clean-trimmed.csv"
OUT_FILE_NAME = "../data/processed.csv"
SAMPLE_SIZE=300000
ROW_TOTAL = 8440931
RANDOM_SEED = 63412

def bin_ages(age_indices, row):
    for index in age_indices:
        try:
            age = round(float(row[index]))
            age -= age%10
            row[index] = "{}s".format(age)
        except ValueError:
            pass
    return(",".join(row))

def main():
    in_file = open(IN_FILE_NAME, "r")
    out_file = open(OUT_FILE_NAME, "w")

    first_line = in_file.readline()
    out_file.write(first_line)

    # Identify the columns which contain ages
    column_names = first_line.split(",")
    age_indices = []
    for i, name in enumerate(column_names):
        if "age" in name and not "raw" in name:
            age_indices.append(i)

    # Select rows to sample
    random.seed(RANDOM_SEED)
    sample_indices = set(random.sample(range(ROW_TOTAL), SAMPLE_SIZE))

    reader = csv.reader(in_file)
    for j, row in enumerate(reader):
        if j not in sample_indices:
            continue
        out_file.write(bin_ages(age_indices, row) + "\n")
    print(len(sample_indices))

    in_file.close()
    out_file.close()

if __name__ == "__main__":
    main()
