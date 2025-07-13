#!/usr/bin/env bash
# ──────────────────────────────────────────────────────────────
# setup_rpi_auto.sh
# Automatiza la preparación de una Raspberry Pi (Debian/RPi OS)
# Instalación de utilidades de escritorio, actualización completa
# e instalación del driver INA219 + Snap Store.
# ──────────────────────────────────────────────────────────────

set -euo pipefail
IFS=$'\n\t'

echo "=== Fase 1 · Actualización e instalación de paquetes ==="
apt -y update
apt -y install \
  xrdp gdebi gparted gfortran viewnior python3-pip \
  unrar-free simple-scan nmap snapd transmission-gtk \
  p7zip p7zip-full gnome-disk-utility

echo "=== Fase 2 · Limpieza y upgrade ==="
apt -y autoremove
apt -y clean
apt -y update
apt -y upgrade -y
apt -y full-upgrade

echo "=== Fase 3 · Instalación del driver INA219 vía pip ==="
pip3 install --upgrade pip
pip3 install --break-system-packages adafruit-circuitpython-ina219

echo "=== Fase 4 · Preparar Snap Store ==="
echo "Es recomendable REINICIAR antes de instalar Snap Store para que snapd se inicialice bien."
read -rp "¿Deseas reiniciar ahora? (s/N) " resp
if [[ $resp =~ ^([sS]|[yY])$ ]]; then
  echo "Reiniciando…"
  reboot
else
  echo "Después del reinicio manual, ejecuta:\n  sudo snap install core\n  sudo snap install snap-store"
fi

echo "✅ Script completado."
