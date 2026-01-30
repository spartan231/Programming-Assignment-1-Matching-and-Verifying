def check_validity(hospital, student, match):
    """
    check the validity of the provided data.

    parameters:
    hospital : The hospital data to be checked.
    student : The student data to be checked.
    match : The match data to be checked.

    returns:
    tuple: (bool, message) message is:
    - "VALID STABLE"
    - "INVALID: <reason>"
    - "UNSTABLE: blocking pair (h, s)"
    """
    n = len(hospital)

    invalid_reasons = []

    if len(match) != n:
        invalid_reasons.append("INVALID: incorrect number of hospital matches")
    
    seen = set()

    for h,s in match.items():
        if h not in hospital:
            invalid_reasons.append(f"INVALID: hospital {h} not in hospital list")
        if s not in student:
            invalid_reasons.append(f"INVALID: student {s} not in student list")
        if s in seen:
            invalid_reasons.append(f"INVALID: student {s} matched to multiple hospitals")
        
        seen.add(s)

    if len(seen) != n:
        invalid_reasons.append("INVALID: not all students matched")

    # stability check (blocking pair)
    unstable_message = None

    # build reverse match: student -> hospital
    student_match = {s: h for h, s in match.items()}

    # precompute ranks for fast preference comparison
    hospital_rank = {
        h: {s: i for i, s in enumerate(prefs)}
        for h, prefs in hospital.items()
    }
    student_rank = {
        s: {h: i for i, h in enumerate(prefs)}
        for s, prefs in student.items()
    }

    for h, h_prefs in hospital.items():
        current_s = match.get(h)
        current_rank = hospital_rank[h].get(current_s, float("inf"))

        for s in h_prefs:
            s_rank_in_h = hospital_rank[h].get(s, float("inf"))
            
            # only students hospital prefers more (lower rank = higher preference)
            if s_rank_in_h >= current_rank:
                break

            # Check if s exists in student list and h is in s's preferences
            if s not in student or h not in student_rank.get(s, {}):
                continue

            s_current = student_match.get(s)

            # If student is unmatched or prefers h over current match -> blocking pair
            if s_current is None:
                return False, f"UNSTABLE: blocking pair ({h}, {s}) - student {s} unmatched"
            
            if student_rank[s][h] < student_rank[s][s_current]:
                return False, f"UNSTABLE: blocking pair ({h}, {s}) - student prefers {h} over {s_current}"

        if unstable_message:
            break

    if not invalid_reasons and not unstable_message:
        return True, "VALID STABLE"

    messages = []
    if invalid_reasons:
        messages.extend(invalid_reasons)
    if unstable_message:
        messages.append(unstable_message)

    return False, " | ".join(messages)