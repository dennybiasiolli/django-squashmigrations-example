DB_NAME=test_database

# delete and recreate the database
dropdb $DB_NAME --if-exists
createdb $DB_NAME

# run the migrations
DB_NAME=$DB_NAME python manage.py migrate

# dump the data in a gzip file
pg_dump $DB_NAME --no-owner | gzip -9 > .dumps/django-squashmigrations-example.sql.gz

dropdb $DB_NAME
