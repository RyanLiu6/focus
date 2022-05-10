# Traefik
For my purposes, I'll be using Traefik as my proxy.

# Setup
1. Create an `.env` file with:
```
MONITOR_DOMAIN=`<traefik domain>`
```

2. Create and edit permissions to `traefik/acme.json`

3. Edit `traefik/traefik.yml` with the correct email.

4. Generating hashed password for Traefik: https://medium.com/@techupbusiness/add-basic-authentication-in-docker-compose-files-with-traefik-34c781234970

```
echo $(htpasswd -nbB <USER> "<PASS>") | sed -e s/\\$/\\$\\$/g
```

5. Run it!
```
docker-compose up -d
```
