Feature: User sees welcome page

  Scenario: Access main site
     Given we are browsing surprisetech.pythonanywhere.com/
      Then we should see a "Welcome!"

  Scenario: Search tifu Subreddit and hot category
     Given we are browsing surprisetech.pythonanywhere.com/
     When we type tifu in search box and select hot category
     Then we should be at page surprisetech.pythonanywhere.com/count/tifu/hot