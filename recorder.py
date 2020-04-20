import sys
import json
import time

path = sys.argv[1]
data = sys.argv[2]

with open(path, "r") as f:
    try:
        log = json.load(f)
    except Exception as e:
        print(f"failed to load log: {e}")
        log = []

with open(path, "w") as f:
    log.append((time.time(), data))
    json.dump(log, f)
