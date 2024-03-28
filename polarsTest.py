import os
import polars as pl
import polars.selectors as cs

df = pl.read_excel('data/raw_morning_data.xlsx')


df = df.drop(["Respondent ID","Collector ID","Start Date", "End Date",	"IP Address",	"Email Address",	"First Name",	"Last Name",	"Custom Data 1"])

# formDatesDF = df.with_columns([pl.col("Start Date"), pl.col("End Date")])
df = df.rename({"Please enter the participant number that was sent to you here so that we can identify you:":"participant ID"})
df2 = df.slice(0,1)

#print(df)

# df = df.slice(1) #removes top row
#print(df2)
# df = df.rename({"Please enter the participant number that was sent to you here so that we can identify you:":"participant ID"})
# df2 = df2.rename({"Please enter the participant number that was sent to you here so that we can identify you:":"participant ID"})
df= df.sort(["participant ID", "What was yesterday&apos;s date? (i.e. the date of your bedtime)"])

#convert to pandas for name filtering
df = df.to_pandas()
print(df.iloc[:,6])
df.loc[df['participant ID'].str.contains('[a-zA-Z]'), 'participant ID'] = ''

for i,col in enumerate(df.columns):
    if (col == ''):
        df.rename(columns={col: f"column_{i}"}, inplace=True)

print(df['column_6'] + '\n')
print('\nnow test concat')
#convert back into polar df
df = pl.from_pandas(df)

#df = pl.concat([df,df2])
print(df)
path = os.curdir + '/data/sorted-data.csv'
df.write_csv(path,separator=',')