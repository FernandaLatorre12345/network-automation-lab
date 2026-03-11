# Challenge de Automatización de Redes

Este repositorio contiene la solución a un challenge técnico orientado a la automatización de redes utilizando Python.

El objetivo del proyecto es demostrar la capacidad de:

* Automatizar la configuración de dispositivos de red.
* Implementar una interfaz gráfica para ingresar parámetros de configuración.
* Validar automáticamente los cambios realizados.
* Gestionar el proyecto utilizando Git.
* Planificar la automatización de una VPN IPSec entre dispositivos de diferentes fabricantes.

El proyecto está dividido en dos partes.

---

# Parte 1 – Automatización de Switch Cisco con Frontend

Se desarrolló una herramienta en Python que permite automatizar la configuración de un switch Cisco mediante una interfaz gráfica.

El sistema permite ingresar los parámetros de configuración desde el frontend y aplicar automáticamente los cambios en el dispositivo a través de una conexión SSH.

## Funcionalidades

* Conexión SSH a dispositivos de red
* Configuración automática de VLANs
* Modificación del hostname del dispositivo
* Guardado automático de la configuración
* Validación de la configuración aplicada
* Generación de backup de la configuración
* Interfaz gráfica para ingreso de parámetros

## VLANs configuradas

El sistema permite configurar las siguientes VLANs:

* VLAN 10 – VLAN_DATOS
* VLAN 20 – VLAN_VOZ
* VLAN 50 – VLAN_SEGURIDAD

## Flujo de automatización

El flujo de funcionamiento del sistema es el siguiente:

Usuario → Interfaz gráfica → Script de automatización → Dispositivo de red

1. El usuario ejecuta la interfaz gráfica.
2. Ingresa los datos del dispositivo y los parámetros de configuración.
3. El frontend envía la información al script de automatización.
4. El script establece una conexión SSH utilizando Netmiko.
5. Se aplican los comandos de configuración en el dispositivo.
6. La configuración se guarda en el equipo.
7. Se ejecutan comandos de validación.
8. Se genera un backup de la configuración.

---

# Entorno de laboratorio

La automatización fue probada utilizando el entorno de laboratorio:

Cisco DevNet Catalyst 9000 Always-On Sandbox.

Este laboratorio provee acceso a un switch Cisco IOS-XE virtual que permite probar automatización y funcionalidades de programabilidad de red.

---

# Instalación

Clonar el repositorio:

```bash
git clone https://github.com/FernandaLatorre12345/network-automation-lab.git
cd network-automation-lab
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

# Ejecución

Para ejecutar la interfaz gráfica:

```bash
python frontend.py
```

También es posible ejecutar directamente el script de automatización:

```bash
python switch_config.py
```

El sistema solicitará:

* Dirección IP o hostname del dispositivo
* Usuario
* Contraseña
* Nuevo hostname
* VLAN ID
* Nombre de VLAN

---

# Evidencias de funcionamiento

El repositorio incluye capturas de pantalla del funcionamiento del sistema en la carpeta:

```
screenshots/
```

Las capturas muestran:

* Interfaz del frontend
* Configuración aplicada en el dispositivo
* Generación del backup de configuración

---

# Parte 2 – Plan de Automatización de VPN IPSec

El repositorio también incluye un documento que describe el plan para automatizar la configuración de una VPN IPSec Site-to-Site entre dos plataformas de seguridad diferentes:

* Fortinet FortiGate
* Palo Alto Networks Firewall

El documento describe:

* Topología de red
* Red del túnel VPN
* Parámetros de seguridad IPSec (Phase 1 y Phase 2)
* Estrategia de automatización utilizando APIs
* Flujo de automatización
* Desafíos de automatización en entornos multi-vendor
* Estrategia de validación de la configuración
* Manejo de alertas

El documento completo se encuentra en:

```
vpn_automation_plan.md
```

---

# Topología de la VPN

El siguiente diagrama muestra la arquitectura de la VPN y la red de túnel utilizada.

![Topología VPN](images/vpn_topology.png)

---

# Scripts de automatización (conceptuales)

Se incluyen scripts de ejemplo que ilustran cómo podría implementarse la automatización de la VPN.

```
scripts/
deploy_vpn.py
fortigate_vpn.py
paloalto_vpn.py
vpn_test.py
```

Estos scripts muestran conceptualmente:

* Flujo de automatización
* Configuración por fabricante
* Validación de conectividad

---

# Tecnologías utilizadas

* Python
* Netmiko
* Paramiko (SFTP)
* Tkinter
* SSH
* Git
* Markdown

---

# Estructura del repositorio

```
network-automation-lab
│
├── README.md
├── vpn_automation_plan.md
├── frontend.py
├── switch_config.py
├── requirements.txt
│
├── scripts/
│
├── screenshots/
│
└── images/
```

---

# Autor

Fernanda Latorre
