import pyautogui
import csv
import time

print("******REGISTRO DE CONTRATOS********")

with open('data/data.txt',newline='') as csvfile:
  data = list(csv.reader(csvfile))

for valor in data:
  print(valor[0])

  pyautogui.click('screenshot/button_codmod.png')
  pyautogui.write(valor[0])

  pyautogui.click('screenshot/buscar.png')

 # validar_nuevo = pyautogui.locateOnScreen('nuevo.png')
  try:
    pyautogui.click('screenshot/nuevo.png')
  except:
    pyautogui.click('screenshot/nuevo1.png')

  time.sleep(2)
  
  try:
    validar_acm = pyautogui.locateOnScreen('screenshot/p_registroacm.png')
    pyautogui.click('screenshot/cerrar_acm.png')
    pyautogui.doubleClick('screenshot/limpiar_texto.png')
    pyautogui.press('delete')
  except:
    pyautogui.click('screenshot/cod_nexus.png')
    pyautogui.write(valor[1])

    pyautogui.click('screenshot/validar_nexus.png')
    time.sleep(2)

    
    try:
      validar_diten = pyautogui.locateOnScreen('screenshot/validar_diten.png')
      pyautogui.click('screenshot/cerrar_validar_diten.png')
      pyautogui.click('screenshot/cerrar_registro.png')
      pyautogui.doubleClick('screenshot/limpiar_texto.png')
      pyautogui.press('delete')
    except:
      print("registro")
      pyautogui.click('screenshot/doc_referencia.png')
      pyautogui.write(valor[2])
      pyautogui.press('tab')
      pyautogui.write(valor[3])
      pyautogui.press('tab',presses=2)
      pyautogui.write(valor[4])
      pyautogui.press('tab',presses=2)
      pyautogui.write(valor[5])
      pyautogui.write(valor[6])
      pyautogui.press('tab',presses=2)
      pyautogui.write(valor[7])
      pyautogui.press('tab')
      pyautogui.write(valor[8])
      pyautogui.press('tab')
      pyautogui.write(valor[9])
      pyautogui.press('tab',presses=5)
      pyautogui.keyDown('shift')
      pyautogui.write(valor[10])
      pyautogui.press('tab',presses=20)
      pyautogui.write(valor[11])
      pyautogui.press('tab',presses=3)
      pyautogui.write(valor[12])
      pyautogui.press('tab')
      pyautogui.press('delete',presses=3)
      pyautogui.write(valor[13])
      pyautogui.press('tab',presses=2)
      pyautogui.write(valor[14])
      pyautogui.click('screenshot/cerrar_registro.png')
      pyautogui.doubleClick('screenshot/limpiar_texto.png')
      pyautogui.press('delete')
    