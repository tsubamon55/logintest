import configparser
_conf = configparser.ConfigParser()
_conf.read('settings.ini')

select_key = _conf['SERVER']['secret_key']
session_lifetime = int(_conf['SERVER']['session_lifetime'])
