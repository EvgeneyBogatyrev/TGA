![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)
![PyTorch 1.1](https://img.shields.io/badge/pytorch-1.1-yellow.svg)

# Video Super-resolution with Temporal Group Attention (TGA)

The *official* source code (partially cleaned) for the [Video Super-resolution with Temporal Group Attention] which is accepted by [CVPR-2020].

![framework](figs/TGA.PNG)

### Train
We utilize 8 Nvidia Tesla V100 GPUs for training.
```
python main.py
```

### Test
```
cd code
unzip TGA-without-align-dla.zip
```
We utilize 1 P100 GPU for testing.
Test the trained model with best performance by
```
python test.py
```
