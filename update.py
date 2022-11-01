import logging
import threading as th
from main_procedure import create_list, complete_list


def update(self, dt):
    self.counter = (self.counter + 1) % self.FPS
    logging.info(f'UPDATE {self.counter}: CURRENT STAGE: {self.stage}')
    if not self.stage:
        return

    if self.stage == 1:
        self.stage1()

    elif self.stage == 2:
        self.stage2()

    elif self.stage == 3:
        self.stage3()

    else:
        self.stage4()


def stage1(self):
    if self.handle_url_STATUS == 'ACTIVE':
        self.upper_msg = self.STAGE1_ACTIVE_MSG
        self.upper_color = self.NEUTRAL_COLOR
        return

    if self.handle_url_STATUS == 'FAILED':
        self.upper_msg = self.STAGE1_FAIL_MSG
        self.upper_color = self.ERROR_COLOR
        self.restart()

    elif self.handle_url_STATUS == 'SUCCEEDED':
        self.upper_msg = self.STAGE1_SUCCESS_MSG
        stage2_thread = th.Thread(target=self.observe, args=(
            create_list, [self.handle_url_RETURN], {}))
        stage2_thread.start()
        self.stage = 2


def stage2(self):
    if self.create_list_STATUS == 'ACTIVE':
        self.upper_msg = self.STAGE2_ACTIVE_MSG
        self.upper_color = self.NEUTRAL_COLOR
        return

    if self.create_list_STATUS == 'FAILED':
        self.upper_msg = self.STAGE2_FAIL_MSG
        self.upper_color = self.ERROR_COLOR
        self.restart()

    elif self.create_list_STATUS == 'SUCCEEDED':
        self.upper_msg = self.STAGE2_SUCCESS_MSG
        self.upper_color = self.SAFETY_COLOR
        stage3_thread = th.Thread(target=self.observe, args=(
            complete_list, [self.create_list_RETURN], {}))
        stage3_thread.start()
        self.cancel_disabled = False
        self.stage = 3


def stage3(self):
    if self.complete_list_STATUS == 'ACTIVE':
        self.upper_msg = self.STAGE3_ACTIVE_MSG
        self.upper_color = self.NEUTRAL_COLOR
        self.update_loading()
        return

    if self.complete_list_STATUS == 'FAILED':
        self.upper_msg = self.STAGE3_FAIL_MSG
        self.upper_color = self.ERROR_COLOR
        self.restart()

    elif self.complete_list_STATUS == 'SUCCEEDED':
        self.loading_percentage = "100%"
        self.loading_ratio = 1
        self.upper_msg = self.STAGE3_SUCCESS_MSG
        self.upper_color = self.SAFETY_COLOR
        self.cancel_disabled = True
        self.save_disabled = False
        self.browser_disabled = False


def stage4(self):
    if self.to_csv_STATUS == 'ACTIVE':
        self.save_disabled = True
        self.browser_disabled = True
        return

    self.upper_msg = 'Try another list!'
    self.upper_color = self.SAFETY_COLOR
    self.restart()
    self.lower_msg = self.STAGE4_SUCCESS_MSG
