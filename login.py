#!/bin/env python
from webbot import Browser
import time
def login(ip, password):
    web = Browser()
    web.go_to('https://'+ ip +':4444/')
    web.type('admin' , into='Username' , id='ELEMENT_login_username')
    web.type(password , into='Password' , id='ELEMENT_login_password')
    web.click('Login' , tag='div' , id='ELEMENT_login_button')
    time.sleep(15);
    web.close_current_tab();

login('insertiphere', 'insertpasswordhere'); #Name Of Customer
#if you want to check other firewalls just do this
#time.sleep(5);
#login('insertiphere', 'insertpasswordhere');
