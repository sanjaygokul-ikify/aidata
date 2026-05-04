import os
import yaml
from data import load_data
from model import train_model
from preprocessing import preprocess_data
from results import save_results

def main():
    config = yaml.safe_load(open('config.yaml'))
    data = load_data(config['data_path'])
    preprocessed_data = preprocess_data(data)
    model = train_model(preprocessed_data)
    results = model.predict(preprocessed_data)
    save_results(results, config['results_path'])
if __name__ == '__main__':
    main()