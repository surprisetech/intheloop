Feature: User sees welcome page

  Scenario: Access main site
     Given we are browsing http://127.0.0.1:5000
      Then we should see a "Welcome!"
