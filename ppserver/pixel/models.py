from ppserver import app


class PPFeedback(object):

    def __init__(self):
        self.feedback = list()
        self.status   = False

    def on(self):
        if not self.status:
            self.feedback.extend(app.config.get('PIXEL_PALS'))
            self.status = True

    def off(self):
        if self.status:
            self.feedback = list()
            self.status = False

    def __str__(self):
        return str(self.feedbackad)
