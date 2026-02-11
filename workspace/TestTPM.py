import subprocess
import time
import os

class TestTPM:
    def flushtpm(self):
        subprocess.run(["tpm2_flushcontext", "-t"])

    def load_aes_key(self):
        subprocess.run([
            "tpm2-load",
            "-C", "primary.ctx",
            "-u", "aes.pub",
            "-r", "aes.priv",
            "-c", "aes.ctx"
        ])

    