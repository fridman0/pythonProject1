from kivy.lang import Builder

from kivymd.app import MDApp


class Test(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(
            '''
MDScreen:

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "orange"
        text_color_active: "lightgrey"
        
# ===============================================

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Mail'
            icon: 'gmail'
            badge_icon: "numeric-10"
            
            FloatLayout:
            
                MDLabel:
                    text: 'Hello'
                    pos_hint: {'center_x': 1, 'center_y': .6}
            
                MDRoundFlatIconButton:
                    text: "MDRoundFlatIconButton"
                    icon: "android"
                    text_color: "white"
                    pos_hint: {'center_x': .5, 'center_y': .5}
# ===============================================

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Twitter'
            icon: 'twitter'
            badge_icon: "numeric-5"

# ================================================

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'LinkedIN'
            icon: 'linkedin'

'''
        )


Test().run()