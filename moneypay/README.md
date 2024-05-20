Pull latest code
```console
git pull
```

Create lib directory put btix library and extract data

Edit/Create common\local_conf.py

Build image for development
```console
docker-compose build
```

Run instance
```console
docker-compose up -d
```

Check logs
```console
docker-compose logs -f
```

Run terminal
```console
docker-compose exec app_dev sh
```

Shutdown instance
```console
docker-compose down
```

Build image for production
```console
docker-compose -f docker-compose.prod.yml
```

Run instance for production
```console
docker-compose -f docker-compose.prod.yml
```

Check logs for production
```console
docker-compose -f docker-compose.prod.yml logs -f
```

Run terminal for production
```console
docker-compose -f docker-compose.prod.yml exec app sh
```

Shutdown instance for production
```console
docker-compose -f docker-compose.prod.yml down
```




