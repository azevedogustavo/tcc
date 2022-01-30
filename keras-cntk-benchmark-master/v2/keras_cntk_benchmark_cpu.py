import os

if not os.path.exists('logs'):
    os.makedirs('logs')

test_files = [f for f in os.listdir("test_files") if f.endswith('.py')]
test_files.remove('CustomCallback.py')
backends = ['tensorflow']
docker_cmd = "sudo docker run -it --rm -v $(pwd)/:/keras --name keras"

for test_file in test_files:
    for backend in backends:
        statement = docker_cmd + \
            " -e KERAS_BACKEND='{}' minimaxir/keras-cntk:cpu python3 test_files/{}".format(
                backend, test_file)

        print(statement)
        print("{} + {}".format(test_file, backend))

        os.system(statement)
