import os
from pathlib import Path

my_file = Path("espeak")
if my_file.is_file():
    print("yes")
else:
    print("no")
