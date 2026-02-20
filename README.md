# Block_Project_2
This is a simple program to demonstrate hashing passwords. It shows the difference between a salted
and unsalted hash of a password. Passwords with no salt will always produce the same hash meaning two people can have the same password and they will produce the exact same hash. Salted passwords will always produce a unique hash regardless if two people have the same passwords.

What is salting?
- It is a technique that adds random data(salt) to a password before it is hashed and stored.

# python setup
Make sure you have python installed on your device. You can install python off python.org.
This program was coded in VS Code.

## Dependencies to install

In the terminal, you need install the following:

pip install PyQt6
pip install bcrypt
(If these do not work use the two commands below)

python -m pip install PyQt6
python -m pip install bcrypt

Once installed, you can run the program by typing "python main.py" inside of the terminal. 

You should be prompted to enter in a fake password and two buttons to either show the unsalted hash of that password or the salted hash of that password. The salted hash will produce a new hash each time with the same password inputted and the unsalted will produce the same hash for the same password.

# Warnings
This tool is for educational use only and should not be used for securing sensitive information. This to simply demonstrate the security of having passwords hashed with salt.

# Ethical considerations and responsible use
The project shows how passwords are protected and why salting them is important for security. It should not be used with real passwords, it should not be used to try and crack passwords, and it should only be used locally to test fake passwords. No other outside use should be considered, it is just to show the importance of salting.





