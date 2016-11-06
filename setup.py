from setuptools import setup, find_packages

version = "0.0.3"

setup(
    name = "django-google-cloud-storage",
    version = version,
    license = "GNU GENERAL PUBLIC LICENSE",
    packages = ["django_google_cloud_storage"],
    description = "Google Cloud Storage file backend for Django",
    long_description = open("README.md").read(),
    author = "Christos Kopanos, Richard Caceres",
    author_email = "ckopanos@redmob.gr, me@rchrd.net",
    install_requires = ["google.cloud"],
    url = "https://github.com/sureshvv/django-google-cloud-storage/",
    download_url = "https://github.com/sureshvv/django-google-cloud-storage/tarball/" + version,
    keywords = ["django", "appengine", "google", "cloud storage"],
    classifiers = [],
)
