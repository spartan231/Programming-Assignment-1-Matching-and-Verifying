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
        h: {s: idx for idx, s in enumerate(prefs)}
        for h, prefs in hospital.items()
    }
    student_rank = {
        s: {h: idx for idx, h in enumerate(prefs)}
        for s, prefs in student.items()
    }

    for h, h_prefs in hospital.items():
        current_s = match.get(h)
        current_rank = hospital_rank.get(h, {}).get(current_s, float("inf"))

        for s in h_prefs:
            if hospital_rank.get(h, {}).get(s, float("inf")) >= current_rank:
                break

            if s not in student:
                continue

            s_current = student_match.get(s)
            s_rank = student_rank.get(s, {})

            if s_current is None:
                unstable_message = f"UNSTABLE: blocking pair ({h}, {s})"
                break

            if s_rank.get(h, float("inf")) < s_rank.get(s_current, float("inf")):
                unstable_message = f"UNSTABLE: blocking pair ({h}, {s})"
                break

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