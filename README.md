# control_pi
# programas básicos necesarios para crear una raspberry pi de escritorio 

sudo apt -y update && sudo apt -y install gdebi arduino gparted onboard gfortran viewnior fritzing texlive-full python3-pip unrar-free rpi-imager inkscape freecad stellarium simple-scan nmap octave snapd transmission-gtk p7zip p7zip-full gnome-disk-utility && sudo apt -y autoremove && sudo apt -y clean && sudo apt -y update && sudo apt -y upgrade && sudo apt -y full-upgrade

# necesario para medidor de voltaje INA 219
sudo pip3 install adafruit-circuitpython-ina219

# brillo 
sudo nano /sys/class/backlight/10-0045/brightness

# fritzing
cd /usr/share/fritzing/ \n
sudo rm -r parts \n
sudo git clone https://github.com/fritzing/fritzing-parts.git parts \n

# snap store
sudo reboot
sudo snap install core
sudo snap install snap-store

#como ejecutar un led testigo
sudo nano /lib/systemd/system/led_testigo.service
# luego dentro pegamos
[Unit]
Description=led testigo
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 /home/"USUARIO"/master/master.py

[Install]
WantedBy=multi-user.target
# cerramos y guardamos
# en la terminal 
sudo chmod 644 /lib/systemd/system/led_testigo.service
sudo systemctl daemon-reload
sudo systemctl enable led_testigo.service

# control led testigo indicador que la raspberry pi esta encendida 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, True)
