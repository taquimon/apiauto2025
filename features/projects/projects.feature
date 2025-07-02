@projects
Feature:  Suite for projects endpoint from TODOIST API

  @acceptance @project_id
  Scenario: Scenario to get a Project
    When user calls "GET" method to "get" "projects" endpoint
    Then the status code is 200

  @acceptance
  Scenario: Scenario to create a Project
  When user calls "POST" method to "create" "projects" endpoint using json
  """
    {
      "name": "project from feature file"
    }
  """
  Then the status code is 200

  @acceptance @project_id
  Scenario: Scenario to update a Project
  When user calls "POST" method to "update" "projects" endpoint using json
  """
    {
      "name": "update project from feature file"
    }
  """
  Then the status code is 200

  @acceptance @project_id
  Scenario: Scenario to delete a project
    When user calls "DELETE" method to "delete" "projects" endpoint
    Then the status code is 204

  @functional
  Scenario Outline: Create several projects using data
    When user calls "POST" method to "create" "projects" endpoint using json
    """
      {
        "name": "<project_name>"
      }
    """
    Then the status code is 200

    Examples:
      | project_name |
      | 123344444    |
      | !@#!#$$      |
      | <script>alert('test');</script> |
      | project with a name from feature |
