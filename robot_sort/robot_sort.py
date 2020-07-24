class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l         # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
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

    def sort(self):
        """
        Sort the robot's list.
        """
        # Using arr = [2, 1, 0] --> small example
        # Start at arr[0], if we can move right,
        while self.can_move_right() == True:
            # swap items to compare arr[0] num to arr[1] num
            self.swap_item()
            # move robot to the next position
            self.move_right()
            print("While can move r", self._light)

            # if robot's num is > arr[1]
            if self.compare_item() == 1:
                # turn on the light, make True
                self.set_light_on()
                # swap items
                self.swap_item()
                # move back
                self.move_left()
                # swap items again, now arr[0] and arr[1] are sorted
                self.swap_item()
                # move right to start over again
                self.move_right()
                print("Compare == 1", self._item)
                print("Compare == 1", self._position)
                print("Compare == 1", self._list)
            # is robot's num is < arr[1]
            else:
                # go back
                self.move_left()
                # swap/replace the item b/c arr[0] and arr[1] were already sorted
                self.swap_item()
                # move right to increment 1
                self.move_right()
                print("Compare ! 1", self._item)
                print("Compare ! 1", self._position)
                print("Compare ! 1", self._list)
        
        # Robot has reached the end of the list, can't move on any more
        # Light is on 
        while self.can_move_left == True:
            # need to move all the way back
            while self.can_move_left():
                # reset position to the beginning
                self.move_left()
                print("Move L", self._item)
                print("Move L", self._position)
                print("Move L", self._list)
                self.sort()
        
        # need to reset the light to beginning state
        # if self.light_is_on() == True:
        #     # turn off the light 
        #     self.set_light_off()
        #     # call the mehtod again to run through the code
        #     self.sort()
        # else:
        #     return self._list


        

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print("You list is", robot._list)