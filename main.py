'''
https://github.com/Uberi/speech_recognition/issues/383
https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst

https://acervolima.com/assistente-de-voz-usando-python/
'''

import speech_recognition as sr
import os
import webbrowser
import pyaudio


# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()

    # usando o microfone
    with sr.Microphone() as source:
        # Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        # Frase para o usuario dizer algo
        print("Diga alguma coisa: ")
        # Armazena o que foi dito numa variavele
        audio = microfone.listen(source)

    try:
        # Passa a variável para o algoritmo reconhecedor de padroes
        # frase = microfone.recognize_google(audio, language='pt-BR', show_all=True)
        frase = microfone.recognize_google(audio, language='pt-BR')

        if "navegador" in frase:
            os.system("start Chrome.exe")

        elif "Excel" in frase:
            os.system("start Excel.exe")

        elif 'Televisão' in frase:
            # speak("Here you go to Google\n")
            webbrowser.open("https://www.youtube.com/")

        # Retorna a frase pronunciada
        print("Você disse: " + frase)

    # Se nao reconheceu o padrao de fala, exibe a mensagem
    except StopIteration:
        print("Não entendi")
    return frase


ouvir_microfone()
