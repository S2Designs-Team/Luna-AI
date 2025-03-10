import os

# Add __init__.py file in all folders
for root, dirs, files in os.walk("."):
    if not files:
        with open(os.path.join(root, "__init__.py"), "w") as f:
            pass

print("Added __init__.py files in all directories.")