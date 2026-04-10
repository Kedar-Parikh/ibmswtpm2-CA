import TestTPM
import os, time, json
import argparse

parser = argparse.ArgumentParser(description="Script that supports TPM CA Research")
parser.add_argument("plain_filename", help="Name of plaintext file")
args = parser.parse_args()
filename = args.plain_filename
encryptedfilename = "cipher.bin"
decryptedfilename = "decrypted.txt"

def return_function_time_taken(func, *args, **kwargs):
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    result = end - start
    return result


def save_metrics_simple(filesize, enc_time, cipher_filesize, dec_time, enc_throughput, dec_throughput, filename="results.json"):
    entry = {
        "plain_filesize (bytes)": filesize,
        "enc_time(s)": enc_time,
        "cipher_filesize(bytes)": cipher_filesize,
        "dec_time(s)": dec_time,
        "enc_throughput(bytes/s)": enc_throughput,
        "dec_throughput(bytes/s)": dec_throughput
    }

    data = []

    
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                data = json.load(f)
            except:
                data = []

    
    data.append(entry)

    
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

tpm = TestTPM.TestTPM()
filesize = os.path.getsize(filename)
result = tpm.initialisetpm()

if(not result):
    flushtime = return_function_time_taken(tpm.flushtpm)
    createprimarytime = return_function_time_taken(tpm.createprimary)
    return_function_time_taken(tpm.flushtpm)
    createaestime = return_function_time_taken(tpm.createaeskeys)
    return_function_time_taken(tpm.flushtpm)
    loadaestime = return_function_time_taken(tpm.load_aes_key)
    aesencrypttime = return_function_time_taken(tpm.encrypt, filename, encryptedfilename)
    return_function_time_taken(tpm.flushtpm)
    return_function_time_taken(tpm.load_aes_key)
    aesdecrypttime = return_function_time_taken(tpm.decrypt, encryptedfilename, decryptedfilename)
    cipher_filesize = os.path.getsize(encryptedfilename)


    encrypt_throughput = (filesize/aesencrypttime)
    decrypt_throughput = (cipher_filesize/aesdecrypttime)

    
    save_metrics_simple(filesize, aesencrypttime, cipher_filesize, aesdecrypttime, encrypt_throughput, decrypt_throughput)
    
else:
    print("[!] Error Initialising TPM, please ensure server is running and connection variables are in order")
    exit(-1)

