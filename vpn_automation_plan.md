# Plan de Automatización de VPN IPSec

# 1. Objetivo

El objetivo de este documento es describir un plan para automatizar la implementación y validación de una VPN IPSec Site-to-Site entre dos plataformas de firewall diferentes:

* Fortinet FortiGate (Sitio A)
* Palo Alto Networks Firewall (Sitio B)

La automatización busca reducir errores de configuración manual, asegurar consistencia en los parámetros de seguridad y proporcionar mecanismos de validación luego del despliegue.

Este enfoque mejora la eficiencia operativa y permite mantener configuraciones consistentes entre distintas plataformas de seguridad.

---

# 2. Topología de Red Propuesta

La siguiente arquitectura conecta dos sitios remotos mediante un túnel VPN IPSec a través de Internet.

```
Sitio A (FortiGate)                   Sitio B (Palo Alto)
------------------                    -------------------
LAN: 10.1.1.0/24                      LAN: 10.2.2.0/24
        |                                      |
        |                                      |
    FortiGate ----------- INTERNET ----------- Palo Alto
    WAN: 200.1.1.1                             WAN: 200.2.2.2
```

El túnel VPN permite la comunicación segura entre ambas redes internas.

Redes protegidas:

* Sitio A: 10.1.1.0/24
* Sitio B: 10.2.2.0/24

## Diagrama de la Topología VPN

![Topología VPN](images/vpn_topology.png)

---

# 3. Red del Túnel

La VPN utilizará una red de tránsito dedicada para las interfaces del túnel.

Red del túnel:

```
169.255.1.0/30
```

Asignación de direcciones:

* FortiGate: 169.255.1.1
* Palo Alto: 169.255.1.2

Esta red permite el enrutamiento entre ambos firewalls y se utiliza comúnmente en configuraciones de VPN basadas en interfaces (route-based VPN).

---

# 4. Tipo de VPN

La solución utiliza:

```
VPN IPSec Site-to-Site
IKE Version: IKEv2
```

Este tipo de VPN permite establecer comunicación cifrada y segura entre dos ubicaciones remotas a través de redes no confiables como Internet.

---

# 5. Parámetros de Seguridad de la VPN

### Phase 1 – IKE (Establecimiento del túnel)

```
Encriptación: AES256
Autenticación: SHA256
Grupo DH: 14
Versión IKE: IKEv2
Método de autenticación: Pre-Shared Key
Lifetime: 28800 segundos
```

### Phase 2 – IPSec (Cifrado del tráfico)

```
Encriptación: AES256
Autenticación: SHA256
Perfect Forward Secrecy (PFS): Grupo 14
Lifetime: 3600 segundos
```

Ambos extremos deben utilizar los mismos parámetros para que el túnel pueda establecerse correctamente.

---

# 6. Estrategia de Automatización

La estrategia de automatización se basa en la utilización de las APIs oficiales proporcionadas por cada fabricante.

La automatización permite desplegar de forma consistente elementos como:

* IKE Gateways
* Túneles IPSec
* Políticas de firewall
* Rutas hacia las redes remotas

---

## Automatización en FortiGate

Fortinet proporciona una API REST que permite configurar objetos del firewall de forma programática.

Algunos endpoints relevantes incluyen:

```
/api/v2/cmdb/vpn.ipsec
/api/v2/cmdb/system.interface
/api/v2/cmdb/firewall.policy
```

La autenticación normalmente se realiza mediante un API Token.

Herramientas posibles para la automatización:

* Python
* Ansible
* FortiOS REST API

---

## Automatización en Palo Alto

Los firewalls Palo Alto exponen una API XML que permite ejecutar configuraciones y comandos operativos de forma remota.

Ejemplos de operaciones incluyen:

* Crear IKE Gateways
* Crear túneles IPSec
* Crear políticas de seguridad

Interfaces disponibles:

```
XML API
REST API (en versiones recientes de PAN-OS)
```

Herramientas posibles:

* Python
* Ansible
* Palo Alto XML API

---

# 7. Flujo de Automatización

El proceso de automatización puede seguir la siguiente secuencia:

1. Cargar los parámetros de la VPN desde un archivo de configuración (direcciones IP, subredes, parámetros de seguridad).
2. Validar los parámetros ingresados:

   * formato de direcciones IP
   * definición de subredes
   * compatibilidad de algoritmos de cifrado entre dispositivos.
3. Configurar el dispositivo FortiGate:

   * crear Phase 1
   * crear Phase 2
   * configurar la interfaz de túnel
   * crear políticas de firewall
   * configurar rutas hacia la red remota.
4. Configurar el firewall Palo Alto:

   * crear IKE Gateway
   * crear interfaz de túnel
   * crear túnel IPSec
   * configurar políticas de seguridad
   * configurar rutas entre redes.
5. Aplicar los cambios de configuración en Palo Alto (commit).
6. Ejecutar validaciones para confirmar el establecimiento del túnel.
7. Realizar pruebas de conectividad entre las redes protegidas.
8. Generar alertas si se detectan fallas.

---

# 8. Desafíos en Automatización Multi-Vendor

Automatizar configuraciones entre dispositivos de diferentes fabricantes presenta varios desafíos.

## Diferencias entre APIs

FortiGate utiliza una API basada en REST, mientras que Palo Alto utiliza principalmente una API XML.

## Diferencias en la estructura de configuración

Cada plataforma organiza la configuración de VPN de forma distinta.

Por ejemplo:

* FortiGate suele utilizar configuraciones de VPN basadas en interfaces de túnel.
* Palo Alto requiere interfaces de túnel asociadas a zonas de seguridad.

## Compatibilidad de parámetros

Los algoritmos de cifrado, grupos DH y parámetros de autenticación deben coincidir en ambos dispositivos.

Cualquier diferencia puede impedir el establecimiento del túnel.

## Manejo de autenticación

Los sistemas de automatización deben manejar de forma segura:

* API tokens
* credenciales de dispositivos
* claves de autenticación

---

# 9. Estrategia de Validación

Luego de aplicar la configuración, el sistema de automatización debe verificar que la VPN esté correctamente establecida y operativa.

La validación incluye tanto verificaciones de configuración como pruebas de conectividad.

## Validación de configuración

El script de automatización debe verificar:

* configuración del IKE Gateway
* estado del túnel IPSec
* políticas de firewall permitiendo tráfico
* rutas entre redes

Ejemplos de comandos:

### FortiGate

```
diagnose vpn tunnel list
get vpn ipsec tunnel summary
```

### Palo Alto

```
show vpn ike-sa
show vpn ipsec-sa
```

---

## Pruebas de conectividad

El sistema de automatización debe realizar pruebas de conectividad entre las redes protegidas.

Ejemplo:

```
ping 10.2.2.10 desde el Sitio A
ping 10.1.1.10 desde el Sitio B
```

Si la conectividad falla, el sistema debe generar una alerta indicando posibles problemas en la VPN.

---

# 10. Manejo de Alertas

Si alguna validación falla, el sistema de automatización debe generar una alerta clara indicando el problema detectado.

Posibles problemas:

* el túnel no se establece
* parámetros de VPN incorrectos
* errores de ruteo
* políticas de firewall bloqueando tráfico

Las alertas pueden integrarse con plataformas de monitoreo como:

* PRTG
* Syslog
* notificaciones por correo electrónico

---

# 11. Scripts de Automatización (Opcional)

Ejemplos de scripts incluidos en el repositorio:

```
deploy_vpn.py
fortigate_vpn.py
paloalto_vpn.py
vpn_test.py
```

Estos scripts demuestran cómo la configuración y validación de la VPN podrían automatizarse utilizando las APIs de los fabricantes.

---

# 12. Script de Prueba de Conectividad (Opcional)

Se puede implementar un script en Python para verificar la conectividad a través del túnel IPSec.

Lógica básica:

1. Ejecutar un ping desde el Sitio A hacia el Sitio B.
2. Verificar tiempo de respuesta y pérdida de paquetes.
3. Reportar éxito o fallo en la prueba de conectividad.

Este script podría integrarse dentro de un pipeline de validación automática luego del despliegue de la VPN.
