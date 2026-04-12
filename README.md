# systemd-coffeed
systemd does it all, it even makes coffee!

# Why this project?

In the Linux community, systemd is often criticized for its "feature creep"—the tendency to absorb functions that were traditionally handled by separate, smaller tools. The project was born as a literal response to the long-standing French joke: if systemd is going to manage everything else, it might as well manage the caffeine intake of the sysadmins too.


The French phrase "faire tout sauf le café" (lit. "to do everything but the coffee") is used to describe a tool that has become so multifunctional it borders on the absurd.


*NOTE:* This specific idiom does not translate directly into English. An English speaker wouldn't say "it does everything but the coffee" to express this sentiment. Instead, they use the expression "everything and the kitchen sink."

*NOTE2:* I use systemd everyday, i don't hate the project. I'm a Fedora Linux and Alma Linux contributor <3


> **French version :**
> 
> Au sein de la communauté Linux, systemd est souvent critiqué pour son aspect usine à gaz, cette tendance à absorber des fonctions qui étaient traditionnellement gérées par des outils distincts et plus légers.
> 
> L'expression « faire tout sauf le café » est utilisée pour décrire un outil devenu tellement polyvalent qu'il en frise l'absurde.
> 
> NOTE : Cet blague ne se traduit pas littéralement en anglais. Un anglophone ne dirait pas « it does everything but the coffee » pour exprimer cette idée. À la place, il utilisera l'expression « everything and the kitchen sink » (littéralement : tout, y compris l'évier de la cuisine).
> 
> NOTE 2 : J'utilise systemd au quotidien, je ne déteste pas le projet. Je suis d'ailleurs contributeur pour Fedora Linux et Alma Linux <3.


# Installation

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
