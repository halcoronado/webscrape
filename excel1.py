from unicodedata import name
import openpyxl as xl
from openpyxl.styles import Font
from setuptools import sic

##create a new excel doc

wb= xl.Workbook()

MySheet =wb.active

MySheet.title = 'First Sheet'

## create a new worksheet 

wb.create_sheet(index=1, title= 'Second Sheet')

#write content to a cell
MySheet['A1']= 'An Ecample of Sum Formula'


# chanfe gont size and italic
MySheet['A1'].font = Font(name= 'Times New Roman', size=24,italic=True, bold= True)

#alternatively u can creat a font object and assign it
fontobject = Font(name= 'Times New Roman', size=24,italic=True, bold= True)


MySheet['A1'].font = fontobject


#adding values to cells
MySheet['B2']= 50
MySheet['B3']= 75
MySheet['B4']= 100



MySheet['A6']= 'Total'

MySheet['A6'].font = Font (size= 19 , bold=True)

MySheet['B6']= '=SUM(B2:B4)'

MySheet.column_dimensions['A'].width = 25









wb.save('PythonToExcel.xlsx')