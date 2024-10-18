import customtkinter as ctk
import keyboard
import time
import threading

countdown_window = None
countdown_label = None

def show_countdown(remaining):
    global countdown_window, countdown_label
    if countdown_window is None or not countdown_window.winfo_exists():
        countdown_window = ctk.CTkToplevel(app)
        countdown_window.title("Обратный отсчет")
        countdown_window.geometry("290x100")
        countdown_window.resizable(False, False)

        countdown_window.iconbitmap("app.ico")

        countdown_window.attributes("-topmost", True)

        screen_width = countdown_window.winfo_screenwidth()
        screen_height = countdown_window.winfo_screenheight()
        countdown_window.geometry(f"+{screen_width - 290 - 20}+{20}")

        countdown_label = ctk.CTkLabel(countdown_window, text=f"Осталось {remaining} секунд(ы)\n(Откройте окно где нужно спамить)", font=("Roboto", 16))
        countdown_label.pack(expand=True, fill='both')

        countdown_window.after(remaining * 1000, countdown_window.destroy)

    if countdown_label:
        countdown_label.configure(text=f"Осталось {remaining} секунд(ы)\n(Откройте окно где нужно спамить)")

def start_spam():
    message = message_entry.get()
    message_count = int(count_entry.get())
    delay = float(delay_entry.get())

    for remaining in range(5, 0, -1):
        show_countdown(remaining)
        countdown_window.update()
        time.sleep(1)

    if countdown_window:
        countdown_window.destroy()

    for _ in range(message_count):
        keyboard.write(message)
        keyboard.press_and_release('enter')
        time.sleep(delay)

    spam_button.configure(state="normal")

def run_spam():
    spam_button.configure(state="disabled")
    threading.Thread(target=start_spam).start()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("themes/purple.json")

app = ctk.CTk()
app.title("Спамер")
app.geometry("300x300")
app.iconbitmap("app.ico")
app.resizable(False, False)

message_label = ctk.CTkLabel(app, text="Сообщение")
message_label.pack(pady=5)
message_entry = ctk.CTkEntry(app)
message_entry.pack(pady=5)

count_label = ctk.CTkLabel(app, text="Количество сообщений")
count_label.pack(pady=5)
count_entry = ctk.CTkEntry(app)
count_entry.pack(pady=5)

delay_label = ctk.CTkLabel(app, text="Задержка (в секундах)")
delay_label.pack(pady=5)
delay_entry = ctk.CTkEntry(app)
delay_entry.pack(pady=5)

spam_button = ctk.CTkButton(app, text="Запустить спам", command=run_spam)
spam_button.pack(pady=20)

app.mainloop()