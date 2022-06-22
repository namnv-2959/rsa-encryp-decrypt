from service import generate_rsa_pair_key
import tkinter as tk


# root = tk.Tk()
# root.title('RSA encrypt and decrypt application')
# root.geometry('1000x500+50+50')

# # place a label on the root window
# message = tk.Label(root, text="Chương trình mã hóa và giải mã RSA")
# message.pack()

# # keep the window displaying
# root.mainloop()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x500+50+50')
        self.title('RSA encrypt and decrypt application')
        

        
        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=3)

        self.create_widgets()

    def create_widgets(self):
        # header
        header_label = tk.Label(self, text="Chương trình mã hóa và giải mã RSA")
        header_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        # username
        username_label = tk.Label(self, text="Username:")
        username_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        username_entry = tk.Entry(self)
        username_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # password
        password_label = tk.Label(self, text="Password:")
        password_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        password_entry = tk.Entry(self,  show="*")
        password_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        # login button
        login_button = tk.Button(self, text="Login")
        login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()