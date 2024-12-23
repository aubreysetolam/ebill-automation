def find_and_save_lines(file_path, word, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    result_lines = []
    for i, line in enumerate(lines):
        # result_lines.extend(lines[i])
        # if word in line:
        #     if any('Tier 2' in line for line in lines[i+1:i+1+n]):
        #         result_lines.extend(lines[i+1:i+1+28])
        #     else:
        result_lines.extend(lines[i+1:i+1+n])
    
    return result_lines

# Example usage
file_path = 'plaintext.txt'
word = 'Electric  (kWh)'
n = 30  # Number of lines to save after the word
result = find_and_save_lines(file_path, word, n)

# Save the result to a new file
with open('plaintext2.txt', 'w') as output_file:
    output_file.writelines(result)