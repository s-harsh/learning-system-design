"""
Day 9: Template Method Pattern Demo
Scenario: Data ETL Pipeline.
We process CSV and PDF files. The overall workflow is the same, but the 'Parsing' step differs.
"""

from abc import ABC, abstractmethod

# ==========================================
# 1. The Abstract Base Class (Template)
# ==========================================
class DataPipeline(ABC):
    
    def run_pipeline(self, file_path):
        """
        The Template Method.
        Defines the skeleton of the algorithm.
        """
        print(f"\n--- Starting Pipeline for: {file_path} ---")
        self.open_file(file_path)
        data = self.extract_data()
        self.analyze_data(data)
        self.close_file()
        print("--- Pipeline Finished ---")

    # --- Common Steps ---
    def open_file(self, path):
        print(f"📂 Opening file at {path}...")
    
    def analyze_data(self, data):
        print(f"🧠 AI Analysis running on: '{data}'")
        
    def close_file(self):
        print("🔒 Closing file resource.")

    # --- Steps that must be overridden ---
    @abstractmethod
    def extract_data(self):
        pass

# ==========================================
# 2. Concrete Classes
# ==========================================
class CSVDataPipeline(DataPipeline):
    def extract_data(self):
        print("📄 text/csv detected. Splitting by commas...")
        return "CSV_DATA_PAYLOAD"

class PDFDataPipeline(DataPipeline):
    def extract_data(self):
        print("📑 application/pdf detected. Running OCR...")
        return "PDF_OCR_PAYLOAD"

# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    print("--- Template Method Pattern Demo: ETL ---")

    # 1. Process CSV
    csv_pipe = CSVDataPipeline()
    csv_pipe.run_pipeline("sales_data.csv")

    # 2. Process PDF
    pdf_pipe = PDFDataPipeline()
    pdf_pipe.run_pipeline("invoice_101.pdf")
