import random

class NeuralNetwork:
    def __init__(self, num_inputs, num_outputs, num_hidden, num_layers):
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.num_hidden = num_hidden
        self.num_layers = num_layers

        self.neural_network = self.create_network()

    def create_network(self):
        neural_network = []

        # Create hidden layers
        for _ in range(self.num_layers):
            layer = []
            for _ in range(self.num_hidden):
                layer.append(Neuron(self.num_inputs))
            neural_network.append(layer)

        # Create output layer
        output_layer = []
        for _ in range(self.num_outputs):
            output_layer.append(Neuron(self.num_hidden))
        neural_network.append(output_layer)

        return neural_network

    def calculate(self, inputs):
        outputs = inputs

        for layer in self.neural_network:
            new_outputs = []
            for neuron in layer:
                neuron_output = neuron.calculate(outputs)
                new_outputs.append(neuron_output)
            outputs = new_outputs

        self.output = outputs

    def get_output(self):
        return self.output

class Neuron:
    def __init__(self, num_inputs):
        self.weights = [random.uniform(-1, 1) for _ in range(num_inputs)]
        self.bias = random.uniform(-1, 1)

    def calculate(self, inputs):
        weighted_sum = sum(weight * input_val for weight, input_val in zip(self.weights, inputs))
        weighted_sum += self.bias
        return weighted_sum
