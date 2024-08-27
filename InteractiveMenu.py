from prompt_toolkit import Application
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style as PromptStyle

class InteractiveMenu:
    """
    This class is our interactive menu for our TUI, it will display a list of options and allow the user to select one.
    """
    def __init__(self, title, options):
        self.title = title
        self.options = options
        self.selected = 0

    def get_formatted_options(self):
        result = []
        for i, option in enumerate(self.options):
            if i == self.selected:
                result.append(('class:selected', f'> {option}\n'))
            else:
                result.append(('', f'  {option}\n'))
        return result

    def create_layout(self):
        return Layout(
            HSplit([
                Window(height=1, content=FormattedTextControl(self.title), align="center", style="class:title"),
                Window(content=FormattedTextControl(self.get_formatted_options), style="class:options")
            ])
        )

    def create_style(self):
        return PromptStyle([
            ('selected', '#CCCC11 bold'),
            ('title', '#00FF00 bold'),
            ('options', '#FFFFFF')
        ])

    def create_keybindings(self):
        kb = KeyBindings()

        @kb.add('up')
        def _(event):
            self.selected = (self.selected - 1) % len(self.options)

        @kb.add('down')
        def _(event):
            self.selected = (self.selected + 1) % len(self.options)

        @kb.add('enter')
        def _(event):
            event.app.exit(result=self.selected)

        return kb

    def run(self):
        application = Application(
            layout=self.create_layout(),
            key_bindings=self.create_keybindings(),
            style=self.create_style(),
            full_screen=True
        )
        return application.run()