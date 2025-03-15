import customtkinter as tk
import time
import threading

class App:
    def __init__(self, master):
        self.master = master
        master.title("Start/Stop Example")

        self.running = False
        self.counter = 0

        self.start_button = tk.CTkButton(master, text="Start", command=self.start)
        self.start_button.pack()

        self.stop_button = tk.CTkButton(master, text="Stop", command=self.stop, state=tk.DISABLED)
        self.stop_button.pack()

        self.label = tk.CTkLabel(master, text="Counter: 0")
        self.label.pack()

    def start(self):
        self.running = True
        self.start_button.configure(state=tk.DISABLED)
        self.stop_button.configure(state=tk.NORMAL)
        threading.Thread(target=self.count).start()

    def stop(self):
        self.running = False
        self.start_button.configure(state=tk.NORMAL)
        self.stop_button.configure(state=tk.DISABLED)

    def count(self):
        while self.running:
            self.counter += 1
            self.label.configure(text="Counter: " + str(self.counter))
            time.sleep(0.1)

root = tk.CTk()
app = App(root)
root.mainloop()