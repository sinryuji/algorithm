import time

now = time.localtime()
print(f"{now.tm_year}-{str(now.tm_mon).zfill(2)}-{now.tm_mday}")