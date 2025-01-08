def encode_data(data, num_pieces):
    piece_size = len(data) // num_pieces
    data_pieces = [data[i * piece_size:(i + 1) * piece_size] for i in range(num_pieces)]
    if len(data) % num_pieces != 0:
        data_pieces[-1] += data[num_pieces * piece_size:]
    return data_pieces