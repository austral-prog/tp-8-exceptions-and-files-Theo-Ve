# Ejercicio 10 - Parser de archivos de log


def parse_log(filename):
    log_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if ':' not in line:
                raise ValueError("invalid log line")

            level, message = line.split(':', 1)

            level = level.strip()
            message = message.strip()

            if level not in log_dict:
                log_dict[level] = []

            log_dict[level].append(message)

    return log_dict
