'''
Modulo para trabalhar em conjunto com a API Json Implementada no Arduino.
Por aqui voce consegue receber os dados e trata-los como
Objetos Json, ou seja, Dicionarios onde cada key e uma porta do arduino
e seu conteudo e o valor daquela porta...

Escrito por: Gabriel Rodrigues de Azeredo
Data: 17/10/2016
'''
import requests
import json
import serial
import serialenum
import time

def identificar_seriais():
    #Retorna uma List em que cada item corresponde a um dispositivo serial
    return serialenum.enumerate()

def json_ethernet(ip):
    #Retorna um Dicionario em que cada Key corresponde a uma porta diferente do Arduino
    #Tanto as Keys quantos seus feedbacks podem ser modificados, modificando diretamente a API escrito no Arduino

    r = requests.get("http://"+ip+"/json") #Cria uma variavel 'r' que envia uma requisicao Get para o endereco de IP do Arduino
    #no endereco /json, que foi implementado diretamente na API escrita no Arduino
    #'r' nesse caso vai receber o conteudo do endereco /json

    if r.status_code == 200: #Faz uma verificacao caso ele tenha obtido sucesso na requisao, ja que em html o codigo '200' significa Sucesso!
        dados = json.loads(r.content)#Cria uma variavel dados que recebe o produto da funcao json.loads, que por sua vez recebe o content de 'r'
        return dados #Retorna o dicionario com o objeto Json


def json_serial(porta, bauld_rate):
    ser = serial.Serial(porta, bauld_rate, timeout=1) #Inicia a comunicacao serial
    time.sleep(1.5) #Implementa um delay entre o estabelicimento da comunicacao e o envio do primeiro caractere
    #Para compensar o tempo de boot do arduino, ja que a cada nova conexao serial o arduino reinicia

    ser.write('!') #Envia o caractere '!' para o arduino, ja que esse caractere da start na funcao feedback que esta
    #gravada no firmware do arduino

    time.sleep(0.5) #Implementa um novo delay para compensar o tempo que o arduino escreve na serial
    dados = ser.readline()#Cria uma variavel dados que recebe os dados da serial em formato string
    dados_json = json.loads(dados)#Cria uma variavel dados_json que transforma a string recebida em um objeto Json

    return dados_json #Retorna um dicionario para ser usado






#-----------------------------------Exemplos de Uso das Funcoes--------------------------------------------------

#Exemplo: Retorna uma List em que cada item corresponde a um dispositivo diferente na serial
#print(identificar_seriais())

#Exemplo: Recebendo dados Json via EthernetShield
#print(json_ethernet("10.0.0.177"))

#Exemplo: Recebendo dados Json via Serial
#print(json_serial('/dev/ttyUSB1', 9600))
