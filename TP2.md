# TP2 : Environnement virtuel

- [TP2 : Environnement virtuel](#tp2--environnement-virtuel)
- [I. Topologie réseau](#i-topologie-réseau)
  - [Compte-rendu](#compte-rendu)
- [II. Interlude accès internet](#ii-interlude-accès-internet)
- [III. Services réseau](#iii-services-réseau)
  - [1. DHCP](#1-dhcp)
  - [2. Web web web](#2-web-web-web)

# I. Topologie réseau

## Compte-rendu

☀️ Sur **`node1.lan1.tp1`**

```
# Cartes réseau
[hugoa@node1 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:f6:4f:f9 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.11/24 brd 10.1.1.255 scope global noprefixroute enp0s3
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fef6:4ff9/64 scope link dadfailed tentative
       valid_lft forever preferred_lft forever

# Table de routage
[hugoa@node1 ~]$ ip r s
10.1.1.0/24 dev enp0s3 proto kernel scope link src 10.1.1.11 metric 100
10.1.2.0/24 via 10.1.1.254 dev enp0s3 proto static metric 100
10.1.2.254 dev enp0s3 proto static scope link metric 100

# Ping de node2.lan2.tp1
[hugoa@node1 ~]$ ping 10.1.2.12
PING 10.1.2.12 (10.1.2.12) 56(84) bytes of data.
64 bytes from 10.1.2.12: icmp_seq=1 ttl=63 time=3.67 ms
64 bytes from 10.1.2.12: icmp_seq=2 ttl=63 time=6.14 ms
^C
--- 10.1.2.12 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1004ms
rtt min/avg/max/mdev = 3.674/4.907/6.140/1.233 ms

# Route du paquet
[hugoa@node1 ~]$ traceroute 10.1.2.12
traceroute to 10.1.2.12 (10.1.2.12), 30 hops max, 60 byte packets
 1  10.1.1.254 (10.1.1.254)  5.358 ms  4.944 ms  4.695 ms
 2  10.1.2.12 (10.1.2.12)  4.456 ms !X  4.084 ms !X  6.233 ms !X
```

# II. Interlude accès internet

**On va donner accès internet à tout le monde.** Le routeur aura un accès internet, et permettra à tout le monde d'y accéder : il sera la passerelle par défaut des membres du LAN1 et des membres du LAN2.

**Ajoutez une carte NAT au routeur pour qu'il ait un accès internet.**

☀️ **Sur `router.tp1`**

```
# Ping ip publique Ynov
[hugoa@router ~]$ ping 172.67.74.226
PING 172.67.74.226 (172.67.74.226) 56(84) bytes of data.
64 bytes from 172.67.74.226: icmp_seq=1 ttl=56 time=13.2 ms
64 bytes from 172.67.74.226: icmp_seq=2 ttl=56 time=13.7 ms
^C
--- 172.67.74.226 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1003ms
rtt min/avg/max/mdev = 13.188/13.457/13.726/0.269 ms

[hugoa@router ~]$ ping google.com
PING google.com (142.250.179.110) 56(84) bytes of data.
64 bytes from par21s20-in-f14.1e100.net (142.250.179.110): icmp_seq=1 ttl=115 time=25.7 ms
64 bytes from par21s20-in-f14.1e100.net (142.250.179.110): icmp_seq=2 ttl=115 time=25.2 ms
^C
--- google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1003ms
rtt min/avg/max/mdev = 25.189/25.440/25.692/0.251 ms
```

☀️ **Accès internet LAN1 et LAN2**

```
[hugoa@node2 ~]$ sudo cat /etc/sysconfig/network-scripts/route-enp0s3
default via 10.1.1.254 dev enp0s3
10.1.2.0/24 via 10.1.1.254 dev enp0s3

[hugoa@node2 ~]$ sudo cat /etc/sysconfig/network-scripts/ifcfg-enp0s3
DEVICE=enp0s3

BOOTPROTO=static
ONBOOT=yes

IPADDR=10.1.1.12
NETMASK=255.255.255.0
DNS1=1.1.1.1

[hugoa@node2 ~]$ ping 141.94.221.62
PING 141.94.221.62 (141.94.221.62) 56(84) bytes of data.
64 bytes from 141.94.221.62: icmp_seq=1 ttl=45 time=85.1 ms
^C
--- 141.94.221.62 ping statistics ---
2 packets transmitted, 1 received, 50% packet loss, time 1003ms
rtt min/avg/max/mdev = 85.072/85.072/85.072/0.000 ms

[hugoa@node2 ~]$ ping httpcats.com
PING httpcats.com (34.111.206.85) 56(84) bytes of data.
64 bytes from 85.206.111.34.bc.googleusercontent.com (34.111.206.85): icmp_seq=1 ttl=112 time=45.1 ms
64 bytes from 85.206.111.34.bc.googleusercontent.com (34.111.206.85): icmp_seq=2 ttl=112 time=74.0 ms
^C
--- httpcats.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1004ms
rtt min/avg/max/mdev = 45.054/59.534/74.015/14.480 ms
```

# III. Services réseau

## 1. DHCP

☀️ **Sur `dhcp.lan1.tp1`**

```
[hugoa@dhcp ~]$ hostname
dhcp.lan1.tp1

[hugoa@dhcp ~]$ ip a
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:51:96:93 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.253/24 brd 10.1.1.255 scope global noprefixroute enp0s3

# Commandes install serveur dhcp
[hugoa@dhcp ~]$ sudo dnf -y install dhcp-server
[hugoa@dhcp ~]$ sudo vim /etc/dhcp/dhcpd.conf
[hugoa@dhcp ~]$ sudo systemctl enable --now dhcpd
[hugoa@dhcp ~]$ firewall-cmd --add-service=dhcp --permanent
[hugoa@dhcp ~]$ sudo firewall-cmd --runtime-to-permanent

# Conf du service dhcp
[hugoa@dhcp ~]$ sudo cat /etc/dhcp/dhcpd.conf
default-lease-time 900;
max-lease-time 10800;

authoritative;

subnet 10.1.1.0 netmask 255.255.255.0 {
        range 10.1.1.100 10.1.1.200;
        option routers 10.1.1.254;
        option domain-name-servers 1.1.1.1;
}
```

☀️ **Sur `node1.lan1.tp1`**

- demandez une IP au serveur DHCP
- prouvez que vous avez bien récupéré une IP *via* le DHCP
- prouvez que vous avez bien récupéré l'IP de la passerelle
- prouvez que vous pouvez `ping node1.lan2.tp1`

```
[hugoa@node1 ~]$ ip a show dev enp0s3
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:de:06:46 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.100/24 brd 10.1.1.255 scope global dynamic noprefixroute enp0s3
       valid_lft 545sec preferred_lft 545sec

[hugoa@node1 ~]$ ip r s
default via 10.1.1.254 dev enp0s3 proto dhcp src 10.1.1.100 metric 100
10.1.1.0/24 dev enp0s3 proto kernel scope link src 10.1.1.100 metric 100

[hugoa@node1 ~]$ ping 10.1.2.11
PING 10.1.2.11 (10.1.2.11) 56(84) bytes of data.
64 bytes from 10.1.2.11: icmp_seq=1 ttl=63 time=3.00 ms
64 bytes from 10.1.2.11: icmp_seq=2 ttl=63 time=2.37 ms
^C
--- 10.1.2.11 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1003ms
rtt min/avg/max/mdev = 2.370/2.684/2.999/0.314 ms
```

## 2. Web web web

Un petit serveur web ? Pour la route ?

On recycle ici, toujours dans un soucis d'économie de ressources, la machine `node2.lan2.tp1` qui devient `web.lan2.tp1`. On va y monter un serveur Web qui mettra à disposition un site web tout nul.

---

La conf du serveur web :

- ce sera notre vieil ami NGINX
- il écoutera sur le port 80, port standard pour du trafic HTTP
- la racine web doit se trouver dans `/var/www/site_nul/`
  - vous y créerez un fichier `/var/www/site_nul/index.html` avec le contenu de votre choix
- vous ajouterez dans la conf NGINX **un fichier dédié** pour servir le site web nul qui se trouve dans `/var/www/site_nul/`
  - écoute sur le port 80
  - répond au nom `site_nul.tp1`
  - sert le dossier `/var/www/site_nul/`
- n'oubliez pas d'ouvrir le port dans le firewall 🌼

---

☀️ **Sur `web.lan2.tp1`**

- n'oubliez pas de renommer la machine (`node2.lan2.tp1` devient `web.lan2.tp1`)
- setup du service Web
  - installation de NGINX
  - gestion de la racine web `/var/www/site_nul/`
  - configuration NGINX
  - service actif
  - ouverture du port firewall
- prouvez qu'il y a un programme NGINX qui tourne derrière le port 80 de la machine (commande `ss`)
- prouvez que le firewall est bien configuré

☀️ **Sur `node1.lan1.tp1`**

- éditez le fichier `hosts` pour que `site_nul.tp1` pointe vers l'IP de `web.lan2.tp1`
- visitez le site nul avec une commande `curl` et en utilisant le nom `site_nul.tp1`