# coding=utf-8
from enum import Enum

class Camera_EN(Enum):
    camera = "camera"
    photo = "photo"
    photo_alias_1 = "picture"
    photo_alias_2 = "photograph"
    video = "video"
    scan = "scan"
    scanner = "scanner"
    qrcode = "qrcode"


class Camera_CN(Enum):
    camera_cn = "照相机"
    camera_cn_alias_1 = "摄像头"
    camera_cn_alias_2 = "相机"
    photo_cn_alias = "照片"
    video_cn = "视频"
    qrcode_cn = "二维码"
    scan_cn = "扫描"



def main():
    for cn in Camera_CN:
        print cn.value

if __name__ == '__main__':
    main()