import tkinter as tk
from turingMachine import TuringMachine

class TuringInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Verificación con Máquina de Turing")
        self.root.geometry("420x320")
        self.root.configure(bg="#8847a3")

        self.title_label = tk.Label(
            self.root, text="Verificador de Cadenas", font=("Arial", 20, "bold"), bg="#8847a3", fg="#ffffff"
        )
        self.title_label.pack(pady=15)

        self.instruction_label = tk.Label(
            self.root, text="Ingresa la cadena binaria a analizar:", font=("Arial", 12), bg="#8847a3", fg="#f0e3ff"
        )
        self.instruction_label.pack(pady=10)

        self.input_entry = tk.Entry(self.root, font=("Arial", 12), bg="#d4b3e7", fg="#350047")
        self.input_entry.pack(pady=10)

        self.verify_button = tk.Button(
            self.root, text="Verificar", font=("Arial", 12, "bold"), bg="#9b2f7b", fg="white",
            relief="flat", padx=10, pady=5, command=self.verify_input
        )
        self.verify_button.pack(pady=15)

        self.result_label = tk.Label(
            self.root, text="", font=("Arial", 12), bg="#8847a3", fg="#f0e3ff"
        )
        self.result_label.pack(pady=10)

    def verify_input(self):
        input_string = self.input_entry.get().strip()

        if not input_string.isdigit() or any(char not in '01' for char in input_string):
            self.show_popup("Error: Solo se permiten caracteres binarios (0 y 1)", "Error", "#e74c3c")
            return

        try:
            turing_machine = TuringMachine(list(input_string))
            is_valid, total_sum = turing_machine.run()

            if is_valid:
                binary_sum = bin(total_sum)[2:]
                self.show_popup(f"Resultado: Suma = {total_sum}, Binario = {binary_sum}", "Éxito", "#2ecc71")
            else:
                self.show_popup("La cadena es inválida", "Resultado", "#c0392b")

        except Exception as error:
            self.show_popup(f"Se produjo un error: {str(error)}", "Error", "#c0392b")

    def show_popup(self, message, title, color):
        popup_window = tk.Toplevel(self.root)
        popup_window.title(title)
        popup_window.geometry("300x150")
        popup_window.configure(bg="#8847a3")

        message_label = tk.Label(
            popup_window, text=message, font=("Arial", 12, "bold"), bg="#8847a3", fg=color
        )
        message_label.pack(pady=20)

        close_btn = tk.Button(
            popup_window, text="Cerrar", font=("Arial", 12, "bold"), bg="#9b2f7b", fg="white",
            relief="flat", padx=10, pady=5, command=popup_window.destroy
        )
        close_btn.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = TuringInterface(root)
    root.mainloop()
