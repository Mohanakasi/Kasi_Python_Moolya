*** Settings ***
Resource    ../Resources/PO/login_page.robot

*** Variables ***

*** Keywords ***
opening & login to the web site
    login_page.entering the user_name
    login_page.entering the password
    login_page.do submit
    login_page.opening another site