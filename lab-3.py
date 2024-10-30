
import tkinter as tk
import random
import string
import pygame  #Pygame нужен для громкости звука и нормального проигрывания, пожалуйста, разрешите, MOLU

# Константы
WINDOW_TITLE = "KeyGen for Factorio"
WINDOW_SIZE = "700x500"
BUTTON_COPY_DEFAULT_TEXT = "Копировать"
BUTTON_COPY_SUCCESS_TEXT = "Скопировано!"
BUTTON_GENERATE_TEXT = "Generate Key"

# Инициализация pygame
pygame.mixer.init()
pygame.mixer.music.load('03. Are We Alone.mp3')
pygame.mixer.music.set_volume(0.2)  #ГРОМКОСТЬ 20%
pygame.mixer.music.play(-1)

def generate_key():
    key_parts = []
    for _ in range(4):
        part = ''.join(random.choices(string.ascii_uppercase, k=3)) + random.choice(string.digits)
        key_parts.append(part)
    key = '-'.join(key_parts)
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)


# Функционал кнопки генерации ключа
def copy_to_clipboard():
    root.clipboard_clear()  
    root.clipboard_append(key_entry.get())  
    copy_button.config(text=BUTTON_COPY_SUCCESS_TEXT)  
    root.after(750, reset_copy_button)

def reset_copy_button():
    copy_button.config(text=BUTTON_COPY_DEFAULT_TEXT)

root = tk.Tk()
root.title(WINDOW_TITLE)
root.geometry(WINDOW_SIZE)  
root.resizable(True, True)  

background_image = tk.PhotoImage(file="space-age-logo.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Поле для генерации ключа
key_entry = tk.Entry(root, font=("Helvetica", 16), fg='black', bg='white', justify='center', width=30)
key_entry.pack(pady=20)

# Кнопка для генерации ключа
generate_button = tk.Button(root, text=BUTTON_GENERATE_TEXT, command=generate_key, font=("Helvetica", 14), bg='green', fg='white')
generate_button.pack(pady=10)

def on_enter(e):
    e.widget['bg'] = 'lightgreen'

def on_leave(e):
    e.widget['bg'] = 'green'

generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)

# Кнопка для копирования ключа
copy_button = tk.Button(root, text=BUTTON_COPY_DEFAULT_TEXT, command=copy_to_clipboard, font=("Helvetica", 12), bg='lightblue')
copy_button.pack(pady=5)


# Запуск основного цикла
root.mainloop()                      
pygame.mixer.music.stop()  # Останавливает музыку при закрытии
