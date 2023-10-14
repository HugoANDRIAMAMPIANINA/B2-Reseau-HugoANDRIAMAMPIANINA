# TP1 : Maîtrise réseau du poste

- [TP1 : Maîtrise réseau du poste](#tp1--maîtrise-réseau-du-poste)
- [I. Basics](#i-basics)
- [II. Go further](#ii-go-further)
- [III. Le requin](#iii-le-requin)

# I. Basics

> Tout est à faire en ligne de commande, sauf si précision contraire.

☀️ **Carte réseau WiFi**

Déterminer...

- l'adresse MAC de votre carte WiFi
    ```
    PS C:\Users\hugoa> ipconfig /all

        Carte réseau sans fil Wi-Fi :

        Adresse physique . . . . . . . . . . . : A0-59-50-B5-97-CB
    ```
- l'adresse IP de votre carte WiFi
    ```
    PS C:\Users\hugoa> ipconfig
    
    Carte réseau sans fil Wi-Fi :

        Adresse IPv4. . . . . . . . . . . . . .: 192.168.240.96
    ```
- le masque de sous-réseau du réseau LAN auquel vous êtes connectés en WiFi
    ```
    PS C:\Users\hugoa> ipconfig

    Carte réseau sans fil Wi-Fi :

        Masque de sous-réseau. . . . . . . . . : 255.255.255.0
    ```
    Notation CIDR : /24

---

☀️ **Déso pas déso**

Site utilisé pour les calculs : [Calculator.net](https://www.calculator.net/ip-subnet-calculator.html)

```
Adresse du réseau : 192.168.240.0
Adresse de Broadcast : 192.168.240.255
Nombre d'IP dispo : 254
```

---

☀️ **Hostname**

```
PS C:\Users\hugoa> hostname
SeigneurHugoPCMasterRace
```

---

☀️ **Passerelle du réseau**

```
# IP passerelle
PS C:\Users\hugoa> ipconfig

Carte réseau sans fil Wi-Fi :

   Passerelle par défaut. . . . . . . . . : fe80::3c96:35ff:fea4:ead8%27
                                       192.168.240.38

# IP passerelle + MAC passerelle
PS C:\Users\hugoa> arp -a 192.168.240.38

Interface : 192.168.240.96 --- 0x1b
  Adresse Internet      Adresse physique      Type
  192.168.240.38        3e-96-35-a4-ea-d8     dynamique
```

---

☀️ **Serveur DHCP et DNS**

```
PS C:\Users\hugoa> ipconfig /all

Carte réseau sans fil Wi-Fi :

   Serveur DHCP . . . . . . . . . . . . . : 192.168.240.38
   Serveurs DNS. . .  . . . . . . . . . . : 192.168.240.38
```

---

☀️ **Table de routage**

```
PS C:\Users\hugoa> netstat -r

IPv4 Table de routage
===========================================================================
Itinéraires actifs :
Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
          0.0.0.0          0.0.0.0   192.168.240.38   192.168.240.96     55
```

---

# II. Go further

> Toujours tout en ligne de commande.

---

☀️ **Hosts ?**

- faites en sorte que pour votre PC, le nom `b2.hello.vous` corresponde à l'IP `1.1.1.1`

```
# ligne ajouté dans le fichier hosts
	1.1.1.1		b2.hello.vous
```

- prouvez avec un `ping b2.hello.vous` que ça ping bien `1.1.1.1`

```
PS C:\Users\hugoa> ping b2.hello.vous

Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=202 ms TTL=55
Réponse de 1.1.1.1 : octets=32 temps=87 ms TTL=55
Réponse de 1.1.1.1 : octets=32 temps=75 ms TTL=55
Réponse de 1.1.1.1 : octets=32 temps=70 ms TTL=55

Statistiques Ping pour 1.1.1.1:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 70ms, Maximum = 202ms, Moyenne = 108ms
```

---

☀️ **Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...**

```
PS C:\Users\hugoa> netstat -f

Connexions actives

  TCP    192.168.240.96:65279   199.232.170.139:https  ESTABLISHED
```

```
Ip du serveur : 199.232.170.139  
Port du serveur : port 443 (https)
Port ouvert sur PC : 65279
```

---

☀️ **Requêtes DNS**

Déterminer...

- à quelle adresse IP correspond le nom de domaine `www.ynov.com`

```
PS C:\Users\hugoa> nslookup www.ynov.com

Réponse ne faisant pas autorité :
Nom :    www.ynov.com
Addresses:  2606:4700:20::ac43:4ae2
          2606:4700:20::681a:ae9
          2606:4700:20::681a:be9
          172.67.74.226
          104.26.11.233
          104.26.10.233
```

- à quel nom de domaine correspond l'IP `174.43.238.89`

```
PS C:\Users\hugoa> nslookup 174.43.238.89

Nom :    89.sub-174-43-238.myvzw.com
Address:  174.43.238.89
```

---

☀️ **Hop hop hop**

```
PS C:\Users\hugoa> tracert www.ynov.com

Détermination de l’itinéraire vers www.ynov.com [2606:4700:20::ac43:4ae2]
avec un maximum de 30 sauts :

  1     9 ms     6 ms    11 ms  2a02-8440-6341-d909-0000-0000-0000-002d.rev.sfr.net [2a02:8440:6341:d909::2d]
  2    52 ms    35 ms    41 ms  2a02-8440-6341-d909-0000-0033-f18d-3340.rev.sfr.net [2a02:8440:6341:d909:0:33:f18d:3340]
  3   125 ms    84 ms    72 ms  fdff:8440:6006:1038::9d
  4    49 ms    39 ms    65 ms  2a02-8400-1001-fc0e-0000-0000-0001-0001.rev.sfr.net [2a02:8400:1001:fc0e::1:1]
  5     *        *        *     Délai d’attente de la demande dépassé.
  6     *        *        *     Délai d’attente de la demande dépassé.
  7     *        *        *     Délai d’attente de la demande dépassé.
  8     *       94 ms     *     fc00:0:0:100::1f
  9    46 ms    80 ms     *     fc00:0:0:100::78
 10    71 ms    74 ms    75 ms  2400:cb00:19:200::48
 11    73 ms    69 ms    47 ms  2400:cb00:19:3::
 12   108 ms    77 ms    56 ms  2606:4700:20::ac43:4ae2

Itinéraire déterminé.
```

---

☀️ **IP publique**

```
PS C:\Users\hugoa> curl -4 icanhazip.com

77.205.152.62
```

---

☀️ **Scan réseau**

```
PS C:\Program Files (x86)\Nmap> .\nmap -sP 192.168.240.1/24

Nmap scan report for 192.168.240.38
Host is up (0.76s latency).
MAC Address: 3E:96:35:A4:EA:D8 (Unknown)
Nmap scan report for 192.168.240.96
Host is up.
Nmap done: 256 IP addresses (2 hosts up) scanned in 48.13 seconds
```

# III. Le requin

☀️ **Capture ARP**

[Capture ARP](./captures/arp.pcap)

Filtre : `arp`

---

☀️ **Capture DNS**

```
# Commande utilisée pour la requête dns
PS C:\Users\hugoa> nslookup www.ynov.com
```

[Capture DNS](./captures/dns.pcap)

Filtre : `dns.qry.name == "www.ynov.com"`

---

☀️ **Capture TCP**

[Capture TCP](./captures/tcp.pcap)

Filtre : `tcp`