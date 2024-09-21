def solution(id_pw, db):
    for i in range(len(db)):
        if db[i][0] == id_pw[0] and db[i][1] == id_pw[1]:
            return 'login'
        elif db[i][0] == id_pw[0] and db[i][1] != id_pw[1]:
            return 'wrong pw'
        else:
            pass
    return 'fail'
        