def obter_media(grade):
    total_sum = sum(grade)
    total_sum = float(total_sum)
    return total_sum / len(grade)


def calcular_media_total(aluno):
    class_work = obter_media(aluno["classwork"])
    tests = obter_media(aluno["tests"])
    laboratorio = obter_media(aluno["lab_work"])
    return (0.25 * class_work + 0.55 * tests + 0.20 * laboratorio)


def atribuir_letra_nota(final_grade):
    if final_grade >= 90:
        return "A"
    elif final_grade >= 80:
        return "B"
    elif final_grade >= 70:
        return "C"
    elif final_grade >= 60:
        return "D"
    else:
        return "F"


def nota_media_classe():
    resultado_lista = []

    for aluno, detalhes in alunos.items():
        media_aluno = calcular_media_total(alunos[aluno])
        resultado_lista.append(media_aluno)

    return obeter_media(resultado_lista)
