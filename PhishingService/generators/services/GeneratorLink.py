import hashlib


class GeneratorLink:
    SECURITY = "SECRET_KEY"

    @staticmethod
    def GetGenerateLinkForEmail(email: str) -> str:
        generated_link = hashlib.md5(email).hexdigest()
        return generated_link
