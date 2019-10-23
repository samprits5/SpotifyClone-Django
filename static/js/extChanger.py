import os
path = os.getcwd()
Allfiles = os.listdir(path)
for each in Allfiles:
	name ,ext = os.path.splitext(each)
	if os.name == "posix":
		if "." == name[0]:
			continue
	if ext==".txt":
		old = os.path.join(path , each)
		newName = name + ".js"
		new = os.path.join(path , newName)
		os.rename(old,new)
	if ext==".js":
		old = os.path.join(path , each)
		newName = name + ".txt"
		new = os.path.join(path , newName)
		os.rename(old,new)