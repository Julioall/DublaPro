import os
import speech_recognition as sr

def transcrever_audio(caminho_arquivo_audio):
    recognizer = sr.Recognizer()

    with sr.AudioFile(caminho_arquivo_audio) as arquivo_audio:
        audio = recognizer.record(arquivo_audio)

    try:
        # Utiliza o Sphinx para transcrever o áudio
        texto = recognizer.recognize_google(audio, language="en-US")
        return texto
    except sr.UnknownValueError:
        print(f"Não foi possível transcrever o áudio {caminho_arquivo_audio}. Áudio vazio ou inaudível.")
        return ""
    except sr.RequestError as e:
        print(f"Erro na requisição ao serviço de reconhecimento de fala: {e}")
        return ""

def mostrar_progresso(atual, total):
    progresso = (atual / total) * 100
    print(f"Progresso: {atual}/{total} ({progresso:.2f}%)")

def transcrever_segmentos(diretorio_segmentos, pasta_resultados):
    # Cria a pasta de resultados se ela não existir
    os.makedirs(pasta_resultados, exist_ok=True)

    # Obtém a lista de arquivos na pasta de segmentos
    lista_arquivos = os.listdir(diretorio_segmentos)

    # Itera sobre os arquivos de áudio e realiza a transcrição
    total_segmentos = len(lista_arquivos)
    for i, nome_arquivo in enumerate(lista_arquivos, 1):
        caminho_arquivo = os.path.join(diretorio_segmentos, nome_arquivo)

        if os.path.isfile(caminho_arquivo):
            texto_transcrito = transcrever_audio(caminho_arquivo)

            if texto_transcrito:
                # Cria um arquivo de texto com o mesmo nome do áudio
                caminho_resultado = os.path.join(pasta_resultados, f"{nome_arquivo}.txt")
                with open(caminho_resultado, "w", encoding="utf-8") as arquivo_resultado:
                    arquivo_resultado.write(texto_transcrito)
                print(f"Transcrição para {nome_arquivo} criada com sucesso!")
            else:
                print(f"Falha na transcrição para {nome_arquivo}.")
        else:
            print(f"Arquivo {nome_arquivo} não encontrado.")

        mostrar_progresso(i, total_segmentos)

    print(f"Resultados salvos em {pasta_resultados}")

if __name__ == "__main__":
    # Diretório onde os segmentos de áudio estão localizados
    diretorio_segmentos = os.path.join(os.path.dirname(os.path.abspath(__file__)), "segmentos")

    # Diretório para salvar os resultados
    pasta_resultados = os.path.join(diretorio_segmentos, "resultados")

    # Chama a função para transcrever os segmentos
    transcrever_segmentos(diretorio_segmentos, pasta_resultados)
