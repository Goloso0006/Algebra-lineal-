import tkinter as tk
from tkinter import messagebox as mb, simpledialog
import numpy as np
from fractions import Fraction

class CalculadoraMatrices:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Matrices")
        
        # Marco de configuración de tamaño para A y B
        marco = tk.Frame(root, pady=10)
        marco.place(x=10, y=10)
        
        # Configuración matriz A
        tk.Label(marco, text="Filas A:").grid(row=0, column=0)
        self.num_filas_A = tk.IntVar(value=2)
        tk.Entry(marco, textvariable=self.num_filas_A, width=5).grid(row=0, column=1, padx=20)
        tk.Label(marco, text="Columnas A:").grid(row=0, column=2)
        self.num_columnas_A = tk.IntVar(value=2)
        tk.Entry(marco, textvariable=self.num_columnas_A, width=5).grid(row=0, column=3)
        
        # Configuración matriz B
        tk.Label(marco, text="Filas B:").grid(row=1, column=0)
        self.num_filas_B = tk.IntVar(value=2)
        tk.Entry(marco, textvariable=self.num_filas_B, width=5).grid(row=1, column=1)
        tk.Label(marco, text="Columnas B:").grid(row=1, column=2)
        self.num_columnas_B = tk.IntVar(value=2)
        tk.Entry(marco, textvariable=self.num_columnas_B, width=5).grid(row=1, column=3)
        
        # Botón para crear matrices
        tk.Button(marco, text="Crear matrices", command=self.crear_cuadriculas, 
                bg='#CCCCFF').grid(row=0, column=8, padx=30)
        
        # Marco para matrices
        self.contenedor_a = tk.LabelFrame(root, text="Matriz A", padx=10, pady=10)
        self.contenedor_a.pack(side=tk.LEFT, padx=10)
        self.contenedor_b = tk.LabelFrame(root, text="Matriz B", padx=10, pady=10)
        self.contenedor_b.pack(side=tk.LEFT, padx=10)

        # Marco de operaciones
        ops = tk.Frame(root, pady=10, padx=20)
        ops.place(x=620, y=10)
        
        # Botones de operaciones básicas
        tk.Button(ops, text="Sumar", command=self.sumar_matrices, 
                pady=5, width=20, bg='#d6eaf8').grid(row=0, column=0, padx=5)
        tk.Button(ops, text="Restar", command=self.restar_matrices,
                pady=5, width=19, bg='#fcf3cf').grid(row=0, column=1, padx=5)
        tk.Button(ops, text="Multiplicar", command=self.multiplicar_matrices,
                pady=5, width=15, bg='#fadbd8').grid(row=0, column=2, padx=5)
        tk.Button(ops, text="Producto Punto (vectores)", command=self.producto_punto,
                bg='#aed6f1').grid(row=1, column=0, padx=5, pady=5)
        tk.Button(ops, text="Producto Cruz (vectores)", command=self.producto_cruz,
                bg='#f9e79f').grid(row=1, column=1, padx=5, pady=5)
        tk.Button(ops, text="Escalar", command=self.matriz_por_escalar,
                width=15, bg='#f5b7b1').grid(row=1, column=2, padx=5, pady=5)

        # Botones de operaciones avanzadas
        tk.Button(ops, text="Det Sarrus (3x3)", command=self.determinante_sarrus, 
                width=20, bg='#85c1e9').grid(row=2, column=0, padx=5, pady=5)
        tk.Button(ops, text="Det Cofactores (3x3)", command=self.determinante_cofactor,
                width=19, bg='#f7dc6f').grid(row=2, column=1, padx=5, pady=5)
        tk.Button(ops, text="Inversa (3x3)", command=self.matriz_inversa,
                width=15, bg='#f1948a').grid(row=2, column=2, padx=5, pady=5)
        tk.Button(ops, text="Cramer (3x3)", command=self.resolver_cramer,
                width=20, bg='#5dade2').grid(row=3, column=0, padx=5, pady=5)
        tk.Button(ops, text="Método Inversa (3x3)", command=self.resolver_metodo_inversa,
                width=19, bg='#f4d03f').grid(row=3, column=1, padx=5, pady=5)

        # Marco de resultado
        self.marco_resultado = tk.LabelFrame(root, text="Resultado", padx=10, pady=10)
        self.marco_resultado.place(x=620, y=200, width=480, height=250)

        self.texto_resultado = tk.Text(self.marco_resultado)
        self.texto_resultado.pack(fill=tk.BOTH, expand=True)

        # Listas para entradas
        self.entrada_A = []
        self.entrada_B = []

    def crear_cuadriculas(self):
        try:
            filas_A = self.num_filas_A.get()
            cols_A = self.num_columnas_A.get()
            filas_B = self.num_filas_B.get()
            cols_B = self.num_columnas_B.get()
            
            if filas_A < 1 or cols_A < 1 or filas_B < 1 or cols_B < 1:
                mb.showerror("Error", "Todas las dimensiones deben ser mayores a 0.")
                return
            
            if filas_A > 5 or cols_A > 5 or filas_B > 5 or cols_B > 5:
                mb.showerror("Error", "El tamaño máximo permitido es 5x5.")
                return
            
            # Limpiar widgets anteriores
            for w in self.contenedor_a.winfo_children(): w.destroy()
            for w in self.contenedor_b.winfo_children(): w.destroy()
            self.entrada_A.clear()
            self.entrada_B.clear()

            # Crear entradas para matriz A
            for i in range(filas_A):
                fila_A = []
                for j in range(cols_A):
                    eA = tk.Entry(self.contenedor_a, width=7)
                    eA.grid(row=i, column=j, padx=3, pady=3)
                    fila_A.append(eA)
                self.entrada_A.append(fila_A)
                
            # Crear entradas para matriz B
            for i in range(filas_B):
                fila_B = []
                for j in range(cols_B):
                    eB = tk.Entry(self.contenedor_b, width=7)
                    eB.grid(row=i, column=j, padx=3, pady=3)
                    fila_B.append(eB)
                self.entrada_B.append(fila_B)
        except tk.TclError:  # Se lanza cuando hay error de conversión (texto en lugar de número)
            mb.showerror("Error", "El tamaño de las matrices debe ser un número entero")
            return

    def analizar_valor(self, val):
        val = val.strip()
        try:
            if not val:  # Si está vacío
                return 0  
            return float(Fraction(val))
        except ValueError:
            raise ValueError("Ingrese un dato de tipo numérico.")
        except Exception:
            raise ValueError("Entrada inválida")

    def leer_matriz(self, entradas):
        try:
            datos = [[self.analizar_valor(e.get()) for e in fila] for fila in entradas]
            return np.array(datos)
        except ValueError:
            mb.showerror("Error", "Ingrese solo números válidos (enteros, decimales o fracciones como 1/2).")
            return None

    def mostrar_resultado(self, mat):
        self.texto_resultado.delete(1.0, tk.END)
        try:
            # Convertir a fracciones
            como_fracciones = np.vectorize(lambda x: str(Fraction(x).limit_denominator()))(mat)
            
            # Mostrar como fracciones primero
            self.texto_resultado.insert(tk.END, "Formato fraccionario:\n")
            for fila in como_fracciones:
                self.texto_resultado.insert(tk.END, '  '.join(fila) + '\n')
            
            # Mostrar como decimales
            self.texto_resultado.insert(tk.END, "\n\nFormato decimal:\n")
            for fila in mat:
                fila_decimal = ['%.2f' % num for num in fila]  # Formato con 2 decimales
                self.texto_resultado.insert(tk.END, '  '.join(fila_decimal) + '\n')
        except Exception:
            self.texto_resultado.insert(tk.END, str(mat))

    def sumar_matrices(self):
        A, B = self.leer_matriz(self.entrada_A), self.leer_matriz(self.entrada_B)
        if A is None or B is None: return
        if A.shape != B.shape:
            mb.showerror("Error", "Las matrices suma deben tener la misma dimensión.")
            return
        self.mostrar_resultado(A + B)

    def restar_matrices(self):
        A, B = self.leer_matriz(self.entrada_A), self.leer_matriz(self.entrada_B)
        if A is None or B is None: return
        if A.shape != B.shape:
            mb.showerror("Error", "Las matrices deben tener la misma dimensión.")
            return
        self.mostrar_resultado(A - B)

    def multiplicar_matrices(self):
        A, B = self.leer_matriz(self.entrada_A), self.leer_matriz(self.entrada_B)
        if A is None or B is None: return
        if A.shape[1] != B.shape[0]:
            mb.showerror("Error", "No se pueden multiplicar las matrices, Columnas de A deben coincidir con filas de B.")
            return
        self.mostrar_resultado(np.matmul(A, B))

    def producto_punto(self):
        v1, v2 = self.leer_matriz(self.entrada_A), self.leer_matriz(self.entrada_B)
        if v1 is None or v2 is None: return
        v1_plano, v2_plano = v1.flatten(), v2.flatten()
        if v1_plano.ndim != 1 or v2_plano.ndim != 1:
            mb.showerror("Error", "Las entradas deben ser vectores (una fila o una columna).")
            return
        if v1_plano.shape != v2_plano.shape:
            mb.showerror("Error", "Los vectores deben ser de la misma longitud.")
            return
        res = np.dot(v1_plano, v2_plano)
        self.mostrar_resultado(np.array([[res]]))

    def producto_cruz(self):
        v1, v2 = self.leer_matriz(self.entrada_A), self.leer_matriz(self.entrada_B)
        if v1 is None or v2 is None: return
        v1_plano, v2_plano = v1.flatten(), v2.flatten()
        if v1_plano.size != 3 or v2_plano.size != 3:
            mb.showerror("Error", "Los vectores deben tener exactamente 3 elementos.")
            return

        res = np.cross(v1_plano, v2_plano)

        self.texto_resultado.delete(1.0, tk.END)
        try:
            x_str = str(Fraction(res[0]).limit_denominator())
            y_str = str(Fraction(res[1]).limit_denominator())
            z_str = str(Fraction(res[2]).limit_denominator())
            salida_formateada = f"<{x_str}, {y_str}, {z_str}>"
            self.texto_resultado.insert(tk.END, salida_formateada)
        except Exception as e:
            self.texto_resultado.insert(tk.END, f"Error al formatear: {e}\nResultado sin formato: {res}")
            print(f"Error formateando producto cruz: {e}")

    def matriz_por_escalar(self):
        entrada_escalar = simpledialog.askstring("Escalar", "Ingrese el valor escalar (puede ser fracción como 3/4):")
        if entrada_escalar is None:
            return
        try:
            escalar = float(Fraction(entrada_escalar.strip()))
        except Exception:
            mb.showerror("Error", "Escalar inválido.")
            return
        A = self.leer_matriz(self.entrada_A)
        if A is None:
            return
        self.mostrar_resultado(A * escalar)

    def determinante_sarrus(self):
        A = self.leer_matriz(self.entrada_A)
        if A is None: return
        if A.shape != (3,3):
            mb.showerror("Error", "Determinante Sarrus solo para matrices 3x3.")
            return
        a = A
        det = (a[0,0]*a[1,1]*a[2,2] + a[0,1]*a[1,2]*a[2,0] + a[0,2]*a[1,0]*a[2,1]
            - a[0,2]*a[1,1]*a[2,0] - a[0,0]*a[1,2]*a[2,1] - a[0,1]*a[1,0]*a[2,2])
        self.texto_resultado.delete(1.0, tk.END)
        self.texto_resultado.insert(tk.END, str(Fraction(det).limit_denominator()))

    def determinante_cofactor(self):
        A = self.leer_matriz(self.entrada_A)
        if A is None: return
        if A.shape != (3,3):
            mb.showerror("Error", "Determinante por cofactores solo para matrices 3x3.")
            return
        det = (
            A[0,0]*(A[1,1]*A[2,2] - A[1,2]*A[2,1])
        - A[0,1]*(A[1,0]*A[2,2] - A[1,2]*A[2,0])
        + A[0,2]*(A[1,0]*A[2,1] - A[1,1]*A[2,0])
        )
        self.texto_resultado.delete(1.0, tk.END)
        self.texto_resultado.insert(tk.END, str(Fraction(det).limit_denominator()))

    def matriz_inversa(self):
        A = self.leer_matriz(self.entrada_A)
        if A is None: return
        if A.shape != (3,3):
            mb.showerror("Error", "Inversa solo para matrices 3x3.")
            return
        
        try:
            # Calcular el determinante
            detA = np.linalg.det(A)
            
            # Si el determinante es cero, la matriz no tiene inversa
            if abs(detA) < 1e-10:  # Usamos un umbral pequeño para comparaciones con cero
                mb.showerror("Error", "La matriz no tiene inversa: det(A)= 0.")
                return
                
            # Calcular la inversa
            inv = np.linalg.inv(A)
            
            # Mostrar resultados
            self.texto_resultado.delete(1.0, tk.END)
            
            # Mostrar la matriz inversa con formato inteligente
            self.texto_resultado.insert(tk.END, "Matriz inversa A^(-1):\n")
            for fila in inv:
                # Formato inteligente: enteros como enteros, decimales con 4 decimales
                fila_formato = []
                for x in fila:
                    if abs(x - round(x)) < 1e-10:  # Si es prácticamente un entero
                        fila_formato.append(str(int(round(x))))
                    else:
                        fila_formato.append(f"{x:.4f}")
                self.texto_resultado.insert(tk.END, '  '.join(fila_formato) + '\n')
            
            # Formato inteligente para el determinante
            if abs(detA - round(detA)) < 1e-10:  # Si el determinante es prácticamente entero
                det_texto = str(int(round(detA)))
            else:
                det_texto = f"{detA:.4f}"
            
            self.texto_resultado.insert(tk.END, f"\nDeterminante de A: {detA}\n\n")
            
        except np.linalg.LinAlgError:
            mb.showerror("Error", "La matriz no tiene inversa.")

    def resolver_cramer(self):
        A = self.leer_matriz(self.entrada_A)
        B = self.leer_matriz(self.entrada_B)
        if A is None or B is None: return
        if A.shape != (3,3) or (B.shape != (3,1) and B.shape != (3,)):
            mb.showerror("Error", "Cramer requiere A 3x3 y B vector 3x1 o 3 elementos.")
            return

        # Preparar el área de resultados
        self.texto_resultado.delete(1.0, tk.END)
        B_vec = B.flatten()
        detA = np.linalg.det(A)
        
        # Verificar si el sistema tiene solución
        if detA == 0:
            self.texto_resultado.insert(tk.END, "El sistema de ecuaciones no tiene solución |A| = 0.")
            return
        
        # Mostrar matriz A y su determinante
        self.texto_resultado.insert(tk.END, "Matriz A:\n")
        for fila in A:
            self.texto_resultado.insert(tk.END, '  '.join([str(Fraction(x).limit_denominator()) for x in fila]) + '\n')
        self.texto_resultado.insert(tk.END, f"\nDeterminante de A: {Fraction(detA).limit_denominator()}\n\n")
        
        # Calcular y mostrar cada matriz reemplazada y solución
        soluciones = []
        nombres = ["x", "y", "z"]
        
        for i in range(3):
            Ai = A.copy().astype(float)
            Ai[:,i] = B_vec  # Reemplazar columna i con vector B
            di = np.linalg.det(Ai)
            soluciones.append(Fraction(di/detA).limit_denominator())
            
            # Mostrar matriz reemplazada
            self.texto_resultado.insert(tk.END, f"Matriz A{nombres[i]}:\n")
            for fila in Ai:
                self.texto_resultado.insert(tk.END, '  '.join([str(Fraction(x).limit_denominator()) for x in fila]) + '\n')
            self.texto_resultado.insert(tk.END, f"Determinante de A{nombres[i]}: {Fraction(di).limit_denominator()}\n\n\n")
        
        # Mostrar la solución final
        self.texto_resultado.insert(tk.END, "Solución del sistema:\n")
        for i, valor in enumerate(soluciones):
            self.texto_resultado.insert(tk.END, f"{nombres[i]} = {valor}\n")

    def resolver_metodo_inversa(self):
        A = self.leer_matriz(self.entrada_A)
        B = self.leer_matriz(self.entrada_B)
        if A is None or B is None: return
        if A.shape != (3,3) or (B.shape != (3,1) and B.shape != (3,)):
            mb.showerror("Error", "Método de inversa requiere A 3x3 y B vector 3x1 o 3 elementos.")
            return
        try:
            invA = np.linalg.inv(A)
        except np.linalg.LinAlgError:
            mb.showerror("Error", "La matriz es singular, no tiene inversa.")
            return
        X = invA.dot(B.flatten())
        X_frac = [str(Fraction(x).limit_denominator()) for x in X]
        self.texto_resultado.delete(1.0, tk.END)
        self.texto_resultado.insert(tk.END, '  '.join(X_frac))
    
if __name__ == "__main__":
    root = tk.Tk()
    CalculadoraMatrices(root)
    root.geometry('1120x470')
    root.configure(bg='#5d6d7e') 
    root.attributes('-alpha', 0.93)
    root.mainloop()