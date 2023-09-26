from cryptography.fernet import Fernet
import PySimpleGUI as sg

class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    # Generating the key to be used
    def create_key(self, path):
        self.key = Fernet.generate_key()
        print(self.key)

        with open(path, 'wb') as f:
            f.write(self.key)
    
    # Loading the key into the class
    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    # Creating a password file to store the passwords
    def create_password_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for key, value, in initial_values.items():
                self.add_password(key, value)

    # Loading the password file
    def load_password_file(self, path):
        self.password_file = path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    # Adds a password to the file
    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")

    # Returns a desired password
    def get_password(self, site):
        return self.password_dict[site]
    
