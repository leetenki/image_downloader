var system = require("system")

var page = require("webpage").create();
page.viewportSize = { width: 512, height: 384 };

page.settings = {
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
};
 
url = "https://www.google.co.jp/search?source=lnms&tbm=isch&q=" + encodeURIComponent(system.args[1])
page.open(url, function(status) {
    page.content.match(/"ou":".*?"/g).map(function(str) {
        console.log(str.split("\"")[3]);
    })
    phantom.exit();
}); 

