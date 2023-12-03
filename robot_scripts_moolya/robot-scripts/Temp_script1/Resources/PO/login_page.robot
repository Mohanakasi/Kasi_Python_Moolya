*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${user_name_xpath}    xpath=//input[@name='username']
${pass_word_xpath}    xpath=//input[@name='password']
${submit_button}      xpath=//button[@type='submit']

*** Keywords ***
entering the user_name
    element should be visible    ${user_name_xpath}
    input text        ${user_name_xpath}      Admin
    sleep    5s
#    clear element text     ${user_name_xpath}

entering the password
    element should be visible       ${pass_word_xpath}
    element should be enabled       ${pass_word_xpath}
    input text      ${pass_word_xpath}     admin123
    sleep    5s
#    clear element text    ${pass_word_xpath}


do submit
    element should be visible    ${submit_button}
    element should be enabled     ${submit_button}
    click button    ${submit_button}

opening another site
    switch window       title:New window
