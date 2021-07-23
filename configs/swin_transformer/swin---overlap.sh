MASTER_PORT=4582 GPUS=16 GPUS_PER_NODE=8 CPUS_PER_TASK=5 tools/slurm_train.sh openmmlab swin_1 configs/swin_transformer/swin_base_overlap_224_b16x64_300e_imagenet.py --seed=0 &

MASTER_PORT=4364 GPUS=16 GPUS_PER_NODE=8 CPUS_PER_TASK=5 tools/slurm_train.sh openmmlab swin_2 configs/swin_transformer/swin_small_overlap_224_b16x64_300e_imagenet.py --seed=0 &

MASTER_PORT=1521 GPUS=16 GPUS_PER_NODE=8 CPUS_PER_TASK=5 tools/slurm_train.sh openmmlab swin_3 configs/swin_transformer/swin_tiny_overlap_224_b16x64_300e_imagenet.py --seed=0 &
