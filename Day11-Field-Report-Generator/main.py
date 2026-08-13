import os

total_size = 0
for root, folders, files in os.walk("documents"):
    for file in files:
        file_path = os.path.join(root, file)
        size = os.path.getsize(file_path)
        total_size += size
print(f"Total size of documents: {total_size}")