### There are 2 scripts:
1. get_copy.py - copies the entire volume and creates a dump
2. restore_from_copy.py - restores the instance and the database

In these scripts, it is needed to add some data about the copied instance (variables at the top of the script). This is data from docker-compos files. For example, container names, database username and password, database name and future url (or ip, for example http://194.182.189.110)

### Instruction:   

Host A - old   
Host B - new  
It is assumed that locally all actions will be performed in the standard directory (/home/ubuntu/), and in the container in the directory (/var/www/html/)

Procedure:
1. Add the get_copy.py file to host A (for example, via git):
git clone https://github.com/MarkBorodin/copy_restore_instances.git
cp ./copy_restore_instances/* ~/.
Add this data to the get_copy.py file and run it. A snapshot folder will be created containing mautic and dump.
2. Copy the snapshot folder to host B. Command:
scp -r /path/user@host:/path/
example:
scp -r /home/ubuntu/snapshot ubuntu@194.182.176.212:/home/ubuntu/
3. Copy to the host B the restore_from_copy.py file (for example, via git):
git clone https://github.com/MarkBorodin/copy_restore_instances.git
cp ./copy_restore_instances/* ~/.
Add data to the restore_from_copy.py file and run it.
Warning! old_url format: http://194.182.189.110
The files in the container will be replaced and the database will be restored.