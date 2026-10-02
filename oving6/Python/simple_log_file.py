from datetime import datetime

log_message = f"(simple_log_file.py) {datetime.now()}: Wrote this to file. \n"

try:
	with open("does_not_exist.txt", "r") as file: #With is used to clean up after resource is used instead of having to manually close it.
		file.read()

except FileNotFoundError: #can also use OSError as it is more general and covers more.
	print("File does not exist")

try:
	with open("../does_not_exist.txt", "r") as file:
		file.read()
except FileNotFoundError:
	print("File does not exist")