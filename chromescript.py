from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys 
import time
from selenium.webdriver.common.action_chains import ActionChains




#Helper takes the open browser
def find_jobs_helper(browser):
	#Iterate through all job postings on the current page
	for job in browser.find_elements_by_class_name('turnstileLink'):
		if job.get_attribute('data-tn-element') == 'jobTitle':
			#Open in new tab
			job.send_keys(Keys.CONTROL + Keys.RETURN)



def find_jobs(num_pages):
	page_number = 1
	# Initialize browser
	browser = webdriver.Chrome()
	browser.get("https://www.indeed.com")
	# Login to indeed, replace email and password fields with appropriate login info
	login = browser.find_element_by_id("userOptionsLabel")
	login.click()
	time.sleep(1.0)
	actions = ActionChains(browser)
	actions.send_keys('email' + Keys.TAB + 'password' + Keys.RETURN)
	actions.perform()
	#Search for jobs non area restricted, this string can easily be changed to look for different jobs
	actions2 = ActionChains(browser)
	actions2.send_keys('Fall Internship Computer Science' + Keys.TAB + Keys.BACK_SPACE + Keys.TAB + Keys.RETURN)
	actions2.perform()
	#Close out of indeed prime advertisement
	browser.find_element_by_id('prime-popover-close-button').click()
	#If user specified multiple pages, navigate to the next page and repeat after normal operations
	if num_pages > 1:
		find_jobs_helper(browser)
		while page_number < num_pages:
			page_number+=1
			pn_list = browser.find_elements_by_class_name("pn")
			for pn in pn_list:
				if pn.text == str(page_number):
					pn.click()
					find_jobs_helper(browser)
					break
	else:
		find_jobs_helper(browser)
	time.sleep(50000)


find_jobs(2)