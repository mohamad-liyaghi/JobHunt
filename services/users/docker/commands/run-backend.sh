echo 'Applying Migrations'
alembic upgrade head

echo 'Running Server'
python src/main.py