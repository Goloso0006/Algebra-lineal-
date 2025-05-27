import tkinter as tk
from tkinter import messagebox
from decimal import Decimal
import math
import matplotlib.pyplot as plt

def obtener_vectores():
    try:
        ax = Decimal(entry_ax.get())
        ay = Decimal(entry_ay.get())
        bx = Decimal(entry_bx.get())
        by = Decimal(entry_by.get())
        return [ax, ay], [bx, by]
    except Exception as e:
        messagebox.showerror("Error", "⚠️ Ingresa valores válidos para todos los campos")
        return None, None

def calcular_magnitud_a():
    v1, _ = obtener_vectores()
    if v1:
        mag = math.sqrt(float(v1[0])**2 + float(v1[1])**2)
        resultado.set(f"📐 Magnitud de A: {mag:.2f}")

def calcular_magnitud_b():
    _, v2 = obtener_vectores()
    if v2:
        mag = math.sqrt(float(v2[0])**2 + float(v2[1])**2)
        resultado.set(f"📐 Magnitud de B: {mag:.2f}")

def sumar_vectores():
    v1, v2 = obtener_vectores()
    if v1 and v2:
        suma_x = v1[0] + v2[0]
        suma_y = v1[1] + v2[1]
        
        # Magnitud del vector suma
        magnitud = math.sqrt(float(suma_x)**2 + float(suma_y)**2)
        
        # Dirección del vector suma (en grados)
        if suma_x == 0 and suma_y == 0:
            angulo = 0
        else:
            angulo_rad = math.atan2(float(suma_y), float(suma_x))
            angulo = math.degrees(angulo_rad)

        # Mostrar resultados
        resultado.set(f"➕ Vector suma: ({suma_x}, {suma_y})\n\n📏 Magnitud: {magnitud:.2f}\n\n📐 Ángulo: {angulo:.2f}°")

def producto_punto():
    v1, v2 = obtener_vectores()
    if v1 and v2:
        ax, ay = float(v1[0]), float(v1[1])
        bx, by = float(v2[0]), float(v2[1])
        
        # Producto punto
        dot = ax * bx + ay * by

        # Magnitudes de A y B
        mag_a = math.sqrt(ax**2 + ay**2)
        mag_b = math.sqrt(bx**2 + by**2)

        # Ángulo entre vectores
        if mag_a == 0 or mag_b == 0:
            resultado.set("⚠️ No se puede calcular el ángulo: uno de los vectores es nulo")
            return
        
        cos_theta = dot / (mag_a * mag_b)
        # Controlar valores fuera del rango por redondeo
        cos_theta = max(min(cos_theta, 1), -1)
        angulo = math.degrees(math.acos(cos_theta))

        # Mostrar resultado
        resultado.set(f"🎯 Producto punto: {dot:.2f}\n\n📐 Ángulo entre vectores: {angulo:.2f}°")

def producto_cruz():
    v1, v2 = obtener_vectores()
    if v1 and v2:
        ax1, ax2 = v1
        bx1, bx2 = v2
        ax3 = 5
        bx3 = -1
        i = +(ax2 * bx3 - bx2 * ax3)
        j = -(ax1 * bx3 - bx1 * ax3)
        k = +(ax1 * bx2 - bx1 * ax2)
        resultado.set(f"🔀 Producto cruz: {i:.3f}i   {j:.3f}j   {k:.3f}k")

def graficar_vectores():
    try:
        usar_mag_ang = all([
            entry_mag_a.get(), entry_ang_a.get(),
            entry_mag_b.get(), entry_ang_b.get()
        ])
        
        if usar_mag_ang:
            mag_a = Decimal(entry_mag_a.get())
            ang_a_deg = Decimal(entry_ang_a.get())
            ang_a_rad = math.radians(float(ang_a_deg))
            ax = float(mag_a * Decimal(math.cos(ang_a_rad)))
            ay = float(mag_a * Decimal(math.sin(ang_a_rad)))

            mag_b = Decimal(entry_mag_b.get())
            ang_b_deg = Decimal(entry_ang_b.get())
            ang_b_rad = math.radians(float(ang_b_deg))
            bx = float(mag_b * Decimal(math.cos(ang_b_rad)))
            by = float(mag_b * Decimal(math.sin(ang_b_rad)))
        else:
            v1, v2 = obtener_vectores()
            if not v1 or not v2:
                return
            ax, ay = float(v1[0]), float(v1[1])
            bx, by = float(v2[0]), float(v2[1])
            mag_a = math.sqrt(ax**2 + ay**2)
            ang_a_deg = math.degrees(math.atan2(ay, ax))
            mag_b = math.sqrt(bx**2 + by**2)
            ang_b_deg = math.degrees(math.atan2(by, bx))

        suma_x = ax + bx
        suma_y = ay + by
        
        plt.figure(figsize=(8, 8), facecolor='#edbb99')
        ax_main = plt.gca()

        # Vectores principales
        vec_a = ax_main.quiver(0, 0, ax, ay, angles='xy', scale_units='xy', scale=1, color='r', label='Vector A')
        vec_b = ax_main.quiver(0, 0, bx, by, angles='xy', scale_units='xy', scale=1, color='b', label='Vector B')
        vec_suma = ax_main.quiver(0, 0, suma_x, suma_y, angles='xy', scale_units='xy', scale=1, color='g', label='Suma A+B')

        # Componentes punteadas con colores distintos
        comp_a_x = ax_main.plot([0, ax], [0, 0], '--', color='red', linewidth=2)
        comp_a_y = ax_main.plot([ax, ax], [0, ay], '--', color='red', linewidth=2)
        comp_b_x = ax_main.plot([0, bx], [0, 0], '--', color='blue', linewidth=2)
        comp_b_y = ax_main.plot([bx, bx], [0, by], '--', color='blue', linewidth=2)
        
        # Etiquetas para Ax y Ay (vector A)
        ax_main.text(ax / 2, -0.8, 'Ax', fontsize=12, color='red', ha='center')
        ax_main.text(ax + 0.5, ay / 2, 'Ay', fontsize=12, color='red', va='center')

        # Etiquetas para Bx y By (vector B)
        ax_main.text(bx / 2, -0.8, 'Bx', fontsize=12, color='blue', ha='center')
        ax_main.text(bx -1, by / 2, 'By', fontsize=12, color='blue', va='center')

        # Ejes y ajustes generales
        ax_main.set_xlim(-12, 12)
        ax_main.set_ylim(-12, 12)
        ax_main.axhline(0, color='gray', linestyle='--')
        ax_main.axvline(0, color='gray', linestyle='--')
        ax_main.grid(True)
        ax_main.set_aspect('equal', adjustable='box')

        # Primera leyenda - vectores principales
        legend1 = ax_main.legend(loc='upper left', fontsize=10, title="Vectores")

        # Segunda leyenda - componentes con medidas
        comp_labels = [
            f"Ax = {ax:.2f}", f"Ay = {ay:.2f}",
            f"Bx = {bx:.2f}", f"By = {by:.2f}"
        ]
        comp_colors = ['red', 'red', 'blue', 'blue']
        from matplotlib.lines import Line2D
        legend_lines = [Line2D([0], [0], color=comp_colors[i], linestyle='--', linewidth=2) for i in range(4)]
        legend2 = ax_main.legend(legend_lines, comp_labels, loc='lower right', fontsize=10, title="Componentes")

        # Añadir ambas leyendas al gráfico
        ax_main.add_artist(legend1)
        ax_main.add_artist(legend2)
        
        # Título y etiquetas
        plt.title('Vectores y Componentes Rectangulares')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.tight_layout()
        
        
    #   ---------------------------------------------------------------------------  
        
        
        # ===== MODO LÁPIZ INTERACTIVO =====
        modo_dibujo = {'activo': False, 'x0': None, 'y0': None}
        vector_preview = {'linea': None}

        def activar_dibujo(event):
            if event.key == 'd':
                modo_dibujo['activo'] = not modo_dibujo['activo']
                if modo_dibujo['activo']:
                    print("🖊️ Modo dibujo ACTIVADO (usa el mouse)")
                else:
                    print("❌ Modo dibujo DESACTIVADO")

        def on_mouse_press(event):
            if modo_dibujo['activo'] and event.inaxes:
                modo_dibujo['x0'], modo_dibujo['y0'] = event.xdata, event.ydata

        def on_mouse_release(event):
            if modo_dibujo['activo'] and event.inaxes:
                x0, y0 = modo_dibujo['x0'], modo_dibujo['y0']
                x1, y1 = event.xdata, event.ydata
                dx, dy = x1 - x0, y1 - y0
                magnitud = math.sqrt(dx**2 + dy**2)

            # Dibuja el vector permanente
            ax_main.quiver(x0, y0, dx, dy, angles='xy', scale_units='xy', scale=1, color='purple')
            
            offset_x = 0.7  # cuánto desplazar en x
            offset_y = 0.7  # cuánto desplazar en y

            ax_main.text(x1 + offset_x, y1 + offset_y, f"📐 {magnitud:.2f}, ({dx:.2f}, {dy:.2f})",fontsize=11,fontweight='bold',color='purple')
            plt.draw()

        def on_mouse_move(event):
            if modo_dibujo['activo'] and event.inaxes and modo_dibujo['x0'] is not None:
                x0, y0 = modo_dibujo['x0'], modo_dibujo['y0']
                x1, y1 = event.xdata, event.ydata
                dx, dy = x1 - x0, y1 - y0

                if vector_preview['linea']:
                    vector_preview['linea'].remove()


        # Conectar eventos
        canvas = plt.gcf().canvas
        canvas.mpl_connect('key_press_event', activar_dibujo)
        canvas.mpl_connect('button_press_event', on_mouse_press)
        canvas.mpl_connect('button_release_event', on_mouse_release)
        canvas.mpl_connect('motion_notify_event', on_mouse_move)

        
    #   ---------------------------------------------------------------------------  
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"⚠️ Error al graficar: {e}")

def convertir_magnitud_angulo():
    try:
        mag_a = Decimal(entry_mag_a.get())
        ang_a_deg = Decimal(entry_ang_a.get())
        mag_b = Decimal(entry_mag_b.get())
        ang_b_deg = Decimal(entry_ang_b.get())

        ang_a_rad = math.radians(float(ang_a_deg))
        ang_b_rad = math.radians(float(ang_b_deg))

        ax = mag_a * Decimal(math.cos(ang_a_rad))
        ay = mag_a * Decimal(math.sin(ang_a_rad))
        bx = mag_b * Decimal(math.cos(ang_b_rad))
        by = mag_b * Decimal(math.sin(ang_b_rad))

        entry_ax.delete(0, tk.END)
        entry_ay.delete(0, tk.END)
        entry_bx.delete(0, tk.END)
        entry_by.delete(0, tk.END)

        entry_ax.insert(0, f"{ax:.2f}")
        entry_ay.insert(0, f"{ay:.2f}")
        entry_bx.insert(0, f"{bx:.2f}")
        entry_by.insert(0, f"{by:.2f}")

        resultado.set(f"✅ Componentes: \n\nA=({ax:.2f}, {ay:.2f}) \nB=({bx:.2f}, {by:.2f})")
    except:
        messagebox.showerror("Error", "⚠️ Ingresa magnitud y ángulo válidos")

# Interfaz Gráfica
ventana = tk.Tk()
ventana.configure(bg='#aab7b8')       
ventana.title("Calculadora de Vectores")
ventana.geometry("400x355+1+1")
ventana.resizable(False, False)
ventana.attributes('-alpha', 0.93)

# Etiquetas e inputs para Vector A y B
tk.Label(ventana, text="Vector A",bg='#cd6155',width=19).place(x=20,y=15)
tk.Label(ventana, text="Vector B",bg='#5dade2',width=19).place(x=224,y=15)

entry_ax = tk.Entry(ventana, width=10)
entry_ay = tk.Entry(ventana, width=10)
entry_bx = tk.Entry(ventana, width=10)
entry_by = tk.Entry(ventana, width=10)
entry_ax.place(x=20, y=40)
entry_ay.place(x=94, y=40)
entry_bx.place(x=224, y=40)
entry_by.place(x=298, y=40)

# Nuevos inputs para magnitud y ángulo
tk.Label(ventana, text="Mag. A", bg='#d6dbdf',width=9).place(x=18, y=70)
tk.Label(ventana, text="Áng. A (°)", bg='#d6dbdf',width=9).place(x=92, y=70)
entry_mag_a = tk.Entry(ventana, width=11)
entry_ang_a = tk.Entry(ventana, width=11)
entry_mag_a.place(x=18, y=93)
entry_ang_a.place(x=92, y=93)

tk.Label(ventana, text="Mag. B", bg='#d6dbdf',width=9).place(x=221, y=68)
tk.Label(ventana, text="Áng. B (°)", bg='#d6dbdf',width=9).place(x=297, y=70)
entry_mag_b = tk.Entry(ventana, width=11)
entry_ang_b = tk.Entry(ventana, width=11)
entry_mag_b.place(x=221, y=93)
entry_ang_b.place(x=297, y=93)

# Botón para convertir magnitud/ángulo a componentes
tk.Button(ventana, text="↪️ Convertir Mag+Áng", command=convertir_magnitud_angulo, bg='#f9e79f', width=48).place(x=20, y=130)

# Botones de operaciones
tk.Button(ventana, text="📐 Magnitud A", command=calcular_magnitud_a, width=15, bg='#d1f2eb').place(y=165, x=20)
tk.Button(ventana, text="📐 Magnitud B", command=calcular_magnitud_b, width=13, bg='#d1f2eb').place(y=165, x=140)
tk.Button(ventana, text="➕ Sumar Vectores", command=sumar_vectores, bg='#d1f2eb', width=15).place(y=165, x=248)
tk.Button(ventana, text="✴️ Producto Punto", command=producto_punto, bg='#fcf3cf').place(y=205, x=20)
tk.Button(ventana, text="🔀 Producto Cruz", command=producto_cruz, bg='#fcf3cf').place(y=205, x=140)
tk.Button(ventana, text="📊 Graficar Vectores", command=graficar_vectores, bg='#fcf3cf').place(y=205, x=248)

# Área para mostrar resultados
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, justify="left", fg="black", bg='#aab7b8', font=('arial', 12)).place(x=20, y=250)

ventana.mainloop()