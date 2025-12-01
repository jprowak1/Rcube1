import sys
import pil
print("--- Loaded Modules ---")
for module_name, module_object in sys.modules.items():
    print(f"Module: {module_name}")
    # Optionally, print the path to the module's file if available
    if hasattr(module_object, '__file__'):
        print(f"  Path: {module_object.__file__}")
    print("--------------------")
    