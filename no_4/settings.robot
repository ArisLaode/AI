*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${Browser}  Chrome
${MainPage}  https://google.com/

*** Keywords ***
Start Browser and Maximize
    [Arguments]  ${URL}  ${chosenBrowser}
    open browser  ${URL}  ${chosenBrowser}
    maximize browser window