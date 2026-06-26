import os
import shutil


def delete_pycache(parent_folder):
    for root, dirs, _ in os.walk(parent_folder):
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            try:
                shutil.rmtree(pycache_path)
                print(f"Deleted: {pycache_path}")
            except Exception as e:
                print(f"Failed to delete {pycache_path}: {e}")


if __name__ == "__main__":
    current_directory = os.getcwd()
    delete_pycache(current_directory)