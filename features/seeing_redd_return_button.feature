Feature: Logo button returns to main page
  Scenario Outline: Logo button returns to welcome page
    Given we are browsing surprisetech.pythonanywhere.com/r/tifu/<category>
      When we select logo picture
      Then we should be browsing surprisetech.pythonanywere.com
     Examples: Categories
       | category           |
       | hot                |
       | topalltime         |
       | top24hrs           |
       | controversialall   |
       | controversial24hrs |