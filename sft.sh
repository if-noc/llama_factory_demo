# device * batch_size * grad_accu_step = 64
CUDA_VISIBLE_DEVICES=0,1,2,3 accelerate launch src/train_bash.py \
    --stage sft \
    --model_name_or_path /mnt/huoyifu/LLaMA-Efficient-Tuning/models/llama-3b \
    --do_train \
    --dataset_dir data \
    --dataset tldr_train \
    --template default \
    --finetuning_type full \
    --output_dir checkpoints/llama-3b \
    --overwrite_output_dir \
    --overwrite_cache \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 16 \
    --lr_scheduler_type cosine \
    --logging_steps 10 \
    --save_steps 1000 \
    --learning_rate 5e-5 \
    --num_train_epochs 3.0 \
    --plot_loss \
    --fp16 