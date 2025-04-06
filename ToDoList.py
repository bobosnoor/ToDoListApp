from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
class ToDoListAPP(App):
    def build(self):
        pass
    def on_start(self):
        self.task_input = self.root.ids.task_input
        self.tasks_list_layout = self.root.ids.tasks_list_layout
        add_button = self.root.ids.add_button
        add_button.bind(on_press=self.add_task)
        # self.main_layout = BoxLayout(orientation = "vertical",spacing=10)
        # # input layout
        # input_layout = BoxLayout(size_hint_y = 0.2, padding = (10,10,10,0) , spacing= 10)
        # self.main_layout.add_widget(input_layout)
        # self.task_input = TextInput(hint_text = "Enter a task ", size_hint_x = 0.7)
        # add_button = Button(text = "Add a task ", size_hint_x = 0.3, background_color = (0,1,0,1), font_size = 22)
        # add_button.bind(on_press = self.add_task)
        # input_layout.add_widget(self.task_input)
        # input_layout.add_widget(add_button)
        # # tasks list layout
        # self.tasks_list_layout = BoxLayout(orientation = "vertical", size_hint_y = 0.8)
        # self.main_layout.add_widget(self.tasks_list_layout)
        # return self.main_layout
    def add_task(self, instance):
        task_text = self.task_input.text
        if task_text:
            task_layout = BoxLayout(spacing = 50, padding = 20)
            task_label = Label(text = task_text, size_hint_x = 0.7, color = (150,100,230,1), font_size = 18)
            task_layout.add_widget(task_label)
            remove_button = Button(text = "Remove task", size_hint_x = 0.3, on_press = lambda btn : self.tasks_list_layout.remove_widget(task_layout), background_color = (1,0,0,0.7), font_size = 20)
            task_layout.add_widget(remove_button)
            self.tasks_list_layout.add_widget(task_layout)
            self.task_input.text = ""   
ToDoListAPP().run()