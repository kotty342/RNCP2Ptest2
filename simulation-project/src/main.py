import hashlib
import time
from blockchain import Blockchain
from encoder import encode_data
from decoder import decode_data
from verifier import verify_piece

class Blockchain:
    def __init__(self):
        self.chain = []

    def add_block(self, block):
        self.chain.append(block)

def record_hashes(data_pieces, blockchain):
    hashes = []
    for piece in data_pieces:
        hash_object = hashlib.sha256(piece)
        hex_dig = hash_object.hexdigest()
        blockchain.add_block(hex_dig)
        hashes.append(hex_dig)
    return hashes

def main():
    start_time = time.time()
    
    # サンプルデータ
    data = "これはシミュレーションプロジェクトのためのテストデータです。".encode('utf-8')
    num_pieces = 4

    # データを符号化
    data_pieces = encode_data(data, num_pieces)

    # ブロックチェーンの初期化
    blockchain = Blockchain()

    # ハッシュを記録
    hashes = record_hashes(data_pieces, blockchain)

    # ハッシュを検証
    for piece, expected_hash in zip(data_pieces, hashes):
        if verify_piece(piece, expected_hash):
            print(f"ハッシュが一致しました: {expected_hash}")
        else:
            print(f"ハッシュが一致しません: {expected_hash}")

    # データを復号化
    decoded_data = decode_data(data_pieces)
    print(f"復号化されたデータ: {decoded_data.decode('utf-8')}")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"プログラムの実行時間: {elapsed_time}秒")

if __name__ == "__main__":
    main()