# Duplicate-File-scanning
A Python script that efficiently scans directories for duplicate files based on their content, saving you valuable disk space and helping maintain organized file systems.

  🌟 Why is This Script Essential?
    Duplicate files can confuse your storage, especially in large file collections. By scanning and identifying duplicates, this script helps:

  1. Save Disk Space: Reclaim storage by removing unnecessary file copies.
  2. Enhance Organization: Keep your file systems clean and manageable.
  3. Prevent Confusion: Eliminate outdated or redundant files.
  4. Improve Performance: Reduce the workload on backup or synchronization tools by removing duplicates.
     
🔍 Levels of Finding Duplicate Files
  1. Name-Based Detection
     Identifies duplicates based on file names. While fast, it is often inaccurate as files with the same name might differ in content.
  2. Content-Based Detection (This Script)
     It uses a hashing algorithm (MD5 by default) to compare file contents. This ensures that files with different names but identical content are detected.

🚀 Features:
    - Content-Based Comparison: Finds duplicates using file hashes, ensuring accuracy.
    - Recursive Scanning: Automatically scans all subdirectories.
    - Customizable Filters: Specify file types/extensions to include or exclude.
    - Error Handling: Safely skips inaccessible files without interrupting the scan.
    - Logging Support: Saves duplicate file details in a log file for easy reference.
    - Command-Line Arguments: Flexible configuration using arguments for paths, filters, and more.
    
📥 Installation:
    Prerequisites
    
    Python 3.x installed on your system.
    Steps: 
    
    Clone this repository:
    git clone   https://github.com/shashwatttttt/Duplicate-File-scanning.git

    Navigate to the project directory:
    cd duplicate-file-scanner

🎛️ Usage
  Command-Line Arguments
  Run the script with the following options:

  folder: Path of the folder to scan for duplicates. (Required)
  --log: Path to save duplicate details into a log file. (Optional)
  --extensions: Specify file extensions to include (e.g., .jpg .txt). (Optional)
  Example Commands
  Basic Scan:
  . python duplicate_file_scanner.py /path/to/directory
  Log Duplicate Details:
  . python duplicate_file_scanner.py /path/to/directory --log duplicates.log
  Filter by Extensions:
  . python duplicate_file_scanner.py /path/to/directory --extensions .jpg .png

Example Output

  Duplicate found:
  /path/to/file1.jpg
  /path/to/duplicate1.jpg

  Duplicate found:
  /path/to/music.mp3
  /path/to/copy_of_music.mp3

🛠️ How It Works
  Hashing:
  The script reads files in chunks to generate a unique hash using the MD5 algorithm.

  Content Matching:
  Files with identical hashes are flagged as duplicates, even if their names differ.

  Output:
  Duplicates are displayed in the terminal, and optionally saved to a log file for later review.

🛠️ Customization
  Change Hashing Algorithm:
  Switch to a stronger algorithm like SHA-256 by modifying the hash_file function:


  h = hashlib.sha256()
  Ignore Specific Files:
  Add logic to skip files based on their size, name patterns, or timestamps.

  Automated Duplicate Deletion:
  Extend the script to automatically delete duplicates after confirmation.

🤝 Contributions
  Contributions are always welcome! Here's how you can help:

  Fork the repository.
  Create a feature branch:

    git checkout -b feature-name
    Commit your changes:

    git commit -m "Add feature"  
    Push your branch:

    git push origin feature-name  
    Submit a Pull Request.
    
  For major changes, open an issue first to discuss your idea.

🌟 Like this project? Star the repository to show your support!
