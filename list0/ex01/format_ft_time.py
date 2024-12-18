from time import time
from datetime import datetime

current_time = time()

current_date = datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {current_time:,.4f} \
or {current_time:.2e} in scientific notation")
print(f"Current date: {current_date}")
