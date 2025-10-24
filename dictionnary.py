def find_grades(grades, students) : 
    """ grades is a dict mapping student names (str) to grades (str)
    students is a list of student names 
    returns a list containing the grades for students (in same order)"""

    list_to_return = [] # on initialise la liste rendue à la fin

    for person in students : # pour chaque étudiant dont on veut la note 
        list_to_return.append(d[person]) # on récupère la note associée à la clé du nom de l'étudiant dans le dictionnaire d

    return list_to_return


# for example 
d = {"Ana":"B", "Matt":"C", "John":"B", "Katy":"A"}
print(find_grades(d, ["Matt", "Katy"])) # returns ["C", "A"]