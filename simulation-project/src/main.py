import hashlib  # ハッシュ関数を提供するモジュールをインポート
from blockchain import Blockchain  # Blockchainクラスをインポート
from encoder import encode_data  # データを符号化する関数をインポート
from decoder import decode_data  # データを復号する関数をインポート
from verifier import verify_piece  # データの一部を検証する関数をインポート

class Blockchain:
    def __init__(self):
        self.chain = []  # ブロックチェーンを格納するリストを初期化

    def add_block(self, block):
        self.chain.append(block)  # 新しいブロックをチェーンに追加

def record_hashes(data_pieces, blockchain):
    hashes = []  # ハッシュ値を格納するリストを初期化
    for piece in data_pieces:
        hash_object = hashlib.sha256(piece)  # データの一部をSHA-256でハッシュ化
        hex_dig = hash_object.hexdigest()  # ハッシュ値を16進数文字列に変換
        blockchain.add_block(hex_dig)  # ハッシュ値をブロックチェーンに追加
        hashes.append(hex_dig)  # ハッシュ値をリストに追加
    return hashes  # ハッシュ値のリストを返す

def main():
    # サンプルデータ
    data = "これはシミュレーションプロジェクトのためのテストデータです。".encode('utf-8')  # テストデータをUTF-8でエンコード
    num_pieces = 4  # データを分割する部分の数

    # データを符号化
    data_pieces = encode_data(data, num_pieces)  # データを指定された部分数に符号化

    # ブロックチェーンの初期化
    blockchain = Blockchain()  # 新しいブロックチェーンを作成

    # ハッシュを記録
    hashes = record_hashes(data_pieces, blockchain)  # データの各部分のハッシュ値を計算し、ブロックチェーンに記録

    # ハッシュを検証
    for piece, expected_hash in zip(data_pieces, hashes):
        if verify_piece(piece, expected_hash):
            print(f"ハッシュが一致しました: {expected_hash}")
        else:
            print(f"ハッシュが一致しません: {expected_hash}")

    # データを復号化
    decoded_data = decode_data(data_pieces)
    print(f"復号化されたデータ: {decoded_data.decode('utf-8')}")

if __name__ == "__main__":
    main()