import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def download_video(m3u8_url, output_file, referer):
    headers = (
        f"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        f"(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36\r\n"
        f"Referer: {referer}\r\n"
    )
    command = ['ffmpeg', '-headers', headers, '-i', m3u8_url, '-c', 'copy', output_file + ".mp4"]
    subprocess.run(command)

def download_button_click():
    m3u8_url = m3u8_url_entry.get()
    output_file = output_file_entry.get()
    referer = referer_entry.get()

    if not m3u8_url or not output_file or not referer:
        messagebox.showinfo("Erro!", "Preencha todos os campos.")
        return

    # Obtém o diretório onde está a aplicação
    app_directory = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(app_directory, output_file)

    download_video(m3u8_url, output_path, referer)
    messagebox.showinfo("Download Concluído", f"Vídeo salvo como {output_path}")

# Criação da janela
root = tk.Tk()
root.title("Download de Vídeo")

# Entradas de texto
m3u8_url_label = tk.Label(root, text="URL do arquivo m3u8:")
m3u8_url_entry = tk.Entry(root)
output_file_label = tk.Label(root, text="Nome do arquivo de saída:")
output_file_entry = tk.Entry(root)
referer_label = tk.Label(root, text="Referer:")
referer_entry = tk.Entry(root)

# Botão de download
download_button = tk.Button(root, text="Download", command=download_button_click)

# Posicionamento dos widgets
m3u8_url_label.pack()
m3u8_url_entry.pack()
output_file_label.pack()
output_file_entry.pack()
referer_label.pack()
referer_entry.pack()
download_button.pack()

root.mainloop()
