from mycroft import MycroftSkill, intent_file_handler


class YogaExperiment(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('experiment.yoga.intent')
    def handle_experiment_yoga(self, message):
        self.speak_dialog('experiment.yoga')


def create_skill():
    return YogaExperiment()

