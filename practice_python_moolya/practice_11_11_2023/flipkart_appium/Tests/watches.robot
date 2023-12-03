*** Settings ***
Library    AppiumLibrary

*** Variables ***

*** Test Cases ***
Launching the flipkart application
    open application    http://localhost:4723/wd/hub    devicename=Motorola moto g(60)       platformName=Android      appPackage=com.flipkart.android    appActivity=com.flipkart.android.SplashActivity
    click element       xpath=//android.widget.TextView[@text='English']/../..//android.widget.RelativeLayout
    click element       id=com.truecaller:id/confirm
    sleep    4s