from common.desired_caps import appium_desired
from baseView.baseView import BaseView
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging,os,time,csv,io

class Common(BaseView):
    cancelBtn_type=(By.ID,'android:id/button2')
    skipBtn_type=(By.ID,'com.tal.kaoyan:id/tv_skip')
    wemedia_cancel=(By.ID,'com.tal.kaoyan:id/view_wemedia_cancel')

    def check_cancelBtn(self):
        logging.info('====check_cancelBtn====')
        try:
            element=self.driver.find_element(*self.cancelBtn_type)
        except NoSuchElementException:
            logging.info('====no cancelBtn====')
        else:
            logging.info('====click cancelBtn====')
            element.click()

    def check_skipBtn(self):
        logging.info('====check_skipBtn====')
        try:
            element=self.driver.find_element(*self.skipBtn_type)
        except NoSuchElementException:
            logging.info('====no skipBtn====')
        else:
            logging.info('====click skipBtn====')
            element.click()

    def get_size(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return x,y

    def swipeLeft(self):
        logging.info('====swipeLeft====')
        a=self.get_size()
        x1=int(a[0]*0.9)
        y1=int(a[1]*0.5)
        x2=int(a[0]*0.1)
        self.swipe(x1,y1,x2,y1,1000)

    def getTime(self):
        self.now=time.strftime('%Y-%m-%d %H-%M-%S')
        return self.now

    def getScreenShot(self,module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)
        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)

    def check_market_ad(self):
        logging.info('====check_market====')
        try:
            element=self.driver.find_element(*self.wemedia_cancel)
        except NoSuchElementException:
            pass
        else:
            logging.info('close market ad')
            element.click()

    def get_csv_data(self, csv_file, line):
        logging.info('========get_csv_data========')
        with io.open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

if __name__ == '__main__':
    driver=appium_desired()
    com=Common(driver)
    com.check_cancelBtn()
    # com.check_skipBtn()
    com.getScreenShot('start app')