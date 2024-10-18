import tkinter as tk
from tkinter import messagebox
import yt_dlp
import threading
import ffmpeg
import os

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Erro", "Por favor, insira a URL do vídeo.")
        return

    def run():
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
            'progress_hooks': [progress_hook],
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'merge_output_format': 'mp4'
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                info_dict = ydl.extract_info(url, download=True)
                title = info_dict.get('title', 'N/A')
                title_label.config(text=f"Título: {title}")
                views_label.config(text=f"Visualizações: {info_dict.get('view_count', 'N/A')}")
                length_label.config(text=f"Duração: {info_dict.get('duration', 'N/A')} segundos")
                author_label.config(text=f"Autor: {info_dict.get('uploader', 'N/A')}")

                video_file = f'downloads/{title}.mp4'
                audio_file = f'downloads/{title}.m4a'
                output_file = f'downloads/{title}_final.mp4'

                if os.path.exists(video_file) and os.path.exists(audio_file):
                    ffmpeg.input(video_file).output(audio_file).output(output_file, vcodec='copy', acodec='aac').run()
                    os.remove(video_file)
                    os.remove(audio_file)
                    os.rename(output_file, video_file)

                messagebox.showinfo("Sucesso", "Download concluído!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao baixar o vídeo: {str(e)}")

    threading.Thread(target=run).start()

def progress_hook(d):
    if d['status'] == 'downloading':
        downloaded = d.get('downloaded_bytes', 0)
        total = d.get('total_bytes', 0)
        percent = (downloaded / total) * 100 if total > 0 else 0
        progress_label.config(text=f"Progresso: {percent:.2f}%")
    elif d['status'] == 'finished':
        progress_label.config(text="Download completo!")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Downloader de Vídeos do YouTube")

tk.Label(root, text="Insira a URL do vídeo:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Baixar Vídeo", command=download_video)
download_button.pack(pady=20)

# Labels para mostrar telemetrias e progresso
title_label = tk.Label(root, text="Título: ")
title_label.pack(pady=5)

views_label = tk.Label(root, text="Visualizações: ")
views_label.pack(pady=5)

length_label = tk.Label(root, text="Duração: ")
length_label.pack(pady=5)

author_label = tk.Label(root, text="Autor: ")
author_label.pack(pady=5)

progress_label = tk.Label(root, text="Progresso: ")
progress_label.pack(pady=5)

root.mainloop()
