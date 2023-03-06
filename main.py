from helpers import *

if __name__ == "__main__":
    for aluno, detalhes in alunos.items():
        print(f"\n {alunos[aluno]['name']}")
        print("-------------------------")
        print(f"Media de notas de {alunos[aluno]['name']}: {round(calcular_media_total(alunos[aluno]), 1)}")
        print(f"Nota final de {alunos[aluno]['name']}: {atribuir_letra_nota(round(calcular_media_total(alunos[aluno]), 1))}")
