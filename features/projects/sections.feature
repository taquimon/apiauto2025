# Created by predator at 2/7/25
Feature: Suite for sections endpoint from TODOIST API
  # Enter feature description here

  @acceptance @project_id @section_id
  Scenario: Scenario to get a Section
    When user calls "GET" method to "get" "sections" endpoint
    Then the status code is 200


  @acceptance @project_id
  Scenario: Scenario to create a Section
  When user calls "POST" method to "create" "sections" endpoint using json
  """
    {
      "project_id": "project_id",
      "name": "Section from feature file"
    }
  """
  Then the status code is 200

  @acceptance @project_id
  Scenario: Scenario to delete a Section
    When user calls "DELETE" method to "delete" "sections" endpoint
    Then the status code is 204


  @acceptance @project_id @section_id @wip
  Scenario: Scenario to update a Section
  When user calls "POST" method to "update" "sections" endpoint using json
  """
    {
        "name": "Updated Section",
        "description": "Section description updated",
        "color": "yellow"
    }
  """
  Then the status code is 200
