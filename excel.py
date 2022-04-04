from xlwt import Workbook

wb = Workbook()

lapa1 = wb.add_sheet('Lapa1')

#lapa1.write(rinda,kolonna,dati,stils)

lapa1.write(0,0,'Sveiki')
lapa1.write(1,0,'Sveiki')
lapa1.write(2,0,'Sveiki')
lapa1.write(3,0,'Sveiki')

#wb.save('meginajums.xls')

import xlsxwriter

fails = xlsxwriter.Workbook('meginajums2.xlsx')
lapa = fails.add_worksheet()

lapa.write('A1','Rīga')
lapa.write('C2','Londona')

fails.close()



