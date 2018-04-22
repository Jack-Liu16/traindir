#coding=utf-8
import sys
import os
import re

path1 = "C:\Users\jackliu\Desktop\kolla-ansible-automation-v1.4.tar\kolla-ansible-automation-v1.4\kolla-ansible-automation\yum_pkgs\libvirt"
path2 = "C:\Users\jackliu\Desktop\kolla-ansible-automation-v1.4.tar\kolla-ansible-automation-v1.4\kolla-ansible-automation\yum_pkgs\devel_pkgs"
path3 = "C:\Users\jackliu\Desktop\kolla-ansible-automation-v1.4.tar\kolla-ansible-automation-v1.4\kolla-ansible-automation\docker_ce_rpm"

def countf(path):
	lt = os.listdir(path)
	print lt
	return len(lt)

if __name__ == '__main__':
	
	a = countf(path1)
	b = countf(path2)
	c = countf(path3)
	print int(a+b+c)
