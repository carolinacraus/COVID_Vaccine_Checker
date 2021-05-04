# dependencies
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# create an instance of Chrome 
driver_options = Options()
driver_options.add_argument("--user-data-dir=C:\\Users\\caroc\\Desktop\\\Selenium-Chrome")
#driver = webdriver.Chrome(options=driver_options, executable_path='./chromedriver')

available = False

while available == False: 
    driver = webdriver.Chrome(options=driver_options, executable_path='./chromedriver')

    # navigate to login page 
    driver.get("https://covid19.austintexas.gov/s/login/?language=en_US&startURL=%2Fs%2F%3Flanguage%3Den_US%26t%3D1612922287953")
    time.sleep(5)

    # Login
    # get the username 
    username = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/div/div[3]/div/div[1]/input")
    #username.clear()
    username.send_keys("carocraus@gmail.com.aph")
    time.sleep(5)

    # get password
    password = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/div/div[3]/div/div[2]/input")
    password.clear()
    password.send_keys("florea123", Keys.ARROW_DOWN)

    # get login button 
    login_button = driver.find_element_by_xpath("//*[@id='centerPanel']/div/div[2]/div/div[3]/div/div[3]/button/span")
    login_button.click()
    time.sleep(5)

    # schedule appointment button
    schedule_button = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div[3]/div[3]/div/div/div/a")    
    schedule_button.click() 
    time.sleep(5)

    appt = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div[1]/h2/span").text
    not_available = "There are currently no appointments available"
    available = False
    if (str(appt) == not_available):
        available = False 
    else: 
        available = True 
    #print(available)

    # send email if appointment available
    if available == True:
        sender = "carocraus.test@gmail.com"
        to = "carocraus@gmail.com"
        # create message container
        msg = MIMEMultipart('alternative')
        msg['Subject']='COVID Vaccine Appointment Available'
        msg['From'] = sender
        msg['To'] = to
        # Create the message (HTML).
        html = """\
        There are COVID vaccine appointments available!
        """
        # Record the MIME type - text/html.
        part1 = MIMEText(html, 'html')
        # Attach parts into message container
        msg.attach(part1)
        # Credentials
        username = 'carocraus.test@gmail.com'  
        password = 'amhunllwsnjxwcno'  
        # Sending the email
        ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo()
        server.starttls()
        server.login(username,password)  
        server.sendmail(sender, to, msg.as_string())  
        server.quit()
    else: 
        driver.close()



