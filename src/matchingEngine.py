def MatchingEngine(hospital, student):
    """
    * hospital is a dictionary with the key being the name of the hospital
    and the value being a list of their preference for students
    * student is a dictionary with the key being the name of the student
    and the value being a list of their preference for hospitals

    RETURN:
    * need to return a dictionary with the key being the name of the hospital
    and the value being the matched student (final matching)
    """
    
    # these hold the names of the hosptials and students not the values each hold
    hospitals_free = list(hospital.keys())
    students_free = list(student.keys())

    hospital_matches = {}
    student_matches = {}
    #TODO: now finish up the rest of the algorithm
    while len(hospitals_free) > 0:
        # pick the first free hospital
        h = hospitals_free[0]
        
        try:
            # get highest ranked student
            s = hospital[h].pop(0)  
        except IndexError:
            # hospital has no more students to propose to
            hospitals_free.pop(0)
            continue
        
        if (s not in student):
            print(f"Student {s} not found in student list.")
            continue

        if (s in students_free):
            students_free.remove(s)
            hospitals_free.remove(h)
            hospital_matches[h] = s
            student_matches[s] = h
            
        else:
            # student has been matched
            # find out who they are matched to
            curr_hospital = student_matches[s]
            # student preference list
            s_prefs = student[s]

            if(s_prefs.index(h) < s_prefs.index(curr_hospital)):
                # student prefers new hospital
                hospital_matches[h] = s
                student_matches[s] = h
                hospitals_free.remove(h)
                hospitals_free.append(curr_hospital)
                del hospital_matches[curr_hospital]
                
            else:
                # student prefers current hospital
                continue
    return hospital_matches
        
