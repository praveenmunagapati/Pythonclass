# '''
# Experiment 21: Write a python program to perform multiplication of two square matrices
#
# Algorithm:
# 1. Define two matrices A and B.
# 2. Initialize a result matrix C with zeros.
# 3. Iterate through rows of A (i).
# 4. Iterate through columns of B (j).
# 5. Iterate through rows of B (k).
# 6. C[i][j] += A[i][k] * B[k][j].
# 7. Print result.
# '''
#
#
# def multiply_matrices(A, B):
#     """
#     Multiplies two square matrices.
#     """
#     n = len(A)
#     # Initialize result matrix with zeros
#     C = [[0 for _ in range(n)] for _ in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 C[i][j] += A[i][k] * B[k][j]
#
#     return C
#
#
# if __name__ == "__main__":
#     A = [[1, 2], [3, 4]]
#     B = [[5, 6], [7, 8]]
#
#     print("Matrix A:")
#     for r in A: print(r)
#
#     print("Matrix B:")
#     for r in B: print(r)
#
#     result = multiply_matrices(A, B)
#     print("Result:")
#     for r in result: print(r)
import threading

lock = threading.Lock()

def task():
    lock.acquire()
    print(threading.current_thread().name)
    print("Thread running")
    lock.release()

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()