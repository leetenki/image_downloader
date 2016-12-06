# Google画像ダウンローダ
## setup
必要なpythonライブラリをインストールしておく

```
pip install bs4
pip install urllib
```

## 画像ダウンロード
以下のコマンドで、googleからcatというキーワードで画像検索した結果をローカルにダウンロードする。

```
python download_image.py "cat"
```

以下のオプションで、画像検索結果を1000件、ローカルの./cat_dir/というディレクトリにダウンロードする(ディレクトリ指定しない場合、ダウンロード先は./images/になる)。

```
python download_image.py "cat" -n 1000 -d "cat_dir"
```