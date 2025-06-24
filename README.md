# Automação de Inserção de Links com PyAutoGUI

Este projeto automatiza o processo de inserção de links em uma interface gráfica utilizando Python e a biblioteca PyAutoGUI.

## Como funciona

O script `app.py` lê uma lista de links do arquivo `links.txt` e, para cada link, executa uma sequência de cliques e digitação simulando a interação do usuário com a interface. As coordenadas dos cliques devem ser ajustadas conforme a posição dos botões na sua tela.

### Passos realizados pelo script:

1. Aguarda 5 segundos para que você posicione a janela correta na tela.
2. Para cada link em `links.txt`:
   - Clica no botão "Adicionar".
   - Clica no botão "YouTube".
   - Clica na caixa de texto.
   - Digita o link.
   - Clica no botão "Inserir".
   - Aguarda 1 segundo entre cada ação.
3. Ao final, exibe "Processo concluído!".

### Como usar

1. Instale as dependências:
   ```zsh
   pip install pyautogui
   ```
2. Adicione os links desejados no arquivo `links.txt`, um por linha.
3. Execute o script:
   ```zsh
   python app.py
   ```
4. Posicione a janela do aplicativo alvo na tela e aguarde a automação.

### Observações

- As coordenadas dos cliques (`x` e `y`) devem ser ajustadas conforme a sua resolução e posição dos botões. Para descobrir as coordenadas, descomente as linhas indicadas no final do `app.py` e siga as instruções no terminal.
- O script foi testado no macOS.

---

Sinta-se à vontade para adaptar o script conforme necessário!