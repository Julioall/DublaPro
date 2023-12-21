import os
from elevenlabs import generate
from googletrans import Translator

def traduzir_para_portugues(texto):
    translator = Translator()
    traducao = translator.translate(texto, dest='pt')
    return traducao.text

def dividir_texto(texto, max_caracteres=2500):
    partes = [texto[i:i + max_caracteres] for i in range(0, len(texto), max_caracteres)]
    return partes

def gerar_audios_elevenlabs(pasta_resultados, pasta_audios, api_key_elevenlabs):
    # Lista de arquivos na pasta de resultados
    lista_arquivos = os.listdir(pasta_resultados)

    # Itera sobre os arquivos de texto e gera os áudios correspondentes
    for nome_arquivo in lista_arquivos:
        caminho_arquivo_texto = os.path.join(pasta_resultados, nome_arquivo)

        if os.path.isfile(caminho_arquivo_texto) and nome_arquivo.endswith(".txt"):
            # Lê o texto do arquivo
            with open(caminho_arquivo_texto, "r", encoding="utf-8") as arquivo_texto:
                texto = arquivo_texto.read()

            # Traduz o texto para o português
            texto_portugues = traduzir_para_portugues(texto)

            # Divide o texto em partes menores
            partes_texto = dividir_texto(texto_portugues)

            # Gera áudio para cada parte
            for i, parte_texto in enumerate(partes_texto, start=1):
                # Gera o áudio usando elevenlabs com autenticação
                audio = generate(text=parte_texto, voice="Daniel", model="eleven_multilingual_v2",
                                 api_key=api_key_elevenlabs)

                # Define o caminho para salvar o arquivo de áudio
                caminho_arquivo_audio = os.path.join(pasta_audios,
                                                     f"{os.path.splitext(nome_arquivo)[0]}_parte_{i}.mp3")

                # Salva o áudio
                with open(caminho_arquivo_audio, "wb") as arquivo_audio:
                    arquivo_audio.write(audio)

                print(f"Áudio para {nome_arquivo}, parte {i} gerado com sucesso em {caminho_arquivo_audio}")
        else:
            print(f"Arquivo {nome_arquivo} não encontrado ou não é um arquivo de texto.")

    print("Processo concluído.")

if __name__ == "__main__":
    # Diretório onde os resultados estão salvos
    pasta_resultados = "segmentos\\resultados"

    # Chave da API da Eleven Labs
    api_key_elevenlabs = "99afa3f65b927bbd17184fcfa33dc79a"  # Substitua com sua chave

    # Diretório para salvar os áudios gerados
    pasta_audios = os.path.join(pasta_resultados, "audios_elevenlabs")
    os.makedirs(pasta_audios, exist_ok=True)

    # Chama a função para gerar os áudios usando Eleven Labs
    gerar_audios_elevenlabs(pasta_resultados, pasta_audios, api_key_elevenlabs)
