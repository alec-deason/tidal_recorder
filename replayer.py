import sys
import json
import time
import pexpect
import pexpect.replwrap
import subprocess

with open(sys.argv[1], 'r') as f:
    log = json.load(f)


tidal_startup = subprocess.check_output('bash -c "ghc-pkg field -f ~/.cabal/store/ghc-$(ghc --numeric-version)/package.db tidal data-dir --simple-output"', shell=True).strip().decode("utf8") + "/BootTidal.hs"
tidal = subprocess.Popen(["ghci", "-ghci-script", tidal_startup])
tidal = pexpect.replwrap.REPLWrapper(f"ghci -ghci-script {tidal_startup}", "tidal>", None, continuation_prompt="tidal|")

current_time = log[0][0]
for (next_time, data) in log:
    #TODO: sleep has no guarentees about how long it will actually last...
    time.sleep(next_time - current_time)
    current_time = next_time
    tidal.run_command(data)
time.sleep(3.0)
tidal.child.kill(0)
print("done")
