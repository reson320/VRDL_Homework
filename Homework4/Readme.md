
# NYCU 2025 Spring - Selected Topics in Visual Recognition using Deep Learning Homework 4

studdent id:110652032

name:許元瑞

## Introduction

This repository contains a **Restormer-based image restoration model** for dual-weather degradation removal, specifically designed to handle both **rain and snow** artifacts in a single unified model. The implementation is based on the efficient transformer architecture from Restormer with enhanced training strategies including early stopping, warmup learning rate scheduling, and robust gradient management.

### Key Features

- **Dual-Weather Restoration**: Single model handles both rain and snow degradation removal
- **Transformer Architecture**: Based on Restormer with Multi-Dconv Head Transposed Attention (MDTA) and Gated-Dconv Feed-Forward Network (GDFN)
- **Advanced Training**: Early stopping with patience mechanism, warmup + cosine annealing learning rate schedule
- **Memory Efficient**: Optimized for A100 GPU with gradient clipping and memory management
- **Comprehensive Evaluation**: PSNR-based validation with detailed training visualization

### Model Architecture

- **Encoder-Decoder Structure**: 4-level hierarchical architecture with skip connections
- **Transformer Blocks**: [4,6,6,8] blocks across different scales
- **Attention Mechanism**: Multi-head attention with [1,2,4,8] heads
- **Parameters**: ~26M parameters (dim=48) for enhanced capacity
- **Loss Function**: Charbonnier Loss (ε=1e-3) for robust gradient properties

### Dataset

- **Training Images**: 3,200 total (1,600 rain + 1,600 snow degraded images)
- **Test Images**: 100 images with unknown degradation types
- **Split**: 80% training / 20% validation
- **Format**: Input degraded images → Output clean images
- **Resolution**: Variable resolution support with random crop augmentation

## How to Install?

### Prerequisites(If you want to run on local)

- Python 3.8+
- CUDA-capable GPU (recommended: run on colab A100 or equivalent)
- 24GB+ GPU memory for optimal performance

### Installation Steps

1. **Install required packages**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install timm einops matplotlib pillow scikit-image tqdm numpy
```


### Dataset Setup

1. **Prepare dataset structure**

If you want to use colab, please mount drive to colab.

```
hw4_realse_dataset/
├── hw4_realse_dataset/
│   ├── train/
│   │   ├── degraded/          # Rain and snow degraded images
│   │   └── clean/             # Corresponding clean images
│   └── test/
│       └── degraded/          # Test images (unknown degradation)
```

2. **Naming convention**
- Degraded images: `rain-xxx.png`, `snow-xxx.png`
- Clean images: `rain_clean-xxx.png`, `snow_clean-xxx.png`

## How to Train?

### Quick Start

1. **Basic training with default settings**

Just run at colab: https://colab.research.google.com/drive/1hGbYA6GjhiQeduCKwgQzyW3UZva1vikR?usp=sharing

2. **Training with custom parameters**
```python
# Modify these parameters in the script
num_epochs = 30
batch_size = 4
base_lr = 3e-4
patience = 10  # Early stopping patience
dim = 48       # Model dimension (32 or 48)
```

### Training Configuration

| Parameter | Default Value | Description |
|-----------|---------------|-------------|
| `num_epochs` | 30 | Maximum training epochs |
| `batch_size` | 4 | Batch size for training |
| `base_lr` | 3e-4 | Base learning rate |
| `patience` | 10 | Early stopping patience |
| `dim` | 48 | Model channel dimension |
| `warmup_epochs` | 5 | Learning rate warmup epochs |

### Training Features

- **Early Stopping**: Automatically stops training when validation PSNR plateaus
- **Learning Rate Schedule**: Warmup + Cosine Annealing for stable convergence
- **Gradient Clipping**: Prevents gradient explosion (max_norm=1.0)
- **Memory Management**: Efficient GPU memory usage with cleanup
- **Resume Training**: Automatically resumes from existing checkpoints

### Monitoring Training

The training process provides comprehensive monitoring:

```
=== Epoch 15/30 ===
訓練 - Loss: 0.1089, PSNR: 15.87dB
驗證 - Loss: 0.1156, PSNR: 16.15dB
學習率: 0.000008 (Cosine Annealing 階段)
驗證指標改善！(目前最佳 PSNR: 16.15dB)
```

## How to Test/Inference?

### Load Existing Model

```python
# The script automatically detects and loads existing models
MODEL_PATH = 'best_restormer_model.pth'

# For inference only, use the model loading section
if os.path.exists(MODEL_PATH):
    checkpoint = torch.load(MODEL_PATH, map_location=device, weights_only=False)
    model.load_state_dict(checkpoint['model_state_dict'])
    print(f"Model loaded with PSNR: {checkpoint['best_psnr']:.2f}dB")
```

### Generate Predictions

The model automatically generates `pred.npz` file containing:
- **Format**: Dictionary with filename as key, restored image as value
- **Shape**: (3, H, W) uint8 arrays
- **Range**: 0-255 pixel values

### Visualization

The script provides automatic visualization of:
- Training/validation loss curves
- PSNR progression over epochs
- Learning rate schedule
- Sample restoration results
- Early stopping indicators

## Model Performance

### Codeforce leaderboard

![image](https://github.com/user-attachments/assets/1827f633-7db5-4af7-beb6-654dfd3825eb)


### Training Results

- **Best Validation PSNR**: ~26.38 dB (on codeforce)
- **Training Stability**: Robust convergence without gradient explosion
- **Memory Usage**: Optimized for A100 GPU (batch_size=4)
- **Training Time**: ~10 minutes per epoch on A100(google colab)

### Architecture Comparison

| Configuration | Parameters | Best PSNR |
|---------------|------------|-----------|
| dim=32 | ~12M | 25.59 dB |
| dim=48 | ~26M | 26.38 dB |
