import argument
import os
origin_extension = (".png")




files = sorted([os.path.join(argument.input_folder, f) for f in os.listdir(argument.input_folder)
     if os.path.isfile(os.path.join(argument.input_folder, f)) 
     and f.endswith(origin_extension)])

print(files)
