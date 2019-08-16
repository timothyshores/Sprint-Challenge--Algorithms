import inspect


def line():
    # Returnsthe current line number
    return str(inspect.currentframe().f_back.f_lineno - 1)


class SortingRobot:
    def __init__(self, l):      # SortingRobot takes a list and sorts it.
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    # returns True if the robot can move right
    # return False if it's at the end of the list.
    def can_move_right(self):
        return self._position < len(self._list) - 1

    # return True if the robot can move left
    # return False if it's at the start of the list
    def can_move_left(self):
        return self._position > 0

    def move_right(self):
        # increment the time counter by 1.
        self._time += 1
        if self._position < len(self._list) - 1:
            # if robot can move right then move to the right and return True
            self._position += 1
            return True
        else:
            # robot can NOT move right, stay in place and return False.
            return False

    def move_left(self):
        # increment the time counter by 1.
        self._time += 1
        if self._position > 0:      # robot can move to the left
            self._position -= 1     # move robot left
            return True             # return True
        else:
            return False            # robot can not move left, return False

    def swap_item(self):
        self._time += 1             # increment the time counter by 1.
        # Swap the current item with the value at current position
        self._item, self._list[self._position] = self._list[self._position], self._item

    # compare current item with current value
    def compare_item(self):
        if self._item is None or self._list[self._position] is None:
            # current item or current value is None, return None
            return None
        elif self._item > self._list[self._position]:
            # current item is greater than the current element, return 1
            return 1
        elif self._item < self._list[self._position]:
            # current item is less than the current element, return -1
            return -1
        else:
            # current item is equal to the current element, return 0.
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):  # sort the robot's list.
        print('\nsort')
        self.debug(line())
        while self.can_move_left():
            self.debug(line())
            self.move_left()
            self.debug(line())
        self.debug(line())
        self.compare_first_last
        self.debug(line())
        self.swap_item()  # set item to first element in list
        self.debug(line())
        # move right if position is not at list[-1]
        while self.right_swap():
            self.debug(line())
            self.right_swap()
            self.debug(line())

    def right_swap(self):
        print('\nright_swap')
        if self.can_move_right():        # check if robot can move right
            self.debug(line())
            self.move_right()               # move right
            self.debug(line())
            if self.compare_item() > 0:  # the current item is greater than the current element
                print("right_swap compare_item > 0:")
                if not self.can_move_right():
                    print("right_swap not self.can_move_right")
                    self.swap_item()
                    self.sort()
                self.move_right()
                self.right_swap()
                return False
            elif self.compare_item() < 0:
                self.swap_item()
                self.move_right()
                self.sort()
            else:
                if self.compare_item() == None:
                    self.debug(line())
                    self.swap_item()            # swap current item with current element
                    self.debug(line())
        else:
            self.debug(line())
            self.left_swap()
            return False
        return self.compare_item()

    # swap current item at the position with the value none
    def left_swap(self):
        print('\nleft_swap')
        if self.can_move_left():                # check if robot can move right
            self.debug(line())
            self.move_left()                    # move left
            self.debug(line())
            print(f"\n{self.debug(line())}\n")
            if self.compare_item() == None:     # the current element contains the value None
                self.debug(line())
                self.swap_item()                # swap current item with current element
                self.debug(line())
            else:
                self.debug(line())
                self.compare_item() < 0
                self.debug(line())
                self.left_swap()
                self.debug(line())
        else:
            self.debug("Completed left_swap")
            return 0
        return self.compare_item()

    def compare_first_last(self):
        print('\ncompare_first_last')
        self.debug(line())
        self.swap_item()
        self.debug(line())
        while self.can_move_right():
            if not self.can_move_right() and self.compare_item() > 0:
                self.debug(line())
                print("Current item is greater than last element in the array")
                break
            self.debug(line())
            self.move_right()
        if self.compare_item() > 0:
            self.sort()
        self.debug(line())
        while self.can_move_left:
            self.debug(line())
            if not self.can_move_left():
                self.debug(line())
                break
            self.debug(line())
            self.move_left()
            self.debug(line())
        self.debug(line())
        if self.compare_item() == None:
            self.debug(line())
            self.swap_item()
            self.debug(line())
            self.sort()
        if self.can_move_right:
            self.move_right()
            self.sort()

    def debug(self, input=""):
        print(
            f"{input}\tList: {self._list},\tItem: {self._item},\tPosition: {self._position}")


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    # l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
    #      45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    l = [4, 3, 2, 1]
    robot = SortingRobot(l)

    robot.sort()
    # print(robot._list)
