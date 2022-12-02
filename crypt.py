# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 23:39:42 2021

@author: ACER
"""

from cryptography.fernet import Fernet
import base64

def write_key():
    """
    Membuat key baru
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Merestore key dari file `key.key`
    """
    return open("key.key", "rb").read()

def encrypt(filename, key):
    """
    Mengenkripsi file dengan key dari file 'key.key'
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # membaca(read) semua data dalam file
        file_data = file.read()
    # mengenkripsi data
    encrypted_data = f.encrypt(file_data)
    encoded = base64.b64encode(encrypted_data)
    # menulis data yang dienkripsi ke dalam file
    with open(filename, "wb") as file:
        file.write(encoded)

def decrypt(filename, key):
    """
    Mendekripsi file dengan key dari file 'key.key'
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # membaca(read) data yang terenkripsi
        encrypted_data = file.read()
    # dekripsi data
    decode = base64.b64decode(encrypted_data)
    decrypted_data = f.decrypt(decode)
    # menulis ulang data sesuai dengan data file sebelum dienkripsi
    with open(filename, "wb") as file:
        file.write(decrypted_data)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="File Encryptor Sederhana || Saluna Alavi")
    parser.add_argument("file", help="File untuk dienkripsi/didekripsi")
    parser.add_argument("-g", "--generate-key", dest="generate_key", action="store_true",
                        help="Untuk menghasilkan key baru")
    parser.add_argument("-e", "--encrypt", action="store_true",
                        help="Enkripsi file, hanya character -e atau -d yang bisa digunakan.")
    parser.add_argument("-d", "--decrypt", action="store_true",
                        help="Dekripsi file, hanya character -e atau -d yang bisa digunakan.")

    args = parser.parse_args()
    file = args.file
    generate_key = args.generate_key

    if generate_key:
        write_key()
    # me'load' key yang sama
    key = load_key()

    encrypt_ = args.encrypt
    decrypt_ = args.decrypt

    if encrypt_ and decrypt_:
        raise TypeError("Harap memilih action, enkripsi atau dekripsi")
    elif encrypt_:
        encrypt(file, key)
    elif decrypt_:
        decrypt(file, key)
    else:
        raise TypeError("Harap memilih action, enkripsi atau dekripsi")