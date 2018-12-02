Feature: Logo button returns to main page
  Scenario: Logo button returns to welcome page for mainpage
    Given we are browsing surprisetech.pythonanywhere.com/
      When we select logo picture
      Then we should be browsing surprisetech.pythonanywere.com

  Scenario Outline: Logo button returns to welcome page for /r/
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

  Scenario Outline: Logo button returns to welcome page for /u/
    Given we are browsing surprisetech.pythonanywhere.com/u/nasa/<category>
      When we select logo picture
      Then we should be browsing surprisetech.pythonanywere.com
     Examples: Categories
       | category           |
       | hot                |
       | topalltime         |
       | top24hrs           |