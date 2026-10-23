from MeMo.plugins.utilities import MeMoPublicView, MeMoPrivateView


class MyPublicView(MeMoPublicView):
    def process_view(self):
        return {"message": self._("Hello world")}


class MyPrivateView(MeMoPrivateView):
    def __init__(self, request):
        MeMoPrivateView.__init__(self, request)
        self.checkCrossPost = False

    def process_view(self):
        return {
            "activeUser": self.user,
            "message": self._("Hello world"),
        }
