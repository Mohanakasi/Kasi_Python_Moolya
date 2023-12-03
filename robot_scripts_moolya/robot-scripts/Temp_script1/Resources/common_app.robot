*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
setting upt the tests
    Set Selenium Speed    .2s
	Set Selenium Timeout    7s
	open browser    ${URL}     ${BROWSER}
    maximize browser window
    sleep    6s

quitting the tests
    close browser