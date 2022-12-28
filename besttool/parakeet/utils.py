import hashlib


def hash_file(file, block_size=65536):
    hasher = hashlib.sha1()
    for buf in iter(partial(file.read, block_size), b''):
        hasher.update(buf)

    return hasher.hexdigest()


def upload_to(instance, filename):
    """
    :type instance: dolphin.models.File
    """
    instance.file.open()
    filename_base, filename_ext = os.path.splitext(filename)

    return "{0}.{1}".format(hash_file(instance.file), filename_ext)
