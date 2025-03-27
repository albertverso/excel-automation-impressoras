import logging
import traceback
import os

# Obtém o diretório raiz do script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define o caminho do log dentro da raiz do projeto
log_file = os.path.join(BASE_DIR, 'log.txt')

# Configuração do logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p',
    filemode='a'
)


def main():
    try:
        logging.info("Iniciando o programa...")
        print("Iniciando o programa...")
        # Seu código principal aqui
        from config.gui import create_gui
        create_gui()
    except Exception: 
        error = traceback.format_exc()
        logging.error(error)
        print(error)
    finally:
        logging.info("Fim do programa.")
        print("Fim do programa.")

if __name__ == "__main__":
    main()