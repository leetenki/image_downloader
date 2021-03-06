import os
import argparse
import urllib.request
import bs4

# コマンドライン実行メソッド
def exec_cmd(cmd):
    from subprocess import Popen, PIPE
    splt = cmd.split(' ')
    p = Popen([splt[0], splt[1], " ".join(splt[2:]).replace('"', '')], stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    lines = str(out).split('\\n')[:-1]
    lines[0] = lines[0].split('\'')[1]
    return lines

# 画像URLダウンロード関数
def download_image(url, file_path):
    print('downloading image %s into %s' % (url, file_path))
    try:
        urllib.request.urlretrieve(url, file_path)
        return True
    except:
        print('※link not found')
        return False

def get_format(url):
    url_lower = url.lower()
    if url_lower.find('png') > -1:
        return 'png'
    elif url_lower.find('gif') > -1:
        return 'gif'
    else:
        return 'jpg' 

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
    search_result = exec_cmd('phantomjs google_search_image.js "%s"' % args.keyword)
    search_result.reverse()
    while len(image_urls) < n_images and len(search_result) > 0:
        image_url = search_result.pop()
        file_path = './%s/%s.%s' % (args.dirname, len(image_urls), get_format(image_url))
        if(download_image(image_url, file_path)):
            image_urls.append(image_url)
