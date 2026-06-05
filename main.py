import pandas as pd
import pyautogui
import sys

def main():
    print("Olá! Seu ambiente Python está configurado.")
    print(f"Versão do Python: {sys.version}")
    
    # Exemplo simples com Pandas
    data = {'Ferramenta': ['Pandas', 'PyAutoGUI', 'PyInstaller'], 
            'Status': ['Instalado', 'Instalado', 'Instalado']}
    df = pd.DataFrame(data)
    print("\nBibliotecas instaladas:")
    print(df)

    print("\nPara criar um .exe deste script, use o comando:")
    print("pyinstaller --onefile main.py")

if __name__ == "__main__":
    main()
