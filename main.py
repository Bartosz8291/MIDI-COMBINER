import tkinter as tk
from tkinter import filedialog, messagebox
from mido import MidiFile

def combine_files():
    try:
        # Ask how many files the user wants to combine
        num_files = int(num_files_entry.get())
        if num_files < 2:
            messagebox.showerror("Error", "You need at least 2 files to combine.")
            return
        
        # Select files
        file_paths = []
        for i in range(num_files):
            file_path = filedialog.askopenfilename(
                title=f"Select MIDI File {i + 1}",
                filetypes=[("MIDI Files", "*.mid *.midi")]
            )
            if not file_path:
                messagebox.showerror("Error", "File selection canceled.")
                return
            file_paths.append(file_path)
        
        # Combine files
        combined_midi = MidiFile()
        for file_path in file_paths:
            midi = MidiFile(file_path)
            for track in midi.tracks:
                combined_midi.tracks.append(track)
        
        # Save combined file
        save_path = filedialog.asksaveasfilename(
            title="Save Combined MIDI File",
            defaultextension=".mid",
            filetypes=[("MIDI Files", "*.mid *.midi")]
        )
        if not save_path:
            messagebox.showerror("Error", "File save canceled.")
            return
        
        combined_midi.save(save_path)
        messagebox.showinfo("Success", f"Combined MIDI saved to: {save_path}")
    except ValueError:
        messagebox.showerror("Error", "Invalid number of files. Please enter a number.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create GUI
root = tk.Tk()
root.title("MIDI File Combiner")

tk.Label(root, text="Enter the number of MIDI files to combine:").pack(pady=5)
num_files_entry = tk.Entry(root)
num_files_entry.pack(pady=5)

combine_button = tk.Button(root, text="Combine Files", command=combine_files)
combine_button.pack(pady=20)

root.mainloop()
