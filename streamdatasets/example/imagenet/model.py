# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: model.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Imagenet(betterproto.Message):
    folder: str = betterproto.string_field(1)
    filename: str = betterproto.string_field(2)
    size_width: int = betterproto.int32_field(4)
    size_height: int = betterproto.int32_field(5)
    object_name: str = betterproto.string_field(8)
    # bool object_pose_unspecified = 9;bool object_truncated = 10;bool
    # object_difficult = 11;
    object_bndbox_xmin: int = betterproto.int32_field(12)
    object_bndbox_ymin: int = betterproto.int32_field(13)
    object_bndbox_xmax: int = betterproto.int32_field(14)
    object_bndbox_ymax: int = betterproto.int32_field(15)
