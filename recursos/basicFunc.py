import os, time
import speech_recognition as controladorVoz

recognizer = controladorVoz.Recognizer()
def ouvir():
    with controladorVoz.Microphone() as source:
        print("Diga Algo...")
        print("Fique em silêncio para finalizar!")
        recognizer.adjust_for_ambient_noise(source, duration=3)
        audio = recognizer.listen(source)
        try:
            texto = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {texto}")
            return texto
        except controladorVoz.UnknownValueError:
            print("Não consegui entender o que você disse.")
            return ""
        except controladorVoz.RequestError:
            print("Erro ao se conectar com o servidor!")
            return ""

def limparTela():
    os.system("cls")

def aguardar(segundos):
    time.sleep(segundos)
    
def inicializarBanco():
    try:
        arquivo = open("database.atitus","r")
        bd = arquivo.readlines()
        arquivo.close()
        return bd
    except FileNotFoundError:
        print("Criando novo banco de dados...")
        aguardar(2)
        arquivo = open("database.atitus","w")
        arquivo.close()
        return []