# Google画像ダウンローダ
## setup
必要なpythonライブラリをインストールしておく

```
pip install bs4
pip install urllib
```

## サブネイル画像ダウンロード
以下のコマンドで、googleからcatというキーワードで画像検索した結果をローカルにダウンロードする。(サイズの小さいサブネイル画像のみ)

```
python download_thumbnail.py "cat"
```

以下のオプションで、画像検索結果を1000件、ローカルの./cat_dir/というディレクトリにダウンロードする(ディレクトリ指定しない場合、ダウンロード先は./images/になる)。

```
python download_thumbnail.py "cat" -n 1000 -d "cat_dir"
```

## フルサイズ画像ダウンロード
サブネイル画像のダウンロードと同様に、以下のコマンドで、フルサイズの画像をダウンロードできる。ただし、指定枚数は最大100枚までしかダウンロードできない。

```
python download_image.py "cat" -n 50 -d "cat_dir"
```

スクレイピングの際phantomjsを使うので、インストールしていない場合は、brewでインストールしておく。

```
brew install phantomjs
```
