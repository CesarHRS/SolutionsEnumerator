import numpy as np
from itertools import combinations
import sys

EPSILON = 1e-9

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <input_file>")
        return

    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        n, m = map(int, f.readline().split()) # Lê o número de variaveis e restrições
        c = np.array(list(map(float, f.readline().split()))) # Cria o vetor de coeficientes da função objetivo
        A = [] # Matriz coeficiente de restrições
        b = [] # Vetor de termos independentes
        for _ in range(m):
            parts = list(map(float, f.readline().split()))
            A.append(parts[:-1])
            b.append(parts[-1])
        A = np.array(A, dtype=float)
        b = np.array(b, dtype=float)

    all_combinations = combinations(range(n), m) # Gera as combinações de m variáveis
    solutions = []

    for basis in all_combinations:
        basis = list(basis)
        A_B = A[:, basis]
        if np.linalg.matrix_rank(A_B) < m: # Verifica se A_B é invertível
            continue
        try:
            x_B = np.linalg.solve(A_B, b) # Encontra os valores das variáveis básicas
        except np.linalg.LinAlgError: # Se não encontrar, ignora
            continue

        x_full = np.zeros(n) # cria um vetor de zeros
        x_full[basis] = x_B
        feasible = all(x >= -EPSILON for x in x_full) # Verifica se as variaveis não são negativas
        obj_value = np.dot(c, x_full) # Calcula a função objetiva
        solutions.append((x_full, obj_value, feasible)) # Guarda as soluções no vetor de soluções

    for x, obj, feasible in solutions:
        print(f"x = [{', '.join(f'{val:.6f}' for val in x)}]")
        print(f"z = {obj:.6f} {'(viável)' if feasible else '(inviável)'}")

    total = len(solutions)
    total_feasible = sum(1 for sol in solutions if sol[2])
    total_infeasible = total - total_feasible

    print(f"\nNúmero total de soluções básicas: {total}")
    print(f"Número de soluções básicas viáveis: {total_feasible}")
    print(f"Número de soluções básicas inviáveis: {total_infeasible}")

    if total_feasible > 0:
        optimal = min((sol for sol in solutions if sol[2]), key=lambda x: x[1])
        print("\nSolução ótima encontrada!")
        print(f"Função objetivo: {optimal[1]:.6f}")
        print(f"x = [{', '.join(f'{val:.6f}' for val in optimal[0])}]")
    else:
        print("\nNenhuma solução básica viável encontrada.")

if __name__ == "__main__":
    main()