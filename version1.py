#!/usr/bin/python3

import argparse

def main():
    parser = argparse.ArgumentParser()#description='Exemplo de programa com argumento -v')
    
    # Adiciona a opção "-v" que é do tipo store_true (booleano)
    parser.add_argument('-v', '--version', action='store_true', help='Shows the version')
    
    args = parser.parse_args()
    
    # Verifica se a opção "-v" foi fornecida
    if args.version:
        print("Versão 1")
    else:
        print("Programa principal aqui...")

if __name__ == "__main__":
    main()




