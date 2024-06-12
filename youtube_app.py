import tkinter as tk
import customtkinter as ctk
from pytube import YouTube
from customtkinter import filedialog
import os


def youtube_app(window):
    url_input = ctk.CTkEntry(window, width=350)
    url_input.pack(pady=20)

    label = ctk.CTkLabel(window, text="")

    combobox = ctk.CTkComboBox(window, values=["mp4", "mp3"])


    def on_progress(stream, chunk, bytes_remaining):
      total_size = stream.filesize
      bytes_downloaded = total_size - bytes_remaining
      percentage_of_completion = bytes_downloaded / total_size * 100
      total_size = (total_size / 1024) / 1024
      total_size = round(total_size, 1)
      remain = (bytes_remaining / 1024) / 1024
      remain = round(remain, 1)
      downloaded = (bytes_downloaded / 1024) / 1024
      downloaded = round(downloaded, 1)
      percentage_of_completion = round(percentage_of_completion, 2)

      print(f'Download Progress: {percentage_of_completion}%, Total Size:{total_size} MB, Downloaded: {downloaded} MB, Remaining:{remain} MB')


    def on_complete(stream, file_path):
      file_name = file_path.split("\\")[-1].split(".")[0]
      label.configure(text=f"Video {file_name}\nhas been downloaded into Downloads folder")

    def download():
        url = url_input.get()
        extension = combobox.get()
        output_path = filedialog.askdirectory()
        try:
          yt = YouTube(url, on_complete_callback=on_complete, on_progress_callback=on_progress)

          if extension == "mp4":
            downloaded_file = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=output_path)
            base, ext = os.path.splitext(downloaded_file)
            file = base + ".mp4"
            os.rename(downloaded_file, file)
          else:
             downloaded_file = yt.streams.get_audio_only().download(output_path=output_path)
             base, ext = os.path.splitext(downloaded_file)
             file = base + ".mp3"
             os.rename(downloaded_file, file)
              
        except:
           print("Something went wrong")

    combobox.pack(pady=10)

    ctk.CTkButton(window, text="Download", command=download).pack()
    label.pack(pady=20)
