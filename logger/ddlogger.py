try:
    import os
    import logging
    from logging import StreamHandler
    from datadog_api_client.v2 import ApiClient, ApiException, Configuration
    from datadog_api_client.v2.api import logs_api
    from datadog_api_client.v2.models import *
except Exception as e:
    print("Error : {} ".format(e))
 
 
class DDHandler(StreamHandler):
    def __init__(self, configuration, service_name, ddsource):
        StreamHandler.__init__(self)
        self.configuration = configuration
        self.service_name = service_name
        self.ddsource = ddsource
 
    def emit(self, record):
        msg = self.format(record)
 
        with ApiClient(self.configuration) as api_client:
            api_instance = logs_api.LogsApi(api_client)
            body = HTTPLog(
                [
                    HTTPLogItem(
                        ddsource=self.ddsource,
                        ddtags="env:{}".format(
                            os.getenv("ENV"),
 
                        ),
                        message=msg,
                        service=self.service_name,
                    ),
                ]
            )
 
            try:
                # Send logs
                api_response = api_instance.submit_log(body)
            except ApiException as e:
                print("Exception when calling LogsApi->submit_log: %s\n" % e)
 
 
class Logging(object):
    def __init__(self, service_name: str="custom_service", ddsource: str="custom_checks", logger_name: str="demoapp", log_level: str="INFO"):
 
        self.service_name = service_name
        self.ddsource = ddsource
        self.logger_name = logger_name
 
 
        self.configuration = Configuration()
        format = "[%(asctime)s] %(name)s %(levelname)s %(message)s"
        self.logger = logging.getLogger(self.logger_name)
        formatter = logging.Formatter(
            format,
        )
 
 
        # Logs to Datadog
        dd = DDHandler(self.configuration, service_name=self.service_name,ddsource=self.ddsource)
        dd.setLevel(getattr(logging, log_level)) # replaced from logging.INFO)
        dd.setFormatter(formatter)
        self.logger.addHandler(dd)
 
        if logging.getLogger().hasHandlers():
            logging.getLogger().setLevel(getattr(logging, log_level)) # replaced from logging.INFO)
        else:
            logging.basicConfig(level=getattr(logging, log_level)) # replaced from logging.INFO)
 
def dd_logger(service_name: str="ntp", ddsource: str="custom_checks", logger_name: str="demoapp", log_level: str="INFO"):

    list_of_levels = ["DEBUG","INFO","WARNING","ERROR","CRITICAL"]
    log_level = (str(log_level)).upper()
    if log_level not in list_of_levels:
        log_level = "INFO"

    os.environ['DD_API_KEY'] = "DD_API_KEY"
    os.environ['DD_SITE'] ="datadoghq.com"
    os.environ['ENV'] = "dev"

    stream_logger = Logging(service_name, ddsource, logger_name, log_level)
    #logger = Logging(service_name='ntp', ddsource='ntp_checks', logger_name='ntp_logger', log_level="INFO")
    
    #stream_logger.logger.info("test message")
    return stream_logger
