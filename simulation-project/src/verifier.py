import hashlib

def verify_piece(piece, expected_hash):
    hash_value = hashlib.sha256(piece).hexdigest()
    return hash_value == expected_hash

def verify_pieces(data_pieces, expected_hashes):
    if len(data_pieces) != len(expected_hashes):
        return False
    for piece, expected_hash in zip(data_pieces, expected_hashes):
        if not verify_piece(piece, expected_hash):
            return False
    return True