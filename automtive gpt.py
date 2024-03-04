import tkinter as tk
from tkinter import scrolledtext, ttk
from openai import OpenAI

class ChatBotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Automotive GPT")

        # Set background color
        self.window.configure(bg="#333")

        self.text_area = scrolledtext.ScrolledText(
            self.window, wrap=tk.WORD, width=50, height=5, bg="#222", fg="white", font=("Sans Serif", 12)
        )
        self.text_area.pack(padx=10, pady=10)

        self.style = ttk.Style()
        self.style.configure("TButton", foreground="black", background="green", font=("Sans Serif", 12))

        self.button = ttk.Button(self.window, text="Ask", command=self.ask_question, style="TButton")
        self.button.pack(pady=5)

        self.answer_text = scrolledtext.ScrolledText(
            self.window, wrap=tk.WORD, width=50, height=10, state=tk.DISABLED, bg="#222", fg="white", font=("Sans Serif", 12)
        )
        self.answer_text.pack(pady=10)

        self.client = OpenAI(api_key="")

    def ask_question(self):
        user_input = self.text_area.get("1.0", tk.END).strip()
        prompt = f"user: {user_input}\n{user_input}\nAI:"
        
        chat_completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}]
        )
        
        answer = chat_completion.choices[0].message.content
        self.display_answer(answer)

    def display_answer(self, answer):
        self.answer_text.config(state=tk.NORMAL)
        self.answer_text.delete(1.0, tk.END)

        for char in answer:
            self.answer_text.insert(tk.END, char)
            self.window.update_idletasks()
            self.window.after(20)  # Adjust the animation speed by changing the sleep duration

        self.answer_text.yview(tk.END)
        self.answer_text.config(state=tk.DISABLED)

    def run(self):
        self.window.geometry("500x400")
        self.text_area.config(height=7)
        self.text_area.config(wrap=tk.WORD)

        self.window.mainloop()

if __name__ == "__main__":
    chatbot_gui = ChatBotGUI()
    chatbot_gui.run()
