# main.py

import pandas as pd
from data_loader import DataLoader
from data_processor import DataProcessor
from visualizer import Visualizer

def main():
    # Initialize components
    data_loader = DataLoader()
    data_processor = DataProcessor()
    visualizer = Visualizer()

    # Load data
    data = data_loader.load_data('data/sample_data.csv')

    # Process data
    cleaned_data = data_processor.clean_data(data)
    analysis_results = data_processor.analyze_data(cleaned_data)

    # Visualize data
    visualizer.plot_data(cleaned_data)
    visualizer.show_summary(analysis_results)

if __name__ == "__main__":
    main()