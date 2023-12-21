from pydub import AudioSegment
import os

def juntar_audios(pasta_audios, caminho_saida):
    # Obtém a lista de arquivos na pasta de áudios
    lista_arquivos = sorted(os.listdir(pasta_audios))

    # Inicializa um áudio vazio
    audio_combinado = AudioSegment.silent(duration=0)

    for nome_arquivo in lista_arquivos:
        caminho_arquivo = os.path.join(pasta_audios, nome_arquivo)

        if os.path.isfile(caminho_arquivo) and nome_arquivo.endswith(".mp3"):
            # Lê o áudio do arquivo
            audio_parte = AudioSegment.from_file(caminho_arquivo)

            # Adiciona o áudio à composição
            audio_combinado += audio_parte

    # Salva o áudio combinado
    audio_combinado.export(caminho_saida, format="mp3")
    print(f"Áudios combinados e salvos em: {caminho_saida}")

if __name__ == "__main__":
    # Pasta onde os áudios foram gerados
    pasta_audios = "segmentos\\audios_elevenlabs"

    # Caminho de saída para o áudio combinado
    caminho_saida = "audio_combinado.mp3"

    # Chama a função para juntar os áudios
    juntar_audios(pasta_audios, caminho_saida)
