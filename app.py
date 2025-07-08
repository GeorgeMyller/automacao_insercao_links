import pyautogui
import time

# Leia os links do arquivo
with open('links.txt') as f:
    links = [line.strip() for line in f if line.strip()]


time.sleep(5)  # Tempo para você posicionar o mouse na tela certa
# Itera sobre cada link e executa as ações necessárias
for link in links:
    #mova o mouse e clique no botão "Adicionar"
    pyautogui.click(x=-949, y=548)  # Ajuste as coordenadas do mouse para o botão "Adicionar"
    #espere 1 segundos
    time.sleep(1)
    # Clique no botão do tipo de fonte "YouTube", "Colar Texto" ou "Site"
    pyautogui.click(x=-607, y=902) # Ajuste as coordenadas do mouse para o botão "YouTube"
    #espere 1 segundos
    time.sleep(1)
    #clique na caixa de texto
    pyautogui.click(x=-780, y=785) # Ajuste as coordenadas do mouse para a caixa de texto
    #espere 1 segundos
    time.sleep(1)
    #escreva o link
    pyautogui.write(link)
    #espere 1 segundos
    time.sleep(1)
    #clique no botão "Inserir"
    pyautogui.click(x=-181, y=912) # Ajuste as coordenadas do mouse para o botão "Inserir"
    #espere 1 segundos
    time.sleep(1)
    #mover para a area de fontes para rolar
    pyautogui.moveTo(x=-766, y=559)  # Ajuste as coordenadas do mouse para a área de fontes
    #clicar na area de fontes e rolar para cima
    pyautogui.click(x=-766, y=559)  # Ajuste as coordenadas do mouse para a área de fontes
    #espere 1 segundos
    time.sleep(1)
    # Rolar para cima
    pyautogui.vscroll(90)  # Rolar para cima
    #espere 1 segundos
    time.sleep(1)

"""


#Para identificar a posição do mouse, descomente a linha abaixo e execute o script
print("Posicione o mouse sobre o botão.")
time.sleep(5)  # Tempo para você posicionar o mouse na tela certa
print(pyautogui.position())# Ajuste a posição do mouse para o botão "Adicionar"

"""

print("Processo concluído!")