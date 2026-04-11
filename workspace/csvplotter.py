import pandas as pd
import matplotlib.pyplot as plt

# load csv
df = pd.read_csv("results.csv")

df = df.sort_values("filesize")


filesize = df["filesize"]
enc_time = df["enc_time"]
dec_time = df["dec_time"]
enc_throughput = df["encryption_throughput"]
dec_throughput = df["decryption_throughput"]


def plot_graph(x, y, xlabel, ylabel, title, filename):
    plt.figure()
    plt.plot(x, y, marker='o')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid()
    
    plt.tight_layout()
    
    plt.savefig(filename)


plot_graph(filesize, enc_time,
           "File Size (kb)", "Encryption Time (ms)",
           "File Size vs Encryption Time", "enc_time.png")


plot_graph(filesize, dec_time,
           "File Size (kb)", "Decryption Time (ms)",
           "File Size vs Decryption Time", "dec_time.png")


plot_graph(filesize, enc_throughput,
           "File Size (kb)", "Encryption Throughput (kb/ms)",
           "File Size vs Encryption Throughput", "enc_throughput.png")


plot_graph(filesize, dec_throughput,
           "File Size (kb)", "Decryption Throughput (kb/ms)",
           "File Size vs Decryption Throughput", "dec_throughput.png")


plt.show()