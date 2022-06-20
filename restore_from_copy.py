import os
import time


# DATA
url: str = 'http://localhost:8083'
old_url: str = 'http://localhost:8082'
db_name: str = 'mautic3'
db_username: str = 'root'
db_password: str = 'mysecret'
db_container_name: str = 'mauticdb_test'
main_container_name: str = 'automationmonkey_latest'

# PATH
base_dir = './'
snapshot_dir = base_dir + 'snapshot/'
path_to_local_file: str = snapshot_dir + 'app/config/local.php'


# COMMANDS
chown = f'docker exec {main_container_name} bash -c "chown -R www-data:www-data /var/www/html"'
copy_all = f'docker cp ./snapshot/. {main_container_name}:/var/www/html/.'
restore_dump = f'docker exec -i {db_container_name} mysql -u {db_username} -p{db_password} {db_name} < ./snapshot/dump.sql'


def change_local_file(path_to_local_file):
    with open(path_to_local_file, 'r') as f:
        text = f.read()
        # lines = f.readlines()
        # for line in lines:
        #     if line.startswith("'site_url' =>"):
        #         old_url = line.split('=>')[1].strip().replace("'", "").replace(",", "")
        #     else:
        #         old_url = "'',"
        text = text.replace(f"'site_url' => '{old_url}',", f"'site_url' => '{url}',")

    with open(path_to_local_file, 'w') as f:
        f.write(text)


change_local_file(path_to_local_file)
commands_list = [copy_all, chown, restore_dump]

for command in commands_list:
    print(f'command is executed: "{command}"')
    os.system(command)
    time.sleep(1)
