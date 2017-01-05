import subprocess
import re, os
from collections import defaultdict

id_pattern = re.compile("linux-(image|headers|image-extra)-(\d+?.\d+?.\d+?-\d+).*install")
def list_kernels():
    outs = subprocess.check_output("dpkg --get-selections | grep linux", shell=True)
    kernels = id_pattern.findall(outs)
    dicts = defaultdict(set)
    for kernel in kernels:
        dicts[kernel[0]].add(kernel[1])
    integrated = set.intersection(*dicts.values())
    damaged = set.union(*dicts.values()) - integrated
    current = re.findall("(\d+?.\d+?.\d+?-\d+)", subprocess.check_output("uname -a", shell=True))
    latest = list(set.union(*dicts.values()))
    latest.sort()
    latest = latest[-1]
    if not current:
        raise Exception("cant find current kernel")
    current = current[0]
    if current in integrated:
        integrated.remove(current)
    elif current in damaged:
        print "WARNING:current kernel is not integrated."
        damaged.remove(current)
    return current, latest, integrated, damaged

def remove():
    current, latest, integrated, damaged = list_kernels()
    if latest > current:
        print "WARNING: current kernel is not the latested kernel installed, you may want to reboot."
        flag = None
        while not flag in ['1', '2', '3']:
            flag = raw_input("which action to take?\n1->remove current 2->remove latest 3->exit\nyour choice:")
            if flag == "3": return
            elif flag == "1":
                if not latest in integrated:
                    print "latest kernel is not integrated, exit..."
                    return
                integrated.remove(latest)
                integrated.add(current)
            elif flag == "2":
                pass
    if damaged:
        print "WARNING:%s is not integrated."%" ".join(damaged)
        flag = None
        while not flag in ['Y', 'y', 'N', 'n']:
            flag = raw_input("remove them?(Y|N)")
    for id_ in integrated:
        for fullname in ["linux-image-%s-generic", "linux-headers-%s"]:
            os.system("sudo apt-get remove -y "+ fullname%id_)



if __name__ == "__main__":
  remove()

