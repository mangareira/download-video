# VIDEOS DOWNLOADER FROM YOUTUBE AND PANDAS VIDEOS

## Pandas Videos Downloader

Este é um script simples em Python, utilizando `tkinter` para interface gráfica, que permite o download de vídeos de uma fonte m3u8 usando o **FFmpeg**. 

### Funcionalidades
- Interface gráfica com campos para inserir URL do arquivo m3u8, nome do arquivo de saída e referer.
- Download de vídeos utilizando a ferramenta **FFmpeg**.
- Exibe mensagens informativas quando o download é concluído ou caso algum campo esteja vazio.

### Requisitos

Antes de executar o script, você precisa ter os seguintes componentes instalados:

- **Python 3.x**
- **Tkinter** (incluído em muitas distribuições Python, mas pode ser necessário instalar)
- **FFmpeg** (instalável em [FFmpeg.org](https://ffmpeg.org/download.html))
  
Certifique-se também de que o FFmpeg esteja disponível no seu `PATH`, de forma que possa ser executado diretamente via linha de comando.

### Instalação do FFmpeg

1. Acesse o [site do FFmpeg](https://ffmpeg.org/download.html) e baixe a versão compatível com seu sistema operacional.
2. Extraia o conteúdo e adicione o diretório `bin` ao `PATH` do sistema.
3. Verifique a instalação executando `ffmpeg` em um terminal.

### Como usar

1. Clone este repositório ou copie o código para um arquivo Python.
2. Execute o script Python:
   ```bash
   python app_pandas_video.py
   ```
3. Uma janela será exibida com três campos:
   - **URL do arquivo m3u8**: Cole o link do arquivo m3u8 que deseja baixar.
   - **Nome do arquivo de saída**: Defina o nome que deseja dar ao vídeo (inclua a extensão, ex: `video.mp4`).
   - **Referer**: O cabeçalho referer necessário para autenticação do vídeo.

4. Clique em **Download** para iniciar o processo. O vídeo será salvo no mesmo diretório em que o script está localizado.

### Exemplo de uso

- **URL do arquivo m3u8**: `https://b-vz-c78d6445-599.tv.pandavideo.com.br/"randon uuid"/playlist.m3u`
- **Nome do arquivo de saída**: `video name`
- **Referer**: `https://player-vz-c78d6445-599.tv.pandavideo.com.br`

![reference image](https://github.com/mangareira/download-video/blob/main/reference.png)

### Observações

- Este script foi projetado para uso pessoal e educacional. Respeite os direitos autorais dos vídeos que deseja baixar.
- Verifique as políticas de acesso e uso de cada fonte de vídeo, especialmente em relação ao uso de "referer" para downloads.

### Licença

Este projeto é distribuído sob a licença MIT.


## YouTube Video Downloader

Este projeto é um downloader de vídeos do YouTube desenvolvido em Python, utilizando `yt-dlp` e `ffmpeg` para baixar e combinar vídeo e áudio. O script oferece uma interface gráfica criada com `tkinter`, facilitando o processo de download para o usuário final.

### Funcionalidades

- **Download de vídeos do YouTube** com a melhor qualidade de vídeo e áudio.
- Combina automaticamente vídeo e áudio em um único arquivo MP4.
- Exibe informações do vídeo, como título, visualizações, duração e autor.
- Atualiza em tempo real o progresso do download.

### Requisitos

Antes de rodar o script, você precisa instalar as seguintes bibliotecas e ferramentas:

- **Python 3.x**
- **yt-dlp** (Para baixar vídeos do YouTube)
- **ffmpeg** (Para combinar vídeo e áudio)
- **Tkinter** (Interface gráfica)

### Instalação

1. Clone este repositório ou copie o código para um arquivo Python.
2. Instale as dependências executando o seguinte comando no terminal:
   ```bash
   pip install yt-dlp ffmpeg-python
   ```

3. Certifique-se de que o **FFmpeg** está instalado no seu sistema. Você pode baixar e configurar o FFmpeg a partir do site oficial [aqui](https://ffmpeg.org/download.html).

### Como usar

1. Execute o script:
   ```bash
   python app_youtube.py
   ```

2. Uma janela será exibida solicitando a URL do vídeo.
   - Insira a URL do vídeo do YouTube que deseja baixar.
   - Clique no botão **Baixar Vídeo**.

3. O download será iniciado e informações como o título, visualizações, duração e autor do vídeo serão exibidas.

4. O progresso do download será mostrado, e ao final, o vídeo será salvo no diretório `downloads` no formato MP4.

### Estrutura do Projeto

- **download_video**: Função principal que baixa o vídeo e áudio, utilizando a `yt-dlp`, e combina ambos utilizando `ffmpeg`.
- **run**: Função auxiliar que é executada em uma nova thread para evitar que a interface gráfica congele durante o download.
- **progress_hook**: Função que atualiza a barra de progresso durante o download.

### Exemplo de uso

1. Insira a URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
2. O vídeo será baixado e salvo como `downloads/Nome_do_Video.mp4`.

### Requisitos do Sistema

- Sistema Operacional: Windows, macOS ou Linux.
- Python 3.x.
- FFmpeg instalado e configurado no `PATH` do sistema.

### Problemas Comuns

- **FFmpeg não encontrado**: Certifique-se de que o FFmpeg esteja corretamente instalado e configurado no `PATH` do seu sistema.
- **Erro de URL inválida**: Verifique se a URL inserida é válida e corresponde a um vídeo do YouTube acessível.

### Licença

Este projeto é distribuído sob a licença MIT.