import logging

class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[97m',  # White
        'INFO': '\033[97m',   # White
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',  # Red
        'CRITICAL': '\033[95m',  # Purple
        'RESET': '\033[0m'  # Reset color
    }

    def format(self, record):
        log_message = super(ColoredFormatter, self).format(record)
        log_level = record.levelname
        color = self.COLORS.get(log_level, self.COLORS['RESET'])
        return f"{color}{log_message}{self.COLORS['RESET']}"