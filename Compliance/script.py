import pandas as pd
import re
import os

file_path = input("Enter CSV file name (example: report.csv): ").strip()

if not os.path.exists(file_path):
    print("❌ File not found.")
    exit()

# Read CSV
df = pd.read_csv(file_path)

# Ensure columns exist
required_cols = ["Description", "Amazon AWS Compliance Checks"]
for col in required_cols:
    if col not in df.columns:
        print(f"❌ Column missing: {col}")
        exit()

# 🔥 FIX: Force columns to string to avoid dtype errors
df["Description"] = df["Description"].astype(str)
df["Amazon AWS Compliance Checks"] = df["Amazon AWS Compliance Checks"].astype(str)

status_pattern = r'"(.*?)"\s*:\s*\[[A-Z]+\]'

for index in df.index:
    desc = df.at[index, "Description"]

    match = re.search(status_pattern, desc)
    if match:
        extracted = match.group(1)

        # Move text
        df.at[index, "Amazon AWS Compliance Checks"] = extracted

        # Remove from description
        df.at[index, "Description"] = re.sub(status_pattern, '', desc).strip()

# Remove leading numeric IDs like 2.13, 1.2.3
df["Amazon AWS Compliance Checks"] = df["Amazon AWS Compliance Checks"].str.replace(
    r'^\s*\d+(\.\d+)*\s+', '', regex=True
)

output_file = "cleaned_" + os.path.basename(file_path)
df.to_csv(output_file, index=False)

print("✅ Done! Output:", output_file)
