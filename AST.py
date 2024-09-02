import ast


def get_class_code(filename, class_name):
    with open(filename, 'r') as file:
        file_content = file.read()
    
    tree = ast.parse(file_content)
    class_node = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == class_name:
            class_node = node
            break
    
    if class_node is None:
        return None
    
    class_lines = file_content.splitlines()[class_node.lineno-1:class_node.end_lineno]
    
    return '\n'.join(class_lines)

# Example usage
filename = 'c:/users/armin/test.py'
class_name = '_get_tensor_values'
class_code = get_class_code(filename, class_name)
print(class_code)
