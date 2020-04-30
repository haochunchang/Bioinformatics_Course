import re
import os
import subprocess

IDs = [
    f
    for f in os.listdir("./students")
    if re.search("^[r|b|f][0-9]{2}[a-zA-Z0-9][0-9]{5}$", f)
]

for ID in IDs:
    cmd = "python3 grade.py {} grade.csv".format(ID)
    code = subprocess.run(cmd.split()).returncode
    if code:
        print(ID)
