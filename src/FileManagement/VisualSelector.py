import sys
from PySide6.QtWidgets import QApplication, QFileDialog

class VisualSelector:
        
    def __init__(self):
        self.app = QApplication(sys.argv)
        
    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Select a File",
            "",
            "All Files (*.*)"
        )

        print("Selected:", file_path)
        return file_path
    
    def select_directory(self, prompt="Select a Directory"):
        directory_path = QFileDialog.getExistingDirectory(
            None,
            prompt,
            ""
        )
        # print("Selected Directory:", directory_path)
        return directory_path
