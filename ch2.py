def unifyVars(var, x, substitution):
    if var != x:
        if is_variable(var):
            substitution[var] = x
        elif is_variable(x):
            substitution[x] = var
        else:
            return None
    return substitution

def lists(list1, list2, substitution):
    if len(list1) != len(list2):
        return None
    for term1, term2 in zip(list1, list2):
        substitution = unify(term1, term2, substitution)
        if substitution is None:
            return None
    return substitution

def unify(term1, term2, substitution=None):
    if substitution is None:
        substitution = {}
    if term1 == term2:
        return substitution
    if is_variable(term1):
        return unifyVars(term1, term2, substitution)
    elif is_variable(term2):
        return unifyVars(term2, term1, substitution)
    elif is_compound(term1) and is_compound(term2):
        return lists(term1, term2, substitution)
    return None

def is_variable(term):
    return isinstance(term, str) and term.islower()

def is_compound(term):
    return isinstance(term, list)

W = [['Q', ['f','a'], ['f','y']], ['Q', 'y', 'y', ['f','a']]]
print("W:", W)
result = unify(W[0], W[1])
print("Substitution:", result)