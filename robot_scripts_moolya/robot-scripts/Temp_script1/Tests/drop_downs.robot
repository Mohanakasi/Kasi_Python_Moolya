*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
drop_downs
    open browser    https://rahulshettyacademy.com/AutomationPractice/    chrome
    maximize browser window
    sleep    5s
    select from list by value       xpath=//select[@name='dropdown-class-example']      option1
    sleep    5s