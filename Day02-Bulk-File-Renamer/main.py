from pathlib import Path


folder = Path ('test_folder')
prefix = input("Enter a prefix: ")
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
count = 1


for number, file in enumerate(folder.iterdir(), start = 1):
   if file.is_file() and file.suffix in image_extensions:
      new_name = f'{preffix}_{count:03}{file.suffix}'
      destination = file.parent/new_name
      file.rename(destination)
      print(f'{file.name} --> {new_name}')
      count+=1