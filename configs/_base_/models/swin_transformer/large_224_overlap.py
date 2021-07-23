# model settings
# Only for evaluation
model = dict(
    type='ImageClassifier',
    backbone=dict(
        type='SwinTransformer',
        arch='large',
        img_size=224,
        patch_cfg=dict(
            conv_cfg=dict(
                type='Conv2d', kernel_size=7, stride=4, padding=3,
                dilation=1)),
        stage_cfgs=[
            dict(downsample_cfg=dict(kernel_size=3, stride=2, padding=1)),
            dict(downsample_cfg=dict(kernel_size=3, stride=2, padding=1)),
            dict(downsample_cfg=dict(kernel_size=3, stride=2, padding=1)),
            dict(downsample_cfg=dict(kernel_size=7, stride=4, padding=3))
        ]),
    neck=dict(type='GlobalAveragePooling', dim=1),
    head=dict(
        type='LinearClsHead',
        num_classes=1000,
        in_channels=1536,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 5)))
