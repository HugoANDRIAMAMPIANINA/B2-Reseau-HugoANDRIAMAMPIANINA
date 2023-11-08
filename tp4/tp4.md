# TP4 : I'm Socketing, r u soketin ?

## I. Simple bs program

### 1. First steps

[bs_server_I1.py](bs_server_I1.py)
[bs_client_I1.py](bs_client_I1.py)

```
[hugoa@server ~]$ git clone https://github.com/HugoANDRIAMAMPIANINA/B2-Reseau-HugoANDRIAMAMPIANINA.git

[hugoa@server ~]$ cd B2-Reseau-HugoANDRIAMAMPIANINA/tp4

[hugoa@client ~]$ git clone https://github.com/HugoANDRIAMAMPIANINA/B2-Reseau-HugoANDRIAMAMPIANINA.git

[hugoa@client ~]$ cd B2-Reseau-HugoANDRIAMAMPIANINA/tp4
```

```
# Côté serveur
[hugoa@server tp4]$ python bs_server_I1.py
Meooooo !

# Côté client
[hugoa@client tp4]$ python bs_client_I1.py
Hi mate!
```

```
[hugoa@server ~]$ ss -alntp | grep 13337
LISTEN 0      1          10.1.1.11:13337      0.0.0.0:*    users:(("python",pid=3407,fd=3))
```

## II

### 2. A. Logs serveur

```
# Création du fichier de log et modification des permissions

[hugoa@server tp4]$ sudo mkdir /var/log/bs_server/
[hugoa@server tp4]$ sudo touch /var/log/bs_server/bs_server.log
[hugoa@server tp4]$ sudo chown -R hugoa:hugoa /var/log/bs_server/
[hugoa@server tp4]$ sudo chmod +x /var/log/bs_server/
```

### 2. B. Logs client

```
# Création du fichier de log et modification des permissions

[hugoa@client tp4]$ sudo mkdir /var/log/bs_client/
[hugoa@client tp4]$ sudo touch /var/log/bs_client/bs_client.log
[hugoa@client tp4]$ sudo chmod -R +x /var/log/bs_client/
[hugoa@client tp4]$ sudo chown -R hugoa:hugoa /var/log/bs_client/
```