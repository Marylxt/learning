from common.desired_caps import appium_desired
from baseView.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging,time,os,csv

class Common(BaseView):
    # 取消升级和跳过引导按钮
    cancel_upgradeBtn = (By.ID, 'android:id/button2')
    skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')

    # 登录后浮窗广告取消按钮
    wemedia_cacel = (By.ID, 'com.tal.kaoyan:id/view_wemedia_cacel')

    def check_cancelBtn(self):
        logging.info('====check_cancelBtn====')
        try:
            element=self.driver.find_element(*self.cancel_upgradeBtn)
        except NoSuchElementException:
            logging.info('no cancel_upgradeBtn')
        else:
            logging.info('====click cancel_upgradeBtn====')
            element.click()

    def check_skipBtn(self):
        logging.info('====check_skipBtn====')
        try:
            element=self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('no skipBtn')
        else:
            logging.info('====click skipBtn====')
            element.click()

    def getSize(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return x,y

    def swipeLeft(self):
        logging.info('====swipeLeft====')
        a=self.getSize()
        x1=int(a[0]*0.9)
        y1=int(a[1]*0.5)
        x2=int(a[0]*0.1)
        self.swipe(x1,y1,x2,y1,1000)

    def getTime(self):
        self.now=time.strftime('%Y-%m-%d %H_%M_%S')
        return self.now

    def getScreenShot(self,module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)

        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)

    def check_market_ad(self):
        '''检测登录或者注册之后的界面浮窗广告'''
        logging.info('====check_market_ad====')
        try:
            element=self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging.info('====click wemedia_cancel====')
            element.click()

if __name__ == '__main__':
    driver=appium_desired()
    com=Common(driver)
    com.check_cancelBtn()
    com.swipeLeft()
    com.getScreenShot('start app')