import os
import sys
from jlclient import jarvisclient
from jlclient.jarvisclient import *

jarvisclient.token = os.getenv("TOKEN_JARVIS")

class InstanceNotFoundError(Exception):
    pass

class ScriptNotFoundError(Exception):
    pass

class InstanceAlreadyRunningError(Exception):
    pass

def get_instance(instance_name: str):

    instance_choosed = None

    instances = User.get_instances()
    
    for instance in instances:
        if instance.name == instance_name:
            instance_choosed = instance
    
    if instance_choosed is None:
        raise InstanceNotFoundError(f"Instância '{instance_name}' não encontrada.")
    
    return instance_choosed
    
def run_instance(instance_name: str, script_name: str):

    instance = get_instance(instance_name)
    if instance.status == 'Running':
        raise InstanceAlreadyRunningError(f"Instância '{instance_name}' já está rodando.")
    
    dict_script = None
    
    scripts = User.get_scripts()
    
    for script in scripts:
        if script_name in script['script_name']:
            
            dict_script = script
            break

    if dict_script is None:
        raise ScriptNotFoundError(f"Script '{script_name}' não encontrado.")

    instance.resume(script_id = dict_script['script_id'])
    print('Resume instance finished')

def stop_instance(instance_name: str):

    instance = get_instance(instance_name)
    if instance.status == 'Running':
        instance.pause()

    print('Stop instance completed')

if __name__ == '__main__':
   
    instance_name= os.getenv("INSTANCE_NAME")
    script_name = os.getenv("SCRIPT_NAME")
   
    if len(sys.argv) != 2:
        print("Usage: python apiclient.py <function_name>")
        sys.exit(1)

    function_name = sys.argv[1]
    
    if function_name == 'run_instance':
        run_instance(instance_name, script_name)
    elif function_name == 'stop_instance':
        stop_instance(instance_name)
    else:
        print(f"Function '{function_name}' not recognized.")
        sys.exit(1)