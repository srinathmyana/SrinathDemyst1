import json
import csv

# Step 1: Read the spec.json file
def load_spec_file(spec_path):
    with open(spec_path, 'r') as file:
        spec = json.load(file)
    return spec

# Step 2: Parse a single line from the fixed-width file
def parse_line(line, offsets):
    start = 0
    row = []
    for offset in offsets:
        end = start + int(offset)
        row.append(line[start:end].strip())  # Strip removes extra spaces
        start = end
    return row

# Step 3: Convert fixed-width file to CSV
def convert_fixed_width_to_csv(fixed_width_file, spec, output_csv):
    offsets = spec['Offsets']
    column_names = spec['ColumnNames']
    fixed_width_encoding = spec['FixedWidthEncoding']
    delimited_encoding = spec['DelimitedEncoding']
    
    with open(fixed_width_file, 'r', encoding=fixed_width_encoding) as infile, \
         open(output_csv, 'w', encoding=delimited_encoding, newline='') as outfile:
        
        reader = infile.readlines()
        writer = csv.writer(outfile)
        
        # Write the header if IncludeHeader is True
        if spec['IncludeHeader'] == "True":
            writer.writerow(column_names)
        
        # Process each line and write to CSV
        for line in reader:
            row = parse_line(line, offsets)
            writer.writerow(row)

# Step 4: Main function to run the script
if __name__ == "__main__":
    # Paths for input and output files
    spec_file_path = "spec.json"  # Replace with your spec.json file path
    fixed_width_file_path = "input_fixed_width.txt"  # Replace with your fixed-width file
    output_csv_path = "output.csv"
    
    # Load the spec and convert the file
    spec = load_spec_file(spec_file_path)
    convert_fixed_width_to_csv(fixed_width_file_path, spec, output_csv_path)
    print(f"Conversion completed! Check the file: {output_csv_path}")
