# Contributing to Found. Poll Buddy

- Clone the repository and install the dependencies:

```shell
git clone https://github.com/FoundTechnology/paul-bot.git
```

- Run the docker-compose file to start and migrate the database:

```shell
docker-compose up -d
```

- Add the following settings to your `.env` file to configure the bot.

```
BOT_TOKEN=<Your bot token goes here.>
DATABASE_URL=<Your database URL goes here.>
ERR_CHANNEL=<Optional. The ID of a Discord channel where the bot will send errors to.>
DBG_CHANNEL=<Optional. The ID of a Discord channel where the bot will send debug messages to.>
MAX_DB_CONNECTIONS=<Optional. The maximum number of database connections to open. This depends on your database hosting plan.>
```

Run the bot:

```shell
poetry shell  # This will start a shell with the development environment. You only need to do it once 
paul
```