# Setup: Instalación automática de programas en Raspberry Pi

Este script tiene como objetivo automatizar la instalación y configuración inicial de programas esenciales para una Raspberry Pi con sistema operativo basado en Debian (como Raspberry Pi OS o Debian Bookworm).

Incluye herramientas de escritorio, utilidades del sistema, soporte para hardware como el sensor INA219, y la instalación del Snap Store para facilitar futuras instalaciones de software.

---

## Archivos

- `setup_rpi_auto.sh`: Script principal de instalación automática.

---

## ¿Qué instala este script?

1. **Programas de escritorio y utilidades:**
   - `xrdp`, `gdebi`, `gparted`, `gfortran`, `viewnior`, `python3-pip`, `unrar-free`, `simple-scan`, `nmap`, `snapd`, `transmission-gtk`, `p7zip`, `p7zip-full`, `gnome-disk-utility`

2. **Limpieza y actualización del sistema:**
   - `autoremove`, `clean`, `update`, `upgrade`, `full-upgrade`

3. **Biblioteca de sensor INA219:**
   - `adafruit-circuitpython-ina219` (vía `pip3`)

4. **Snap Store:**
   - Instalación de `snap core` y `snap-store`

---

## Cómo usarlo

1. **Dar permisos de ejecución:**

   ```bash
   cd setup
   chmod +x setup_rpi_auto.sh
   ```

2. Ejecutar el script:

   ```bash
   sudo ./setup_rpi_auto.sh
   ```

3. Reiniciar el sistema (si el script no lo hizo automáticamente):

   ```bash
   sudo reboot

   ```

--- 

---

## Notas

- El script es **idempotente** en su mayoría: si un programa ya está instalado, no se reinstalará.
- Algunas tareas requieren reinicio del sistema (por ejemplo, después de instalar `snapd`). El script incluye esta acción automáticamente al final del proceso.
- Este script fue diseñado para facilitar la preparación de tu Raspberry Pi como entorno de escritorio y como plataforma para proyectos de hardware embebido.

---

> 📁 Para más detalles técnicos o para integrar hardware adicional como el **LED testigo de batería con el sensor INA219**, consultá la carpeta [`master/`](../master/).

