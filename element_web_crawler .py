
from selenium import webdriver
import time
import urllib
import os
def sogo_img_crawler(local_path,keyword):
    url = 'https://pic.sogou.com/pics?query={}'.format(keyword)
    xpath = '//div[@id="imgid"]/ul/li/a/img'
    driver=webdriver.Chrome(r'C:\Users\chicony\project\NUWA\chromedriver_win32\chromedriver.exe') # chromedriver檔案放的位置
    # 最大化窗口，因為每一次爬取只能看到視窗内的圖片  
    driver.maximize_window()  
    # 紀錄下載過的圖片網址，避免重複下載  
    img_url_dic = {}  
    # 瀏覽器打開爬取頁面
    driver.get(url)  
    # 模擬滾動視窗瀏覽更多圖片
    pos = 0  
    m = 0 # 圖片編號 
    for i in range(3):
        print(i)
        pos += i*500 # 每次下滾500  
        js = "document.documentElement.scrollTop=%d" % pos  
        driver.execute_script(js)  
        time.sleep(1)
        print(driver.find_elements_by_css_selector("div.img-layout img"))
        for element in driver.find_elements_by_css_selector("div.img-layout img"):

            img_url = element.get_attribute('src')
            try:
                # 保存圖片到指定路徑
                if img_url != None and not img_url in img_url_dic:
                    img_url_dic[img_url] = ''  
                    m += 1
                    print(img_url)
                    ext = img_url.split('/')[-1]
                    print(ext)
                    filename = str(m) + keyword + '_' + ext +'.jpg'
                    print(filename)

                    # 保存圖片
                    urllib.request.urlretrieve(img_url, os.path.join(local_path , filename))
            except OSError:
                print('發生OSError!')
                print(pos)
                break;
    driver.close()
def sogo_img_crawler_CN(local_path,keyword):
    keyword=urllib.parse.quote(keyword)
    sogo_img_crawler(local_path,keyword)





