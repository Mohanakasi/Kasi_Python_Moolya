*** Settings ***
Resource    Juno_Resources.robot

*** Keywords ***

Wait for and Click on Element
    [Arguments]    ${element}    ${element2}
    Wait Until Element Is Visible  ${element}    ${element2}
    Click Element    ${element}

Wait Time
    Sleep    5s