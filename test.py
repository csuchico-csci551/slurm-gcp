import subprocess
import time
import re

cmd=subprocess.Popen("gcloud auth list", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
cmd.wait()
cmd_out = cmd.stdout.read()
# cmd_err = cmd.stderr.read()
lst = re.findall('\S+@\S+', cmd_out)
email = lst[0]
print(email)

# Does a list of files, and


cmd=subprocess.Popen("gcloud compute ssh g1-login1 --zone=us-central1-b --command 'sinfo'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
cmd.wait()
cmd_out = cmd.stdout.read()
cmd_err = cmd.stderr.read()
print(cmd_err)
while "command not found" in cmd_err:
    time.sleep(60)
    cmd=subprocess.Popen("gcloud compute ssh g1-login1 --zone=us-central1-b --command 'sinfo'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cmd.wait()
    cmd_out = cmd.stdout.read()
    cmd_err = cmd.stderr.read()
    print(cmd_err)

print("Ready")
