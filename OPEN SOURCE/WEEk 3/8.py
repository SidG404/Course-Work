def mutate(word):
    mutants = []
    l = len(word)
    for i in range(l+1):
        pre, suf = word[:i], word[i:]
        for j in range(97, 123):
            mutants.append(pre+chr(j)+suf)
    for i in range(l):
        mutants.append(word[:i]+word[i+1:])
    for i in range(l):
        for j in range(97, 123):
            mutants.append(word[:i]+chr(j)+word[i+1:])
        mutants.remove(word)
    for i in range(l-1):
        mutants.append(word[:i]+word[i+1]+word[i]+word[i+2:])
    return(mutants)

if __name__ == "__main__":
    print(*mutate('anime'))