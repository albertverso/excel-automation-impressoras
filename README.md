# Automação de Planilha de Impressão para ACFOR
 ## Descrição do Projeto
  - Este projeto foi desenvolvido para automatizar o processo de organização e separação de uma planilha de impressão utilizada pela ACFOR. Ele realiza o processamento mensal dos dados de impressão de toda a empresa, filtrando as colunas mais importantes, somando e exibindo os totais relevantes de páginas coloridas e em preto e branco. O objetivo é facilitar e acelerar a análise mensal desses dados de impressão.

 ## Funcionalidades
 ### Seleção de Arquivo CSV:

 - O projeto permite ao usuário selecionar um arquivo CSV contendo as informações de impressão. Através de uma interface gráfica, o usuário pode  facilmente escolher o arquivo a ser processado.
### Filtragem de Colunas:
- Somente as colunas essenciais, como Nome Completo, Páginas Coloridas, Páginas Preto e Branco e Data de Impressão, são extraídas e processadas.
  
### Processamento de Datas:
- O usuário pode fornecer uma data inicial e/ou final para filtrar os dados de impressão no intervalo desejado.
- Caso o usuário não forneça datas, o sistema considera todas as entradas de impressão.
  
### Cálculos e Totalizações:
- O sistema soma o total de páginas coloridas e em preto e branco para cada colaborador e calcula o total geral.
- Uma linha de total é adicionada ao final da planilha para facilitar a visualização do total de páginas impressas.
  
### Saída em Excel:
- O resultado é salvo em um arquivo Excel formatado, contendo bordas e estilos adequados para uma visualização clara e organizada dos dados.
  
### Criação Automática de Diretório:
- O arquivo Excel gerado é salvo automaticamente em uma pasta chamada salvos. Caso essa pasta não exista, ela será criada pelo programa.

## Dependências

### Este projeto requer as seguintes bibliotecas:
- pandas
- openpyxl
- tkinter (nativo no Python)
  
## Instalação
### Clone o repositório para o seu diretório local:
````
git clone https://github.com/usuario/projeto-acfor.git
````

## Execução
 - Para rodar o projeto, utilize o arquivo app.py localizado no diretório raiz. Este arquivo irá garantir que as dependências sejam instaladas automaticamente e que a interface gráfica seja inicializada.
````
python app.py
````

## Estrutura do Projeto
````
.
├── config
│   ├── gui.py        # Interface gráfica (Tkinter)
│   ├── logic.py      # Lógica de processamento de dados
│   └── main.py       # Função principal para executar a lógica
├── app.py            # Arquivo de entrada que executa o projeto
├── requirements.txt  # Dependências do projeto
└── README.md         # Documentação do projeto
````

## Licença
- Este projeto é de uso interno e foi desenvolvido exclusivamente para a ACFOR.
- Este sistema foi desenvolvido com o intuito de melhorar o processo de coleta e análise de dados de impressão, reduzindo o tempo de trabalho manual e garantindo uma maior precisão nas totalizações mensais.
