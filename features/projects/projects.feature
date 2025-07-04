@projects
Feature:  Suite for projects endpoint from TODOIST API

  @normal
  @allure.label.owner:Edwin_Taquichiri
  @allure.link:https://developer.todoist.com/api/v1/#tag/Projects
  @acceptance @project_id
  Scenario: Scenario to get a Project
    When user calls "GET" method to "get" "projects" endpoint
    Then the status code is 200

  @normal
  @allure.label.owner:Edwin_Taquichiri
  @allure.link:https://developer.todoist.com/api/v1/#tag/Projects
  @acceptance
  Scenario: Scenario to create a Project
  When user calls "POST" method to "create" "projects" endpoint using json
  """
    {
      "name": "project from feature file"
    }
  """
  Then the status code is 200

  @normal
  @allure.label.owner:Edwin_Taquichiri
  @allure.link:https://developer.todoist.com/api/v1/#tag/Projects
  @acceptance @project_id
  Scenario: Scenario to update a Project
  When user calls "POST" method to "update" "projects" endpoint using json
  """
    {
      "name": "update project from feature file"
    }
  """
  Then the status code is 200

  @normal
  @allure.label.owner:Edwin_Taquichiri
  @allure.link:https://developer.todoist.com/api/v1/#tag/Projects
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


  @normal
  @allure.label.owner:Edwin_Taquichiri
  @allure.link:https://developer.todoist.com/api/v1/#tag/Projects
  @functional @negative @wip
  Scenario: Scenario to create a Project without name
  When user calls "POST" method to "create" "projects" endpoint using json
  """
    {
    }
  """
  Then the status code is 400
  And the response is validated with "create_project_without_body" file
