### To create image
```shell
docker build . -f .\Dockerfile -t <image-name>
```

### Run django python shell
```shell
uv run python manage.py shell
```

### create migrations
```shell
uv run python manage.py makemigrations
```

### apply migrations
```shell
uv run python manage.py migrate
```
