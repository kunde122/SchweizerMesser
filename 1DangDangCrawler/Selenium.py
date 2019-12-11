#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver

# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
def test():
    #创建浏览器对象
    driver = webdriver.Firefox()

    driver.get("http://www.baidu.com")

    #打印页面标题“百度一下你就知道”
    print(driver.title)

    #生成当前页面快照
    driver.save_screenshot("baidu.png")

    # id="kw"是百度搜索框，输入字符串“微博”，跳转到搜索中国页面
    driver.find_element_by_id("kw").send_keys(u"微博")

    # id="su"是百度搜索按钮，click() 是模拟点击
    driver.find_element_by_id("su").click()

    # 获取新的页面快照
    driver.save_screenshot(u"微博.png")

    # 打印网页渲染后的源代码
    print(driver.page_source)

    # 获取当前页面Cookie
    print(driver.get_cookies())

    # ctrl+a 全选输入框内容
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')

    # ctrl+x 剪切输入框内容
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')

    # 输入框重新输入内容
    driver.find_element_by_id("kw").send_keys("test")

    # 模拟Enter回车键
    driver.find_element_by_id("su").send_keys(Keys.RETURN)

    # 清除输入框内容
    driver.find_element_by_id("kw").clear()

    # 生成新的页面快照
    driver.save_screenshot("test.png")

    # 获取当前url
    print(driver.current_url)

    # 关闭当前页面，如果只有一个页面，会关闭浏览器
    # driver.close()

    # 关闭浏览器
    driver.quit()
def test2():
    # !/usr/bin/env python
    # -*- coding:utf-8 -*-

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time

    driver = webdriver.Firefox()
    driver.get("http://www.douban.com")

    # 输入账号密码
    # driver.find_element_by_name("form_email").send_keys("158xxxxxxxx")
    # driver.find_element_by_name("form_password").send_keys("zhxxxxxxxx")
    # driver.switch_to.frame()
    # tmp=driver.find_elements_by_tag_name(driver.find_elements_by_tag_name('iframe'))
    # tmp[0].click()
    fsh=driver.find_elements_by_tag_name("iframe")
    for id,frame in enumerate(fsh):
        driver.switch_to.frame(frame)
        driver.save_screenshot(u"douban{}.png".format(id))
        driver.switch_to.default_content()
    driver.switch_to.frame(fsh)
    driver.find_element_by_css_selector('li.account-tab-account').click()
    driver.find_element_by_id("username").send_keys('18519792042')
    driver.find_element_by_id("password").send_keys('db332484583')

    # 模拟点击登录
    driver.find_element_by_css_selector("a.btn:nth-child(1)").click()

    # 等待3秒
    time.sleep(3)

    # 生成登陆后快照
    driver.save_screenshot(u"douban.png")

    driver.quit()

def pro_page():
    pass


def daomu0():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    from selenium.webdriver import ActionChains
    import os

    driver = webdriver.Firefox()
    driver.get("http://www.dmbj.cc/")
    main_handle=driver.current_window_handle
    books=driver.find_elements_by_xpath(".//li[@class='pop-book']")

    for id,book in enumerate(books):
        name=book.find_element_by_class_name('pop-tit')
        name=name.text
        book_dir='/Users/user/code/mycode/SchweizerMesser/1 DangDangCrawler/book/{}'.format(name)
        if not os.path.exists(book_dir):
            os.mkdir(book_dir)

        page=book.click()
        all_handles=driver.window_handles
        driver.switch_to.window(all_handles[1])
        driver.maximize_window()
        js = "document.documentElement.scrollTop=%d" % 2000

        # driver.save_screenshot(u"daomu{}.png".format(id))

        chapters = driver.find_elements_by_xpath(".//li")
        chapter_name=''
        for chapter in chapters:

            # driver.execute_script("arguments[0].scrollIntoView();", chapter)
            #鼠标移动到该章节并单击
            # ActionChains(driver).move_to_element(chapter).click(chapter).perform()

            tmp=chapter.find_elements_by_tag_name('a')
            chapter_name=tmp[0].text
            file_name = book_dir +'/'+chapter_name+'.txt'
            fout=open(file_name,'w')
            tmp[0].click()
            #切换到新打开的网页
            driver.switch_to.window(driver.window_handles[1])
            paras=driver.find_element_by_xpath(".//div[@class='m-post']").find_elements_by_xpath(".//p")
            for para in paras:
                text=para.text
                fout.write(text+'\n')
                fout.write('\n')
                pass
            fout.close()
            #本章保存完毕
            print(chapter_name)
            # driver.close()
            # driver.switch_to.window(main_handle)
            driver.back()


            # save_action = driver.find_elements_by_xpath(".//div[@class='m-post']")
            # ActionChains(driver).move_to_element(save_action).context_click(save_action).perform()
        driver.close()
        driver.switch_to.window(main_handle)

def daomu():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    from selenium.webdriver import ActionChains
    import os

    driver = webdriver.Firefox()
    driver.get("http://www.dmbj.cc/")
    main_handle=driver.current_window_handle
    books=driver.find_elements_by_xpath(".//li[@class='pop-book']")

    for id,book in enumerate(books):
        name=book.find_element_by_class_name('pop-tit')
        name=name.text
        book_dir='/Users/user/code/mycode/SchweizerMesser/1 DangDangCrawler/book/{}'.format(name)
        if not os.path.exists(book_dir):
            os.mkdir(book_dir)

        page=book.click()
        time.sleep(2)
        all_handles=driver.window_handles

        # driver.maximize_window()
        js = "document.documentElement.scrollTop=%d" % 2000

        # driver.save_screenshot(u"daomu{}.png".format(id))

        # chapters = driver.find_elements_by_xpath(".//li")
        chapter_name=''
        index=0
        while True:
            driver.switch_to.window(all_handles[1])
            #写到这里是因为driver绑定了网页，网页变化后driver失效了？？？
            chapters = driver.find_elements_by_xpath(".//li")
            driver.save_screenshot(u"douban1.png")
            if index >= len(chapters):
                break
            chapter=chapters[index]
            # driver.execute_script("arguments[0].scrollIntoView();", chapter)
            # 鼠标移动到该章节并单击
            # ActionChains(driver).move_to_element(chapter).click(chapter).perform()

            tmp = chapter.find_elements_by_tag_name('a')
            chapter_name = tmp[0].text
            file_name = book_dir + '/' + chapter_name + '.txt'
            if os.path.exists(file_name):
                index+=1
                print('repeat')
                continue

            fout = open(file_name, 'w')
            tmp[0].click()
            time.sleep(2)
            # 切换到新打开的网页
            driver.switch_to.window(driver.window_handles[1])
            paras = driver.find_element_by_xpath(".//div[@class='m-post']").find_elements_by_xpath(".//p")
            for para in paras:
                text = para.text
                fout.write(text + '\n')
                fout.write('\n')
                pass
            fout.close()
            # 本章保存完毕
            print(chapter_name)
            # driver.close()
            # driver.switch_to.window(main_handle)
            driver.back()
            index += 1

            # save_action = driver.find_elements_by_xpath(".//div[@class='m-post']")
            # ActionChains(driver).move_to_element(save_action).context_click(save_action).perform()
        driver.close()
        driver.switch_to.window(main_handle)

daomu()