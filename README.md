# folderescape.py

## Description
Small python script that takes files or folders from a child folder and moves them to the root folder. Affected elemments take the foldername as prefix.

## Example
**Before:**

* Root
  * Folder1
    * File1
    * File2
  * Folder2
    * File1
    * File2
    * File3
    * File4
  * Folder3
    * File1

**After:**

* Root
  * Folder1File1
  * Folder1File2
  * Folder2File1
  * Folder2File2
  * Folder2File3
  * Folder2File4
  * Folder3File1



## Usage
Run folderescape.py in the root directory. For nested folders run the script multiple times.
