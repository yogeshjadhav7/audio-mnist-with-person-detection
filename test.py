import os
for file in os.listdir("./recordings/"):
    if file.endswith(".wav"):
        print(os.path.join(file))
