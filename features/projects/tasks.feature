# Created by predator at 4/7/25
@tasks
Feature: Tasks
  # Enter feature description here


  @acceptance @task_id
  Scenario: Scenario to get a Task
    When user calls "GET" method to "get" "tasks" endpoint
    Then the status code is 200

  @acceptance
  Scenario: Scenario to create a Task
  When user calls "POST" method to "create" "tasks" endpoint using json
  """
    {
      "content": "Task without project and Task ids",
      "description": "Task created for testing purposes",
      "labels": ["API", "Automation", "Test"]
    }
  """
  Then the status code is 200

  @acceptance @task_id
  Scenario: Scenario to delete a Task
    When user calls "DELETE" method to "delete" "tasks" endpoint
    Then the status code is 204


  @functional @project_id
  Scenario Outline: Create multiple tasks using a project
    When user calls "POST" method to "create" "tasks" endpoint using json
    """
    {
      "content": "<content>",
      "project_id": "project_id",
      "description": "Task created in project",
      "labels": ["API", "Automation", "Test"],
      "priority": <priority>

    }
    """
    Then the status code is 200

    Examples:
    | content     | priority |
    | First Task  |    2     |
    | Second Task |    3     |
    | Third Task  |    3     |
    | Fourth Task |    4     |
