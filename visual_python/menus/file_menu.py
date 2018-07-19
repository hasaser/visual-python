import tkinter as tk
import tkinter.filedialog as tk_filedialog
import tokenize
import os

class FileMenu(tk.Menu):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.opened_file_path = None
        # Add open file command
        self.add_command(label='Open File', command=self.open_file)
        # Add save file command
        self.add_command(label='Save File', command=self.save_file)
        # Add save file as command
        self.add_command(label='Save File as...', command=self.save_file_as)

    def open_file(self):
        self.opened_file_path = tk_filedialog.askopenfilename(parent=self.app, filetypes=[('Python Files', '.py')])
        if self.opened_file_path:
            # Set editor text with file content
            with tokenize.open(self.opened_file_path) as file:
                self.app.main_frame.editor_frame.text_widget.set_text(file.read())
            # Prefix window title with opened file name
            opened_file_name = os.path.basename(self.opened_file_path)
            self.app.title(f'{opened_file_name} - {self.app.app_title}')

    def save_file(self):
        # If a file is not opened before, call save_file_as method
        # Else, save editor text to file
        if not self.opened_file_path:
            self.save_file_as()
        else:
            with open(self.opened_file_path, 'w', encoding='UTF-8') as file:
                file.write(self.app.main_frame.editor_frame.text_widget.get_wo_eol())
            # Prefix window title with opened file name
            opened_file_name = os.path.basename(self.opened_file_path)
            self.app.title(f'{opened_file_name} - {self.app.app_title}')

    def save_file_as(self):
        self.opened_file_path = tk_filedialog.asksaveasfilename(
            parent=self.app,
            defaultextension='.py',
            filetypes=[('Python Files', '.py')]
        )
        if self.opened_file_path:
            with open(self.opened_file_path, 'w', encoding='UTF-8') as file:
                file.write(self.app.main_frame.editor_frame.text_widget.get_wo_eol())
            # Prefix window title with opened file name
            opened_file_name = os.path.basename(self.opened_file_path)
            self.app.title(f'{opened_file_name} - {self.app.app_title}')
