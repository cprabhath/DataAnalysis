from Command import Command


class PriceAnalysisCommand(Command):
    def __init__(self, analysis_component):
        self.analysis_component = analysis_component

    def execute(self):
        self.analysis_component.perform_analysis()
