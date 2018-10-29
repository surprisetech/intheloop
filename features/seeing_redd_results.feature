Feature: See results

  Scenario Outline: Search for results
     Given we are browsing http://127.0.0.1:5000
       When we search a subreddit and <category>
       Then we should see bar graphs

    Examples: Categories
      | category          |
      | hot               |
      | topalltime        |
      | top24hrs          |
      | controversalall   |
      | controversal24hrs |