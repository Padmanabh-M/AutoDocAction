import os
from pathlib import Path
import ast
import shutil



def save_file(file_path, function_defs):
    
    # Code to check if src_for_doc folder exists, if not make one.
    if os.path.exists('./src_for_doc'):
        pass
    else:
        # print("Making new src_for_doc folder")
        os.mkdir("./src_for_doc")


    # Code to check if folder for file exists, if not make one
    parent_folder_path = "/".join(file_path.split("/")[:-1])


    new_parent_folder_path = "./src_for_doc" + parent_folder_path[1:]


    if os.path.exists(new_parent_folder_path):
        # print("new_parent_folder_path exists")
        pass
    else:
        os.makedirs(new_parent_folder_path)


    # Code to open py file at folder, and save contents
    working_directory = os.getcwd()
    with open(working_directory + "/src_for_doc" + file_path[1:], 'w') as file:
        initPath = working_directory + "/src_for_doc" + "/".join(file_path.split("/")[:-1])[1:] + "/__init__.py"
        # print(initPath)
        if not os.path.exists(initPath):
            with open(initPath, 'w') as init_file:
                pass

        for func in function_defs:
            file.write(ast.unparse(func) + "\n"*4)




def extract_functions(file_path):
    print(file_path)
    with open(file_path, 'r', encoding="utf8") as file:
        tree = ast.parse(file.read())

    function_defs = []

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            function_defs.append(node)

    if function_defs:    
        return function_defs
    else:
        False





def process_directory(directory_path):

    working_directory = os.getcwd()
    # Removing if exists: src_for_doc
    if os.path.exists(working_directory + "/src_for_doc"):
        shutil.rmtree(working_directory + "/src_for_doc")

    # Removing if exists: docs
    if os.path.exists(working_directory + "/docs"):
        shutil.rmtree(working_directory + "/docs")

    os.makedirs(working_directory + "/docs")
    with open(working_directory + "/docs/requirements.txt", 'w') as file:
        file.write("sphinx\nsphinx_rtd_theme\nghp-import")


    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):  # Process only Python files
                if not file.endswith('crawler.py'): # Except the crawler
                    file_path = os.path.join(root, file)
                    function_defs = extract_functions(file_path)
                    if function_defs:
                        save_file(file_path, function_defs)
                
        



directory_path = '.'
process_directory(directory_path)





