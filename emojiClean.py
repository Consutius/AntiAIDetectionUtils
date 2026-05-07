import sys
import subprocess
import os
from clean import cleanComments


def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(__file__), relative_path)


try:
    import emoji
    import tkinter as tk
except ImportError:
    print("Emoji library not installed. Running installer...")
    install_path = get_resource_path('install.bat')
    subprocess.run([install_path], shell=True)
    print("Installation complete. Please run the script again.")
    sys.exit(0)

from tkinter import filedialog, messagebox


def remove_emojis(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # replace_emoji defaults to an empty string, effectively deleting them
        clean_content = emoji.replace_emoji(content, replace='')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(clean_content)
            
        return f"Success! Emojis removed from: {file_path}"

    except FileNotFoundError:
        return "Error: The file was not found."
    except Exception as e:
        return f"An error occurred: {e}"
    


class EmojiCleanerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emoji Cleaner")
        self.root.geometry("400x200")

        self.label = tk.Label(root, text="Select a file to remove emojis from:")
        self.label.pack(pady=20)

        self.select_button = tk.Button(root, text="Select File", command=self.select_file)
        self.select_button.pack(pady=10)

        self.clean_button = tk.Button(root, text="Clean Emojis", command=self.clean_emojis, state=tk.DISABLED)
        self.clean_button.pack(pady=10)

        self.for_code_button = tk.Button(root, text="Clean Code Comments and Emojis", command=self.call_clean_comments, state=tk.DISABLED)
        self.for_code_button.pack(pady=10)

        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=20)

        self.file_path = None

    def select_file(self):
        self.file_path = filedialog.askopenfilename(title="Select file", filetypes=(("All files", "*.*"),))
        if self.file_path:
            self.clean_button.config(state=tk.NORMAL)
            self.status_label.config(text=f"Selected: {self.file_path}")

    def clean_emojis(self):
        if self.file_path:
            result = remove_emojis(self.file_path)
            messagebox.showinfo("Result", result)
            self.status_label.config(text=result)

    def call_clean_comments(self):
        if self.file_path:
            cleanComments(self.file_path)
            self.status_label.config(text=f"Success! Comments cleaned from: {self.file_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Command line mode
        file_path = sys.argv[1]
        result = remove_emojis(file_path)
        print(result)
    else:
        # GUI mode
        root = tk.Tk()
        app = EmojiCleanerApp(root)
        root.mainloop()