from fastapi import HTTPException, status

ContentTypeJSON = "application/json"
ContentTypeYAML = "application/yaml"
ContentTypeSSZ = "application/octet-stream"
ContentTypeUnknown = "unknown"


def validate_content_type(content_type: str, expected_content_type: str):
    if content_type != expected_content_type:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"Unsupported content-type: {content_type}")
