import django
import os


# We manually designate which settings we will be using in an environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fileupload.tests.test_settings')


# `pytest` automatically calls this function once when tests are run.
def pytest_configure():
    django.setup()