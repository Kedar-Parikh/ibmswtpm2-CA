import TestTPM
import os, time

filename = "plain.txt"
encryptedfilename = "cipher.bin"
decryptedfilename = "decrypted.txt"

def return_function_time_taken(func, *args, **kwargs):
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    result = end - start
    return result


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

    print(
        f'Flush Time: {flushtime}\n Create Primary Time: {createprimarytime}\n Create AES Key Time: {createaestime}\n Load AES Time: {loadaestime}\n AES Encryption Time: {aesencrypttime}\n AES Decryption Time: {aesdecrypttime}\n'
    )
else:
    print("[!] Error Initialising TPM, please ensure server is running and connection variables are in order")
    exit(-1)

