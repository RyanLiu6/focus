# nextcloud

# Setup
1. Clone the repo
2. Create `.env` with:

```
CLOUD_DOMAIN=<nextcloud domain>
```

3. Create `db.env` with:

```
MYSQL_PASSWORD=<PASSWORD>
MYSQL_DATABASE=nextcloud
MYSQL_USER=nextcloud
MYSQL_ROOT_PASSWORD=<PASSWORD>
```

4. Run it!

```
docker-compose up -d
```

# Backups
1. Nextcloud data is mounted at `$HOME/Data/nextcloud`

2. To back up MySQL

```
# Backup
docker exec CONTAINER /usr/bin/mysqldump -u root --password=<root password> nextcloud > backup.sql

# Restore
cat backup.sql | docker exec -i CONTAINER /usr/bin/mysql -u root --password=<root password> nextcloud
```
