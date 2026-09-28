import re
import os
import string

def sanitize_filename(filename):
    # Remove invalid characters
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    cleaned = ''.join(c for c in filename if c in valid_chars)
    # Remove leading/trailing spaces
    return cleaned.strip()

def split_emotions():
    input_file = "base/The-Book-of-Human-Emotions-An-Encyclopedia.md"
    output_dir = "segments"
    
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # The headings seem to be `## `
    # We will split by `\n## ` and then add `## ` back
    sections = content.split('\n## ')
    
    os.makedirs(output_dir, exist_ok=True)
    
    for section in sections:
        if not section.strip():
            continue
            
        # Add back the `## ` if it's missing (except for the first split chunk if it didn't start with \n)
        if not section.startswith("## ") and not section.startswith('THE BOOK') and not section.startswith('Introduction'):
            full_section = "## " + section
        else:
            full_section = section
            
        lines = full_section.split('\n')
        first_line = lines[0].strip()
        
        # Remove `## ` prefix if present in the first_line
        if first_line.startswith("## "):
            title_raw = first_line[3:]
        else:
            title_raw = first_line
            
        # Remove any bold (`**`), italic (`_`), or other unwanted characters from title
        title_raw = title_raw.replace('**', '').replace('_', '')
        
        # Handle cases like "COLLYWOBBLES The ," by removing rogue commas
        title = title_raw.replace(',', '').strip()
        
        # Skip generic book parts
        skip_list = ["THE BOOK OF HUMAN EMOTIONS", "Contents", "Introduction", "Acknowledgements", "Notes and Further Reading", "Index"]
        if any(skip_word in title for skip_word in skip_list):
            continue
            
        # Clean filename
        filename = sanitize_filename(title)
        if not filename:
            continue
            
        file_path = os.path.join(output_dir, f"{filename}.md")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(full_section)
            
    print(f"Extraction complete.")

if __name__ == "__main__":
    split_emotions()
