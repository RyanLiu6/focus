# Focus

<p align="center">
<img src="_images/moonlight_vigil.png" alt="focus" title="focus" />
</p>


Self-hosted tools and services I have setup for myself at home.

The most recent update to config files and this README has been inspired by [this](https://github.com/BaptisteBdn/docker-selfhosted-apps) amazing repo!

## Services
### Core
* [traefik](traefik/) - reverse proxy and SSL manager
* [borg-backup](borg-backup/) - backup scripts (local and AWS)
* [watchtower](watchtower/) - automatic docker images update
* [pihole](pihole/) - combination of WireGuard, PiHole, and Unbound

### Content
* [plex](plex/) - media system
* [jellyfin](jellyfin/) - media system, alternative to plex
* [nextcloud](nextcloud/) - file-hosting software system
* [transmission](transmission/) - fast, easy, and free BitTorrent client

### Games
* [foundryvtt](foundryvtt/) - [FoundryVTT](https://foundryvtt.com/), a Virtual Table Top for games
* [gloomhaven](gloomhaven/) - My own copy of Gloomhaven Helper, an assistant to play Gloomhaven

### Misc
* [homebridge](homebridge/) - (WIP) SmartHome integration with Apple's HomeKit

## Usage
Each folder has description and usage for individual services, should you wish only do so.

In order to run things smoothly, a script has been provided `generate_compose.py`, that, depending on input, aggregates compose files and `.env` files to generate one main file to work with.
