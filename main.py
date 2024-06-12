import tkinter as tk
import customtkinter as ctk
from youtube_app import youtube_app
from audio_app import audio_app


window = ctk.CTk()
window.geometry("600x400+40+40")
window.title("Youtube | Audio")
window._set_appearance_mode("dark")

is_dark_mode = True

def change_mode():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    window._set_appearance_mode("dark" if is_dark_mode else "light")


ctk.CTkButton(window, text="Change mode", command=change_mode).place(x=450, y=10)


tabview = ctk.CTkTabview(window, width=500, height=300)
tabview.pack(pady=50)

youtube_tab = tabview.add("Youtube")
audio_tab = tabview.add("Audio")

youtube_app(youtube_tab)
audio_app(audio_tab)

window.mainloop()