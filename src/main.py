from kivy.app import App
from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.widget import Widget

from src.app_base import AppBase, get_logger
from src.model.enums import Languages
from src.model.people import FullName, Person
from src.views.people import ManagePeopleLayout

# TODO(joel): save data using a consistent store
model = {
    "people": [Person(names=[FullName(language=Languages.ENGLISH,
                                      first_names="Joel", last_names="Koenka")]),
               Person(names=[FullName(language=Languages.ENGLISH,
                                      first_names="Noam", last_names="Koenka")])
               ]
}


class UiMedApp(AppBase):
    """
    The main app
    """

    def __init__(self, **kwargs) -> None:
        """
        Initialize
        :return: Nothing
        """
        super().__init__(**kwargs)

        self.model = model
        self.manage_people_layout = ManagePeopleLayout(people=self.model["people"])

    def build(self):
        inspector.create_inspector(Window, self.manage_people_layout)
        return self.manage_people_layout

    def set_root_widget(self, widget: Widget) -> None:
        get_logger().info(f"set_root_widget {self.root} -> {widget}")
        window = self.root.parent
        window.remove_widget(self.root)
        window.add_widget(widget)
        self.root = widget

    def get_cur_lang(self) -> Languages:
        # TODO(joel): use app config for default language
        return Languages.ENGLISH

    def save_model(self) -> None:
        # TODO(joel): Save model
        get_logger().info(f"model saved:\n{self.model}")


if __name__ == '__main__':
    app = UiMedApp()
    app.run()
