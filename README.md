# DublaPro

**DublaPro** é um projeto em desenvolvimento que visa simplificar o processo de dublagem de áudios de um idioma para outro. A aplicação utiliza diversas tecnologias, como reconhecimento de fala, tradução automática e síntese de voz para criar dublagens em um novo idioma.

## Funcionalidades

- **Transcrição de Áudio**: Utilizando tecnologias de reconhecimento de fala, o projeto transcreve áudios em um idioma específico.
  
- **Tradução Automática**: Os textos transcritos são traduzidos automaticamente para o idioma desejado.

- **Síntese de Voz**: Com base nos textos traduzidos, são gerados áudios dublados no novo idioma.

## Como Usar

1. **Configuração do Ambiente**: Certifique-se de ter todas as dependências instaladas. Utilize o arquivo `requirements.txt` para configurar o ambiente com o comando:

    ```bash
    pip install -r requirements.txt
    ```

2. **Divisão de Áudios (Opcional)**: Se desejar dividir seus áudios em segmentos menores, utilize a função `dividir_audio` fornecida.

3. **Transcrição e Tradução**: Execute o script para transcrever e traduzir os áudios, gerando arquivos de texto correspondentes.

4. **Dublagem**: Utilize o script para gerar áudios dublados com base nos arquivos de texto traduzidos.

## Exemplos de Uso

- Dividindo um áudio em segmentos de 1 minuto:

    ```bash
    python dividir_audio.py
    ```

- Transcrevendo e traduzindo áudios:

    ```bash
    python transcrever_traduzir.py
    ```

- Gerando áudios dublados:

    ```bash
    python dublar_audio.py
    ```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar solicitações de pull (pull requests).

## Notas

Este projeto ainda está em desenvolvimento, e novas funcionalidades podem ser adicionadas. Certifique-se de verificar as atualizações frequentemente.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
