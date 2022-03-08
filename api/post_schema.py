from rest_framework.schemas import AutoSchema
import coreapi
import coreschema


class PostSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() == "post":
            extra_fields = [
                coreapi.Field("author", required=True, location="form", schema=coreschema.String() ),
                coreapi.Field("upload", required=True, location="form", schema=coreschema.String()),
                coreapi.Field("caption", required=False, location="form", schema=coreschema.String()),
                coreapi.Field("slug", required=False, location="form", schema=coreschema.String()),
                coreapi.Field("date_posted", required=False, location="form", schema=coreschema.String()),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields