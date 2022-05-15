Feature: first repeated element
    As a first_repeated_element function user
    I want to get the first repeated number from a two given vectors of integer
    So the function result is as expected

@tc:test_method_1 @DataDrivenTest
Scenario Outline: first repeated element nominal behaviour
    Given two vectors of integers with <configuration>
    When i run first_repeated_element with the given vectors as input
    Then the <expected result> occurs
Examples:
| configuration                                                             | expected result              |
| Two duplicated elements, first duplicated element is in the first vector  | the first duplicated element |
| Two duplicated elements, first duplicated element is in the second vector | the first duplicated element |
| No duplicated elements                                                    | None                         |
| Empty given vector                                                        | None                         |

@tc:test_method_2 @ErrorHandling
Scenario Outline: first repeated element error handling
    Given two vectors with <configuration>
    When i run first_repeated_element with the given vectors as input
    Then the <expected error> occurs
Examples:
| configuration                           | expected result                     |
| one of the vector has a float element   | please enter two vectors of integer |
| one of the vector has a String element  | please enter two vectors of integer |