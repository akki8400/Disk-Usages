# Disk-Usages
This script is for checking file sizes in particular mount

#Usages

Clone complete repository at any desired location on linux machine. 

Pre-Requistes 
Pyhton 2.7

Note: Both files should be in same directoty. 

Execution: 
```
python disk-run.py mount-directory-path
```
Eg. 
```
python disk-run.py  /tmp
```
Output: 
```
{     "files":     [       {"/tmp/foo", 1000},       {"/tmp/bar", 1000000},       {"/tmp/buzzz", 42},     ], } 
```


File disk-run.py file call a shell script disk-use.sh, which contains a single command of du and the result is shown in above format.

