def principal ():
    #Método para limpar consola
    import os
    clear = lambda: os.system('cls')
    barraLonga='\n________________________________________________________\n'
    criptoLogo = ("""
          .d8888b           d8b          888                
         d88P  Y88b         Y8P          888                
         888    888         888          888                
         888        888d888 888 88888b   888888   d88b      
         888        888P    888 888  88b 888    d88  88b    
         888    888 888     888 888  888 888    888  888    
         Y88b  d88P 888     888 888 d88P Y88b   Y88  88P    
           Y8888P   888     888 88888P   Y888     Y88P 
                                888                         
                                888                         
                                888
        \n""")
    print(criptoLogo)
    print( 'Qual seu nome?')
    nome=input()
    clear()
    print(f'{criptoLogo}\n{nome}, Qual seu e-mail?')
    email=input()
    clear()
    #Função Encriptar Mensagem 
    def encriptar():        
        clear()
        assunto=  'Codificada'
        print(f'{criptoLogo}  {barraLonga}                 Codificar Mensagem {barraLonga}')
        print('Escolha uma opção abaixo:\n \n1. Importar a mensagem desde um arquivo (mensagem.txt) \n2. Digitar a mensagem \n3. Menu Inicial')
        opcao = input()
        #ler mensagem de arquivo
        if (opcao=='1'):
            arquivo = 'mensagem.txt'
            try:
                mensagem = open(arquivo, "r", encoding="utf-8", errors='ignore')               
                mensagem = mensagem.read()
                print(barraLonga, 'Mensagem Encontrada: \n', mensagem, barraLonga)
            except:
                print('Arquivo não encontrado. Nome do arquivo deve ser mensagem.txt \n')
                menuInicial()
                exit()
        elif (opcao=='2'):
            print(f'{barraLonga}')
            mensagem = input("Digite a mensagem: \n")
            print(barraLonga)
        elif (opcao=='3'):
            menu()       
        else: 
            print('Seleção Inválida. Presione ENTER para continuar')
            input()
            encriptar()
        #Inserir Chave
        print('\nEscolha uma opção abaixo para escolher a chave: \n')
        print('\n1. Gerar a chave aleatória  \n2. Digitar a chave: \n3. Menu Inical')
        opcao = input()
        if (opcao=='1'):
            key = randomKey()
        elif (opcao=='2'):
            key = verificador() 
        elif (opcao=='3'):
            menu()
        else: 
            print('Seleção Inválida. Presione ENTER para continuar')
            input()
            menu()
        
        #Conversão ASCII
        mensagemAscii = [ord(c) for c in mensagem]
        keyAscii = [ord(c) for c in key]
        #Adicionar Indicador na primera posicao
        tamanhoKey = len(keyAscii)
        tamanhoMensagem =len(mensagemAscii)
        indicador=tamanhoKey-tamanhoMensagem
        if (tamanhoKey==tamanhoMensagem):
            print('Tamanho da chave é incompativel com mensagem \n')
            menuInicial()
        #Selecção de Algoritmo de Encriptação de acordo ao tamanho
        elif (tamanhoKey>tamanhoMensagem):
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
            file = open("Mensagem Codificada.txt", "w",  encoding="utf-8", errors='ignore')
            file.write(mensagemString)
            file.close()
            keyExpandida= str(indicador) + key
            keyArquivo = open("Chave.txt", "w", errors="ignore")
            keyArquivo.write(keyExpandida)
            keyArquivo.close()
            clear() 
            print (f" {criptoLogo} {barraLonga}Mensagem Codificada: \n {mensagemString} {barraLonga}")
            print('Atento a sua chave: \n', str(indicador) + key, barraLonga)
            #print("Chave: ", key)
            print (f"{criptoLogo}Sua   mensagem foi codificada com sucesso. Mensagem codificada e chave armazenados no disco como arquivos. \n")
            enviarEmail(mensagem, mensagemString,key,nome,email,assunto)
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
            file = open("Mensagem Codificada.txt", "w",  encoding="utf-8", errors='ignore')
            file.write(mensagemString)
            file.close()
            keyArquivo = open("Chave.txt", "w", errors="ignore")
            keyArquivo.write(key)
            keyArquivo.close()
            clear()
            print (f"{criptoLogo} Sua mensagem foi codificada com sucesso e armazenada no arquivo Mensagem Codificada.txt. \n")
            print(f' {barraLonga} Mensagem Codificada:  {mensagemString} {barraLonga} Chave: {key} {barraLonga}')
            enviarEmail(mensagem, mensagemString,key,nome,email,assunto)
            return menuInicial()
    #Função Desencriptar Mensagem
    def desencriptar ():
        assunto=  'Decodificada'
        clear()
        keyArquivo = open("Chave.txt", "r", encoding="utf-8", errors='ignore')
        keyArquivo = keyArquivo.read()
        #Leitura da mensagem encriptada
        print(f'{criptoLogo} \n {barraLonga}                Decodificar Mensagem\n {barraLonga}')
        print('\n1. Importar Mensagem Codificada (Mensagem Codificada.txt) \n2. Digitar mensagem Codificada \n3. Menu Inical')
        opcao = input()
        if (opcao=='1'):
            clear()
            cripto = open("Mensagem Codificada.txt", "r", encoding="utf-8", errors='ignore')
            cripto = cripto.read()
            print(f'{criptoLogo} {barraLonga} Mensagem importada: {cripto} {barraLonga}')
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
                file = open("Mensagem Decodificada.txt", "w", errors="ignore")
                file.write(mensagemDesencriptada)
                file.close()
                clear()
                print(f'{criptoLogo}{barraLonga} Mensagem Deodificada:  {mensagemDesencriptada} {barraLonga}')          
                print ("Confira sua mensagem decodificada!. Mensagem aramazenada no arquivo Mensagem Decodificada.txt \n")
                enviarEmail(cripto, mensagemDesencriptada,key,nome,email,assunto)
                menuInicial()
            except:
                print('Chave é incompátivel.  \n')
                menu()
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
                file = open("Mensagem Decodificada.txt", "w", errors="ignore")
                file.write(mensagemDesencriptada)
                file.close()
                clear()
                print(f'{criptoLogo} {barraLonga} Mensagem Deodificada:  {mensagemDesencriptada} {barraLonga}')          
                print ("Confira sua mensagem decodificada!. Mensagem aramazenada no arquivo Mensagem Decodificada.txt \n")
                enviarEmail(cripto, mensagemDesencriptada,key,nome,email,assunto)
                menuInicial()
            except:
                print('Chave não corresponde.  \n')
                return menuInicial()
        
    #Voltar ao Menu
    def menuInicial():
        print('Voltar ao menú incial S/N:')
        opcao = input()
        if (opcao=='s' or opcao=='S'):
            clear()
            menu()
        elif (opcao=='n' or opcao=='N'):
            clear()
            print("Obrigado por utilizar Cripto!")
            input()
        else:
            menu()
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
        if tamanhoKey>2 and tamanhoKey<33:
            while (x<tamanhoKey):
                item= random.randint(97,122)
                list.append(item)
                x=x+1
            keyAscci = [chr(x) for x in list]
            key = "".join(keyAscci)
            return key
        elif(tamanhoKey<3 or tamanhoKey>32):
            print ("Tamanho da chave incompátivel.")
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
            print('\nChave não cumpre com os criterios mínimos de segurança. \n')
            print('1. A chave não pode ter todos os caracteres iguais \n2. A chave não pode ter números\n')
            return verificador()

    # Sobre Cripto
    def info ():
        clear()
        print(f'{criptoLogo} \n {barraLonga} Atividades Praticas Supervisionadas | Universidade Paulista \n')
        print ('\nCripto codifica e decodifica mensagems com foco na segurança da informação.')
        print('O nivel de segurança é proporcional ao tamanho da respectiva chave.', barraLonga)
        menuInicial()
    def enviarEmail(mensagem, mensagemString,key, nome,email,assunto):
        try:
            import smtplib, ssl
            from email.mime.text import MIMEText as text
            assunto
            port = 587  # For starttls
            smtp_server = "smtp.gmail.com"
            sender_email = "cripto.projectunip@gmail.com"
            receiver_email = email
            print('Enviando informações a ', email)
            password = 'criptoproject'
            message = f"""Subject: Parabens! Mensagem {assunto}

            Olá {nome},

            Sua mensagem foi {assunto} com sucesso:

            Mensagem Original:   {mensagem}
            Mensagem {assunto}: {mensagemString}
            Chave: {key}


            Abraços,

            A equipe de Cripto
            https://github.com/AlfredoSh/Cripto

            """
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.encode('utf8'))
                message.encode("utf8") 
            print('Informações enviadas!')
        except:
            print('Informações não enviadas!')
    #Menu de Opções
    def menu ():
        clear()
        print(criptoLogo)
        print(barraLonga, 'Codifica e decodifica uma mensagem com Cripto', barraLonga)
        print('Escolha uma das opções abaixo: \n ')
        print("1. Codificar Mensagem \n2. Decodificar Mensagem \n3. Sobre Cripto \n4. Sair")    
        opcao = input()
        if (opcao=="1"):
            encriptar()
        elif(opcao=="2"):
            desencriptar()
        elif (opcao=="3"):
            info()
        elif(opcao=="4"):
            print("Obrigado por utilizar Cripto!")
            input()
            exit()
        else:
            print('Seleção Inválida. Presione ENTER para continuar')
            input()
            menu()
    menu()
principal()
