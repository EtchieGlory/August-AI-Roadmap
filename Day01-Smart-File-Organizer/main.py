# Import calls
from pathlib import Path
from config import FILE_TYPES
import shutil

# setting arrangement path to test_folder
folder = Path('test_folder')
print(folder.exists())


# looping through files in test_folder
for item in folder.iterdir():
   if item.is_file():
      category = 'Others'
      
        
      for file_type, extensions in FILE_TYPES.items():
         if item.suffix.lower() in extensions:
            category = file_type
            break
      destination = folder/category
      destination.mkdir(exist_ok = True)
      try:
         shutil.move(str(item), str(destination/item.name))
         print(f'{item.name} moved to {category}')
      except OSError:
         print('File already exists')