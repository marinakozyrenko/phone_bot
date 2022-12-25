import user_interface as ui
import logger as lg
import checking as ch

lg.logging.info('Start')
ch.init_data_base('base_phone.csv')
ui.ls_menu()