import yaml



def yaml_to_dict(yaml_dir):
    with open(yaml_dir, 'r') as file:
        data = yaml.safe_load(file)
    return data
        
        

