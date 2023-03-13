#!/usr/bin/env python

import os

import django

from django.contrib.auth import get_user_model
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'koodausblogi.settings')
    django.setup()

    username=os.environ.get('ADMIN_USER_NAME', 'admin'),
    email=os.environ.get('ADMIN_USER_EMAIL', ''),
    password=os.environ['ADMIN_USER_PASSWORD']

    print(f"Creating superuser, {username!r}")
    get_user_model().objects.create_superuser(username, email, password)

if __name__ == '__main__':
    main()