# test_parser
## To run project locally:
```shell
docker-compose up -d --build
```
Server will be available at the localhost:
 - `localhost:5000`
 - `localhost:5000/api/docs/` - SWAGGER UI
 - `http://localhost:5000/api/article` - get all articles

## What can be done better:
- scale the logic of work (now the tie is only on one table)
- tests
- letters and typing
- ci/cd on github
- rewrite to asynchronous code, which is more optimal when parsing several dozen resources
- make logging for the entire project

## Run migrations:

### initial db for developing

```shell
make init db
```
### migrate
```shell
make migrate
```
### upgrade
```shell
make upgrade
```
