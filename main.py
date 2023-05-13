import argparse
import pickle

from convert_img import *
from neuron import *

def load_images(image_paths, image_size):
    images = []
    for image_path in image_paths:
        img = get_img(image_path, image_size, image_size)
        images.append(img)
    return images


def parse_args():
    parser = argparse.ArgumentParser(description='Neural Network Trainer')
    parser.add_argument('--num_inputs', type=int, default=2, help='Number of input neurons')
    parser.add_argument('--num_outputs', type=int, default=1, help='Number of output neurons')
    parser.add_argument('--num_hidden', type=int, default=2, help='Number of neurons in the hidden layer')
    parser.add_argument('--num_layers', type=int, default=1, help='Number of hidden layers')
    parser.add_argument('--use_memory', action='store_true', help='Use neurons with memory')
    parser.add_argument('--image_paths', nargs='+', help='Paths to the input images')
    parser.add_argument('--image_size', type=int, default=64, help='Dimensione delle immagini di input')
    parser.add_argument('--kernel_size', type=int, default=3, help='Size of the kernel')
    parser.add_argument('--pool_size', type=int, default=2, help='Size of the pooling')
    parser.add_argument('--epochs', type=int, default=100, help='Number of training epochs')
    parser.add_argument('--learning_rate', type=float, default=0.1, help='Learning rate for training')
    parser.add_argument('--save_model', action='store_true', help='Save the trained model')
    parser.add_argument('--model_file', type=str, default='model.pkl', help='File path to save the trained model')
    return parser.parse_args()


def train(neural_network, dataset, epochs, learning_rate):
    for epoch in range(epochs):
        total_error = 0.0
        for inputs in dataset:
            neural_network.calculate(inputs)
            output = neural_network.get_output()[0]
            target = 1.0  # Aggiungi qui il valore target corretto per ogni immagine
            error = target - output
            neural_network.backpropagate(error, learning_rate)
            total_error += abs(error)
        avg_error = total_error / len(dataset)
        print(f'Epoch {epoch + 1}/{epochs}, Average Error: {avg_error}')


def save_model(neural_network, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(neural_network, file)
    print(f'Model saved to {file_path}')


def main():
    args = parse_args()

    # Load the images
    images = load_images(args.image_paths, args.image_size)

    # Apply kernel filter and pooling to images
    filtered_images = []
    for img in images:
        filtered_img = kernel_filter_k(img, args.kernel_size)
        pooled_img = max_pooling(filtered_img, args.pool_size)
        converted_inputs = convert_img(pooled_img)
        filtered_images.append(converted_inputs)

    # Create the neural network
    neural_network = NeuralNetwork(args.num_inputs, args.num_outputs, args.num_hidden, args.num_layers, args.use_memory)

    # Train the neural network
    train(neural_network, filtered_images, args.epochs, args.learning_rate)

    # Save the trained model
    if args.save_model:
        save_model(neural_network, args.model_file)


if __name__ == '__main__':
    main()