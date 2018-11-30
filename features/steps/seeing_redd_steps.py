from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

@given(u'we are browsing surprisetech.pythonanywhere.com/')
def step_impl(context):
    browser = webdriver.Chrome()
    context.browser = browser 
    browser.get("http://surprisetech.pythonanywhere.com")
    time.sleep(4)
    assert 'Welcome to Seeing Redd.' in browser.page_source 

@when(u'we search tifu subreddit and {category}')
def step_impl(context,category):
    browser = context.browser
    browser.get("http://surprisetech.pythonanywhere.com/r/tifu/" + category)
    
@when(u'we search nasa user and {category}')
def step_impl(context,category):
    browser = context.browser
    browser.get("http://surprisetech.pythonanywhere.com/r/tifu/" + category)
    
@then(u'we should see bar graphs')
def step_impl(context):
    browser = context.browser
    assert "mpld3" in browser.page_source

@then(u'we should see \"Welcome to Seeing Redd\"')
def step_impl(context):
    browser = context.browser
    assert 'Welcome to Seeing Redd.' in browser.page_source 

@given(u'we are browsing surprisetech.pythonanywhere.com/r/tifu/{category}')
def step_impl(context,category):
    browser = webdriver.Chrome()
    context.browser = browser
    browser.get("http://surprisetech.pythonanywhere.com/r/tifu/" + category)
    assert "mpld3" in browser.page_source

@when(u"we type tifu in search box and select {category}")
def step_impl(context,category):
    browser = context.browser

    Radio = browser.find_element_by_xpath(".//*[@type='radio' and @value='subreddit']")
    Radio.click()

    dropDown = browser.find_element_by_id('category')
    Select(dropDown).select_by_visible_text(category)

    searchbox = browser.find_element_by_id("q")
    searchbox.send_keys("tifu")
    searchbox.send_keys(Keys.RETURN)

@then(u'we should be at page surprisetech.pythonanywhere.com/r/tifu/{url}')
def step_impl(context,url):
    browser = context.browser
    assert browser.current_url == ("http://surprisetech.pythonanywhere.com/r/tifu/" + url)

@then(u'we should see radio buttons to select subreddit or user')
def step_impl(context):
    browser = context.browser
    browser.find_element_by_xpath(".//*[@type='radio' and @value='subre\
ddit']")
    browser.find_element_by_xpath(".//*[@type='radio' and @value='user']")

@then(u'we should have drop down box to select subreddit')
def step_impl(context):
    browser = context.browser
    browser.find_element_by_id('category')

@then(u'we should see a menu to select category')
def step_impl(context):
    browser = context.browser
    dropDown = browser.find_element_by_id('category')
    for row in context.table:
        Select(dropDown).select_by_visible_text(row['category'])

@when(u"we type user nasa in search box and select {category}")
def step_impl(context,category):
    browser = context.browser

    Radio = browser.find_element_by_xpath(".//*[@type='radio' and @value='user']")
    Radio.click()

    dropDown = browser.find_element_by_id('category')
    Select(dropDown).select_by_visible_text(category)

    searchbox = browser.find_element_by_id("q")
    searchbox.send_keys("nasa")
    searchbox.send_keys(Keys.RETURN)

@then(u'we should be at page surprisetech.pythonanywhere.com/u/nasa/{url}')
def step_impl(context,url):
    browser = context.browser
    assert browser.current_url == ("http://surprisetech.pythonanywhere.com/u/nasa/" + url)

@when(u'we select logo picture')
def step_impl(context):
    browser = context.browser
    #picture = browser.find_element_by_id('/')
    #picture = WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.XPATH,'//a[img/@src="/logo.png"]')))
    picture = browser.find_element_by_css_selector("a[href='/']")
    action = ActionChains(browser)
    #action.move_to_element(picture).perform()
    #action.click()
    action.move_to_element(picture).perform()
    picture.click

@then(u'we should be browsing surprisetech.pythonanywere.com')
def step_impl(context):
    browser = context.browser
    assert 'Welcome to Seeing Redd.' in browser.page_source
