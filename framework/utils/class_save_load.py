import pickle

def load_object_from_pickle(path_to_file):
    with open(path_to_file, 'rb') as file:
        serialized_data = file.read()
    return pickle.loads(serialized_data)


def save_object_to_pickle(object, path_to_file):
    serialized_person = pickle.dumps(object)
    with open(path_to_file, 'wb') as file:
        file.write(serialized_person)
