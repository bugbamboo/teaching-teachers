from datasets import Dataset
from trl import SFTConfig, SFTTrainer
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import json

os.environ["WANDB_PROJECT"] = "chess-sft"


# Save DeepSpeed config to a f
ds = Dataset.load_from_disk("toetactic_train_dataset")

model = AutoModelForCausalLM.from_pretrained(
"Qwen/Qwen2.5-0.5B",
torch_dtype=torch.bfloat16   # load using bf16 weights
)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B")
tokenizer.padding_side = 'right'
config = SFTConfig(
    output_dir="output/qwen2.5-0.5B",
    run_name="Qwen2.5-0.5B-SFT",
    learning_rate=1e-4,
    adam_beta1=0.9,
    adam_beta2=0.99,
    weight_decay=0.1,
    warmup_ratio=0.1,
    lr_scheduler_type='cosine',
    bf16=True,
    per_device_train_batch_size=4,
    num_train_epochs=3,
    max_grad_norm=0.1,
    report_to="wandb",
    max_seq_length=1024,
    log_on_each_node=False,
    logging_strategy="steps",
    logging_steps=1,
    save_strategy="steps",
    save_total_limit=1,
    save_steps=120,
    # DeepSpeed configuration
    deepspeed="ds_config.json",
)

trainer = SFTTrainer(
    model=model,
    processing_class=tokenizer,
    args=config,
    train_dataset=ds
)

trainer.train()
