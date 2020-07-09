*** Settings ***
Library           SeleniumLibrary

Resource  ../settings.robot
Resource  ../resources/googleMainPagePO.robot

*** Test Cases ***
TC_001 Browser Start and Close
    start browser and maximize  ${MainPage}  ${Browser}
    enterSearchWord  who let the dogs out
    ${word}  getSearchTbxVal
    should be equal as strings  I'm Feeling Lucky  ${word}
    sleep  5
    close browser

