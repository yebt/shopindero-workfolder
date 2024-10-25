import os

repo_url = "https://gitlab.com/metalmessiah87/shopindero.git"

folders = ["shopindero", "mysql"]

for dir in folders:
    if not os.path.exists(dir):
        os.makedirs(dir)
        print(f"La carpeta '{dir}' ha sido creada.")
    else:
        print(f"La carpeta '{dir}' ya existe.")

shopindero_path = "shopindero"

# Verify
if os.path.exists(shopindero_path) and not os.listdir(shopindero_path):
    print(f"La carpeta '{shopindero_path}' está vacía. Clonando el repositorio...")
    os.system(f"git clone {repo_url} {shopindero_path}")
else:
    print(f"La carpeta '{shopindero_path}' ya contiene archivos o no existe.")

