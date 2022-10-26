Title: Disposable test databases and loading test data
Author: AC
Date: 2022-08-03
Tags: testing
Slug: loading-test-data
Summary: Setting up local testing with a disposable database
Status: draft

- Sqlite, pathlib, and pytest fixtures

## The relational database

### Sqlite
Good if you:
- Can't spin up a docker-compose network
- Have a simple use case

Sqlite is just a file, which means that you can easily spin it up, populate it with your test data, and throw it away at the end of a session. You can use most of the same tools and techniques that you'd use with Postgres via Sqlalchemy, too.

## The nosql database

### TinyDB
Is also just a file, so you can use it in situations where you can't or don't want to use docker-compose and a full mongodb instance.
