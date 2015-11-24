#!/user/sbin/python

import datetime
import subprocess
import os
import sys
import time

base_tcpdump = 'tcpdump %s -w %s.pcap'
base_kill = 'kill -2 %s'
interval = 1800
pcap_dir = '.'

if __name__ == '__main__':

  if len(sys.argv) < 3:
    print "[ERROR] Need parameters. First is filter. Second is file location."
    exit()
  filter = sys.argv[1]
  pcap_dir = sys.argv[2]
  if not os.path.exists(pcap_dir):
    os.mkdir(pcap_dir)
  print "[INFO] Run tcpdump as 'tcpdump %s'." % filter
  while True:
    filename = datetime.datetime.now().strftime('%y%m%d%H%M%S');
    filename = os.path.join(pcap_dir, filename)
    print filename
    tcpdump = base_tcpdump % (filter, filename)
    proc = subprocess.Popen([tcpdump], shell=True)
    time.sleep(1)
    pid = proc.pid
    print "[INFO] Start tcpdump to wirte to %s." % filename
    time.sleep(interval)
    kill = base_kill % pid
    os.system(kill)
