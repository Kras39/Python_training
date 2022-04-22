Scenario Outline: Add new contact
    Given a contact list
    Given a contact with <firstname>, <middlename> and <lastname>
    When I add the contact to the list
    Then the new contact list is equal to the old list with the added contact

    Examples:
    | firstname  | middlename  | lastname  |
    | firstname1 | middlename1 | lastname1 |
    | firstname2 | middlename2 | lastname2 |


Scenario: Delete a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete the contact from the list
    Then the new contact list is equal to the old list without the deleted contact


Scenario Outline: Modify a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I modify the contact from the list with <firstname456> and <middlename456>
    Then the new contact list is equal to the old list with modified contact

    Examples:
    | firstname456 | middlename456 |
    | firstname457 | middlename457 |
    | firstname458 | middlename458 |