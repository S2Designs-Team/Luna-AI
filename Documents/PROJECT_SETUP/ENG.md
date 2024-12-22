# Project Setup: Verification and Configuration of the Development Environment (Python, dependencies, etc.)
<UL>

## 1. Development Environment Verification:

<UL>
<LI>

### 1.1 Python Verification

Ensure that Python (min. 3.10) is correctly installed.
<UL>
<LI>

#### [Step 1] Open a terminal and check the installed Python version:
```console
python --version
```
Expected Result:

<UL> 
  <li>[SUCCESS] If the version is >= 3.10.</li>
  <li>[FAILURE] If the version is < 3.10.</li>
</UL>
[ON FAILURE]: Download and install the latest version [https://www.python.org/downloads/](https://www.python.org/downloads/)</LI>
<LI>

<LI>

#### [Step 2] Update or install pip
Ensure pip is up-to-date:
```console
python -m pip install --upgrade pip
```
</LI>
</UL> 
</LI>

<LI>

### 1.2 Installation and Configuration of virtualenv
<UL> 
<LI>

#### [Step 1.2.1] Install virtualenv if not already present:
```console
python -m pip install virtualenv
```
</LI>
<LI>

#### [Step 1.2.2] Create a virtual environment in the project directory:
```console
python -m virtualenv luna_env
```
</LI>
<LI>

#### [Step 1.2.3] Activate the virtual environment:
- Windows:
```console
.\luna_env\Scripts\activate
```
- Linux:
```console
source luna_env/bin/activate
```
</LI>
</UL> 
</LI>

<LI>

### 1.3 NVIDIA Drivers, CUDA, and cuDNN Verification
<UL> 
<LI>

#### [Step 1.3.1] Check if your GPU is recognized:
  ```console 
  nvidia-smi
  ```
Expected Result:
<UL> 
    <LI>[SUCCESS] The output displays the features of your NVIDIA GPU.</LI>
    <LI>[FAILURE] The output does NOT display the features of your NVIDIA GPU.</LI>
</UL>
[ON FAILURE]: If the GPU is not recognized, install the drivers from NVIDIA's official website. 
</LI>
<LI>

  #### [Step 1.3.2] Check the installed CUDA version:
  ```console
  nvcc --version
  ```
  Expected Result:
  <UL> 
    <LI>[SUCCESS] The output displays a message similar to the following:

```console    
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2024 NVIDIA Corporation
Built on Wed_Oct_30_01:18:48_Pacific_Daylight_Time_2024
Cuda compilation tools, release 12.6, V12.6.85
Build cuda_12.6.r12.6/compiler.35059454_0
```

  </LI>
  <LI>[FAILURE] The output displays an error message such as:

  ```console
  nvcc : Termine 'nvcc' non riconosciuto come nome di cmdlet, funzione, programma eseguibile o file script. Controllare
  l'ortografia del nome o verificare che il percorso sia incluso e corretto, quindi riprovare.                         
  In riga:1 car:1                                                                                                      
  + nvcc --version                                                                                                     
  + ~~~~                                                                                                               
              + CategoryInfo          : ObjectNotFound: (nvcc:String) [], CommandNotFoundException                             
              + FullyQualifiedErrorId : CommandNotFoundException}$$
  ```
  </LI>
  </UL>
  [ON FAILURE]: The error indicates that the nvcc command is not recognized, possibly because:
  <UL> 
    <LI>CUDA is not installed on your system.</LI>
    <LI>CUDA is installed but not in the system PATH, so the terminal cannot locate the nvcc command.</LI>
  </UL>

  [SOLUTION] Steps to resolve the issue:
  <UL> 
  <LI> 
  
  #### [Step 1.3.2.1] Check if CUDA is installed
  Verify the presence of the CUDA directory on your system:
  <UL> 
    <LI> Windows: </LI>
  Look for the folder C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA. The version of CUDA is usually indicated in the subfolder name, such as v12.0.
    <LI> Linux: </LI>
  Check if a directory like /usr/local/cuda exists.
  </UL> 
  </LI>

  <LI>
  
  #### [Step 1.3.2.2] Install CUDA if necessary
  If CUDA is not found on your system:
  <UL> 
    <LI>ScDownload the CUDA installer compatible with your GPU and operating system from NVIDIA's official CUDA Toolkit website: <A href:"https://developer.nvidia.com/cuda-toolkit">https://developer.nvidia.com/cuda-toolkit</A>.</LI>
    During installation, ensure you check the option to add CUDA binaries to the PATH.
  </UL>
  </LI>

  <LI>

  #### [Step 1.3.2.3] Add CUDA to the PATH (if already installed)
  If CUDA is installed but the nvcc command does not work, the binary paths are likely not configured correctly in your system.
  <UL> 
  To add CUDA to PATH on Windows:
    <LI>Open Control Panel > System > Advanced System Settings > Environment Variables.</LI>
    <LI>In the System Variables section, locate the Path variable and select Edit.</LI>
    <LI>Add the following paths (adjust version numbers as needed):</LI>

```console
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.0\bin
```
```console
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.0\libnvvp
```
  </UL>
  <BR>
  <UL> 
  To add CUDA to PATH on Linux: 
  <LI>Open a terminal and edit the .bashrc file (or .zshrc if using Zsh):

```console
nano ~/.bashrc
```
  </LI>
  <LI>Add the following lines at the end of the file (adjust the path to your CUDA version):

```console
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
```
  <LI>Save the changes and update the configuration:

```console
source ~/.bashrc
```
  </LI>
  </LI>
  </UL> 
  <LI>

  #### [Step 1.3.2.4] Save and close everything.
  Restart the terminal and verify again with:

```console
nvcc --version
```
  </LI>

  * The version must be compatible with PyTorch or TensorFlow, which we will use.
</LI>
</UL> 

<LI>

  #### [Step 1.3.3] Install cuDNN:
      - Download and install the version of cuDNN corresponding to your CUDA version from NVIDIA's website (https://developer.nvidia.com/cudnn)
</LI>
<LI>

  #### [Step 1.3.4] Configure CUDA/cuDNN:
      - Add the binary paths for CUDA/cuDNN to your PATH (if not already done).
</LI>
</UL> 


#   2. Dependency Setup:

##      2.1 Creating the requirements.txt File:
  Create a requirements.txt file in the project directory with the following content:
  ```console
  torch
  transformers
  datasets
  whisper
  pyttsx3
  ```
  If you prefer an advanced TTS framework, replace pyttsx3 with 'TTS' (https://github.com/coqui-ai/TTS):

##      2.2 Installing the Dependencies
  After activating the virtual environment (SEE STEP 1.2.c), execute:
  ```console
  pip install -r requirements.txt
  ```
</UL> 