from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_evaluation import ModelEvaluation
from textSummarizer.logging import logger


class ModelEvaluationTrainingPipeline:
    def __init__(sefl):
        pass

    def main(sefl): 
       config = ConfigurationManager()
       model_evaluation_config = config.get_model_evaluation_config()
       model_evaluation = ModelEvaluation(config=model_evaluation_config)
       model_evaluation.evaluate()