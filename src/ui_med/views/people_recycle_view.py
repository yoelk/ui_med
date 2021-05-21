from typing import Any, Callable, List, Optional

from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from ui_med.app_base import get_app
from ui_med.model.people import Person

Builder.load_string('''
<SelectableLabel>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size
<SelectionRecycleView>:
    viewclass: 'SelectableLabel'
    SelectableRecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True
''')


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    """
    Adds selection and focus behaviour to the view.
    """


# TODO(joel): Make multiselect optional and save a list of the selected entries
class SelectionRecycleView(RecycleView):
    def __init__(self, objects: Optional[List[Any]],
                 on_selection: Optional[Callable[[Any], None]], **kwargs):
        """
        Initialize
        :param data: A list of objects to be presented in the view
        :param on_selection: Callback for when an entry is selected
        """
        super(SelectionRecycleView, self).__init__(**kwargs)
        self.objects: List[Any] = objects if objects else []
        self._on_selection: Optional[Callable[[Any], None]] = on_selection

        self.data = [{'text': str(x)} for x in self.objects]

    def on_selected_index(self, index: int) -> None:
        """
        Callback for when an entry is selected
        :param index: The index of the selected entry
        :return: None
        """
        if self._on_selection:
            self._on_selection(self.objects[index])


class SelectableLabel(RecycleDataViewBehavior, Label):
    """
    Add selection support to the Label
    """
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        """ Catch and handle the view changes """
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        """ Add selection on touch down """
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv: SelectionRecycleView, index, is_selected) -> None:
        """ Respond to the selection of items in the view. """
        self.selected = is_selected
        if is_selected:
            rv.on_selected_index(index)
