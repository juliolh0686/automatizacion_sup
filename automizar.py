from PyPDF2 import PdfReader
import os
import csv

contenido = os.listdir('documentos')

# headers = ['id', 'username', 'email']
# users = [
#     ['1', 'user1', 'user1@pywombat.com'],
#     ['2', 'user2', 'user2@pywombat.com'],
#     ['3', 'user3', 'user3@pywombat.com'],
#     ['4', 'user4', 'user3@pywombat.com'],
# ]

# with open('users.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow( headers) # Creamos las columnas

#     for user in users:
#         writer.writerow(user)

for elemento in contenido:
  ###CODIGO PARA LEER ARCHIVO PDF
  reader = PdfReader("documentos/"+elemento)

  text = ''
  #####leer varias paginas###
  # for num in range(len(reader.pages)):
  #   page = reader.pages[num]
  #   text += page.extract_text()
  
  ###Leer una pagina###
  text = reader.pages[1].extract_text()

  text = text.replace("\n","")

  pos_apellidos_nombres = text.find('DATOS PERSONALES::')
  pos_doc = text.find('D.N.I.')

  apellidos_nombres = text[pos_apellidos_nombres+20:pos_doc-10]
  apellidos_nombres.strip()

  # if apellidos_nombres.replace(" ", "") == "" :
  #   pos_apellidos_nombres = text.find('PENSIONARIOCUISSP:')
  #   pos_doc = text.find('D.N.I.')

  # if apellidos_nombres.replace(" ", "") == "" :
  #   pos_apellidos_nombres = text.find('ADJUDICACION :')
  #   pos_doc = text.find('D.N.I.')

    # apellidos_nombres = text[pos_apellidos_nombres+19:pos_doc-1]
    # apellidos_nombres.strip()

  #print(text)
  print(apellidos_nombres)
  #print(text)
  #print("-----------------------")

