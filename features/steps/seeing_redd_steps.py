from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
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

#@then(u"we should be at page surprisetech.pythonanywhere.com/count/tifu/{category}")
#def step_impl(context,category):
#    print ("hello world")
