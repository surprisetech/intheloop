from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@given(u'we are browsing http://127.0.0.1:5000')
def step_impl(context):
    browser = webdriver.Chrome()
    context.browser = browser 
    browser.get("http://127.0.0.1:5000")
    time.sleep(4)
    #assert "Welcome" in browser.title

@when(u'we search tifu subreddit and {category}')
def step_impl(context,category):
    browser = context.browser
    browser.get("http://127.0.0.1:5000/count/tifu/" + category)
    
@then(u'we should see bar graphs')
def step_impl(context):
    browser = context.browser
    assert "mpld3" in browser.page_source

@then(u'we should see a "Welcome!"')
def step_impl(context):
    browser = context.browser
    assert 'Wecome!' in browser.title 
