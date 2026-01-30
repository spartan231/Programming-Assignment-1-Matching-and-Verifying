import sys
# Ensure matchingEngine is accessible. 
# If in the same folder: from matchingEngine import MatchingEngine
# If in src: from src.matchingEngine import MatchingEngine
from matchingEngine import MatchingEngine
from verifier import check_validity

def main():
    file_path = "data/sampleData.txt"
    
    # 1. Read and clean lines
    try:
        with open(file_path, 'r') as f:
            # Strip whitespace and ignore empty lines
            lines = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return

    iter_lines = iter(lines)

    try:
        # 2. Parse Number of items (n)
        header = next(iter_lines)
        num = int(header)
        
        hospitals = {}
        students = {}

        # 3. Parse Hospitals
        # The names are NOT in the file. We must assign IDs "1", "2", "3"...
        for i in range(num):
            line = next(iter_lines)
            parts = line.split()
            
            # ID is based on loop index (1-based to match the example output)
            h_name = str(i + 1) 
            
            # The WHOLE line is the preference list
            hospitals[h_name] = parts 

        # 4. Parse Students
        for i in range(num):
            line = next(iter_lines)
            parts = line.split()
            
            # ID is based on loop index (1-based)
            s_name = str(i + 1)
            
            # The WHOLE line is the preference list
            students[s_name] = parts

        # 5. Run Engine
        # Make copies for the matching engine since it modifies preferences
        hospitals_copy = {h: prefs[:] for h, prefs in hospitals.items()}
        matches = MatchingEngine(hospitals_copy, students)
        
        # 6. Output formatted as "i j"
        # We sort by hospital ID to ensure the output order matches the input order
        for i in range(num):
            h_name = str(i + 1)
            if h_name in matches:
                print(f"{h_name} {matches[h_name]}")

        # 7. Verify matches
        is_valid, message = check_validity(hospitals, students, matches)
        print(message)
        if not is_valid:
            return

    except StopIteration:
        print("Error: The file ended unexpectedly. Check if 'n' matches the actual number of lines.")
    except ValueError:
        print("Error: Could not parse a number. Check input format.")

if __name__ == "__main__":
    main()