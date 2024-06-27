import ast

def extract_function_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read(), filename=file_path)

        function_names = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                function_names.append(node.name)

        return function_names

if __name__ == "__main__":
    file_path = "/home/kali/school_telgram_bot/telegram_bot/utils1.py"
    function_names = extract_function_names(file_path)

    # Print the extracted function names
    names_list=[]
    print("Extracted function names:")
    for name in function_names:
        names_list.append(name)

    print(len(names_list))