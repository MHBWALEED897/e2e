import os
import sys
import shutil
from setuptools import setup, Extension
from Cython.Build import cythonize

# File jisko compile karna hai
target_file = "waleede2enew.py"

# Check agar file exist karti hai
if not os.path.exists(target_file):
    print(f"Error: {target_file} not found!")
    sys.exit(1)

print("Starting compilation for Python 3.12...")

# Setup configuration
setup(
    name='FacebookBot',
    ext_modules=cythonize(
        Extension(
            name="waleede2enew",  # Output name (without .so)
            sources=[target_file],
        ),
        compiler_directives={'language_level': "3", 'always_allow_keywords': True}
    ),
    script_args=["build_ext", "--inplace"]
)

# Safai (Cleanup) - C file aur build folder delete karna
if os.path.exists("build"):
    shutil.rmtree("build")
if os.path.exists("waleede2enew.c"):
    os.remove("waleede2enew.c")

print("\n✅ Compilation Complete!")
print(f"Check for the .so file starting with 'waleede2enew'.")
