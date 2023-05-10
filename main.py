import argparse
import csv
import numpy as np
import pickle
from neuron import NeuralNetwork

def parse_args():
    parser = argparse.ArgumentParser(description='Neural Network Trainer')
    parser.add_argument('--num_inputs', type=int, default=2, help='Number of input neurons')
    parser.add_argument('--num_outputs', type=int, default=1, help='Number of output neurons')
    parser.add_argument('--num_hidden', type=int, default=2, help='Number of neurons in the hidden layer')
    parser.add_argument('--num_layers', type=int, default=1, help='Number of hidden layers')
    parser.add_argument('--use_memory', action='store_true', help='Use neurons with memory')
    parser.add_argument('--dataset', type=str, default='dataset.csv', help='Path to the dataset CSV file')
    parser.add_argument('--epochs', type=int, default=100, help='Number of training epochs')
    parser.add_argument('--learning_rate', type=float, default=0.1, help='Learning rate for training')
    parser.add_argument('--save_model', action='store_true', help='Save the trained model')
    parser.add_argument('--model_file', type=str, default='model.pkl', help='File path to save the trained model')
    return parser.parse_args()

def load_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Ignore the first row (column labels)
        for row in reader:
            inputs = list(map(float, row[:-1]))
            output = float(row[-1])
            dataset.append((inputs, output))
    return dataset

def train(neural_network, dataset, epochs, learning_rate):
    for epoch in range(epochs):
        total_error = 0.0
        for inputs, target in dataset:
            neural_network.calculate(inputs)
            output = neural_network.get_output()[0]
            error = target - output
            neural_network.backpropagate(error, learning_rate)
            total_error += abs(error)
        avg_error = total_error / len(dataset)
        print(f'Epoch {epoch+1}/{epochs}, Average Error: {avg_error}')

def save_model(neural_network, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(neural_network, file)
    print(f'Model saved to {file_path}')

def main():
    args = parse_args()

    neural_network = NeuralNetwork(args.num_inputs, args.num_outputs, args.num_hidden, args.num_layers)

    dataset = load_dataset(args.dataset)

    train(neural_network, dataset, args.epochs, args.learning_rate)

    # Generate random inputs
    inputs = np.random.rand(args.num_inputs)

    print('Input:', inputs)
    neural_network.calculate(inputs)
    print('Output:', neural_network.get_output())

    if args.save_model:
        save_model(neural_network, args.model_file)

if __name__ == '__main__':
    main()
