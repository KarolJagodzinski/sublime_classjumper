import sublime
import sublime_plugin


class ClassJumperCommand(sublime_plugin.TextCommand):

    @staticmethod
    def is_same_pointer_position(pointer_position, closest_class_to_pointer):
        return pointer_position == closest_class_to_pointer

    @staticmethod
    def keep_current_class_index(
        jump_to,
        pointer_position,
        current_class,
    ):
        if jump_to == 'up':
            return pointer_position < current_class
        elif jump_to == 'down':
            return pointer_position > current_class

    @staticmethod
    def get_new_pointer(
        jump_to,
        class_positions,
        class_index,
        keep_current_class_index,
        is_same_pointer_position,
    ):
        if jump_to == 'up':
            new_pointer = (
                class_positions[class_index - 1] if
                (is_same_pointer_position or keep_current_class_index) else
                class_positions[class_index]
            )
        elif jump_to == 'down':
            try:
                new_pointer = (
                    class_positions[class_index + 1] if
                    (is_same_pointer_position or keep_current_class_index) else
                    class_positions[class_index]
                )
            except IndexError:
                new_pointer = class_positions[0]

        return new_pointer

    def move_pointer(self, jump_to, pointer_position, classes):
        class_positions = [region.begin() for region in classes]
        closest_class_to_pointer = min(
            class_positions,
            key=lambda x: abs(x - pointer_position)
        )
        is_same_pointer_position = self.is_same_pointer_position(
            pointer_position, closest_class_to_pointer
        )
        class_index = (
            class_positions.index(pointer_position) if
            is_same_pointer_position else
            class_positions.index(closest_class_to_pointer)
        )
        keep_current_class_index = self.keep_current_class_index(
            jump_to, pointer_position, class_positions[class_index]
        )

        new_pointer = self.get_new_pointer(
            jump_to,
            class_positions,
            class_index,
            keep_current_class_index,
            is_same_pointer_position,
        )

        return new_pointer

    def run(self, edit, jump_to=None):
        all_classes = self.view.find_all(r'class?\s{1}\w+')
        selected = self.view.sel()
        pointer_position = selected[0].begin()

        new_pointer = self.move_pointer(
            jump_to,
            pointer_position,
            all_classes,
        )
        selected.clear()
        selected.add(sublime.Region(new_pointer))

        self.view.show_at_center(new_pointer)
