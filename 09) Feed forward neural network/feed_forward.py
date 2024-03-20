import numpy as np
class FeedForwardNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.bias_hidden = np.random.randn(1, self.hidden_size)
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)
        self.bias_output = np.random.randn(1, self.output_size)
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x)) 
    def forward(self, inputs):
        hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        hidden_output = self.sigmoid(hidden_input)
        output_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
        output = self.sigmoid(output_input)
        return output

input_size = 2
hidden_size = 3
output_size = 1
model = FeedForwardNN(input_size, hidden_size, output_size)
input_data = np.array([[0, 1], [1, 0], [1, 1], [0, 0]])
output = model.forward(input_data)
print("Output:")
print(output)
