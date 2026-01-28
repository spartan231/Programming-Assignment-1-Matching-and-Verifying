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


    # print("H -> ", hospitals_free)
    # print("S -> ", students_free)

    #TODO: now finish up the rest of the algorithm