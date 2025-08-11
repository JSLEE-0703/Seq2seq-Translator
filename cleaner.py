def clean_data(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as f, open(output_path, 'w', encoding='utf-8') as out:
        for line in f:
            # Remove newline characters at the end of the line
            line = line.strip()
            # Find the position of the first tab character
            tab_index = line.find('\t')
            # Extract source language sentence and target language sentence
            if tab_index != -1:
                source_sentence = line[:tab_index]
                target_sentence = line[tab_index + 1:line.find('\t', tab_index + 1)]
                # Write the cleaned sentence pair
                out.write(f"{source_sentence}\t{target_sentence}\n")

# Call the function to clean the data
clean_data('data/cmn.txt', 'data/cmn-cleaned.txt')
