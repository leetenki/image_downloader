import os
import argparse
import urllib.request
import bs4

# google画像検索関数
def google_search_image(keyword, start_from):
    image_urls = []
    url = 'https://www.google.co.jp/search?q=%s&source=lnms&tbm=isch&tbs=isz:l&start=%d' % (urllib.request.quote(args.keyword), start_from)
    req = urllib.request.Request(
        url,
        data = None,
        headers = {
            'User-Agent': 'Mozilla/5.0 (MSIE 10.0; Windows NT 6.1; Trident/5.0)'
        }
    )
    soup = bs4.BeautifulSoup(urllib.request.urlopen(req).read(), "html.parser")

    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            image_urls.append(src)

    return image_urls

# 画像URLダウンロード関数
def download_image(url, file_path):
    print('downloading image %s into %s' % (url, file_path))
    urllib.request.urlretrieve(url, file_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='download images from google')
    parser.add_argument('keyword', help='keyword to search for')
    parser.add_argument('--num', '-n', default='20', help='num of images to download')
    parser.add_argument('--dirname', '-d', default='images', help='directory name to save images')
    args = parser.parse_args()

    # ディレクトリ作成
    if not os.path.exists(args.dirname):
        print('create directory %s/' % (args.dirname))
        os.mkdir(args.dirname)

    # google画像検索
    print('searching keyword [%s] ...' % (args.keyword))
    image_urls = []
    n_images = int(args.num)
    while len(image_urls) < n_images:
        search_result = google_search_image(args.keyword, len(image_urls))
        search_result.reverse()
        while len(image_urls) < n_images and len(search_result) > 0:
            image_urls.append(search_result.pop())

    # 画像ダウンロード
    for image_url in image_urls:
        file_path = './%s/%s.jpg' % (args.dirname, image_url.split(':')[-1])
        download_image(image_url, file_path)
