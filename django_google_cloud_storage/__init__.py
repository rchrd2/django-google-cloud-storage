import os.path

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import Storage
from google.cloud import storage
from google.cloud.storage import Blob

__author__ = 'ckopanos@redmob.gr'


class GoogleCloudStorage(Storage):

    def __init__(self, project=None, bucket=None):
        if project is None:
            project = settings.GOOGLE_CLOUD_STORAGE_PROJECT
        if bucket is None:
            bucket = settings.GOOGLE_CLOUD_STORAGE_BUCKET
        self.client = storage.Client(project=project)
        self.bucket = self.client.get_bucket(bucket)

    def _open(self, name, mode='rb'):
        blob = Blob(name, self.bucket)
        file = ContentFile(blob.download_as_string(client=self.client))
        return file

    def _save(self, name, content):
        name = os.path.basename(name)
        new_name = name
        count = 0
        while True:
            blob = Blob(new_name, self.bucket, chunk_size=1024*256)
            if not blob.exists():
                break
            count += 1
            new_name = name + '.%d' % count
        blob.upload_from_file(content)
        blob.make_public()
        return new_name

    def delete(self, name):
        blob = Blob(name, self.bucket)
        blob.delete()

    def exists(self, name):
        blob = Blob(name, self.bucket)
        return blob.exists()

    def listdir(self, path=None):
        directories, files = [], []
        for b1 in self.bucket.list_blobs():
            files.append(b1.name)
        return directories, files

    def size(self, name):
        blob = Blob(name, self.bucket)
        return blob.size()

    def accessed_time(self, name):
        raise NotImplementedError

    def created_time(self, name):
        blob = Blob(name, self.bucket)
        return blob.timeCreated

    def modified_time(self, name):
        blob = Blob(name, self.bucket)
        return blob.updated

    def url(self, name):
        blob = Blob(name, self.bucket)
        return blob.public_url

    def statFile(self, name):
        raise NotImplementedError
