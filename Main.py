import numpy as np
import pandas as pd


conversion_file = "Csv_files/conversion-factors-2019-flat-file-v01-02(1).csv"
airplane_file = "Csv_files/airline-traffic-and-operations-1929-present-data.csv"
train_file = "Csv_files/scotrail-journey-data-2016-2022.csv"
kiloConversion = 1.60934
df_con = pd.read_csv(conversion_file)
df_plane = pd.read_csv(airplane_file)
df_train = pd.read_csv(train_file)

# finds how many planes where flown in 2019
df_plane.loc[df_plane["Year"] == 2019]

air_co2 = df_con.loc[df_con["Level 1"] == "Business travel- air"]
train_co2 = df_con.loc[df_con["Level 3"] == "National rail"]
#total gas per passenger per kilometer traveled
trainAverageCo2=train_co2["#REF!"].astype(float).mean()

print(air_co2["#REF!"].astype(float).mean())

train_2019 = df_train.loc[df_train["CalendarYear"] == 2019]
train_2019 = train_2019.replace(",","", regex = True)

trainKilos2019 = train_2019["OpMiles on selDates"].astype(float).sum()* kiloConversion
#average green house produced
print(trainKilos2019*trainAverageCo2)



