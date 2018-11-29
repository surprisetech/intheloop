Feature: Search bar

  Scenario: Have radio buttons for subreddit or user
    Given we are browsing surprisetech.pythonanywhere.com/
      Then we should see radio buttons to select subreddit or user

  Scenario: Have drop down box of search catergory
    Given we are browsing surprisetech.pythonanywhere.com/
    Then  we should have drop down box to select subreddit
      Then we should see a menu to select category
       | category          |
       | Hot               |
       | Top All           |
       | Top Day           |
       | Controversial All |
       | Controversial Day |

  Scenario Outline: Search tifu Subreddit and hot <category>
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