import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QTableWidget, QTableWidgetItem, QFileDialog, QLabel
)
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

class DataViewer (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Viewer")
        self.resize(800, 600)

        # Layout
        self.layout= QVBoxLayout()

        #Button
        self.load_button = QPushButton("Load CSV File")
        self.load_button.clicked.connect(self.load_csv)
        self.layout.addWidget(self.load_button)

        #Label
        self.info_label = QLabel("No file loaded.")
        self.layout.addWidget(self.info_label)

        #Table
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)

    def load_csv(self):
        file_path = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        df = pd.read_csv(file_path[0])
        self.display_data(df)
        self.info_label.setText(f"Loaded: {file_path}")
        self.plot_column(df)

    def display_data(self, df):
        self.table.setRowCount(df.shape[0])
        self.table.setColumnCount(df.shape[1])
        self.table.setHorizontalHeaderLabels(df.columns)

        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                self.table.setItem(i,j,QTableWidgetItem(str(df.iat[i, j])))

    def plot_column(self, df):
        numeric_cols = df.select_dtypes(include='number').columns
        if not numeric_cols.empty:
            col = numeric_cols[0]
            fig = px.histogram(df, x=col, nbins=20, title=f"Histogram of {col}")
            fig.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = DataViewer()
    viewer.show()
    sys.exit(app.exec())




