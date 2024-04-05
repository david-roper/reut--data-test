import os
import polars as pl
import polars.selectors as cs
import pandas as pd

df = pl.read_excel('data/raw_morning_data.xlsx')


df = df.drop(["Respondent ID","Collector ID","Start Date", "End Date",	"IP Address",	"Email Address",	"First Name",	"Last Name",	"Custom Data 1"])

# formDatesDF = df.with_columns([pl.col("Start Date"), pl.col("End Date")])
df = df.rename({"Please enter the participant number that was sent to you here so that we can identify you:":"participant ID"})
df2 = df.slice(0,1)

#print(df)

df = df.slice(1) #removes top row
print('here is df2 \n')
print(df2)
# df = df.rename({"Please enter the participant number that was sent to you here so that we can identify you:":"participant ID"})
# df2 = df2.rename({"Please enter the participant number that was sent to you here so that we can identify you:":"participant ID"})
df= df.sort(["participant ID", "What was yesterday&apos;s date? (i.e. the date of your bedtime)"])

#convert to pandas for name filtering
df = df.to_pandas()

df.loc[df['participant ID'].str.contains('[a-zA-Z]'), 'participant ID'] = ''

for i,col in enumerate(df.columns):
    if (col == ''):
        df.rename(columns={col: f"column_{i}"}, inplace=True)


print('\nnow test concat')
df2 = df2.to_pandas()

df = pd.concat([df2,df], ignore_index=True)
print(df)


#convert back into polar df
df = pl.from_pandas(df)
print(df)

path = os.curdir + '/data/sorted-data.csv'
df.write_csv(path,separator=',')