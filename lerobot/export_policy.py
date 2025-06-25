import yaml
from pathlib import Path
import torch

from lerobot.common.policies.factory import make_policy
from lerobot.common.utils.utils import get_safe_torch_device
from lerobot.configs.train import TrainPipelineConfig
from lerobot.common.datasets.factory import make_dataset

# === Load YAML manually ===
with open("configs/train/act_so100_test.yaml", "r") as f:
    cfg_dict = yaml.safe_load(f)

cfg = TrainPipelineConfig.from_dict(cfg_dict)

# === Set paths ===
checkpoint_path = Path("outputs/train/act_so100_test/checkpoints/last/model.pt")
save_path = Path("outputs/train/act_so100_test/final_policy")

# === Build dataset to get meta ===
dataset = make_dataset(cfg)

# === Build policy ===
device = get_safe_torch_device(cfg.policy.device)
policy = make_policy(cfg.policy, ds_meta=dataset.meta)
policy = policy.to(device)

# === Load checkpoint ===
print(f"Loading checkpoint from {checkpoint_path}")
ckpt = torch.load(checkpoint_path, map_location=device)
policy.load_state_dict(ckpt["model"])

# === Save HuggingFace-style policy ===
print(f"Saving pretrained policy to {save_path}")
policy.save_pretrained_policy(save_path, meta=dataset.meta)
print("✅ Policy exported successfully!")
