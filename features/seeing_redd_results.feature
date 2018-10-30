Feature: See results

  Scenario Outline: Search for results
     Given we are browsing surprisetech.pythonanywhere.com/
       When we search tifu subreddit and <category>
       Then we should see bar graphs

    Examples: Categories
      | category          |
      | hot               |
      | topalltime        |
      | top24hrs          |
      | controversalall   |
      | controversal24hrs |