# Control Pi

Este repositorio tiene como objetivo proporcionar una serie de programas y configuraciones básicas necesarias para convertir una Raspberry Pi en un sistema de escritorio funcional, así como para facilitar la integración de hardware adicional, como el medidor de voltaje INA 219 y la configuración de un LED indicador para mostrar cuando la Raspberry Pi está encendida.

### Propósito

El propósito de este repositorio es facilitar la instalación y configuración de herramientas y programas comunes para que puedas usar tu Raspberry Pi como una computadora de escritorio. Además, incluye algunos scripts para integrar hardware adicional como el medidor de voltaje y un LED indicador para mostrar el estado de la Raspberry Pi.

---

## Archivos

Los archivos importantes de este repositorio están dentro de la carpeta `master`, que contiene los siguientes archivos:

- **'master.py'**: Un script que incluye una serie de programas y configuraciones básicas para el funcionamiento de la Raspberry Pi, además de controlar un LED indicador de encendido.
- **'master_portable.py'**: Un script diseñado para hacer que la Raspberry Pi sea portable mediante el uso de baterías externas. Utiliza el medidor de voltaje INA 219 para leer el nivel de carga de la batería, y hace que el LED parpadee cuando la batería está baja, permitiendo que el usuario conecte la Raspberry Pi a la corriente sin riesgo de apagados repentinos debido a un bajo voltaje.
- **'README.md'**: Este archivo que describe el repositorio, su propósito y cómo utilizarlo.

---

## Requisitos previos

Antes de comenzar, asegúrate de tener una Raspberry Pi con el sistema operativo **Raspberry Pi OS** (anteriormente Raspbian) instalado.

---

## Instrucciones de instalación y uso

### 1. Copiar los archivos a tu Raspberry Pi

1. Descarga los archivos del repositorio o clónalos en tu Raspberry Pi.
2. Copia la carpeta 'master' a tu Raspberry Pi.

### 2. Ejecutar los scripts

1. Una vez copiada la carpeta 'master' a tu Raspberry Pi, abre una terminal y navega a la carpeta 'master'.
2. Abre el archivo 'master.py' o 'master_portable.py' con un editor de texto. Puedes usar un editor de texto como 'nano' o 'vim'.
   
   Por ejemplo:

   ```bash
   nano master.py
