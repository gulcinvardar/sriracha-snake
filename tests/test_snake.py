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

from turtle import position
import spicy_snake.moves
import pytest
import random

@pytest.mark.parametrize('position,direction,expected', [
    # data examples
    ((5, 5), 'left', (4, 5)),
    ((5, 5), 'right', (6, 5)),
    ((5, 0), 'left', (4, 0)),
    ((5, 5), 'up', (5, 6)),
    ((5, 5), 'down', (5, 4)),
    ((3, 3), 'left', (2, 3))
    # ((0 , 5), 'left', (10, 5)) only if 
])
def test_move(position, direction,expected):
    """The snake is moving in all 4 directions"""
    assert spicy_snake.moves.move(position, direction) == expected

# def test_move_left():
#     position = (5, 5) # x, y
#     new_position = move(position, 'left')
#     assert new_position == (4, 5)

def test_move_invalid_direction():
    with pytest.raises(Exception):
        spicy_snake.moves.move((1, 1), 'dummy')

def test_move_fraction():
    """This is an examople of a code that's not supposed to work"""
    position = (3.14519, 5) # x, y
    with pytest.raises(Exception):
        spicy_snake.moves.move(position, 'down')

def test_move_random():
    """test random position"""
    for _ in range(100):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        direction = random.choice(list(spicy_snake.moves.VALID_DIRECTIONS))
        position = x, y
        spicy_snake.moves.move(position, direction)
        