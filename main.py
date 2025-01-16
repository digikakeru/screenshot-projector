import argparse

def get_arguments():
    parser = argparse.ArgumentParser()

    # 引数の追加
    parser.add_argument('input', help='入力ファイル名')    


    return parser.parse_args()

def main():
    args = get_arguments()

    print(args.input)


if __name__ == '__main__':
    main()

