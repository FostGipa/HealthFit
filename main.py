from kivy import utils
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.pickers import MDDatePicker

Window.size = (310, 580)

KV = """
#:import NoTransition kivy.uix.screenmanager.NoTransition
#:import C kivy.utils.get_color_from_hex

ScreenManager:
    id: scr1
    MDScreen:
        name: "welcome"
        MDBoxLayout:
            padding: (0, 0, 0, 50)
            orientation: "vertical"
            Image:
                source: "4310860.png"
                pos_hint: {"center_x": .5}
            MDLabel:
                text: "HealthFit"
                color: C('#92A3FD')
                halign: "center"
                font_size: 30
                font_name: "Poppins-Regular.ttf"
                size_hint_y: None
                height: self.texture_size[1]
            MDBoxLayout:
                size_hint_y: None
                pos_hint: {"center_x": .5}
                size_hint_x: .6
                MDFillRoundFlatButton:
                    text: "Start"
                    font_size: 20
                    size_hint_x: .6
                    pos_hint: {"center_x": .5}
                    font_name: "Poppins-Regular.ttf"
                    md_bg_color: C("#92A3FD")
                    on_press:
                        scr1.current = "start"
    MDScreen:
        name: "start"
        MDBoxLayout:
            orientation: "vertical"
            MDBoxLayout:
                orientation: "vertical"
                MDRectangleFlatIconButton:
                    pos_hint: {"center_x": .5}
                    id: btn
                    icon: "account-multiple-outline"
                    icon_color: C("#ADA4A5")
                    text: 'Выберите пол'
                    text_color: C("#ADA4A5")
                    halign: 'left'
                    on_release: dropdown.open(self)
                    size_hint_x: .9
                    line_color: C("#ADA4A5")
                Widget:
                    on_parent: dropdown.dismiss()
                DropDown:
                    id: dropdown
                    on_select: btn.text = '{}'.format(args[1])
                    MDRectangleFlatButton:
                        text: 'Мужской'
                        size_hint_x: .5
                        halign: 'left'
                        line_color: C("#ADA4A5")
                        icon_color: C("#ADA4A5")
                        text_color: C("#ADA4A5")
                        on_release: dropdown.select('Мужской')
                    MDRectangleFlatButton:
                        text: 'Женский'
                        size_hint_x: .5
                        halign: 'left'
                        line_color: C("#ADA4A5")
                        icon_color: C("#ADA4A5")
                        text_color: C("#ADA4A5")
                        on_release: dropdown.select('Женский')  
            MDRectangleFlatIconButton:
                pos_hint: {"center_x": .5}
                id: btn2
                icon: "calendar-range"
                icon_color: C("#ADA4A5")
                text: 'Дата рождения'
                text_color: C("#ADA4A5")
                halign: 'left'
                on_release: app.show_date_picker()
                size_hint_x: .9
                line_color: C("#ADA4A5")
            MDTextField:
                hint_text: "Rectangle mode"
                mode: "rectangle"
                size_hint_x: .9
                pos_hint: {"center_x": .5}
            Widget:
    MDScreen:
        name: "main"
        MDFloatLayout:
            md_bg_color: 1, 1, 1, 1
            ScreenManager:
                id: scr
                transition: NoTransition()
                MDScreen:
                    name: "home"
                    MDLabel:
                        text: "Home"
                        pos_hint: {"center_y": .5}
                        halign: "center"
                MDScreen:
                    name: "sport"
                    MDLabel:
                        text: "Search"
                        pos_hint: {"center_y": .5}
                        halign: "center"
                MDScreen:
                    name: "food"
                    MDLabel:
                        text: "Music"
                        pos_hint: {"center_y": .5}
                        halign: "center"
                MDScreen:
                    name: "settings"
                    MDLabel:
                        text: "Home"
                        pos_hint: {"center_y": .5}
                        halign: "center"
            
            NavBar:
                size_hint: .85, .1
                pos_hint: {"center_x": .5, "center_y": .1}
                elevation: 1
                md_bg_color: 1, 1, 1, 1
                radius: [16]
                MDGridLayout: 
                    cols: 4
                    spacing: 8
                    size_hint_x: .9
                    size_hint_y: .9
                    pos_hint: {"center_x": .5, "center_y": .5}
                    MDIconButton:
                        id: nav_icon1
                        icon: 'home'
                        icon_size: "0.30in"
                        ripple_scale: 0
                        theme_text_color: "Custom"
                        text_color: C('#92A3FD')
                        on_release:
                            scr.current = "home"
                            app.change_color(self)
                            
                    MDIconButton:
                        id: nav_icon2
                        icon: "dumbbell"
                        ripple_scale: 0
                        icon_size: "0.30in"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1
                        on_release:
                            scr.current = "sport"
                            app.change_color(self)
                            
                    MDIconButton:
                        id: nav_icon3
                        icon: "silverware-fork-knife"
                        ripple_scale: 0
                        icon_size: "0.30in"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1
                        on_release:
                            scr.current = "food"
                            app.change_color(self)
                            
                    MDIconButton:
                        id: nav_icon4
                        icon: "cog"
                        ripple_scale: 0
                        icon_size: "0.30in"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1
                        on_release:
                            scr.current = "settings"
                            app.change_color(self)
"""


class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass


class MyApp(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def change_color(self, instance):
        if instance in self.root.ids.values():
            current_id = list(self.root.ids.keys())[list(self.root.ids.values()).index(instance)]
            for i in range(4):
                if f"nav_icon{i + 1}" == current_id:
                    self.root.ids[f"nav_icon{i + 1}"].text_color = utils.get_color_from_hex('#92A3FD')
                else:
                    self.root.ids[f"nav_icon{i + 1}"].text_color = 0, 0, 0, 1

    def show_date_picker(self):
        date_dialog = MDDatePicker(primary_color=utils.get_color_from_hex('#92A3FD'),
                                   text_button_color=utils.get_color_from_hex('#92A3FD'),
                                   selector_color=utils.get_color_from_hex('#92A3FD'))
        date_dialog.open()
        date_dialog.bind(on_save=self.on_save)

    def on_save(self, instance1, value, date_range):
        self.root.ids.btn2.text = str(value)


MyApp().run()
