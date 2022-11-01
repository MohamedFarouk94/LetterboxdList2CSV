from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import StringProperty, ColorProperty, NumericProperty, BooleanProperty, Clock
from kivy.utils import platform

if platform not in ['android', 'ios']:
    Window.size = (840, 1163)


class MainComponent(BoxLayout):
    BACKGROUND_COLOR = ColorProperty((25/255, 70/255, 131/255, 1))
    ERROR_COLOR = ColorProperty((1, 0, 0, 1))
    SAFETY_COLOR = ColorProperty((0, 1, 0, 1))
    NEUTRAL_COLOR = ColorProperty((1, 1, 0, 1))
    FPS = 5

    STAGE1_ACTIVE_MSG = 'Checking URL...'
    STAGE1_FAIL_MSG = 'Invaid link or bad internet connection'
    STAGE1_SUCCESS_MSG = STAGE1_ACTIVE_MSG
    STAGE2_ACTIVE_MSG = STAGE1_SUCCESS_MSG
    STAGE2_FAIL_MSG = STAGE1_FAIL_MSG
    STAGE2_SUCCESS_MSG = 'Downloading list...\nIt may take a while depending on list size & internet connection.'
    STAGE3_ACTIVE_MSG = STAGE2_SUCCESS_MSG
    STAGE3_FAIL_MSG = 'Download Stopped! @_@ You can try again.'
    STAGE3_SUCCESS_MSG = 'Your file is ready, choose a directory to save it in.'
    STAGE4_SUCCESS_MSG = 'Your file has been saved successfully!'

    stage = NumericProperty(0)
    input_url = StringProperty('')
    dir_path = StringProperty('')
    upper_msg = StringProperty('')
    lower_msg = StringProperty('')
    upper_color = ColorProperty((1, 1, 1, 1))
    loading_ratio = NumericProperty(0)
    loading_percentage = StringProperty('')

    go_disabled = BooleanProperty(True)
    cancel_disabled = BooleanProperty(True)
    save_disabled = BooleanProperty(True)
    browser_disabled = BooleanProperty(True)
    text_disabled = BooleanProperty(False)

    handle_url_STATUS = 'HALT'
    create_list_STATUS = 'HALT'
    complete_list_STATUS = 'HALT'
    to_csv_STATUS = 'HALT'

    handle_url_RETURN = None
    create_list_RETURN = None
    complete_list_RETURN = None
    to_csv_RETURN = None

    counter = 0

    from events import on_go, on_cancel, on_save, on_text, on_path
    from events import clear_text, update_loading, observe, restart
    from update import update, stage1, stage2, stage3, stage4

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1/self.FPS)


class Lbxd2CSVApp(App):
    pass


Lbxd2CSVApp().run()
