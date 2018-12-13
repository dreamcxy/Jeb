#encoding=utf-8
from enum import Enum

class Camera(Enum):
    camera = "camera"
    photo = "photo"
    photo_alias_1 = "picture"
    photo_alias_2 = "photograph"
    video = "video"
    scan = "scan"
    scanner = "scanner"
    qrcode = "qrcode"
    
    camera_cn = "照相机"
    camera_cn_alias_1 = "摄像头"
    photo_cn_alias = "照片"
    video_cn = "视频"

    