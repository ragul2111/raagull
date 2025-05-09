import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PersonalFinanceDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Dashboard")
        self.root.configure(bg='light blue')  

        self.monthly_income = tk.StringVar()
        self.monthly_expenses = tk.StringVar()
        self.monthly_savings = tk.StringVar()
        self.monthly_investments = tk.StringVar()

        self.create_gui()

    def create_gui(self):
        input_frame = tk.LabelFrame(self.root, text="Enter Monthly Financial Data", bg='white')
        input_frame.pack(padx=20, pady=10, fill=tk.BOTH)

        tk.Label(input_frame, text="Monthly Income:", bg='light gray').grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        tk.Entry(input_frame, textvariable=self.monthly_income).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Monthly Expenses:", bg='light gray').grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        tk.Entry(input_frame, textvariable=self.monthly_expenses).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Monthly Savings:", bg='light gray').grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        tk.Entry(input_frame, textvariable=self.monthly_savings).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Monthly Investments:", bg='light gray').grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
        tk.Entry(input_frame, textvariable=self.monthly_investments).grid(row=3, column=1, padx=10, pady=5)

        update_button = tk.Button(input_frame, text="Update Data", command=self.update_data)
        update_button.grid(row=4, columnspan=2, pady=10)

        self.chart_frame = tk.Frame(self.root, bg='white')  # Set background color for chart frame
        self.chart_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    def update_data(self):
        try:
           
            income_str = self.monthly_income.get()
            expenses_str = self.monthly_expenses.get()
            savings_str = self.monthly_savings.get()
            investments_str = self.monthly_investments.get()

            if not (income_str.replace('.', '', 1).isdigit() and
                    expenses_str.replace('.', '', 1).isdigit() and
                    savings_str.replace('.', '', 1).isdigit() and
                    investments_str.replace('.', '', 1).isdigit()):
                messagebox.showerror("Error", "Please enter valid numeric values")
                return

            income = float(income_str)
            expenses = float(expenses_str)
            savings = float(savings_str)
            investments = float(investments_str)

            
            if income < 0 or expenses < 0 or savings < 0 or investments < 0:
                messagebox.showerror("Error", "Values cannot be negative")
                return

            
            if income <= expenses + savings + investments:
                messagebox.showerror("Error", "monthly income not tagly")
                return

            for widget in self.chart_frame.winfo_children():
                widget.destroy()

            labels = ['Income', 'Expenses', 'Savings', 'Investments']
            values = [income, expenses, savings, investments]

            fig, ax = plt.subplots()
            ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  
            

            canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values")

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalFinanceDashboard(root)
    root.mainloop()
