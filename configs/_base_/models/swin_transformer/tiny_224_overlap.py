# model settings
model = dict(
    type='ImageClassifier',
    backbone=dict(
        type='SwinTransformer',
        arch='tiny',
        img_size=224,
        drop_path_rate=0.2,
        patch_cfg=dict(
            conv_cfg=dict(
                type='Conv2d', kernel_size=7, stride=4, padding=3,
                dilation=1)),
        stage_cfgs=[
            dict(downsample_cfg=dict(kernel_size=3, stride=2, padding=1)),
            dict(downsample_cfg=dict(kernel_size=3, stride=2, padding=1)),
            dict(downsample_cfg=dict(kernel_size=3, stride=2, padding=1)),
            dict(downsample_cfg=dict(kernel_size=3, stride=2, padding=1))
        ]),
    neck=dict(type='GlobalAveragePooling', dim=1),
    head=dict(
        type='LinearClsHead',
        num_classes=1000,
        in_channels=768,
        init_cfg=None,  # suppress the default init_cfg of LinearClsHead.
        loss=dict(
            type='LabelSmoothLoss', label_smooth_val=0.1, mode='original'),
        cal_acc=False),
    init_cfg=[
        dict(type='TruncNormal', layer='Linear', std=0.02, bias=0.),
        dict(type='Constant', layer='LayerNorm', val=1., bias=0.)
    ],
    train_cfg=dict(augments=[
        dict(type='BatchMixup', alpha=0.8, num_classes=1000, prob=0.5),
        dict(type='BatchCutMix', alpha=1.0, num_classes=1000, prob=0.5)
    ]))
