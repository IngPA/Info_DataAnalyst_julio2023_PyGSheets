# https://www.youtube.com/watch?v=A1URtaaA-v0
#tutorial Python y Hojas de calculo de Google Drive 

import gspread

gc = gspread.service_account(filename= 'conexionsheetspython-392422-0a820babdddc.json')

# Abrir por titulo
sh = gc.open('Indexacion proyectos')

# Seleccionar primera hoja
worksheet = sh.get_worksheet(0)

#Introducir datos
worksheet.update('A1', 'dominio')