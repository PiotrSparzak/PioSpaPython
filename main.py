import numpy as np

#ZAD1
arr = np.arange(20) * 4
print(arr)
#ZAD2
lst_float = [1.2, 2.3, 3.4, 4.5, 5.6]
lst_int32 = np.array(lst_float, dtype='int32')
print(lst_int32)
#ZAD3
def podwa(n):
    return np.array([2 ** i for i in range(n*n)]).reshape((n, n))
print(podwa(3))
#ZAD4

def generuj(base, n):
    return np.logspace(0, n-1, n, base=base)
print(generuj(2, 4))
#ZAD5

def macierz(n):
    reversed_vector = np.arange(n)[::-1]
    diagonal_vector = np.diag(reversed_vector, k=2)
    return diagonal_vector
print(macierz(5))
#ZAD6

# słowa do umieszczenia w macierzy
words = ['PYTHON', 'NUMPY', 'ARRAY', 'MATRIX']

# wymiary macierzy
n_rows = len(words)
n_cols = max(len(word) for word in words)

# inicjalizacja macierzy zerami
matrix = np.zeros((n_rows, n_cols), dtype='U1')

# umieszczenie słów w macierzy
for i, word in enumerate(words):
    matrix[i, :len(word)] = list(word)

# wypisanie macierzy w postaci wykreślanki
for i in range(n_rows):
    for j in range(n_cols):
        if matrix[i, j] != '':
            print(matrix[i, j], end=' ')
        else:
            print(' ', end=' ')
    print()

# dodanie słowa po ukosie (od prawej do lewej)
diagonal_word = 'NUM'
for i in range(len(diagonal_word)):
    matrix[i, n_cols-len(diagonal_word)+i] = diagonal_word[i]

# ponowne wypisanie macierzy w postaci wykreślanki z dodanym słowem po ukosie
print()
for i in range(n_rows):
    for j in range(n_cols):
        if matrix[i, j] != '':
            print(matrix[i, j], end=' ')
        else:
            print(' ', end=' ')
    print()
#ZAD7

def genmacierz(n):
    # Tworzenie macierzy n*n wypełnionej zerami
    matrix = np.zeros((n, n), dtype=int)

    # Uzupełnianie macierzy o kolejne wielokrotności liczby 2 na przekątnych
    for i in range(n):
        matrix[i, i] = 2 * (i + 1)
        if i < n - 1:
            matrix[i, i + 1] = 2 * (i + 1)
            matrix[i + 1, i] = 2 * (i + 1)

    return matrix
#ZAD8

def array(arr, direction):
    if direction == 'vertical':
        if arr.shape[0] % 2 != 0:
            print('Ilość wierszy nie pozwala na operację.')
            return arr
        else:
            half = arr.shape[0] // 2
            return arr[:half], arr[half:]
    elif direction == 'horizontal':
        if arr.shape[1] % 2 != 0:
            print('Ilość kolumn nie pozwala na operację.')
            return arr
        else:
            half = arr.shape[1] // 2
            return arr[:, :half], arr[:, half:]
    else:
        print('Nieprawidłowy kierunek podziału.')
        return arr
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(arr)

    # Podział pionowy
    arr1, arr2 = divide_array(arr, 'vertical')
    print(arr1)
    print(arr2)

    # Podział poziomy
    arr3, arr4 = divide_array(arr, 'horizontal')
    print(arr3)
    print(arr4)

    # Nieprawidłowy kierunek podziału
    arr5 = divide_array(arr, 'wrong')
    print(arr5)

    #ZAD9

    # wygenerowanie tablicy jednowymiarowej
    arr = np.arange(1, 26)

    # zmiana kształtu na macierz 5x5
    arr = arr.reshape((5, 5))

    print(arr)