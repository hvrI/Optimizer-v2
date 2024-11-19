import logging
import datetime

class Log:

    logging.basicConfig(
        format="{levelname} | {asctime} | {message}",
        style="{",
        datefmt="%H:%M",
        filename="optimizer.log",
        filemode="w",
        level=logging.DEBUG
        )

    def __init__(self):
        date = datetime.datetime.now().strftime("%d %A %Y")
        logging.info(f"Start Logging - {date}")
    
    def registry_path_not_found(self, error_message):
        logging.error(error_message)

    def registry_key_changed(self, info_message):
        logging.info(info_message)

    def registry_key_not_changed(self, error_message):
        logging.error(error_message)

    def unexpected_error(self, error_message):
        logging.critical(error_message)

    def finished_tweaks(self):
        logging.info("\n=============== END OF TWEAK ===============\n")

    def added_latest_untweaks(self, latest_untweak_list: list):
        # (path, ('Start', 'Reg_DWORD', '3'), '2')
        if not latest_untweak_list:
            return
        for data in latest_untweak_list:
            logging.info(f"Untweak List Updated: {data[0]} - {data[1][0]} : Current Value: {data[2]} | Value: {data[1][2]}")

    def registry_key_not_found(self, path, value_name):
        logging.error(f"Unable to locate key after changes made: {path} - {value_name}")

    def registry_key_deleted(self, path):
        logging.info(f"Deleted: {path}")
