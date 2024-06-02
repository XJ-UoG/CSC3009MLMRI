# CSC3009MLMRI
CSC3009 Group Project

1. Install Miniconda
https://docs.anaconda.com/free/miniconda/#quick-command-line-install

2. Create conda environment for Python 3.9
```
conda create --name pytorchenv python=3.9
conda activate pytorchenv
```
3. Install Dependencies
```
conda install ipykernel matplotlib seaborn
```
Install PyTorch 2.30


Mac
```
conda install pytorch::pytorch torchvision torchaudio -c pytorch
```
Windows
```
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```
4. Test Pytorch installation
```
python test_pytorch.py
```
5. Using a Conda Environment in Jupyter Notebook
```
python -m ipykernel install --user --name=pytorchenv
```
