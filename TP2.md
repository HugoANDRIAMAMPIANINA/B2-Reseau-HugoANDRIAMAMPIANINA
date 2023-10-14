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
[hugoa@node1 ~]$ ip n s
10.1.2.254 dev enp0s3 lladdr 08:00:27:f6:4f:f9 STALE
10.1.1.12 dev enp0s3 lladdr 08:00:27:f6:4f:f9 STALE
10.1.1.1 dev enp0s3 lladdr 0a:00:27:00:00:0a REACHABLE
10.1.1.254 dev enp0s3 lladdr 08:00:27:f6:4f:f9 REACHABLE

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

- prouvez que vous avez un accès internet (ping d'une IP publique)
- prouvez que vous pouvez résoudre des noms publics (ping d'un nom de domaine public)

☀️ **Accès internet LAN1 et LAN2**

- ajoutez une route par défaut sur les deux machines du LAN1
- ajoutez une route par défaut sur les deux machines du LAN2
- configurez l'adresse d'un serveur DNS que vos machines peuvent utiliser pour résoudre des noms
- dans le compte-rendu, mettez-moi que la conf des points précédents sur `node2.lan1.tp1`
- prouvez que `node2.lan1.tp1` a un accès internet :
  - il peut ping une IP publique
  - il peut ping un nom de domaine public

# III. Services réseau

**Adresses IP et routage OK, maintenant, il s'agirait d'en faire quelque chose nan ?**

Dans cette partie, on va **monter quelques services orientés réseau** au sein de la topologie, afin de la rendre un peu utile que diable. Des machines qui se `ping` c'est rigolo mais ça sert à rien, des machines qui font des trucs c'est mieux.

## 1. DHCP

Petite **install d'un serveur DHCP** dans cette partie. Par soucis d'économie de ressources, on recycle une des machines précédentes : `node2.lan1.tp1` devient `dhcp.lan1.tp1`.

**Pour rappel**, un serveur DHCP, on en trouve un dans la plupart des LANs auxquels vous vous êtes connectés. Si quand tu te connectes dans un réseau, tu n'es pas **obligé** de saisir une IP statique à la mano, et que t'as un accès internet wala, alors il y a **forcément** un serveur DHCP dans le réseau qui t'a proposé une IP disponible.

> Le serveur DHCP a aussi pour rôle de donner, en plus d'une IP disponible, deux informations primordiales pour l'accès internet : l'adresse IP de la passerelle du réseau, et l'adresse d'un serveur DNS joignable depuis ce réseau.

**Dans notre TP, son rôle sera de proposer une IP libre à toute machine qui le demande dans le LAN1.**

> Vous pouvez vous référer à [ce lien](https://www.server-world.info/en/note?os=Rocky_Linux_8&p=dhcp&f=1) ou n'importe quel autre truc sur internet (je sais c'est du Rocky 8, m'enfin, la conf de ce serveur DHCP ça bouge pas trop).

---

Pour ce qui est de la configuration du serveur DHCP, quelques précisions :

- vous ferez en sorte qu'il propose des adresses IPs entre `10.1.1.100` et `10.1.1.200`
- vous utiliserez aussi une option DHCP pour indiquer aux clients que la passerelle du réseau est `10.1.1.254` : le routeur
- vous utiliserez aussi une option DHCP pour indiquer aux clients qu'un serveur DNS joignable depuis le réseau c'est `1.1.1.1`

---

☀️ **Sur `dhcp.lan1.tp1`**

- n'oubliez pas de renommer la machine (`node2.lan1.tp1` devient `dhcp.lan1.tp1`)
- changez son adresse IP en `10.1.1.253`
- setup du serveur DHCP
  - commande d'installation du paquet
  - fichier de conf
  - service actif

☀️ **Sur `node1.lan1.tp1`**

- demandez une IP au serveur DHCP
- prouvez que vous avez bien récupéré une IP *via* le DHCP
- prouvez que vous avez bien récupéré l'IP de la passerelle
- prouvez que vous pouvez `ping node1.lan2.tp1`

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