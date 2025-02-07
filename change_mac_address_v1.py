import subprocess as sp

sp.call(["ifconfig", "eth0","down"])
sp.call(["ifconfig","eth0","hw","ether","00:11:22:33:44:55"])
sp.call(["ifconfig", "eth0","up"])