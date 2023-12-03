*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/orrange_hrm_app.robot
Resource    ../Resources/common_app.robot
Suite Setup    common_app.setting upt the tests
Suite Teardown      common_app.quitting the tests

*** Variables ***

${URL}      https://opensource-demo.orangehrmlive.com/
${BROWSER}      chrome


*** Test Cases ***
login_validation
    orrange_hrm_app.opening & login to the web site




