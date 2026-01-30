from matchingEngine import MatchingEngine

def main():
    hospitals = {
        "h1": ["a", "b", "c"],
        "h2": ["a", "b", "c"],
        "h3": ["b", "a", "c"]
    }

    students = {
        "a": ["h1", "h2", "h3"],
        "b": ["h2", "h1", "h3"],
        "c": ["h1", "h2", "h3"]
    }


    matches = MatchingEngine(hospitals, students)
    for h,s in matches.items():
        print(f"{h} {s}")
    
    return 0

main()