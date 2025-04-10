import os
import subprocess

#Make sure folders exist
os.makedirs("data", exist_ok=True)

#Define the kaggle dataset
dataset = "dhruvildave/covid19-deaths-dataset"

#Run the Kaggle API command
print(f"📥 Downloading dataset: {dataset}")
subprocess.run(["kaggle", "datasets", "download", "-d", dataset, "-p", "data", "--unzip"])

print("✅ Download complete!")