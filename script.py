import os
import sys


# if len(sys.argv) != 3:
#     print("Make sure you entered the script as such: python script.py <badhash> <goodhash>")
#     # sys.exit(1)  

script_name = sys.argv[0]
badhash = sys.argv[1]
goodhash = sys.argv[2]

os.system(f'git bisect start c1a4be04b972b6c17db242fc37752ad517c29402 e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c') 
os.system('git bisect run python manage.py test')
os.system('git bisect reset')
