Feature: minimum quantity of permutations so that the sequence ends interspersed
    As a minimum_quantity_of_changes user
    I want to get the minimum quantity of permutations so that the sequence ends interspersed
    So the function result is as expected

@tc:test_method_1 @DataDrivenTest
Scenario Outline: minimum quantity of permutations nominal behaviour
    Given a sequence of  of coin flips with <configuration>
    When i run minimum_quantity_of_changes with the sequence as input
    Then the <expected result> occurs
Examples:
| configuration                                    | expected result  |
| interspersed sequence                            | 0                |
| sequence with one element                        | 0                |
| non interspersed sequence with p modification    | p                |

@tc:test_method_2 @ErrorHandling
Scenario Outline: minimum quantity of permutations error handling
    Given a sequence of  of coin flips with <configuration>
    When i run minimum_quantity_of_changes with the sequence as input
    Then the <expected error> appears
Examples:
| configuration                    | expected error                                           |
| Empty sequence                   | please put a non empty sequence as input                 |
| sequence with non 0,1 elements   | please put a sequence of of coin flips with 0,1 elements |