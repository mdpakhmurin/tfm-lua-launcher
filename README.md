# Transformice Lua Launcher
## 💡 Idea
The idea of the project is to simplify the creation and launch of modules in the Lua programming language in the Transformice game. Currently, the user can only send one file and must do it manually.

## 🛠 Implementation
The project, created in Python, allows you to combine several Lua files into one by adding support for the dofiles command. After creating one file from several, the program automatically finds the Transformice game window and launches the Lua module in it. Currently, Lua launch is only supported on the Windows operating system.

## 📈 Advantages
This project significantly simplifies the process of creating and launching modules in the Transformice game, allowing users to focus on developing their modules rather than on routine tasks for their installation and launch. It also provides more flexible work with modules, allowing you to use several files to organize code.

## ⌨ Usage
1. You need to download this project.
2. Run the project: Python TFM-LUANCHER.py path/to/lua/directory (the entry point file is the main.lua file)
3. Use the lua command dofile('path/to/file') to attach additional files to the assembly. Remember that all elements are global
