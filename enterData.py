import pandas as pd
import polars as pl

from spire.xls import *
from spire.xls.common import *

workbook = Workbook()
workbook2 = Workbook()
finalBook = Workbook()

workbook.LoadFromFile('morningdata.xlsx')
workbook2.LoadFromFile('eveningdata.xlsx')
finalBook.LoadFromFile('SleepLogFormattingSheet.xlsx')


morningSheet = workbook.Worksheets[0]
eveningSheet = workbook2.Worksheets[0]
finalSheet = finalBook.Worksheets[0]


morningRange = morningSheet.Range["A1:EL7"]
eveningRange = eveningSheet.Range["A1:FX8"]

finalMorning = finalSheet.Range["E3:EQ9"]
finalEvening = finalSheet.Range["E15:GB22"]

# Copy the source cell range to the destination cell range, and keep its original styles
morningSheet.Copy(morningRange, finalMorning, True)

# Copy the row heights from the source range to the destination range
for i in range(morningRange.Rows.Length):    
    finalMorning.Rows[i].RowHeight = morningRange.Rows[i].RowHeight

# Copy the column widths from the source range to the destination range
for j in range(morningRange.Columns.Length):
    finalMorning.Columns[j].ColumnWidth = morningRange.Columns[j].ColumnWidth


# # Copy the source cell range to the destination cell range, and keep its original styles
# eveningSheet.Copy(eveningRange, finalEvening, True)

# # Copy the row heights from the source range to the destination range
# for i in range(eveningRange.Rows.Length):    
#     finalEvening.Rows[i].RowHeight = eveningRange.Rows[i].RowHeight

# # Copy the column widths from the source range to the destination range
# for j in range(eveningRange.Columns.Length):
#     finalEvening.Columns[j].ColumnWidth = eveningRange.Columns[j].ColumnWidth


# Save the second workbook
finalBook.SaveToFile("CopyCellsToDifferentWorkbook.xlsx", ExcelVersion.Version2013)
workbook.Dispose()
workbook2.Dispose()
finalBook.Dispose()