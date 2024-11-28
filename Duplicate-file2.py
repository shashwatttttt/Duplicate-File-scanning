import os
import hashlib


def hash_file(filename):
    """
    Generate an MD5 hash for the contents of a file.

    :param filename: Path to the file.
    :return: MD5 hash as a string.
    """
    h = hashlib.md5()
    try:
        with open(filename, 'rb') as file:
            while chunk := file.read(8192):
                h.update(chunk)
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        return None
    return h.hexdigest()


def find_duplicates(folder, log_file=None, extensions=None):
    """
    Find and report duplicate files in a directory.

    :param folder: Path to the folder to scan.
    :param log_file: Path to a log file where duplicate details will be saved (optional).
    :param extensions: List of allowed file extensions to scan (optional).
    """
    hashes = {}
    duplicates = []

    for dirpath, _, filenames in os.walk(folder):
        for f in filenames:
            full_path = os.path.join(dirpath, f)

            # Skip files if a filter is applied
            if extensions and not any(f.endswith(ext) for ext in extensions):
                continue

            # Hash the file and handle errors
            file_hash = hash_file(full_path)
            if not file_hash:
                continue

            # Check for duplicates
            if file_hash in hashes:
                duplicates.append((full_path, hashes[file_hash]))
                print(f"Duplicate found:\n  {full_path}\n  {hashes[file_hash]}")
            else:
                hashes[file_hash] = full_path

    # Save duplicates to a log file if specified
    if log_file:
        with open(log_file, 'w') as log:
            for dup in duplicates:
                log.write(f"Duplicate found:\n  {dup[0]}\n  {dup[1]}\n")
        print(f"\nDuplicate details saved in {log_file}")


if __name__ == "__main__":
    import argparse

    # Argument parser for command-line usage
    parser = argparse.ArgumentParser(description="Duplicate File Scanner")
    parser.add_argument(
        "folder", help="Path of the folder to scan for duplicate files"
    )
    parser.add_argument(
        "--log", help="Path to save the duplicate details as a log file", default=None
    )
    parser.add_argument(
        "--extensions",
        nargs="*",
        help="File extensions to include (e.g., .txt .jpg)",
        default=None,
    )

    args = parser.parse_args()

    # Validate folder path
    if not os.path.isdir(args.folder):
        print(f"Error: The path '{args.folder}' is not a valid directory.")
    else:
        find_duplicates(args.folder, log_file=args.log, extensions=args.extensions)
