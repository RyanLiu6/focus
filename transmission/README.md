# Transmission <img src="https://upload.wikimedia.org/wikipedia/commons/6/6d/Transmission_icon.png" width="24">
[Transmission](https://transmissionbt.com/) is a highly customizable and free BitTorrent client.

Docker Image is from Linuxserver, found [here](https://hub.docker.com/r/linuxserver/transmission).

## Setup
1. Create an `.env` file with
```
TRANSMISSION_USERNAME=<some_username>
TRANSMISSION_PASSWORD=<some_password>
BT_DOMAIN=`<some_domain>`
```

2. Ensure that port 51413 is open, on the host (via `ufw`) and on the router.
For `ufw`:
```bash
sudo ufw allow 51413
```

For your router, you'll need to configure that manually as each router will look different!

3. Create `${HOME}/Data/transmission` and cp `settings.json` over.
> [!NOTE]
> This step is optional since most settings are personalized towards my own needs.
> Feel free to skip this step or modify `settings.json` to your own needs!

4. Run it!
```bash
docker-compose up -d
```

## Notes
### Updates
This container will have its image automatically updated via [watchtower](https://ryanliu6/focus/watchtower).

### Backup
Data for Transmission is stored locally at `${HOME}/Data/transmission`, and if you wish, create or update cronjob to backup data with:

```
0 2 * * 4 sudo tar -cf /home/<user>/Data/transmission/backups/transmission_`date +\%F`.tar /home/<user>/Data/transmission
```
