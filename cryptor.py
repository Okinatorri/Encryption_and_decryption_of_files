import pyAesCrypt

password = input('Введите пароль для файла: ')

pyAesCrypt.encryptFile('fille.txt', 'fillle.txt.aes', password)
