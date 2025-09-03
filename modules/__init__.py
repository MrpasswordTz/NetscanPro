# modules/__init__.py
import os
import importlib

base_dir = os.path.dirname(__file__)

for filename in os.listdir(base_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]
        module = importlib.import_module(f".{module_name}", package="modules")
        globals().update(vars(module))  # inject all functions/classes
