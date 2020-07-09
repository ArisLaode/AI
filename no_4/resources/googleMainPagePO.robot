*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${searchTbx}  class:gsfi
${luckyBtn}  name:btnI

${searchBtn}  value:Google Search

*** Keywords ***
enterSearchWord
  [Arguments]  ${text}
  input text  ${searchTbx}  ${text}

getSearchTbxVal
  ${mystring}  get element attribute  ${luckyBtn}  value
  [Return]  ${mystring}
