# Created by Jimmy at 2/11/2017
Feature: Start time editing
  # Enter feature description here

  Scenario: Default start time should be in time format
    When I add a local video to a power hour
    Then I should see the start time in the correct format

  Scenario: Should show an error if start time is greater than track length
    When I add a local video to a power hour
    And I set the track's start time to something equal to the track length
    Then there should be an error that the start time is invalid
    And the track's start time should be set blank

  Scenario: Blank start times shouldn't crash app
    When I add a local video to a power hour
    And I set track 1's start time to ' '
    Then the track's start time should be set blank
