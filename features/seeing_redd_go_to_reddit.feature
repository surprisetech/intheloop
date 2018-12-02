Feature: Go to reddit picture
  Scenario: Logo button returns to welcome page for mainpage
    Given we are browsing surprisetech.pythonanywhere.com/
      When we select reddit picture
      Then we should be browsing reddit.com

  Scenario Outline: Reddit picture goes to reddit.com/r/tifu/<category>
    Given we are browsing surprisetech.pythonanywhere.com/r/tifu/<category>
      When we select reddit picture
      Then we should be browsing https://www.reddit.com/r/tifu/<category>
     Examples: Categories
       | category           |
       | new		    |
       | hot                |
       | topalltime         |
       | top24hrs           |
       | controversialall   |
       | controversial24hrs |

  Scenario Outline: Reddit picture goes to reddit.com/u/nasa/<category>
    Given we are browsing surprisetech.pythonanywhere.com/u/nasa/<category>
      When we select reddit picture
      Then we should be browsing https://www.reddit.com/u/nasa/<category>
     Examples: Categories
       | category           |
       | new		    |
       | hot                |
       | topalltime         |
       | top24hrs           |