from matchingEngine import MatchingEngine

def main():
    hospitals = {
        "h1": ["a", "b"],
        "h2": ["a", "b"]
    }

    students = {
        "s1": ["h1", "h2"],
        "s2": ["h2", "h1"]
    }


    MatchingEngine(hospitals, students)
    return 0

main()
