import os
import csv

out_dir = "/concourse-results"
os.makedirs(out_dir, exist_ok=True)

# TXT file
with open(f"{out_dir}/hello.txt", "w") as f:
    f.write("Hello from Concourse!\n")

# CSV file
with open(f"{out_dir}/data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "ip"])
    writer.writerow(["router1", "10.0.0.1"])
    writer.writerow(["router2", "10.0.0.2"])

print("Files generated successfully")
