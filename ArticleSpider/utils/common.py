import hashlib


def get_md5(text):
    if isinstance(text, str):
        text = text.encode('utf-8')
    h = hashlib.md5()
    h.update(text)

    return h.hexdigest()
