from time import sleep
import ddlogger
log = ddlogger.dd_logger('ntp','ntp_checks','ntp_logger','INFO')
log.logger.info("info 1")
sleep(1)
log.logger.warning("warning 2")
sleep(1)
log.logger.error("error 3")