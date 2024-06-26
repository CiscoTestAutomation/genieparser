#!/bin/bash

# Static array of subfolders to exclude
declare -a exclude_list=("dummy_parser" "__pycache__")

# Function to check if a folder is in the exclude list
is_excluded() {
    local folder=$1
    for excluded in "${exclude_list[@]}"; do
        if [[ "$folder" == "$excluded" ]]; then
            return 0 # True, the folder is excluded
        fi
    done
    return 1 # False, the folder is not excluded
}

# Flag to indicate if an error has occurred
error_found=0

script_path=$(dirname "$0")

# Find all directories named "tests" recursively
while IFS= read -r -d '' test_dir; do
    # Find all immediate subdirectories of the current "tests" directory
    while IFS= read -r -d '' sub_dir; do
        # Extract the name of the subdirectory
        sub_dir_name=$(basename "$sub_dir")

        # Check if the subdirectory is in the exclude list
        if is_excluded "$sub_dir_name"; then
            continue # Skip this subdirectory
        fi

        # Check if the "cli" directory exists within the subdirectory
        if [[ ! -d "$sub_dir/cli" ]]; then
            # If the "cli" directory does not exist, output the path
            echo "$sub_dir does not have a 'cli' folder"
            # Set the error flag
            error_found=1
        fi
    done < <(find "$test_dir" -mindepth 1 -maxdepth 1 -type d -print0)
done < <(find "$script_path"/../src -type d -name "tests" -print0)

# Exit with an error code if any errors were found
if [[ $error_found -ne 0 ]]; then
    exit 1
fi

# Exit with a success code if no errors were found
exit 0