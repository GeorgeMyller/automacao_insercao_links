import pyautogui
import time

# Leia os links do arquivo
with open('links.txt') as f:
    links = [line.strip() for line in f if line.strip()]



time.sleep(5)  # Tempo para você posicionar o mouse na tela certa

for link in links:
    #mova o mouse e clique no botão "Adicionar"
    pyautogui.click(x=-606, y=627)  # Ajuste as coordenadas conforme
    #espere 1 segundos
    time.sleep(1)
    # Clique no botão "YouTube"
    pyautogui.click(x=-501, y=972)
    #espere 1 segundos
    time.sleep(1)
    #clique na caixa de texto
    pyautogui.click(x=-619, y=720)
    #escreva o link
    pyautogui.write(link)
    #espere 1 segundos
    time.sleep(1)
    #clique no botão "Inserir"
    pyautogui.click(x=-227, y=1064)
    #espere 1 segundos
    time.sleep(1)

time.sleep(5)  # Tempo para você posicionar o mouse na tela certa
print(pyautogui.position())# Ajuste a posição do mouse para o botão "Adicionar"



print("Processo concluído!")