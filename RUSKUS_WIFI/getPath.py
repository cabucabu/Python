#!/usr/bin/python
def autoparts():
	parts_dict={}
	list_of_parts = open('include/Ruckus.cfg', 'r')
	for line in list_of_parts:
		k,v = line.strip().split('=')
		parts_dict[k] = v
	return parts_dict
 
test_dict = autoparts()
print test_dict['controller_user']