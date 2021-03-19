#### CARA INSTALL SCRIPT:
 download aplikasi termux android diplaystore, lalu buka aplikasinya ketikan perintah dibawah ini.
 ```
  pkg update && pkg upgrade
  pkg install python git
  pip install requests bs4 futures cython
  rm -rf smbf
  git clone https://github.com/CrackerSilent67/smbf
  cd $HOME/smbf
  cythonize -i smbf.c && rm smbf.c
  python run.py
 ```
