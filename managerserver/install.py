from cryptography.fernet import Fernet
import json
import settings

cursor = settings.cursor
config = settings.config

#create the tables we need
cursor.execute("CREATE TABLE IF NOT EXISTS `users` (\
  `ID` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY ,\
  `username` varchar(255) COLLATE utf8mb4_bin NOT NULL,\
  `password` varchar(255) COLLATE utf8mb4_bin NOT NULL,\
  `email` varchar(255) COLLATE utf8mb4_bin NOT NULL\
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;")

#generate crypto pwd
config['CRYPTO_PWD'] = Fernet.generate_key().decode("utf-8")
#update config file
with open('settings.json', "w") as f:
    json.dump(config, f)