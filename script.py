import os
import sys


if len(sys.argv) != 3:
    print("Make sure you entered the script as such: python script.py <badhash> <goodhash>")
    sys.exit(1)  

script_name = sys.argv[0]
badhash = sys.argv[1]
goodhash = sys.argv[2]

os.system(f'git bisect start {badhash} {goodhash}') 
os.system('git bisect run python manage.py test')
os.system('git bisect reset')
