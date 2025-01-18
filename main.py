import argparse
import cv2
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

def convert_to_video(files, output):
    # 画像を読み込む
    images = []
    for file in files:
        img = cv2.imread(file)
        images.append(img)

    # 動画に変換
    height, width, layers = images[0].shape
    size = (width, height)
    video = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*'mp4v'), 1, size)
    for img in images:
        video.write(img)
    video.release()

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
    
    # ディレクトリを作る
    outdir = os.path.join(os.path.dirname(__file__), settings["output-dir"])    
    if not os.path.exists(outdir):
        logging.debug("{} created".format(outdir))
        os.makedirs(outdir)

    # 連結して動画にする
    outfile = os.path.join(outdir, settings["output-file"])
    convert_to_video(files, outfile)
    logging.debug("AAA.mp4 created")


if __name__ == '__main__':
    main()

