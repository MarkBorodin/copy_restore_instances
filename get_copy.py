import os
import time

# DATA
backend_container_name = 'automationmonkey_latest'
db_name: str = 'mautic3'
db_username: str = 'root'
db_password: str = 'mysecret'
db_container_name: str = 'mauticdb_test'

# COMMANDS
get_volume = f'docker cp {backend_container_name}:/var/www/html ./snapshot/'
get_db_dump = f'docker exec -i {db_container_name} mysqldump -u{db_username} -p{db_password} --databases {db_name} --no-tablespaces --skip-comments > ./snapshot/dump.sql'  # noqa

commands_list = [get_volume, get_db_dump]

for command in commands_list:
    print(f'command is executed: "{command}"')
    os.system(command)
    time.sleep(1)
