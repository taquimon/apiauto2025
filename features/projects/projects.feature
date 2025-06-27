@projects
Feature:  Suite for projects endpoint from TODOIST API

  @acceptance @project_id
  Scenario: Scenario to get a Project
    When user calls "GET" method to "get a project" endpoint
    Then the status code is 200

  @acceptance
  Scenario: Scenario to create a Project
  When user calls "POST" method to "create a project" endpoint using json
  """
    {
      "name": "project from feature file"
    }
  """
  Then the status code is 200

  @acceptance @project_id
  Scenario: Scenario to update a Project
  When user calls "POST" method to "update a project" endpoint using json
  """
    {
      "name": "update project from feature file"
    }
  """
  Then the status code is 200

  @acceptance @project_id
  Scenario: Scenario to delete a project
    When user calls "DELETE" method to "delete a project" endpoint
    Then the status code is 204

  @negative @functional
  Scenario: create a project without name
