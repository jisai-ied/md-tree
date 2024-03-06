<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Markdown Tree](#markdown-tree)
  - [Use](#use)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Markdown Tree

## Use

Use the following code in your markdown code to generate a directory tree write where you want to add your directory tree:

```md
Content
<!-- _TREE_ -->
<!-- _ENDTREE_ -->
More content
```

For running the program, you should run the following command in the terminal:

```bash
./main.py --filename README.md --level 3 --ignore_list "node_modules, .git, .idea, __pycache__"
```
