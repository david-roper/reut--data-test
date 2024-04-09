import polars as pl
import pandas as pd

df = pl.read_excel('data/formattedMorningData.xlsx')

df = df.slice(1)

print(df)

df.rename({'':"participant ID"})


'''
convert calculations into python code, iterate through each participants morning and evening weekly data. take those weeks of data and produce the spss lines through calculations

'''

