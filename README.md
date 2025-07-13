# Control Pi

Este repositorio tiene como objetivo proporcionar una serie de scripts y configuraciones necesarias para convertir una Raspberry Pi en un sistema funcional, con integración de sensores y controladores como el INA219 para monitoreo de voltaje, y un LED testigo para indicar estado de batería.

---

## 🧠 Propósito

Facilitar el uso de una Raspberry Pi como sistema portátil alimentado por baterías, mostrando alertas visuales mediante un LED cuando la batería está baja. Ideal para proyectos embebidos o portables.

---

## 📁 Estructura del proyecto

La carpeta `master/` contiene los scripts principales:

- `master.py`: Script base para escritorio, configura GPIO y funciones comunes.
- `master_portable.py`: Versión portable. Lee el voltaje del INA219 y hace parpadear un LED cuando la batería baja de cierto umbral.
- `led_testigo.service`: (opcional) Archivo de servicio para iniciar el script automáticamente al arrancar.

---

## 🧰 Requisitos

### Hardware

- Raspberry Pi 4 (u otra compatible)
- Sensor INA219 conectado vía I²C
- LED + resistencia (por ejemplo, 330Ω)
- Cables dupont
- Fuente o batería externa

### Pines por defecto

| Componente | GPIO usado    | Descripción     |
|------------|---------------|-----------------|
| LED        | GPIO 23       | Testigo batería |
| INA219     | I²C (SDA/SCL) | GPIO 2 / 3      |

---

## 🛠️ Instalación paso a paso

### 1. Clonar el repositorio

```bash
git clone https://github.com/eremohn/control_pi.git
cd control_pi

```
### 2. Crear y activar entorno virtual (opcional pero recomendado)

```bash

python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install adafruit-blinka adafruit-circuitpython-ina219 RPi.GPIO

```

Asegúrate de tener habilitado I²C desde raspi-config:

```bash
sudo raspi-config
# Interfacing Options -> I2C -> Enable

```
### 4. Cablear el hardware
Conecta el sensor INA219 a los pines SDA/SCL (GPIO 2 y 3), alimentación (3.3V o 5V), GND y conecta el LED al GPIO 23 con su respectiva resistencia.

---

## Agregar como servicio de sistema (Opcional)
Puedes hacer que el script master_portable.py se inicie automáticamente con el sistema:

### 1. Crear el archivo del servicio

```bash
sudo nano /etc/systemd/system/led_testigo.service

```
Pegar:

```bash
[Unit]
Description=LED testigo de bateria con INA219
After=multi-user.target

[Service]
Type=simple
User='USUARIO'
Group='USUARIO'
SupplementaryGroups=gpio,i2c
Environment=PYTHONUNBUFFERED=1
ExecStart=/home/'USUARIO'/.venv/bin/python3 /home/'USUARIO'/master/master_portable.py
WorkingDirectory=/home/'USUARIO'/master
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target

```
Asegúrate de reemplazar /home/'USUARIO'/ por tu ruta real si difiere.

### 2. Recargar y habilitar el servicio

```
bashsudo systemctl daemon-reload
sudo systemctl enable led_testigo.service
sudo systemctl start led_testigo.service


```
---

## Prueba manual

También puedes ejecutarlo directamente:


```
source .venv/bin/activate
python3 master/master_portable.py

```
---

---

## ✅ Estado

✔️ Funcional en Raspberry Pi 4 + Debian Bookworm (Julio 2025)

---

## Próximamente

- Captura del LED en funcionamiento  
- Gráfico de consumo con INA219  
- Versión con apagado seguro si el voltaje es crítico  

---

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

  
