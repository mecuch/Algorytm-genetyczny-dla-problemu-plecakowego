
import tkinter as tk
from tkinter import ttk, messagebox

from knapsackga import KnapsackProblemAG


class SimpleApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Problem Plecakowy - AG")
        self.center_window(700, 340)
        self.resizable(False, False)

        # ====== Warunek stopu ======
        self.option_var = tk.StringVar(value="generations")  # "generations" | "stagnation"

        frame_radio = ttk.Frame(self)
        frame_radio.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        ttk.Label(frame_radio, text="Warunek zatrzymania algorytmu:").grid(row=0, column=0, padx=5)

        ttk.Radiobutton(
            frame_radio,
            text="liczba generacji",
            variable=self.option_var,
            value="generations"
        ).grid(row=0, column=1, padx=5)

        ttk.Radiobutton(
            frame_radio,
            text="brak poprawy (stagnacja)",
            variable=self.option_var,
            value="stagnation"
        ).grid(row=0, column=2, padx=5)

        # ====== Pola wejściowe ======
        frame_input = ttk.Frame(self)
        frame_input.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Rząd 1
        ttk.Label(frame_input, text="Liczba przedmiotów").grid(row=0, column=0, padx=5, sticky="w")
        self.entry_num_items = ttk.Entry(frame_input, width=6)
        self.entry_num_items.grid(row=0, column=1, padx=5, sticky="w")

        ttk.Label(frame_input, text="Liczba osobników").grid(row=0, column=2, padx=5, sticky="w")
        self.entry_num_individ = ttk.Entry(frame_input, width=6)
        self.entry_num_individ.grid(row=0, column=3, padx=5, sticky="w")

        # Rząd 2
        ttk.Label(frame_input, text="Wagi (np. 3,5,1,8)").grid(row=1, column=0, padx=5, sticky="w")
        self.entry_weights = ttk.Entry(frame_input, width=24)
        self.entry_weights.grid(row=1, column=1, padx=5, sticky="w")

        ttk.Label(frame_input, text="Wartości (np. 2,3,4,5)").grid(row=1, column=2, padx=5, sticky="w")
        self.entry_values = ttk.Entry(frame_input, width=24)
        self.entry_values.grid(row=1, column=3, padx=5, sticky="w")

        # Rząd 3
        ttk.Label(frame_input, text="Maks. udźwig").grid(row=2, column=0, padx=5, sticky="w")
        self.entry_capacity = ttk.Entry(frame_input, width=6)
        self.entry_capacity.grid(row=2, column=1, padx=5, sticky="w")

        ttk.Label(frame_input, text="Stagnacja X (gdy wybrano 2)").grid(row=2, column=2, padx=5, sticky="w")
        self.entry_max_stagnation = ttk.Entry(frame_input, width=6)
        self.entry_max_stagnation.grid(row=2, column=3, padx=5, sticky="w")

        # Rząd 4
        ttk.Label(frame_input, text="Liczba generacji (gdy wybrano 1)").grid(row=3, column=0, padx=5, sticky="w")
        self.entry_generations = ttk.Entry(frame_input, width=6)
        self.entry_generations.grid(row=3, column=1, padx=5, sticky="w")

        ttk.Label(frame_input, text="P(krzyżowania) (opcjonalnie)").grid(row=3, column=2, padx=5, sticky="w")
        self.entry_pc = ttk.Entry(frame_input, width=6)
        self.entry_pc.grid(row=3, column=3, padx=5, sticky="w")

        ttk.Label(frame_input, text="P(mutacji) (opcjonalnie)").grid(row=4, column=2, padx=5, sticky="w")
        self.entry_pm = ttk.Entry(frame_input, width=6)
        self.entry_pm.grid(row=4, column=3, padx=5, sticky="w")

        # ====== Przycisk ======
        self.button = ttk.Button(self, text="Uruchom algorytm", command=self.on_button_click)
        self.button.grid(row=5, column=0, padx=10, pady=12, sticky="w")

        # ====== Wynik ======
        frame_output = ttk.Frame(self)
        frame_output.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        ttk.Label(frame_output, text="Wynik algorytmu (najlepszy osobnik):").grid(row=0, column=0, padx=5, sticky="w")
        self.output_var = tk.StringVar(value="-")
        ttk.Label(frame_output, textvariable=self.output_var).grid(row=0, column=1, padx=5, sticky="w")

        # (opcjonalnie) Ustaw wartości startowe, żeby szybciej testować GUI
        self._prefill_example()

    def center_window(self, width: int, height: int):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.geometry(f"{width}x{height}+{x}+{y}")

    # ---------- parsowanie bez ast ----------
    def parse_list_of_ints(self, text: str) -> list[int]:
        text = text.strip()
        if text.startswith("[") and text.endswith("]"):
            text = text[1:-1].strip()

        if text == "":
            raise ValueError("Lista nie może być pusta.")

        parts = text.split(",")
        result = []
        for p in parts:
            p = p.strip()
            if p == "":
                raise ValueError("Nieprawidłowy format listy (pusty element).")
            result.append(int(p))
        return result

    def _parse_int(self, entry: ttk.Entry, field_name: str) -> int:
        raw = entry.get().strip()
        if raw == "":
            raise ValueError(f"Pole '{field_name}' jest puste.")
        return int(raw)

    def _parse_float_optional(self, entry: ttk.Entry):
        raw = entry.get().strip()
        if raw == "":
            return None
        return float(raw.replace(",", "."))

    def _prefill_example(self):
        self.entry_num_items.insert(0, "6")
        self.entry_num_individ.insert(0, "10")
        self.entry_weights.insert(0, "3,5,1,8,9,4")
        self.entry_values.insert(0, "2,3,4,5,6,7")
        self.entry_capacity.insert(0, "14")
        self.entry_max_stagnation.insert(0, "50")
        self.entry_generations.insert(0, "50")
        self.entry_pc.insert(0, "0.8")
        self.entry_pm.insert(0, "0.2")

    def on_button_click(self):
        try:
            num_items = self._parse_int(self.entry_num_items, "Liczba przedmiotów")
            num_individ = self._parse_int(self.entry_num_individ, "Liczba osobników")
            weights = self.parse_list_of_ints(self.entry_weights.get())
            values = self.parse_list_of_ints(self.entry_values.get())
            capacity = self._parse_int(self.entry_capacity, "Maks. udźwig")
            max_stagnation = self._parse_int(self.entry_max_stagnation, "Stagnacja X")
            generations = self._parse_int(self.entry_generations, "Liczba generacji")

            # opcjonalnie (GUI pozwala wpisać, ale Twoja klasa może mieć Pc/Pm na stałe)
            pc = self._parse_float_optional(self.entry_pc)
            pm = self._parse_float_optional(self.entry_pm)

            if len(weights) != num_items or len(values) != num_items:
                raise ValueError("Długość list wag i wartości musi być równa liczbie przedmiotów.")
            if num_items <= 1:
                raise ValueError("Liczba przedmiotów musi być >= 2 (krzyżowanie jednopunktowe).")

            mode = self.option_var.get()
            stop_numb = (mode == "generations")
            stop_stag = (mode == "stagnation")

            # Jeśli Twoja klasa nie przyjmuje 'generations', usuń ten argument tutaj
            ag = KnapsackProblemAG(
                num_of_items=num_items,
                num_of_individ=num_individ,
                max_stagnation=max_stagnation,
                weight_items=weights,
                value_items=values,
                load_capacity=capacity,
                pc=0.8,
                pm=0.2,
                stop_numb=stop_numb,
                stop_stag=stop_stag
            )

            stop_numb = True,
            stop_stag = False

            if stop_numb:
                best_ind, best_fit = ag.stop_by_numb()
            else:
                best_ind, best_fit = ag.stop_by_stagnation()

            self.output_var.set(f"osobnik={best_ind}, fitness={best_fit}")

        except Exception as e:
            messagebox.showerror("Błąd", str(e))


if __name__ == "__main__":
    app = SimpleApp()
    app.mainloop()
