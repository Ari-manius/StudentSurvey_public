import random

random.seed(42)

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

def generate_codes(count, max_attempts=100000):
    """Generate unique, dissimilar codes"""
    codes = set()
    attempts = 0
    
    while len(codes) < count and attempts < max_attempts:
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
    
    if len(codes) < count:
        print(f"Warning: Only generated {len(codes)} of {count} codes after {max_attempts} attempts")
    
    return list(codes)

# Generate codes
code_list = generate_codes(300)

# Save to file
with open('code_list.txt', 'w') as f:
    for code in code_list:
        f.write(code + '\n')

print(f"Generated {len(code_list)} unique codes")
print("Saved to codes.txt")