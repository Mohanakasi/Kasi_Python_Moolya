*** Settings ***
Resource    Juno_Resources.robot


*** Test Cases ***
#Test Case 1
User Opens the Juno Application and Logs In
    [Tags]  Sign_In
    Given User Launches the Application
    When User Enters the Email Email ID
    Then User Logs IN

#Test Case 2
User Adds Cash to the Juno App
    [Tags]  Add_Cash
    Given User adds cash to the Juno Wallet
    