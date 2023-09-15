import pyAesCrypt

password = input('Введите пароль для файла: ')

pyAesCrypt.decryptFile('fillle.txt.aes', 'fille_open.txt', password)