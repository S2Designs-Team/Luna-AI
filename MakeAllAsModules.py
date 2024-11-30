import os

# Aggiungi il file __init__.py in tutte le cartelle
for root, dirs, files in os.walk("."):
    if not files:
        with open(os.path.join(root, "__init__.py"), "w") as f:
            pass

print("Aggiunti file __init__.py in tutte le directory.")