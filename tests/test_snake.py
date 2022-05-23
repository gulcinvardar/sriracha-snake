"""
Automated Test with pytest
(we write another program to test our application)

The discipline of TDD (Test-Driven-Development)
-----------------------------
1. Write a test
2. Run the test and make sure it fails
3. Write just enough code to make the test pass
4. Run the test again and make sure it passes
5. Clean up
6. Run the tests again (regression testing)
7. Back to step 1

also see: Uncle Bob "Clean Code Lectures"
"""

# feature: the snake is moving in all 4 directions
# TODO: also test random positions

from spiced_snake import move
import pytest

def test_move_left():
    position = (5, 5) # x, y
    new_position = move(position, 'left')
    assert new_position == (4, 5)

def test_move_left_smwelse():
    position = (5, 0) # x, y
    new_position = move(position, 'left')
    assert new_position == (4, 0)

def test_move_left():
    position = (5, 5) # x, y
    new_position = move(position, 'right')
    assert new_position == (6, 5)

def test_move_up():
    position = (5, 5) # x, y
    new_position = move(position, 'up')
    assert new_position == (5, 6)

def test_move_down():
    position = (5, 5) # x, y
    new_position = move(position, 'down')
    assert new_position == (5, 4)

def test_move_fraction():
    """This is an examople of a code that's not supposed to work"""
    position = (3.14519, 5) # x, y
    with pytest.raises(Exception):
        move(position, 'down')
