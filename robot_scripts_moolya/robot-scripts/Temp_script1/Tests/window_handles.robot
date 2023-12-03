*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
#wind hadling
#    open browser    https://rahulshettyacademy.com/AutomationPractice/    chrome
#    maximize browser window
#    sleep    5s
#    click link    xpath=//a[text()='Open Tab']
#    ${win_handles}      get window handles
#    switch window    ${win_handles}[-1]
#    sleep    5s
#    switch window    ${win_handles}[0]
#    ${sel_speed}    get selenium speed
#    ${sel_time_out}     get selenium timeout
#    log to console    ${sel_speed}
#    log to console    ${sel_time_out}

alerts_handling
    open browser    https://rahulshettyacademy.com/AutomationPractice/    chrome
    maximize browser window
    sleep    5s
    click button      id=alertbtn
    sleep    7s
#    alert should be present    Hello , share this practice page and share your knowledge
#    alert should be present    No this text
#    handle alert    accept
    handle alert    dismiss
#    handle alert    leave
