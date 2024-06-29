from tkinter import *
from tkinter import messagebox
import customtkinter as cus
import yt_dlp
from pytube import YouTube
def download_action():
    url = entryUrl.get()
    url_type = combobox.get()
    ydl_opts = {
                'format': 'best', # Choose the best quality
                # 'outtmpl': 'downloaded_video.mp4',  # Output path
                     }
    if url and url_type:
        messagebox.showinfo("Download Started", f"Downloading {url} of type {url_type}")
        if url_type == "Youtube":
            print("Youtube selected")
            try:
                yt = YouTube(url)
                stream = yt.streams.get_highest_resolution()
                stream.download()
                messagebox.showinfo("Success", "Video downloaded successfully")
                entryUrl.delete(0, END)
                combobox.set("")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
            # Add your specific action for Youtube here
        elif url_type == "Facebook":
            print("Facebook selected")
            # Add your specific action for Facebook here
           
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                    messagebox.showinfo("Success", "Video downloaded successfully")
                    entryUrl.delete(0, END)
                    combobox.set("")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Download Error", "Please enter URL and select type.")

def clear_action():
    entryUrl.delete(0, END)
    combobox.set("")

root = cus.CTk()
cus.set_appearance_mode("dark")  # Set the appearance mode
cus.set_default_color_theme("dark-blue")  # Set the color theme
root.geometry('380x270')
root.title('Tool for download video V1.0')

label = cus.CTkLabel(root, text='Tool Download Videos', text_color="LightSeaGreen", font=("Kozuka Gothic Pro H", 20))
label.pack(pady=10)

# URL Label and Entry
labeTextUrl = cus.CTkLabel(root, text='URL', font=("Kozuka Gothic Pro",12))
labeTextUrl.place(x=30, y=80)
entryUrl = cus.CTkEntry(root, placeholder_text="input your url", width=220)
entryUrl.place(x=100, y=80)

# Type of URL Label and ComboBox
labeTextUrlType = cus.CTkLabel(root, text='Type of URL : (FB/YT)', font=("Kozuka Gothic Pro",12))
labeTextUrlType.place(x=30, y=135)
types = ["","Youtube", "Facebook"]
combobox = cus.CTkComboBox(root, values=types)
combobox.place(x=180, y=135)

# Download Button
btnDownload = cus.CTkButton(root, text="Download", command=download_action)
btnDownload.place(x=30, y=200)

# Clear Button
btnClear = cus.CTkButton(root, text="Clear", fg_color="red", hover_color="Coral", command=clear_action)
btnClear.place(x=180, y=200)

# about me

def about_me():
    messagebox.showinfo("About Me", "This tool is made by Damrith <2024>\nVersion 1.0")

btnAbout = cus.CTkButton(root, text="?", command=about_me, width=10, )
btnAbout.place(x=350, y=10)

root.mainloop()
