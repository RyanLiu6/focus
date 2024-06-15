# Traefik <img src="https://upload.wikimedia.org/wikipedia/commons/1/1b/Traefik.logo.png" width="24">
[Traefik](https://doc.traefik.io/traefik/) is an open-source reverse proxy and load balancer.

Docker Image is from traefik, found [here](https://hub.docker.com/r/traefik/traefik).

## Setup
1. Generate a password with `generate_password.sh`

> [!NOTE]
> This step is entirely optional. To skip this step, edit docker-compose.yml and remove the line
> at the bottom that specifies the password

2. Update `traefik.yml` with your correct contact information (Email)

3. Create an `.env` file with:
```ini
DOMAIN=example
TLD=com
ADMIN_PASSWORD=<password from step 4 with duplicate $ removed>
```

4. Add DNS Provider specific configuration to `.env` and `docker-compose.yml`. In my case, I'm using CloudFlare, and so my file will have the following:
```ini
CLOUDFLARE_DNS_API_TOKEN=<some token>
```

```yaml
  environment:
    - CLOUDFLARE_DNS_API_TOKEN=${CLOUDFLARE_DNS_API_TOKEN}
```

Other DNS Providers will have differing configuration. You can find providers [here](https://doc.traefik.io/traefik/https/acme/#providers) and additional configuration [here](https://go-acme.github.io/lego/dns/).

5. Run it!
```bash
docker-compose up -d
```

## Updates
This container will have its image automatically updated via [watchtower](https://ryanliu6/focus/watchtower).

## Backups
N/A
