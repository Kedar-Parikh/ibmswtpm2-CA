
# AES Encryption using IBM SW TPM 2.0
  
This documentation serves as a reference guide for automating the AES
encryption testing process using the IBM Software TPM 2.0 simulator. It
supports an efficient workflow for execution, data collection, and
analysis.
## Script Flow

  

``` mermaid

graph LR

A(Start TPM Server)

A --> B(Initialize TPM)

B --> C(Create Primary & AES Keys)

C --> D(Load Keys)

D --> E(Encryption)

D --> F(Decryption)

E --> G(Data Collection & Visualization)

F --> G

```


## Commands

  

These commands were used as a reference while building the automation script.

  

------------------------------------------------------------------------

  

### 1. Start TPM Server

  

``` bash

./tpm_server &

```

  

------------------------------------------------------------------------

  

### 2. Set TPM Connection Environment

  

``` bash

export  TPM2TOOLS_TCTI="mssim:host=localhost,port=2321"

```

  

------------------------------------------------------------------------

  

### 3. Initialize TPM

  

``` bash

tpm2_startup  -c

```

  

------------------------------------------------------------------------

  

### 4. Clear Loaded Objects (Prevents Slot Errors)

  

``` bash

tpm2_flushcontext  -t

```

  

------------------------------------------------------------------------

  

### 5. Create Primary Key

  

``` bash

tpm2_createprimary  -C  o  -g  sha256  -G  rsa  -c  primary.ctx

```

  

------------------------------------------------------------------------

  

### 6. Create AES Key

  

``` bash

tpm2_create  -C  primary.ctx  -G  aes256  -u  aes.pub  -r  aes.priv

```

  

------------------------------------------------------------------------

  

### 7. Load AES Key

  

``` bash

tpm2_load  -C  primary.ctx  -u  aes.pub  -r  aes.priv  -c  aes.ctx

```

  

------------------------------------------------------------------------

  

### 8. Create Sample Plaintext

  

``` bash

echo  "Secret Message by Kedar" > plain.txt

```

  

------------------------------------------------------------------------

  

### 9. Encrypt Data

  

``` bash

tpm2_encryptdecrypt  -c  aes.ctx  -o  encrypted.dat  plain.txt

```

  

------------------------------------------------------------------------

### 10. Clear loaded objects and load keys again (Prevents Slot Errors)

``` bash

tpm2_flushcontext  -t

```
  

``` bash

tpm2_load  -C  primary.ctx  -u  aes.pub  -r  aes.priv  -c  aes.ctx

```

  

------------------------------------------------------------------------

  

### 11. Decrypt Data

  

``` bash

tpm2_encryptdecrypt  -d  -c  aes.ctx  -o  decrypted.txt  encrypted.dat

```

  

------------------------------------------------------------------------

  

### 12. Verify Decryption

  

``` bash

cat  decrypted.txt

```

  

------------------------------------------------------------------------

  

### 13. Flush Loaded Keys

  

Flush AES key:

  

``` bash

tpm2_flushcontext  -c  aes.ctx

```

  

Flush primary key:

  

``` bash

tpm2_flushcontext  -c  primary.ctx

```

  

## Conclusion

  

- Successful AES-256 encryption and decryption using IBM SW TPM 2.0

- Automated workflow ready for batch testing

- Supports structured data collection for performance analysis
