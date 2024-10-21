import mux_python

from binary_sets import settings


class MuxUploadClient:
    def __init__(self):
        self.configuration = mux_python.Configuration()
        self.configuration.username = settings.MUX_ACCESS_TOKEN_ID
        self.configuration.password = settings.MUX_SECRET_KEY

        self.uploads_api = mux_python.DirectUploadsApi(
            mux_python.ApiClient(self.configuration)
        )

    def get_upload_url(self):
        create_asset_request = mux_python.CreateAssetRequest(playback_policy=["PUBLIC"])
        create_upload_request = mux_python.CreateUploadRequest(
            timeout=7200, new_asset_settings=create_asset_request, cors_origin=["*"]
        )
        create_upload_response = self.uploads_api.create_direct_upload(
            create_upload_request
        )
        return create_upload_response
