import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil
from pathlib import Path


class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Intelligent File Organizer")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # File type mappings
        self.file_categories = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.webp'],
            'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx', '.ppt', '.odt', '.csv'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
            'Scripts': ['.py', '.js', '.html', '.css', '.cpp', '.c', '.java', '.php', '.rb', '.go', '.sh']
        }

        self.selected_folder = None
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        title_label = tk.Label(
            self.root,
            text="📂 Intelligent File Organizer",
            font=("Arial", 18, "bold"),
            fg="#2c3e50"
        )
        title_label.pack(pady=20)

        # Description
        desc_label = tk.Label(
            self.root,
            text="Automatically organize your files into categorized folders",
            font=("Arial", 10),
            fg="#7f8c8d"
        )
        desc_label.pack(pady=5)

        # Folder selection frame
        folder_frame = tk.Frame(self.root)
        folder_frame.pack(pady=20, padx=20, fill='x')

        self.folder_label = tk.Label(
            folder_frame,
            text="No folder selected",
            font=("Arial", 10),
            fg="#95a5a6",
            bg="#ecf0f1",
            relief="sunken",
            anchor="w",
            padx=10,
            pady=10
        )
        self.folder_label.pack(side='left', fill='x', expand=True)

        browse_btn = tk.Button(
            folder_frame,
            text="Browse",
            command=self.browse_folder,
            font=("Arial", 10, "bold"),
            bg="#3498db",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
            relief="flat"
        )
        browse_btn.pack(side='right', padx=(10, 0))

        # Progress bar
        progress_frame = tk.Frame(self.root)
        progress_frame.pack(pady=20, padx=20, fill='x')

        self.progress_label = tk.Label(
            progress_frame,
            text="Ready to organize files",
            font=("Arial", 9),
            fg="#7f8c8d"
        )
        self.progress_label.pack(anchor='w', pady=(0, 5))

        self.progress_bar = ttk.Progressbar(
            progress_frame,
            mode='determinate',
            length=560
        )
        self.progress_bar.pack()

        # Organize button
        self.organize_btn = tk.Button(
            self.root,
            text="Organize Files",
            command=self.organize_files,
            font=("Arial", 12, "bold"),
            bg="#27ae60",
            fg="white",
            padx=30,
            pady=15,
            cursor="hand2",
            relief="flat",
            state='disabled'
        )
        self.organize_btn.pack(pady=20)

        # Status text
        self.status_text = tk.Text(
            self.root,
            height=6,
            width=70,
            font=("Courier", 9),
            bg="#ecf0f1",
            relief="sunken",
            state='disabled'
        )
        self.status_text.pack(pady=10, padx=20)

    def browse_folder(self):
        folder = filedialog.askdirectory(title="Select Folder to Organize")
        if folder:
            self.selected_folder = folder
            self.folder_label.config(text=folder, fg="#2c3e50")
            self.organize_btn.config(state='normal')
            self.log_status(f"Selected folder: {folder}")

    def log_status(self, message):
        self.status_text.config(state='normal')
        self.status_text.insert('end', message + '\n')
        self.status_text.see('end')
        self.status_text.config(state='disabled')
        self.root.update_idletasks()

    def organize_files(self):
        if not self.selected_folder:
            messagebox.showerror("Error", "Please select a folder first!")
            return

        # Reset progress
        self.progress_bar['value'] = 0
        self.status_text.config(state='normal')
        self.status_text.delete('1.0', 'end')
        self.status_text.config(state='disabled')

        self.log_status("Starting file organization...")
        self.organize_btn.config(state='disabled')

        try:
            # Get all files
            all_files = [f for f in os.listdir(self.selected_folder)
                         if os.path.isfile(os.path.join(self.selected_folder, f))]

            if not all_files:
                self.log_status("No files found to organize.")
                messagebox.showinfo("Info", "No files found in the selected folder.")
                self.organize_btn.config(state='normal')
                return

            total_files = len(all_files)
            files_moved = 0

            self.log_status(f"Found {total_files} files to organize.\n")

            # Create category folders
            for category in self.file_categories.keys():
                category_path = os.path.join(self.selected_folder, category)
                if not os.path.exists(category_path):
                    os.makedirs(category_path)
                    self.log_status(f"Created folder: {category}")

            # Organize files
            for idx, filename in enumerate(all_files, 1):
                file_ext = Path(filename).suffix.lower()
                source_path = os.path.join(self.selected_folder, filename)

                # Find category for file
                moved = False
                for category, extensions in self.file_categories.items():
                    if file_ext in extensions:
                        dest_folder = os.path.join(self.selected_folder, category)
                        dest_path = os.path.join(dest_folder, filename)

                        # Handle duplicate filenames
                        if os.path.exists(dest_path):
                            base, ext = os.path.splitext(filename)
                            counter = 1
                            while os.path.exists(dest_path):
                                new_filename = f"{base}_{counter}{ext}"
                                dest_path = os.path.join(dest_folder, new_filename)
                                counter += 1

                        shutil.move(source_path, dest_path)
                        self.log_status(f"✓ Moved: {filename} → {category}/")
                        files_moved += 1
                        moved = True
                        break

                if not moved:
                    self.log_status(f"⊘ Skipped: {filename} (unknown type)")

                # Update progress
                progress = (idx / total_files) * 100
                self.progress_bar['value'] = progress
                self.progress_label.config(text=f"Processing: {idx}/{total_files} files")
                self.root.update_idletasks()

            # Complete
            self.progress_label.config(text="Organization complete!")
            self.log_status(f"\n✓ Successfully organized {files_moved} out of {total_files} files!")
            messagebox.showinfo("Success", f"Successfully organized {files_moved} files!")

        except Exception as e:
            self.log_status(f"\n✗ Error: {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        finally:
            self.organize_btn.config(state='normal')


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()