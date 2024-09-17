import subprocess
import sys
import os

def install_dependencies():
    """Instala as dependências usando o pip a partir do arquivo requirements.txt"""
    try:
        # Verifica se o pip está instalado
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
        
        # Instala as dependências do requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar dependências: {e}")
        sys.exit(1)

# Verifica se o arquivo requirements.txt existe
if not os.path.isfile('requirements.txt'):
    print("Arquivo requirements.txt não encontrado. Por favor, crie-o com as dependências necessárias.")
    sys.exit(1)

# Chama a função para instalar as dependências
install_dependencies()

from config.main import main

if __name__ == "__main__":
    main()