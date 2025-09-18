# Realtime Chat with Django and Redis

## Development

### Dependencies

The following dependencies must be installed before development:

- Docker
- Python 3.13
- uv

### Setup

Next, we must run supporting services in the background.

```
$ docker compose up --detach
```

If this is the first time setting up the development environment, the database
must be initialized by running the migration scripts.

```
$ uv run manage.py migrate
```

Finally, we can start the development web server:

```
$ uv run manage.py runserver
```

Now you can access the application in your browser at [localhost:8000/chat](http://localhost:8000/chat)
