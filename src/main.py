from kivy.app import App

from src.model.enums import Languages
from src.model.people import FullName, Person
from src.views.people import ManagePeopleLayout

# Static data for debugging
model = {
    "people": [Person(names=[FullName(language=Languages.ENGLISH,
                                      first_names="Joel", last_names="Koenka")])]
}


class MainApp(App):
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
        self.manage_people_layout = ManagePeopleLayout(people=self.model["people"],
                                                       on_add_person=self.add_person)

    def build(self):
        return self.manage_people_layout

    def add_person(self, person: Person) -> None:
        """
        Add a person
        :param person: The person
        :return: Nothing
        """
        # TODO(joel): Save model
        print(f"person added:\n{person}")


if __name__ == '__main__':
    app = MainApp()
    app.run()
