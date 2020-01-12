# dataset_populator.py
# 
# Reads content from tweets parsed into CSV format by csv_converter.py
# and allows a user to input data through the terminal for "Positivity",
# "Technicality", and "Relevancy" parameters. This data will then be
# used to train a machine learning model.

import csv
import os

#Create temp file with column headers for CSV file
with open("temp.csv", mode="w", newline = '') as csv_new:
    csv_writer = csv.writer(csv_new, delimiter=',')
    csv_writer.writerow(["ID","Text","Date", "User Name", "Screen Name", "Profile Picture", "Positivity", "Technicality", "Relevancy"])
    csv_new.close()

#Open existing CSV file to read 
with open("dataset.csv") as csv_old:
    csv_reader = csv.reader(csv_old, delimiter=',')

    quit_now = 0
    tweet_count = 0
    for row in csv_reader:
        if tweet_count == 0:
            print(f"Column names are {', '.join(row)}")
            tweet_count += 1
        elif row and (row[6] != '' or quit_now):
            with open("temp.csv", mode='a', newline = '') as csv_new:
                csv_writer = csv.writer(csv_new, delimiter=',')
                csv_writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
                csv_new.close()

        elif row and row[6] == '':
            print()
            print("______________________________________________________________________________________")
            print()
            print("Tweet: ", row[1])
            print("______________________________________________________________________________________")
            print()
            positivity, technicality, relevancy = input("Input positivity, technicality, relevancy (or q q q to quit): ").split()

            if positivity == "q" or technicality == "q" or relevancy == "q":
                quit_now = 1
                with open("temp.csv", mode='a', newline = '') as csv_new:
                    csv_writer = csv.writer(csv_new, delimiter=',')
                    csv_writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
                    csv_new.close()
            else:
                with open("temp.csv", mode='a', newline = '') as csv_new:
                    csv_writer = csv.writer(csv_new, delimiter=',')
                    csv_writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], positivity, technicality, relevancy])
                    csv_new.close()

            tweet_count += 1
    csv_old.close()

    print(f"Processed {tweet_count-1} tweets.")

os.remove("dataset.csv")
os.rename("temp.csv", "dataset.csv")