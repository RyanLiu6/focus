# Focus

Collection of self-hosted services for my personal multi-media home server.

Full credits to [this](https://github.com/BaptisteBdn/docker-selfhosted-apps) repo for introducing borg and watchtower, as those configs were directly from there! Documentation for this repo has been influenced for the better from there as well.

## Services
### Core
* [traefik](traefik/) - reverse proxy and cert manager
* [borg-backup](borg-backup/) - backups
* [watchtower](watchtower/) - automatic docker images update

### Content
* [plex](plex/) - media system
* [jellyfin](jellyfin/) - media system
* [nextcloud](nextcloud/) - file storage
* [transmission](transmission/) - torrent client

### Games
* [foundryvtt](foundryvtt/) - [FoundryVTT](https://foundryvtt.com/), a Virtual Table Top for games

### Misc
* [homebridge](homebridge/) - (WIP) SmartHome integration with Apple's HomeKit

## Usage
Each folder has description and usage for individual services, should you wish only do so. Otherwise, an aggregated, "centralized" docker-compose.yml file can be generated via the provided `generate_compose.py` file. Please look at the [Docker](#Docker) section for further details.

## Docker
Some basic knowledge of Docker and Docker Compose would be good, but not required, as it is fairly easy to pick up and learn. For Docker, please refer to [this](https://docs.docker.com/get-started/overview/) document, and [this](https://docs.docker.com/compose/gettingstarted/) for Docker Compose.

The provided `generate_compose.py` script uses my custom Python Library, [Vigor](https://www.github.com/ryanliu6/vigor) to interface with the CLI to generate an aggregated compose file with the correct values from related `.env` files. This is done so that each individual service is self-contained within their own subdirectories and can be run independently of each other. But, the intended usage is to pick and choose which services to run for your servers and only generate a compose file for what is needed.

To be specific, Traefik will always be included in the generated compose file as the absolute core, since its needed to serve traffic. The other core services of Borg and Watchtower are optional and can be included manually.

There's a flag to include everything, `--all`, which will generate a compose file that includes all possible services. Further extension of this flag to generate specific subsets of services is something that can be considered, but with how many services are in consideration now, it is not of much help for the average user.

### Examples
To generate and run for just Plex, Transmission and Nextcloud:
```bash
./generate_compose --service plex --service transmission --service nextcloud
docker compose run -d
```

### Note
My personal preference is to use images from folks at [linuxserver](https://www.linuxserver.io/). Feel free to change these Docker images to official or any other 3rd party images.
