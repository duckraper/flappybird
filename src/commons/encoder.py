from base64 import b64decode, b64encode


class Encoder:
    @staticmethod
    def validate(data: bytes | str):
        if isinstance(data, str):
            data = data.encode()
        return data

    @staticmethod
    def encode(data: str | bytes) -> bytes:
        return b64encode(Encoder.validate(data))

    @staticmethod
    def decode(data: str | bytes) -> bytes:
        return b64decode(Encoder.validate(data))
