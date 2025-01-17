import argparse
import json
import logging
import os


def get_arguments():
    parser = argparse.ArgumentParser()

    # 引数の追加
    parser.add_argument('--input', help='入力ファイル')

    return parser.parse_args()

def setup_logging():
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def find_files(dir, ext = "png"):
    matched_files = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(f".{ext}"):
                matched_files.append(os.path.join(root, file))
    return matched_files

def main():
    # loggingを設定
    setup_logging()

    # コマンドライン引数を受け取り、動的なオプションを処理する
    args = get_arguments()

    # 静的な設定を読み込む
    # settings
    settings = json.load(open("settings.json", "r"))

    # 何も指定されていない場合、デフォルトディレクトリの中のpng画像を読み込む
    files = find_files(settings["input-dir"])
    
    logging.debug("The following files are used for the video")
    for f in files:
        logging.debug("  {}".format(f))
    
    # 連結して動画にする
    logging.debug("Conversion to be implemented")

    # ディレクトリを作る
    outdir = os.path.join(os.path.dirname(__file__), settings["output-dir"])    
    if not os.path.exists(outdir):
        logging.debug("{} created".format(outdir))
        os.makedirs(outdir)

    # ファイル出力する
    logging.debug("AAA.mp4 created")

if __name__ == '__main__':
    main()

