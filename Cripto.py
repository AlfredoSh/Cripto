def principal ():
    #Método para limpar consola
    import os
    clear = lambda: os.system('cls')
    #Função Encriptar Mensagem 
    def encriptar():
        clear()
        print('Encriptação de Mensagem... \n\nSelecione o método para encriptar a mensagem: ')
        print('\n1. Importar Mensagem (mensagem.txt) \n2. Digitar Mensagem \n3. Menu Inicial')
        opcao = input()
        #ler mensagem de arquivo
        if (opcao=='1'):
            arquivo = 'mensagem.txt'
            try:
                mensagem = open(arquivo, "r", errors='ignore')               
                mensagem = mensagem.read()
                clear()
                print("\nMesagem importada: ", mensagem)
            except:
                print('Arquivo não encontrado. \n')
                input()
                menu()
        elif (opcao=='2'):
            mensagem = input("Digite a mensagen que deseja criptografar: \n")
        elif (opcao=='3'):
            menu()       
        else: 
            print('Seleção Inválida')
            input()
            encriptar()
        #Inserir Chave
        print('\n1. Para gerar Chave  \n2. Para digitar chave: \n3. Para Menu Inical')
        opcao = input()
        if (opcao=='1'):
            key = randomKey()
        elif (opcao=='2'):
            key = verificador() 
        elif (opcao=='3'):
            menu()
        else: 
            print('Seleção Inválida')
            input()
            menu()
        #Conversão ASCII
        mensagemAscii = [ord(c) for c in mensagem]
        keyAscii = [ord(c) for c in key]
        #Adicionar Indicador na primera posicao
        tamanhoKey = len(keyAscii)
        tamanhoMensagem =len(mensagemAscii)
        indicador=tamanhoKey-tamanhoMensagem
        #Selecção de Algoritmo de Encriptação de acordo ao tamanho
        if (tamanhoKey>tamanhoMensagem):
            #Expandir Mensagem ao mesmo tamanho da key
            for e in mensagemAscii:
                tamanhoMensagem=len(mensagemAscii)
                if (tamanhoMensagem  != tamanhoKey):
                    mensagemAscii.append(e)
            
            #Soma key & Mensagem e sustrae a media da key na Cripto
            mensagemCripto = []
            contador=0
            soma = 0
            for e in keyAscii:
                soma = soma + e
            media = soma / len(keyAscii)
            media = int (media)
            while(contador<tamanhoMensagem):
                soma=keyAscii[contador] + mensagemAscii[contador]
                soma=soma-media
                mensagemCripto.append(soma)
                contador = contador + 1
            mensagemTest = [chr(x) for x in mensagemCripto]
            mensagemString = "".join(mensagemTest)
            #Salvar Arquivo
            file = open("cripto.txt", "w",  encoding="utf-8", errors='ignore')
            file.write(mensagemString)
            file.close()
            clear()
            print ("Mensagem Encriptada: ", mensagemString)
            print('Chave com indicador', str(indicador) + key)
            #print("Chave: ", key)
            print ("\nSua mensagem foi encriptada com sucesso. Mesagem armazenada no arquivo cripto.txt. \n")
            #print('indicador',indicador)
            return menuInicial()
        else:
            #Expandir Key ao mesmo tamanho da mensagem
            for e in keyAscii:
                tamanhoKey=len(keyAscii)
                if (tamanhoMensagem  != tamanhoKey):
                    keyAscii.append(e)
            #Soma key & Mensagem e sustrae a media da key na Cripto
            mensagemCripto = []
            contador=0
            soma = 0
            for e in keyAscii:
                soma = soma + e
            media = soma / len(keyAscii)
            media = int (media)
            while(contador<tamanhoMensagem):
                soma=keyAscii[contador] + mensagemAscii[contador]
                soma=soma-media
                mensagemCripto.append(soma)
                contador = contador + 1
            mensagemTest = [chr(x) for x in mensagemCripto]
            mensagemString = "".join(mensagemTest)
            #Salvar Arquivo
            file = open("cripto.txt", "w",  encoding="utf-8", errors='ignore')
            file.write(mensagemString)
            file.close()
            clear()
            print ("Mensagem Encriptada: ", mensagemString)
            print("Chave: ", key)
            print ("\nSua mensagem foi encriptada com sucesso. Mesagem armazenada no arquivo cripto.txt. \n")
            return menuInicial()
    #Função Desencriptar Mensagem
    def desencriptar (): 
        clear()
        #Leitura da mensagem encriptada
        print('Desencriptar Mensagem... \n\nSelecione o método para encriptar a mensagem: ')
        print('\n1. Importar Criptografia (cripto.txt) \n2. Digitar Cripto \n3. Menu Inical')
        opcao = input()
        if (opcao=='1'):
            clear()
            cripto = open("cripto.txt", "r", encoding="utf-8", errors='ignore')
            cripto = cripto.read()
            print("Mesagem importada: ", cripto)
            key =  input ("Insira a respectiva chave: \n")
        elif (opcao=='2'):
            clear()
            cripto = input("Digite o Cripto: \n")
            key =  input ("Insira a respectiva chave: \n")     
        elif (opcao=='3'):
            menu()       
        else: 
            print('Seleção Inválida')
            input()
            desencriptar()
        #Indicador
        numeros = ['0','1','2','3','4','5','6','7','8','9',]
        indicador=[]
        for e in key:
            for i in numeros:
                if (e==i):
                    indicador.append(e)
                    key=key.replace(e,'')
        if (indicador!=[]):
          indicador="".join(indicador)
          indicador=int(indicador)
        #Conversão ASCII
        mensagemAscii = [ord(c) for c in cripto]
        keyAscii = [ord(c) for c in key]
        tamanhoKey = len(keyAscii)
        tamanhoMensagem =len(mensagemAscii)
        if (tamanhoKey==tamanhoMensagem):
            #criar mensagem do mesmo tamanho da key
            for e in mensagemAscii:
                tamanhoMensagem=len(mensagemAscii)
                if (tamanhoMensagem  != tamanhoKey):
                    mensagemAscii.append(e)
            #Somar key e mensagem
            mensagemCripto = []
            contador=0
            #Calcular media
            soma = 0
            for e in keyAscii:
                soma = soma + e
            media = soma / len(keyAscii)
            media = int (media)
            while(contador<tamanhoMensagem-indicador):
                soma= mensagemAscii[contador] - keyAscii[contador]
                soma=soma+media
                mensagemCripto.append(soma)
                contador = contador + 1
            #Adicionar a cada elemento da mensagem assci e restar
            try:
                mensagemTest = [chr(x) for x in mensagemCripto]
                mensagemDesencriptada = "".join(mensagemTest)
                #save the file
                file = open("decripto.txt", "w", errors="ignore")
                file.write(mensagemDesencriptada)
                file.close()
            # clear()
                print (f"Mensagem Desencriptada: {mensagemDesencriptada}\n ")
                print ("Confira sua mensagem desencriptada:. \nMesagem armazenada no arquivo decripto.txt \n")
            except:
                print('Chave não corresponde.  \n')
                return menuInicial()
        else:
            #criar key do mesmo tamanho da mensagem
            for e in keyAscii:
                tamanhoKey=len(keyAscii)
                if (tamanhoMensagem  != tamanhoKey):
                    keyAscii.append(e)
            #Somar key e mensagem
            mensagemCripto = []
            contador=0
            #Calcular media
            soma = 0
            for e in keyAscii:
                soma = soma + e
            media = soma / len(keyAscii)
            media = int (media)
            while(contador<tamanhoMensagem):
                soma= mensagemAscii[contador] - keyAscii[contador]
                soma=soma+media
                mensagemCripto.append(soma)
                contador = contador + 1
            #Adicionar a cada elemento da mensagem assci e restar
            try:
                mensagemTest = [chr(x) for x in mensagemCripto]
                mensagemDesencriptada = "".join(mensagemTest)
                #save the file
                file = open("decripto.txt", "w", errors="ignore")
                file.write(mensagemDesencriptada)
                file.close()
            # clear()
                print (f"Mensagem Desencriptada: {mensagemDesencriptada}\n ")
                print ("Sua mensagem foi desencriptada com sucesso. \nMesagem armazenada no arquivo decripto.txt \n")
            except:
                print('Chave não corresponde.  \n')
                return menuInicial()
    #Voltar ao Menu
    def menuInicial():
        print('Voltar ao menú incial S/N:')
        opcao = input()
        if (opcao=='s' or opcao=='S'):
            clear()
            principal()
        elif (opcao=='n' or opcao=='N'):
            clear()
            print("Obrigado por utilizar Crypto!")
            input()
        else:
            menuInicial()
    #Generado de Chave aleatoria
    def randomKey():
        import random    
        list = []
        x=0
        print('Digite o tamanho da Key:')
        try:
            tamanhoKey=int(input())
        except:
            print('\nNúmero Inválido!')
            return randomKey()
        if tamanhoKey>2:
            while (x<tamanhoKey):
                item= random.randint(97,122)
                list.append(item)
                x=x+1
            keyAscci = [chr(x) for x in list]
            key = "".join(keyAscci)
            return key
        elif(tamanhoKey<3):
            print ("Chave deve ser maior a tres caracteres.")
            return randomKey()      
    def verificador():
        key =  str (input ("Insira uma chave:" ))
        while len(key)<=2:
            print ("Chave deve ser maior a tres caracteres.")
            key =  str (input ("Insira uma chave:" ))
        i=key[0]
        numeros = ['0','1','2','3','4','5','6','7','8','9',]
        keyAprovada=False
        keyAprovada2=True
        for e in key:
            if e!=i:
                keyAprovada=True
        for j in key:
            for k in numeros:
                if (j==k):
                    keyAprovada2=False
                    break    

        if (keyAprovada and keyAprovada2):
            return key
        else:
            print('Chave não cumpre com os criterios mínimos de segurança.')
            verificador()

    # Sobre Cripto
    def info ():
        clear()
        print ('Cripto faz suas informações mais seguras, utilizando uma encriptação com uma chave simétrica. \n')
        menuInicial()
    #Menu de Opções
    def menu ():
        clear()
        print("\n"
        " .d8888b           d8b          888                \n"   
        "d88P  Y88b         Y8P          888                \n"  
        "888    888         888          888                \n"  
        "888        888d888 888 88888b.  888888  .d88b.     \n" 
        "888        888P    888 888  88b 888    d88  88b    \n"
        "888    888 888     888 888  888 888    888  888    \n"
        "Y88b  d88P 888     888 888 d88P Y88b.  Y88..88P    \n"
        "  Y8888P   888     888 88888P   Y888     Y88P"  "  \n"
        "                       888                         \n"
        "                       888                         \n"
        "                       888                         \n"                   
        "\n")
        print("Escolha uma das opções abaixo: \n")
        print("1. Encriptar Mensagem.")
        print("2. Desencriptar Mensagem.")
        print("3. Sobre Cripto.")
        print("4. Sair.")    
        opcao = input()
        if (opcao=="1"):
            encriptar()
        elif(opcao=="2"):
            desencriptar()
        elif (opcao=="3"):
            info()
        elif(opcao=="4"):
            print("Obrigado por utilizar Crypto!")
            input()
            exit()
        else:
            menu()
    menu()
principal()
