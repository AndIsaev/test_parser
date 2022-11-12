# test_parser
## To run project locally:
```shell
docker-compose up -d --build
```
Server will be available at the localhost:
 - `localhost:5000`
 - `localhost:5000/api/docs/` - SWAGGER UI
 - `http://localhost:5000/api/article` - get all articles


## Run migrations:

### initial db

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
