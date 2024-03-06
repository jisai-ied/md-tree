from main import get_tree, replace_content

replace_content('TEST.md', get_tree(ignore_list=["__pycache__"]))