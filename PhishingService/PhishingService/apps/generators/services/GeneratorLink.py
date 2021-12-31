import hashlib
from base64 import encode


class GeneratorLink:

    @staticmethod
    def GetGenerateLinkForEmail(email: str) -> str:
        bytes_email = email
        generated_link = hashlib.md5(email.encode()).hexdigest()
        return generated_link
