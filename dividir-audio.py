from pydub import AudioSegment
import os
import warnings

def dividir_audio(caminho_audio, duracao_segmento_minutos, pasta_saida):
    # Cria a pasta de saída se ela não existir
    os.makedirs(pasta_saida, exist_ok=True)

    audio = AudioSegment.from_file(caminho_audio)
    duracao_segmento_milissegundos = duracao_segmento_minutos * 60 * 1000

    for i, segmento in enumerate(audio[::duracao_segmento_milissegundos]):
        caminho_saida = os.path.join(pasta_saida, f"segmento_{i + 1}.wav")
        segmento.export(caminho_saida, format="wav")
        print(f"Segmento {i + 1}: {caminho_saida} criado com sucesso!")

if __name__ == "__main__":
    # Obtém o diretório do script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Especifique o caminho do FFmpeg em relação ao diretório do script
    caminho_ffmpeg = os.path.join(script_dir, 'ffmpeg')  # Substitua 'ffmpeg' pelo nome real do executável se necessário

    # Adicione o caminho do FFmpeg ao PATH
    os.environ["PATH"] += os.pathsep + os.path.dirname(caminho_ffmpeg)

    # Caminho do arquivo de áudio
    caminho_audio = "D:\\Arquivos\\Repositorios\Dublador\\audio.mp3"

    # Duração desejada para cada segmento (em minutos)
    duracao_segmento_minutos = 1

    # Pasta de saída para os segmentos
    pasta_saida = "segmentos"

    # Chama a função para dividir o áudio
    dividir_audio(caminho_audio, duracao_segmento_minutos, pasta_saida)
