import random

class NeuralNetwork:
    def __init__(self, num_inputs, num_outputs, num_hidden, num_layers, use_memory=False):
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.num_hidden = num_hidden
        self.num_layers = num_layers
        self.use_memory = use_memory

        self.neural_network = self.create_network()

    def create_network(self):
        neural_network = []

        # Create hidden layers
        for _ in range(self.num_layers):
            layer = []
            for _ in range(self.num_hidden):
                if self.use_memory:
                    layer.append(MemoryNeuron(self.num_inputs))
                else:
                    layer.append(Neuron(self.num_inputs))
            neural_network.append(layer)

        # Create output layer
        output_layer = []
        for _ in range(self.num_outputs):
            if self.use_memory:
                output_layer.append(MemoryNeuron(self.num_hidden))
            else:
                output_layer.append(Neuron(self.num_hidden))
        neural_network.append(output_layer)

        return neural_network

    def backpropagate(self, error, learning_rate):
        for layer in reversed(self.neural_network):
            for neuron in layer:
                neuron.backpropagate(error, learning_rate)

    def calculate(self, inputs):
        outputs = inputs

        for layer in self.neural_network:
            new_outputs = []
            for neuron in layer:
                neuron_output = neuron.calculate(outputs)
                neuron.last_inputs = outputs  # Aggiorna last_inputs per il neurone corrente
                new_outputs.append(neuron_output)
            outputs = new_outputs

        self.output = outputs

    def get_output(self):
        return self.output

class Neuron:
    def __init__(self, num_inputs):
        self.weights = [random.uniform(-1, 1) for _ in range(num_inputs)]  # Utilizza random.uniform per pesi in float
        self.bias = random.uniform(-1, 1)  # Utilizza random.uniform per bias in float

    def calculate(self, inputs):
        weighted_sum = sum(weight * input_val for weight, input_val in zip(self.weights, inputs))
        weighted_sum += self.bias
        return weighted_sum

    def backpropagate(self, error, learning_rate):
        for i in range(len(self.weights)):
            self.weights[i] += learning_rate * error * self.last_inputs[i]
        self.bias += learning_rate * error

class MemoryNeuron(Neuron):
    def __init__(self, num_inputs):
        super().__init__(num_inputs)
        self.state = 0

    def calculate(self, inputs):
        weighted_sum = super().calculate(inputs)
        weighted_sum += self.state
        return weighted_sum

    def backpropagate(self, error, learning_rate):
        super().backpropagate(error, learning_rate)
        self.state = error
