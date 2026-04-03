import TestTPM
import json, os, time

filename = "plain.txt"
encryptedfilename = "cipher.bin"
decryptedfilename = "decrypted.txt"
metricsfilename = "metrics.json"

def measure_metrics(label, func):
    start = time.perf_counter
    func()
    time_in_ms = round((time.perf_counter() - start) * 1000, 2)
    print(f"{label:30s} {time_in_ms} ms")
    return {"Operation: ": label, "Elapsed Time (in ms)": time_in_ms}

def main():
    tpm_tester = TestTPM()
    metrics = []
    filesize = os.path.getsize(filename)
    
    print("[*] Startup and Key Generation")
    metrics.append(measure_metrics("start",          tpm_tester.start))
    metrics.append(measure_metrics("create_primary", tpm_tester.createprimary))
    metrics.append(measure_metrics("flush",          tpm_tester.flushtpm))
    metrics.append(measure_metrics("create_aes_key", tpm_tester.createaeskeys))
    metrics.append(measure_metrics("flush",          tpm_tester.flushtpm))

    
