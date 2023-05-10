import argparse
import numpy as np
from neuron import NeuralNetwork

def parse_args():
    parser = argparse.ArgumentParser(description='Neural Network Calculator')
    parser.add_argument('--num_inputs', type=int, default=2, help='Number of input neurons')
    parser.add_argument('--num_outputs', type=int, default=1, help='Number of output neurons')
    parser.add_argument('--num_hidden', type=int, default=2, help='Number of neurons in the hidden layer')
    parser.add_argument('--num_layers', type=int, default=1, help='Number of hidden layers')
    return parser.parse_args()

def main():
    args = parse_args()

    neural_network = NeuralNetwork(args.num_inputs, args.num_outputs, args.num_hidden, args.num_layers)

    # Generate random inputs
    inputs = np.random.rand(args.num_inputs)

    print('Input:', inputs)
    neural_network.calculate(inputs)
    print('Output:', neural_network.get_output())

if __name__ == '__main__':
    main()
