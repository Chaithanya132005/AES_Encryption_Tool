import os
from tkinter import Tk, Label, Button, filedialog
from cryptography.fernet import Fernet

# Generate or load a key
def generate_key():
    return Fernet.generate_key()

def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        key = generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        return key

key = load_key()
fernet = Fernet(key)

# File encryption
def encrypt_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        with open(filepath, 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open(filepath + ".enc", 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

# File decryption
def decrypt_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        with open(filepath, 'rb') as enc_file:
            encrypted = enc_file.read()
        try:
            decrypted = fernet.decrypt(encrypted)
            with open(filepath.replace(".enc", "_decrypted"), 'wb') as dec_file:
                dec_file.write(decrypted)
        except:
            print("Decryption failed: Invalid Key or Corrupt File")

# GUI
app = Tk()
app.title("AES-256 File Encryptor")
app.geometry("400x200")

Label(app, text="AES-256 Encryption Tool", font=("Arial", 16)).pack(pady=10)

Button(app, text="Encrypt File", command=encrypt_file, bg='green', fg='white').pack(pady=10)
Button(app, text="Decrypt File", command=decrypt_file, bg='blue', fg='white').pack(pady=10)

app.mainloop()
