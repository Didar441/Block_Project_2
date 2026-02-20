import sys
import hashlib
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QTextEdit
from PyQt6.QtCore import Qt
import bcrypt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Example")
        self.setGeometry(200, 100, 800, 600)

        label = QLabel("Welcome to the password Hasher! This program demonstrates" 
        "a salted and unsalted hash for a password. Please enter" 
        " a test password.", self)
        label.setAlignment(Qt.AlignmentFlag.AlignTop)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setCentralWidget(label)

        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText("Type a test password here")
        self.text_input.setGeometry(200, 50, 400, 30)

        hash_button = QPushButton("Unsalted Hash", self)
        hash_button.setGeometry(350, 100, 100, 30)
        hash_button.clicked.connect(self.print_hash)

        salt_button = QPushButton("Hash with Salt", self)
        salt_button.setGeometry(350, 150, 100, 30)
        salt_button.clicked.connect(self.print_salt_hash)

        self.hashes = QTextEdit(self)
        self.hashes.setGeometry(200, 200, 400, 200)
        self.hashes.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.hashes.setReadOnly(True)

       


    def print_hash(self):
        password = self.text_input.text()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.hashes.setText(
            f"Unsalted Hash: {hashed_password}\n\n"
            "The unsalted hash is a SHA-256 hash of the password you entered. The problem with unsalted hashes is that" 
            " two users with the same password will have the same hash, which can make it easier for attackers to crack" 
            " passwords especially if people have common passwords."
        )
        
    def print_salt_hash(self):
        password = self.text_input.text()
        saltedPassword = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.hashes.setText(f"Salted Hash: {saltedPassword.decode()}\n\n"
        "The salted hash is a much more secure way to hash a password. It uses the bcrypt library to create a unique salt for each password, " 
        "which makes it resistant to brute-force attacks and rainbow table attacks. "
        "Even if two users have the same password, "
        "their salted hashes will be different due to the unique salt. Try and hash the same password twice to see the different hashes!"
        )


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":    
    main()