import subprocess


class TestTPM:
    def start(self):
        subprocess.run(["tpm2_startup", "-c"])

    def flushtpm(self):
        subprocess.run(["tpm2_flushcontext", "-t"])

    def createprimary(self):
        subprocess.run([
            "tpm2_createprimary", "-C", "o",
            "-g", "sha256", "-G", "rsa", "-c", "primary.ctx"
        ])

    def createaeskeys(self):
        subprocess.run([
            "tpm2_create", "-C", "primary.ctx",
            "-G", "aes256cfb", "-u", "aes.pub", "-r", "aes.priv"
        ])

    def load_aes_key(self):
        subprocess.run([
            "tpm2_load", "-C", "primary.ctx",
            "-u", "aes.pub", "-r", "aes.priv", "-c", "aes.ctx"
        ])

    def encrypt(self, input, output):
        subprocess.run([
            "tpm2_encryptdecrypt", "-c", "aes.ctx", "-o", output, input
        ])

    def decrypt(self, input, output):
        subprocess.run([
            "tpm2_encryptdecrypt", "-d", "-c", "aes.ctx", "-o", output, input
        ])