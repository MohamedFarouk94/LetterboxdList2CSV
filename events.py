import threading as th
from main_procedure import set_interrupt, clear_interrupt, read_loading, clear_loading, handle_url
from film import to_csv
import logging


def on_go(self):
    self.go_disabled = True
    self.text_disabled = True
    stage1_thread = th.Thread(target=self.observe, args=(handle_url, [self.input_url], {}))
    stage1_thread.start()
    self.stage = 1


def on_cancel(self):
    set_interrupt()


def on_save(self):
    stage4_thread = th.Thread(target=self.observe, args=(to_csv, [self.complete_list_RETURN, self.dir_path], {}))
    stage4_thread.start()
    self.stage = 4


def on_text(self, widget):
    self.input_url = widget.text
    self.go_disabled = not bool(self.input_url)


def clear_text(self, widget):
    if not self.text_disabled:
        widget.text = ''


def on_path(self, widget):
    self.dir_path = widget.path
    self.lower_msg = self.dir_path


def update_loading(self):
    self.loading_ratio = read_loading()
    int_loading = int(self.loading_ratio * 100)
    self.loading_percentage = f'{int_loading}%'


def observe(self, fun, args, kwargs):
    logging.info(f'OBSERVE {fun.__name__}: I AM IN THE THREAD')
    setattr(self, f'{fun.__name__}_STATUS', 'ACTIVE')
    logging.info(f'OBSERVE {fun.__name__}: STATUS ACTIVE, NOW CALLING FUNCTION')
    return_value = fun(*args, **kwargs)
    logging.info(f'OBSERVE {fun.__name__}: FUNCTION CALLED SUCCESSFULLY!')
    setattr(self, f'{fun.__name__}_RETURN', return_value)
    if return_value:
        logging.info(f'OBSERVE {fun.__name__}: FUNCTION RETURN SUCCEEDED')
        setattr(self, f'{fun.__name__}_STATUS', 'SUCCEEDED')
    else:
        logging.warning(f'OBSERVE {fun.__name__}: FUNCTION RETURN FAILED')
        setattr(self, f'{fun.__name__}_STATUS', 'FAILED')
    logging.info(f'OBSERVE {fun.__name__}: LEAVING PEACEFULLY')


def restart(self):
    self.stage = 0
    self.cancel_disabled = True
    self.save_disabled = True
    self.browser_disabled = True
    self.text_disabled = False
    self.go_disabled = False
    self.lower_msg = ''
    clear_interrupt()
    clear_loading()
    self.update_loading()
    for fun in ['handle_url', 'create_list', 'complete_list', 'to_csv']:
        setattr(self, f'{fun}_STATUS', 'HALT')
        setattr(self, f'{fun}_RETURN', None)
