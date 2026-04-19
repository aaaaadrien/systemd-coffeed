# systemd-coffeed
systemd does it all, it even makes coffee!

# Why this project?

In the Linux community, systemd is often criticized for its "feature creep"—the tendency to absorb functions traditionally handled by separate, smaller tools. This project plays on the classic idioms about systemd's omnipotence, then flips them for humor:

- **French idiom**: *"Il fait tout sauf le café."*
  → **Project response**: *"Il fait MÊME le café !"*

- **English equivalent**: *"It does everything and the kitchen sink."*
  → **Project response**: *"It does EVERYTHING, even the kitchen sink!"*

- **Spanish idiom**: While Spanish lacks a direct equivalent to "faire tout sauf le café," we invented:
  *"Lo hace todo, hablar también."* (It does everything, even talk!)
  Because if systemd managed *everything else*, why not speech too?
  → **Project response**: *"Lo hace todo, hablar también."*

The ASCII art adapts to each language, reinforcing the absurdity of systemd’s hypothetical reach.

> **Note**: These idioms highlight how systemd is jokingly seen as an all-encompassing tool. The project’s responses twist them for comedic effect.

> **Note 2**: I use systemd daily and contribute to Fedora Linux and Alma Linux. This is a lighthearted tribute, not criticism. <3

---

> **Version française :**
>
> Dans la communauté Linux, systemd est souvent critiqué pour son *"feature creep"*, cette tendance à absorber des fonctions traditionnellement gérées par des outils distincts. Ce projet joue sur les idiomes classiques autour de l'omnipotence de systemd, puis les retourne de manière humoristique :
>
> - **Idiome français** : *« Il fait tout sauf le café. »*
>   → **Réponse du projet** : *« Il fait MÊME le café ! »*
>
> - **Équivalent anglais** : *« It does everything and the kitchen sink. »*
>   → **Réponse du projet** : *« It does EVERYTHING, even the kitchen sink! »*
>
> - **Idiome espagnol** : Bien qu'il n'existe pas d'équivalent direct en espagnol à *« faire tout sauf le café »*, nous avons inventé :
  *« Lo hace todo, hablar también. »* (Il fait tout, même parler !)
  *Parce que si systemd gérait déjà tout le reste, pourquoi pas la parole aussi ?*
>   → **Réponse du projet** : *« Lo hace todo, hablar también. »*
>
> L'art ASCII s'adapte à chaque langue pour renforcer l'absurdité de la portée hypothétique de systemd.
>
> > **Note** : Ces idiomes soulignent comment systemd est perçu comme un outil tout-puissant. Les réponses du projet les détournent pour un effet comique.
> >
> > **Note 2** : J'utilise systemd quotidiennement et contribue à Fedora et Alma Linux. Ce projet est un hommage léger, pas une critique. <3


# Installation

## Fedora Linux with adriend COPR

Add the adriend copr repo :
``` bash
sudo dnf copr enable adriend/fedora-apps
```

Install the package :
``` bash
sudo dnf install systemd-coffeed
```

## RHEL, Alma Linux and other EL based with adriend COPR

Add the adriend copr repo :
``` bash
sudo dnf copr enable adriend/el-apps
```

Install the package :
``` bash
sudo dnf install systemd-coffeed
```

## Manual installation

Clone the repo:
``` bash
git clone https://github.com/aaaaadrien/systemd-coffeed.git
```

Go to the project:
```bash
cd systemd-coffeed
```

Install: 
```bash
make install
```

# Uninstall

## Fedora Linux, RHEL, Alma Linux and other EL based

Remove the package :
``` bash
sudo dnf remove systemd-coffeed
```
## Manual uninstallation

Clone the repo:

```bash
git clone https://github.com/aaaaadrien/systemd-coffeed.git
```

Go to the project:

```bash
cd systemd-coffeed
```

Uninstall:

```bash
make uninstall
```

# Build RPM

Clone the repo:

```bash
git clone https://github.com/aaaaadrien/systemd-coffeed.git
```

Go to the project:

```bash
cd systemd-coffeed
```

Build:

```bash
make rpm
```

# Usage

Start the service:

```bash
systemctl start systemd-coffeed.service
```

See the status:

```bash
systemctl status systemd-coffeed.service
```

Example of output: 

```bash
○ systemd-coffeed.service - systemd does it all, it even makes the coffee
     Loaded: loaded (/usr/lib/systemd/system/systemd-coffeed.service; disabled; preset: disabled)
    Drop-In: /usr/lib/systemd/system/service.d
             └─10-timeout-abort.conf
     Active: inactive (dead)

avril 08 17:56:09 superlinux systemd-coffeed[2540693]:      ) (   )  (  (
avril 08 17:56:09 superlinux systemd-coffeed[2540693]:      ( )  (    ) )
avril 08 17:56:09 superlinux systemd-coffeed[2540693]:      _____________
avril 08 17:56:09 superlinux systemd-coffeed[2540693]:     <_____________> ___
avril 08 17:56:09 superlinux systemd-coffeed[2540693]:     |             |/ _ \
avril 08 17:56:09 superlinux systemd-coffeed[2540693]:     |               | | |
avril 08 17:56:09 superlinux systemd-coffeed[2540693]:     |               |_| |
avril 08 17:56:09 superlinux systemd-coffeed[2540693]:     |             |\___/
avril 08 17:56:09 superlinux systemd-coffeed[2540693]:      \___________/
avril 08 17:56:09 superlinux systemd[1]: systemd-coffeed.service: Deactivated successfully.
```
