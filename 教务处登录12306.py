from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time



def main():

    yonghu = input("请输入学号:")
    mima = input("请输入密码:")
    # 创建 WebDriver 对象
    options = Options()
    # options.add_argument("--inprivate")  # 启用Edge浏览器无痕模式

    service = Service(executable_path=EdgeChromiumDriverManager().install())
    wd = webdriver.Edge(service=service, options=options)
    

    # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
    wd.get('https://jwglxt.wuit.cn/jwglxt/xtgl/login_slogin.html')

    # 根据id选择元素，返回的就是该元素对应的WebElement对
    # 通过该 WebElement对象，就可以对页面元素进行操作了
    # 比如输入字符串到 这个 输入框里
    

    #检测当前页面url，后期上线可删除
    window_handles = wd.window_handles
    print(window_handles)
    
    

    #自动登录
    try:  
        username = wd.find_element(By.XPATH, '//input[@placeholder="用户名"]')
        username.click
        username.send_keys(yonghu)  
        print("用户名 button clicked successfully.")  
    except NoSuchElementException:  
        print("Logout button not found on the page.")  
    except Exception as e:  
        print(f"An error occurred while clicking the logout button: {e}")  
    
    
    try: 
        password = wd.find_element(By.XPATH, '//input[@placeholder="密码"]')
        password.click
        password.send_keys(mima) 
        print("密码 button clicked successfully.")  
    except NoSuchElementException:  
        print("Logout button not found on the page.")  
    except Exception as e:  
        print(f"An error occurred while clicking the logout button: {e}")  
    

    try:  
        email = wd.find_element(By.XPATH, '//button[@class="btn btn-primary btn-block"]')
        time.sleep(0.5)
        for i in range(10):
            email.click
            email.send_keys(Keys.ENTER) 
        print("提交 button clicked successfully.")  
    except NoSuchElementException:  
        print("Logout button not found on the page.")  
    except Exception as e:  
        print(f"An error occurred while clicking the logout button: {e}")  
    

    current_url = wd.current_url
    print(f"当前页面的url为——————————{current_url}——————————")
    time.sleep(0.5)
    
    
    #进入二级界面
    #准备进入获取课程表界面
    
    try:  
        email = wd.find_element(By.XPATH, "//a[contains(text(), '信息查询')]")
        email.click
        email.send_keys(Keys.ENTER) 
        print("提交 button clicked successfully.")  
    except NoSuchElementException:  
        print("Logout button not found on the page.")  
    except Exception as e:  
        print(f"An error occurred while clicking the logout button: {e}")

    try:  
        email = wd.find_element(By.XPATH, "//a[contains(text(), '个人课表查询')]")
        email.click
        email.send_keys(Keys.ENTER) 
        print("提交 button clicked successfully.")  
    except NoSuchElementException:  
        print("Logout button not found on the page.")  
    except Exception as e:  
        print(f"An error occurred while clicking the logout button: {e}")

    

    #检测当前页面url，后期可删除
    window_handles = wd.window_handles
    print(window_handles)
    #切换到当前url
    latest_handle = window_handles[-1]  
    wd.switch_to.window(latest_handle)




    current_url1 = wd.current_url
    print(f"当前页面的url为——————————{current_url1}——————————")
    

    
    try:  
        email = wd.find_element(By.XPATH, '//button[@id="shcPDF"]')
        email.click
        email.send_keys(Keys.ENTER) 
        print("下载 button clicked successfully.")  
    except NoSuchElementException:  
        print("Logout button not found on the page.")  
    except Exception as e:  
        print(f"An error occurred while clicking the logout button: {e}")

    time.sleep(500000000)

    wd.quit



main()






