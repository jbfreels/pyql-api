# pyql-api
Sample GraphQL python API (tested on MacOSX)

Original tutorial here: https://www.apollographql.com/blog/complete-api-guide

# setup
`python3 -m venv .`

`source bin/activate`

`pip install -r requirements.txt`

### database
`docker run --name pyql-api -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres:12-alpine`

Update **SQLALCHEMY_DATABASE_URI** in *\_\_init\_\_.py* if you make any changes to pw/port, or if 
you're not going with local db then update with your appropriate postgres URI.

# run
`flask run`

