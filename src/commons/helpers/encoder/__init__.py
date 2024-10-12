from base64 import b64encode, b64decode


def __validate(data: bytes | str):
    if isinstance(data, str):
        data = data.encode()
    return data


def encode(data: str | bytes) -> bytes:
    return b64encode(__validate(data))


def decode(data: str | bytes) -> bytes:
    return b64decode(__validate(data))
