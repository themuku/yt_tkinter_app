import tkinter as tk
import customtkinter as ctk
from customtkinter import filedialog
from moviepy.editor import VideoFileClip


def audio_app(window):
    label = ctk.CTkLabel(window, text="")
    file_path = ""


    def select_file():
        nonlocal file_path
        file_name = filedialog.askopenfilename()
        file_path = file_name


    def convert():
        if not file_path:
            label.configure(text="You have to choose one video")
            return
        
        video = VideoFileClip(file_path)
        audio = video.audio
        output_src = filedialog.asksaveasfilename(defaultextension="mp3")
        audio.write_audiofile(output_src)


    ctk.CTkButton(window, text="Choose video", command=select_file).pack()
    ctk.CTkButton(window, text="Convert to MP3", command=convert).pack(pady=20)

    label.pack(pady=20)
    