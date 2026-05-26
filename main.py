from functions import carregar_arquivo, gerar_pares


'''função que exibe um menu para o usuáro com opções de funcionalidades do programa'''
def menu():
    print("\n ======== MENU ========")
    print("1. Carregar arquivo de publicações")
    print("2. Gerar pares de autores")
    print("3. Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try: 
            nome_arquivo = input("Digite o nome do arquivo: ")
            publicacoes = carregar_arquivo(nome_arquivo)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    elif opcao == "2":
        try:
            for publicacao in publicacoes:
                pares = gerar_pares(publicacao)
            print("Pares de autores gerados com sucesso.")
            
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    elif opcao == "0":
        print("Saindo...")
        exit()
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()