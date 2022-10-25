import coreapi
from rest_framework.schemas import AutoSchema


class CommentSchema(AutoSchema):
    """
        For blog crud
        """

    def get_manual_fields(self, path, method):
        extra_fields = [
            coreapi.Field("message", required=True, location="form"),
        ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields
