import subprocess
import time
import os

class TestTPM:
    def flushtpm(self):
        subprocess.run(["tpm2_flushcontext", "-t"])

    def load_aes_key(self):
        subprocess.run([
            "tpm2_load",
            "-C", "primary.ctx",
            "-u", "aes.pub",
            "-r", "aes.priv",
            "-c", "aes.ctx"
        ])

    def encrypt(self, input, output):
        subprocess.run([
            "tpm2_encryptdecrypt",
            "-c", "aes.ctx",
            "-o", output,
            input
        ])

    def decrypt(self, input, output):
        subprocess.run([
            "tpm2_encryptdecrypt", "-d"
            "-c", "aes.ctx",
            "-o", output,
            input
        ])