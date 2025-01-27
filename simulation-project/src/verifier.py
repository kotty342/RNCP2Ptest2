import hashlib  # ハッシュ関数を提供するモジュールをインポート

def verify_piece(piece, expected_hash):
    hash_value = hashlib.sha256(piece).hexdigest()  # データのSHA-256ハッシュ値を計算
    return hash_value == expected_hash  # 計算したハッシュ値が期待されるハッシュ値と一致するかを返す

def verify_pieces(data_pieces, expected_hashes):
    if len(data_pieces) != len(expected_hashes):  # データのピースと期待されるハッシュの数が一致するかを確認
        return False  # 一致しない場合はFalseを返す
    for piece, expected_hash in zip(data_pieces, expected_hashes):  # 各データのピースと期待されるハッシュをペアにしてループ
        if not verify_piece(piece, expected_hash):  # 各ピースが期待されるハッシュと一致するかを確認
            return False  # 一致しない場合はFalseを返す
    return True  # 全てのピースが期待されるハッシュと一致する場合はTrueを返す