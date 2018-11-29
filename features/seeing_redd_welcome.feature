Feature: User sees welcome page
  
  Scenario: Access main site
     Given we are browsing surprisetech.pythonanywhere.com/
       Then we should see "Welcome to Seeing Redd"

  Scenario Outline: Search tifu Subreddit and <category>
     Given we are browsing surprisetech.pythonanywhere.com/
       When we type tifu in search box and select <category>
       Then we should be at page surprisetech.pythonanywhere.com/r/tifu/<url>
     Examples: Categories
       | category          | url                |
       | Hot               | hot                |
       | Top All           | topalltime         |
       | Top Day           | top24hrs           |
       | Controversial All | controversialall   |
       | Controversial Day | controversial24hrs |

  Scenario: Have drop down menu for subreddit or user
    Given we are browsing surprisetech.pythonanywhere.com/
      Then we should see a menu to select subreddit or user
  
  Scenario: Have selection of search catergory
    Given we select menu to select subreddit
      Then we should see a menu to select category

  Scenario Outline: Logo button returns to welcome page
    Given we are browsing surprisetech.pythonanywhere.com/r/tifu/<category>
      When we select logo button
      Then we should be browsing surprisetech.pythonanywere.com
     Examples: Categories
       | category           |
       | hot                |
       | topalltime         |
       | top24hrs           |
       | controversialall   |
       | controversial24hrs |

