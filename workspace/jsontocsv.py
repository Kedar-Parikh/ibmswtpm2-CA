import json
import csv

with open("results.json") as f:
    data = json.load(f)

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["filesize", "enc_time", "dec_time", "encryption_throughput", "decryption_throughput"])

    for d in data:
        writer.writerow([
            d["plain_filesize (kb)"],
            d["enc_time(ms)"],
            d["dec_time(ms)"],
            d["enc_throughput(kb/ms)"],
            d["dec_throughput(kb/ms)"]
        ])