import random
import os
from pathlib import Path

# Blacklist of problematic codes
blacklist = {
    'nan', 'nil', 'die', 'wtf', 'fuk', 'fuc', 'sex', 'xxx', 'ass',
    'cum', 'kys', 'kkk', 'fag', 'gay', 'poo', 'pee', 'dmn', 'hel',
    '666', '420', 'sus', 'sos', 'omg', 'lol', 'wth', 'fml', 'api',
    'sql', 'exe', 'bat', 'cmd', 'run', 'bin', 'tmp', 'var', 'dev'
}

def hamming_distance(a, b):
    """Calculate Hamming distance between two codes"""
    return sum(c1 != c2 for c1, c2 in zip(a, b))

def is_similar(code, existing_codes, min_distance=2):
    """Check if code is too similar to existing codes"""
    for existing in existing_codes:
        if hamming_distance(code, existing) < min_distance:
            return True
    return False

def generate_code():
    """Generate random 3-character code"""
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(chars) for _ in range(3))

def load_existing_codes(filepath):
    """Load existing codes from a file"""
    if not os.path.exists(filepath):
        return set()

    with open(filepath, 'r') as f:
        # Read and clean codes, filtering out empty lines
        codes = set(line.strip() for line in f if line.strip())

    return codes

def generate_codes(count, existing_codes=None, max_attempts=100000, seed=42):
    """Generate unique, dissimilar codes

    Args:
        count: Number of new codes to generate
        existing_codes: Set of existing codes to avoid duplicates
        max_attempts: Maximum attempts before giving up
        seed: Random seed for reproducibility

    Returns:
        List of newly generated codes
    """
    if existing_codes is None:
        existing_codes = set()

    # Set seed based on the number of existing codes for reproducibility
    # This ensures that generating codes 1-300 always gives the same result,
    # and generating codes 301-400 always gives the same result, etc.
    initial_count = len(existing_codes)
    random.seed(seed + initial_count)

    codes = set(existing_codes)  # Start with existing codes
    target_count = initial_count + count
    attempts = 0

    while len(codes) < target_count and attempts < max_attempts:
        code = generate_code()
        attempts += 1

        # Skip if blacklisted
        if code in blacklist:
            continue

        # Skip if already exists
        if code in codes:
            continue

        # Skip if too similar to existing codes
        if is_similar(code, codes):
            continue

        codes.add(code)

    if len(codes) < target_count:
        actual_generated = len(codes) - initial_count
        print(f"Warning: Only generated {actual_generated} of {count} codes after {max_attempts} attempts")

    # Return only the newly generated codes
    new_codes = codes - existing_codes
    return list(new_codes)

# Main execution
if __name__ == "__main__":
    # Path to code list file
    code_list_path = Path(__file__).parent.parent / 'code_list.txt'

    # Check if we should extend existing codes or create new ones
    existing = load_existing_codes(code_list_path)

    if existing:
        print(f"Found {len(existing)} existing codes")
        # Generate additional codes
        num_to_generate = int(input(f"How many additional codes to generate? "))

        # Ask where to save
        save_option = input("Save to: (1) Append to existing file, (2) New file [default: 2]: ").strip()

        new_codes = generate_codes(num_to_generate, existing_codes=existing)

        if save_option == "1":
            # Append to existing file
            with open(code_list_path, 'a') as f:
                for code in new_codes:
                    f.write(code + '\n')
            print(f"Generated {len(new_codes)} new codes")
            print(f"Total codes: {len(existing) + len(new_codes)}")
            print(f"Appended to {code_list_path}")
        else:
            # Save to new file
            output_file = input("Output filename [default: code_list_extra.txt]: ").strip()
            if not output_file:
                output_file = "code_list_extra.txt"

            output_path = Path(__file__).parent.parent / output_file
            with open(output_path, 'w') as f:
                for code in new_codes:
                    f.write(code + '\n')

            print(f"Generated {len(new_codes)} new codes")
            print(f"Saved to {output_path}")
    else:
        print("No existing codes found. Generating initial set...")
        # Generate initial codes
        code_list = generate_codes(500)

        # Save to file
        with open(code_list_path, 'w') as f:
            for code in code_list:
                f.write(code + '\n')

        print(f"Generated {len(code_list)} unique codes")
        print(f"Saved to {code_list_path}")