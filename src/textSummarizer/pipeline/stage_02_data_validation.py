from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValiadtion
from textSummarizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(sefl):
        pass

    def main(sefl):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config= data_validation_config)
        data_validation.validate_all_files_exist()
