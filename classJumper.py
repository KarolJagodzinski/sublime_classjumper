import sublime
import sublime_plugin


class ClassJumperCommand(sublime_plugin.TextCommand):

    @staticmethod
    def is_same_pointer_position(pointer_position, closest_area_to_pointer):
        return pointer_position == closest_area_to_pointer

    @staticmethod
    def keep_current_area_index(
        direction,
        pointer_position,
        current_position,
    ):
        if direction == 'up':
            return pointer_position < current_position
        elif direction == 'down':
            return pointer_position > current_position

    @staticmethod
    def get_new_pointer(
        direction,
        available_positions,
        new_position_index,
        keep_current_area_index,
        is_same_pointer_position,
    ):
        if direction == 'up':
            new_pointer = (
                available_positions[new_position_index - 1] if
                (is_same_pointer_position or keep_current_area_index) else
                available_positions[new_position_index]
            )
        elif direction == 'down':
            try:
                new_pointer = (
                    available_positions[new_position_index + 1] if
                    (is_same_pointer_position or keep_current_area_index) else
                    available_positions[new_position_index]
                )
            except IndexError:
                new_pointer = available_positions[0]

        return new_pointer

    def move_pointer(self, direction, pointer_position, jump_area):
        available_positions = [region.begin() for region in jump_area]
        closest_area_to_pointer = min(
            available_positions,
            key=lambda x: abs(x - pointer_position)
        )
        is_same_pointer_position = self.is_same_pointer_position(
            pointer_position,
            closest_area_to_pointer,
        )
        new_position_index = (
            available_positions.index(pointer_position) if
            is_same_pointer_position else
            available_positions.index(closest_area_to_pointer)
        )
        keep_current_area_index = self.keep_current_area_index(
            available_positions[new_position_index],
            direction,
            pointer_position,
        )

        new_pointer = self.get_new_pointer(
            direction,
            available_positions,
            new_position_index,
            keep_current_area_index,
            is_same_pointer_position,
        )

        return new_pointer

    def jump_to_select(self, jump_to):
        if jump_to == 'class':
            return self.view.find_all(r'(class?)(\s{1}\w+\()')
        elif jump_to == 'method':
            return self.view.find_all(r'(def?)(\s{1}\w+\()')

    def run(self, edit, direction, jump_to):
        selected = self.view.sel()
        pointer_position = selected[0].begin()

        new_pointer = self.move_pointer(
            direction,
            pointer_position,
            self.jump_to_select(jump_to),
        )
        selected.clear()
        selected.add(sublime.Region(new_pointer))

        self.view.show_at_center(new_pointer)
