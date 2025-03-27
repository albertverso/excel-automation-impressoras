import logging
import traceback

logging.basicConfig(
        filename='C:\\Users\\carlos.filho\\Projects\\excel-automation-impressoras\\log.txt',
        level=logging.INFO, 
        format=' %(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d/%m/%Y %I:%M:%S %p',filemode='a')

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