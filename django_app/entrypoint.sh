#!/bin/bash
set -e

sleep 10

echo "Application des migrations..."
python manage.py migrate

echo "Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

echo "Création de superadmin par défaut"
python manage.py createsuperuser --noinput || true

echo "Démarrage du serveur Django..."
exec python manage.py runserver 0.0.0.0:8000