import re
import sys
import os


def reduce_number(match):
    __doc__ = """
    Takes a regex match of a number in a pos statement and reduces it by 20%.
    The reduced number is rounded and returned as an integer.
    """
    number = int(match.group(1))
    # Reduce by 20% and round to the nearest integer
    reduced_number = int(round(number * 0.8))
    return f' {reduced_number} '


def process_dist_feature(file_content):
    __doc__ = """
    Process the lines in the DIST feature block and reduce the numbers in the 'pos' lines.
    """
    inside_dist = False
    processed_lines = []

    for line in file_content.splitlines():
        stripped_line = line.strip()

        if stripped_line.startswith("feature dist {"):
            inside_dist = True  # Start of the DIST feature block
            processed_lines.append(line)
        elif stripped_line.startswith("} dist;"):
            if inside_dist:
                inside_dist = False  # End of the DIST feature block
            processed_lines.append(line)
        elif inside_dist and stripped_line.startswith("pos "):
            # Modify only 'pos' lines within the DIST feature block
            modified_line = re.sub(r'\s(\d+)\s', reduce_number, line)
            processed_lines.append(modified_line)
        else:
            processed_lines.append(line)  # Leave other lines unchanged

    return '\n'.join(processed_lines)


def save_modified_file(original_path, modified_content):
    __doc__ = """
    Save the modified content to a new file with a '.scale' suffix.
    """
    base, ext = os.path.splitext(original_path)
    new_fea_path = f"{base}-scaled-dist{ext}"

    with open(new_fea_path, 'w') as new_file:
        new_file.write(modified_content)

    print(f"Modified file saved as: {new_fea_path}")


def main(fea_path):
    __doc__ = """
    Main function to open the file, process it, and save the modified 
version.
    """
    if not os.path.isfile(fea_path):
        print(f"Error: File '{fea_path}' not found.")
        return

    with open(fea_path, 'r') as file:
        file_content = file.read()

    modified_content = process_dist_feature(file_content)
    save_modified_file(fea_path, modified_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scale-dist.py <path_to_opentype_feature_file>")
        sys.exit(1)

    input_fea_path = sys.argv[1]
    main(input_fea_path)
