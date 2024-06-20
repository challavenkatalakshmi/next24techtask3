import tkinter as tk
from tkinter import messagebox
import requests

def get_lyrics(artist, song):
    url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('lyrics', 'Lyrics not found')
    else:
        return "Error: Lyrics not found"

def fetch_lyrics():
    artist = artist_entry.get()
    song = song_entry.get()
    
    if artist and song:
        lyrics = get_lyrics(artist, song)
        lyrics_text.delete(1.0, tk.END)
        lyrics_text.insert(tk.END, lyrics)
    else:
        messagebox.showwarning("Input Error", "Please enter both artist and song names")

# Create main window
root = tk.Tk()
root.title("Lyrics Fetcher")
root.geometry("600x500")
root.config(bg="#282c34")

# Title label
title_label = tk.Label(root, text="Lyrics Fetcher", font=("Helvetica", 24, "bold"), bg="#282c34", fg="#61dafb")
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Artist label and entry
artist_label = tk.Label(root, text="Artist:", font=("Helvetica", 14), bg="#282c34", fg="#ffffff")
artist_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")
artist_entry = tk.Entry(root, width=40, font=("Helvetica", 14), bg="#3c4043", fg="#ffffff", insertbackground='white')
artist_entry.grid(row=1, column=1, padx=20, pady=10)

# Song label and entry
song_label = tk.Label(root, text="Song:", font=("Helvetica", 14), bg="#282c34", fg="#ffffff")
song_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")
song_entry = tk.Entry(root, width=40, font=("Helvetica", 14), bg="#3c4043", fg="#ffffff", insertbackground='white')
song_entry.grid(row=2, column=1, padx=20, pady=10)

# Fetch lyrics button
fetch_button = tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics, font=("Helvetica", 14), bg="#61dafb", fg="#282c34", padx=10, pady=5)
fetch_button.grid(row=3, column=0, columnspan=2, pady=20)

# Text area for displaying lyrics
lyrics_text = tk.Text(root, wrap=tk.WORD, width=60, height=20, font=("Helvetica", 12), bg="#ffffff", fg="#282c34")
lyrics_text.grid(row=4, column=0, columnspan=2, padx=20, pady=10)

# Scrollbar for the text area
scrollbar = tk.Scrollbar(root, command=lyrics_text.yview, bg="#3c4043")
scrollbar.grid(row=4, column=2, sticky='nsew')
lyrics_text['yscrollcommand'] = scrollbar.set

# Run the application
root.mainloop()
