import argparse
import json
import logging
import os

def get_arguments():
    parser = argparse.ArgumentParser()

    # 引数の追加
    parser.add_argument('--input', help='入力ファイル名')    


    return parser.parse_args()

def main():
    # loggingを設定
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

    # コマンドライン引数を受け取り、動的なオプションを処理する
    args = get_arguments()

    # 処理するファイル名のリスト
    files = []

    # 静的な設定を読み込む
    # settings
    settings = json.load(open("settings.json", "r"))

    # 画像を読み込む

    # 連結して動画にする

    # ファイル出力する
    # なければディレクトリを作る
    dir = os.path.dirname(__file__)
    indir = os.path.join(dir, settings["input-dir"])
    outdir = os.path.join(dir, settings["output-dir"])

    if not os.path.exists(indir):
        logging.debug("{} created".format(indir))
        os.makedirs(outdir)

    if not os.path.exists(outdir):
        logging.debug("{} created".format(outdir))
        os.makedirs(outdir)


if __name__ == '__main__':
    main()

