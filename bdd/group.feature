Feature: Group feature
  description

  Scenario Outline: Add new group
    Given a group list
    Given a group with <name>, <header>, <footer>
    When I add this new group to the list
    Then a new group list is equal to the old list with the new group

    Examples:
    | name | header | footer |
    | as dfg | fdg  | djfhs  |
    | 32324 | 4543653 |      |
    | ывыв | ывпыпроор | рвпывыоа |



