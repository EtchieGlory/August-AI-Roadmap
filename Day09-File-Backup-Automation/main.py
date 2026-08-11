import os
import shutil


def backup_files():
	source = input("Enter source folder: ").strip()
	backup = "backup"
	try:
		os.makedirs("backup", exist_ok = True)
		files = os.listdir(source)
		count = 0
		for file in files:
			source_path = os.path.join(source, file)
			backup_path = os.path.join(backup, file)
			
			if os.path.isfile(source_path):
				shutil.copy2(source_path, backup_path)
				print(f"{file} has been backed up successlly")
				count +=1
		print (f"{count} files were sucessfully backed up")
	except FileNotFoundError:
		print(f"Source folder not found")
	
backup_files()