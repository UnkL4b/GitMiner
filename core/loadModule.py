import sys
import os
import json
sys.path.append('../')
from config.banner import colors
from config.banner import banner 

def loadModule(module_name):
    try:
        with open("config/parsers.json",'r') as file_module:
            config = file_module.read()
            module_json = json.loads(config)
        if module_name not in module_json.keys():
            os.system('cls' if os.name == 'nt' else 'clear')
            print(banner())
            if module_name is None:
                pass
            else:
                print('\n{RED}[!]{END} Module {YELLOW}\"%s\"{END} not found in module file.'.format(**colors) % module_name)
            print('\n{GREEN}[+]{END} Modules found:'.format(**colors))
            for modules in module_json.keys():
                print('    {GREEN}+{END} %s'.format(**colors) % modules)
            print('\n\n')
            sys.exit()
        else:
            return(module_json[module_name])
            
    except FileNotFoundError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner())
        print("\n{RED}[!]{END} Configuration file not found in {YELLOW}\"configs/\"{END}.".format(**colors))
        print("{RED}[!]{END} Please, get file {YELLOW}parsers.json{END} in {YELLOW}github.com/UnkL4b/GitMiner{END} and put in {YELLOW}\"configs/\"{END}\n\n".format(**colors))
        sys.exit()
        
            
            
            

