import os

def clean_filename(filename):
    name, ext = os.path.splitext(filename)

    # Remove leading 'x' if it exists
    if name.lower().startswith('x'):
        name = name[1:]

    # Remove spaces and lowercase
    cleaned = name.lower().replace(" ", "") + ext.lower()
    return cleaned

def rename_files_only(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            old_path = os.path.join(dirpath, filename)
            new_filename = clean_filename(filename)
            new_path = os.path.join(dirpath, new_filename)

            if old_path != new_path:
                try:
                    if not os.path.exists(new_path):
                        os.rename(old_path, new_path)
                        print(f"Renamed: {old_path} -> {new_path}")
                    else:
                        print(f"Skipped (already exists): {new_path}")
                except Exception as e:
                    print(f"Error renaming {old_path}: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        target_path = sys.argv[1]
    else:
        target_path = os.getcwd()

    rename_files_only(target_path)
    print(f"\n✅ File renaming (removed 'x', lowercase, no spaces) completed in: {target_path}")
