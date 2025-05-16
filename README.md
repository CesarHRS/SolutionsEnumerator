# **Enumerador de Soluções Básicas em Programação Linear**

**Autor**: César Henrique Resende Soares
**Disciplina**: Pesquisa Operacional I  
**Professor**: André L. Maravilha  
**Instituição**: CEFET-MG

---

## **1. Objetivo**

Este programa tem como objetivo **enumerar todas as soluções básicas** (viáveis e inviáveis) de um problema de
Programação Linear na forma padrão, identificando a **solução ótima**.

---

## **2. Funcionamento**

### **2.1. Entrada**

O programa recebe um **arquivo de texto** (`*.txt`) com a seguinte estrutura:

```
n m  
c₁ c₂ ... cₙ  
a₁₁ a₁₂ ... a₁ₙ b₁  
a₂₁ a₂₂ ... a₂ₙ b₂  
...  
aₘ₁ aₘ₂ ... aₘₙ bₘ  
```  

Onde:

- `n` = Número de variáveis de decisão.
- `m` = Número de restrições.
- `c` = Coeficientes da função objetivo.
- `A` = Matriz de coeficientes das restrições.
- `b` = Vetor de termos independentes.

### **2.2. Saída**

Para cada solução básica encontrada, o programa exibe:

- Valores das variáveis de decisão (`x`).
- Valor da função objetivo (`z`).
- Se é **viável** ou **inviável**.

No final, são exibidos:

- Total de soluções básicas.
- Número de soluções viáveis/inviáveis.
- **Solução ótima**, caso exista.

**Exemplo de Saída**:

```
x = [2.000000, 3.000000, -1.000000, 0.000000, 0.000000]  
z = -8.000000 (inviável)  
x = [1.000000, 3.000000, 0.000000, 1.000000, 0.000000]  
z = -7.000000 (viável)  
...  
Número total de soluções básicas: 8  
Número de soluções básicas viáveis: 5  
Número de soluções básicas inviáveis: 3  

Solução ótima encontrada!  
Função objetivo: -7.000000  
x = [1.000000, 3.000000, 0.000000, 1.000000, 0.000000]  
```  

---

## **3. Método Utilizado**

### **3.1. Algoritmo**

1. **Gera combinações básicas**:
    - Calcula todas as combinações de \(m\) variáveis (base) em \(n\) possíveis (\(C(n, m)\)).
    - Para cada combinação, verifica se a submatriz \(A_B\) (colunas da base) é invertível.

2. **Resolve o sistema linear**:
    - Para cada base válida, resolve \(A_B \cdot x_B = b\) para encontrar \(x_B\).
    - As variáveis não básicas são definidas como zero.

3. **Classifica a solução**:
    - Se todas as variáveis em \(x_B\) forem \(\geq 0\), a solução é **viável**.
    - Caso contrário, é **inviável**.

4. **Identifica a solução ótima**:
    - Entre as soluções viáveis, seleciona aquela com o menor valor da função objetivo.

### **3.2. Bibliotecas Utilizadas**

- `numpy`: Para operações matriciais e resolução de sistemas lineares.
- `itertools`: Para gerar combinações de variáveis básicas.

---

## **4. Como Executar**

### **4.1. Pré-requisitos**

- Python 3.x instalado.
- Bibliotecas: `numpy` (instalável via `pip install numpy`).

### **4.2. Comando de Execução**

```bash
python3 main.py <arquivo_de_entrada.txt>
```  

**Exemplo**:

```bash
python3 main.py LP_00.txt
```  

### **4.3. Exemplo de Arquivo de Entrada**

**Exemplo** (`LP_00.txt`):

```
5 3  
-1 -2 0 0 0  
1 1 1 0 0 4  
1 0 0 1 0 2  
0 1 0 0 1 3  
```  

Também consulte os arquivos`LP_01.txt` a `LP_05.txt` fornecidos.

---

## **5. Limitações**

- **Eficiência**: Para problemas grandes (n > 20\), o algoritmo pode ser lento devido a necessidade de calcular as
combinação des n e m.
- **Precisão Numérica**: Valores muito próximos de zero podem ser classificados erroneamente, para isso, é necessário o
  reajuste da constante `EPSILON`.

---

## **6. Contato**

Em caso de dúvidas, entre em contato:

- **Nome**: César Henrique Resende Soares
- **Email**: cesar@cefetmg.aluno.com

---
