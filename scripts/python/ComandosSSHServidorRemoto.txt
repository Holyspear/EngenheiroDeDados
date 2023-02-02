import paramiko
import time
#----------------------------------Parametros de conexão----------------------------------
servidor = "portifolio.com"
usuario = "holyspear"
senha = "showtimes!"
porta = "77"

#----------------------------------Conexão SSH com servidor-------------------------------
conssh = paramiko.SSHClient()
conssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conssh.connect(servidor, porta, usuario, senha)

#----------------------------------Lista de comandos a serem executados-------------------
comandos = ["ls",
            "pwd"
            ]

#----------------------------------Cria uma instância de conexão--------------------------
sessao = conssh.invoke_shell()

time.sleep(1) 
sessao.recv(9999999999)
sessao.send("\n")
time.sleep(1)

#----------------------------------Executa os comandos e gera OUTPUT---------------------
for comando in comandos:
    sessao.send(comando + "\n")
    while not sessao.recv_ready(): 
        time.sleep(1)
    time.sleep(1) 
    saida = sessao.recv(9999999999) 
    saidatStr = saida.decode('utf-8')
    print(saidatStr)
    time.sleep(1)
sessao.close()