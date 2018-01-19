from better_neural_network import Neural_Network

myNN = Neural_Network([3, 4, 2])

for i in range(1000):
	myNN.train([0,0,0], [0,0])
	myNN.train([0,0,1], [0,0])
	myNN.train([0,1,0], [1,0])
	myNN.train([0,1,1], [1,0])
	myNN.train([1,0,0], [1,0])
	myNN.train([1,0,1], [1,0])
	myNN.train([1,1,0], [1,0])
	myNN.train([1,1,1], [1,0])


print myNN.get_output([0,0,1])

