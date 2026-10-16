# 🎨 StudioAI: Stable Diffusion Image Generation & Editing Studio

StudioAI is an AI image generator website that allows users to create custom image using prompts and negative prompts. Users also can fine tune the image by edit some parameters such as quality steps and CFG scale to set AI creativity limits. Furthermore the website also enables users to modify uploaded photos using inpainting and outpainting features.
---

## 🚀 Key Features

### 1. ✨ Text-to-Image Generation
- **Prompt Engineering**: Support for descriptive positive prompts and negative prompts to guide image synthesis and eliminate artifacts.
- **Configurable Parameters**:
  - **Inference Steps**: Fine-tune quality vs. generation speed (15–50 steps).
  - **Guidance Scale (CFG)**: Control adherence to prompt vs. creative liberty (1.0–20.0).
  - **Reproducibility**: Seed control for deterministic generation.
- **Batch Processing**: Generate single or multiple images (up to 4) per inference pass.
- **Dynamic Schedulers**: Seamlessly switch between popular diffusion samplers:
  - `Euler Ancestral (Euler A)`
  - `DPM++ (DPMSolverMultistepScheduler)`
  - `DDIM (DDIMScheduler)`

### 2. 🛠️ Interactive Image Editing
- **Interactive Inpainting (Object Editing)**:
  - Built-in drawing canvas (`streamlit-drawable-canvas`) allows users to mask specific areas directly on generated images.
  - Custom inpainting prompts and mask dilation/filtering for seamless blending using `runwayml/stable-diffusion-inpainting`.
  - Adjustable strength parameter to fine-tune how aggressively the masked region is modified.
- **Outpainting (Canvas Zoom-Out / Expansion)**:
  - Extends canvas dimensions symmetrically (e.g., +128px padding with 8-pixel alignment safety).
  - Employs blurred edge padding and binary masking for smooth contextual expansions.

### 3. ⚡ Performance & Resource Management
- **VRAM / RAM Flush**: One-click GPU cache cleanup (`torch.cuda.empty_cache()` and `gc.collect()`) to prevent Out-Of-Memory (OOM) errors during prolonged usage.
- **Half-Precision (FP16)**: Pipeline execution using `torch.float16` for optimal GPU memory footprint and faster inference.
- **Cloud Deployment Ready**: Integrated Ngrok tunneling for quick deployment from cloud notebook environments (e.g., Google Colab).

---

## 📂 Project Structure

```plaintext
BFGAI_Fakhira-Lahen-Siregar/
│
├── Streamlit_submission_BFGAI_Fakhira_Lahen_Siregar.ipynb  # Primary notebook (Logic, App, & Deployment)
├── Pipeline_submission_BFGAI_Fakhira_Lahen_Siregar (5).ipynb # Pipeline experimentation & evaluation
├── requirements.txt                                        # Python dependencies
├── video_demo_aplikasi_BFGAI.mp4                           # Application walkthrough demo video
└── README.md                                               # Documentation
```

---

## 🛠️ Tech Stack & Dependencies

- **Programming Language**: Python 3.10+
- **Deep Learning Framework**: PyTorch with CUDA acceleration
- **Generative AI Libraries**: Hugging Face `diffusers`, `transformers`, `accelerate`, `safetensors`
- **Foundation Models**:
  - Text-to-Image: [`runwayml/stable-diffusion-v1-5`](https://huggingface.co/runwayml/stable-diffusion-v1-5)
  - Inpainting: [`runwayml/stable-diffusion-inpainting`](https://huggingface.co/runwayml/stable-diffusion-inpainting)
- **Web Interface**: Streamlit, `streamlit-drawable-canvas`
- **Image Processing**: Pillow (`PIL`), NumPy
- **Tunneling**: `pyngrok`

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- An NVIDIA GPU with CUDA support (recommended: minimum 8GB VRAM for Stable Diffusion v1.5)

### 1. Clone or Open the Workspace
```bash
git clone <repository-url>
cd BFGAI_Fakhira-Lahen-Siregar
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🖥️ Running the Application

### Option A: Local Execution
If you have written out `logic.py` and `app.py` from the notebook:
```bash
streamlit run app.py
```
Open your browser and navigate to `http://localhost:8501`.

### Option B: Google Colab / Cloud Deployment via Ngrok
1. Open [`Streamlit_submission_BFGAI_Fakhira_Lahen_Siregar.ipynb`](Streamlit_submission_BFGAI_Fakhira_Lahen_Siregar.ipynb) in Google Colab (ensure runtime type is set to **GPU**).
2. Run the dependency installation cells.
3. Run the cells generating `logic.py` and `app.py`.
4. Enter your Ngrok authtoken in the deployment cell:
   ```python
   auth_token = "YOUR_NGROK_AUTHTOKEN"
   ngrok.set_auth_token(auth_token)
   subprocess.Popen(["streamlit", "run", "app.py"])
   public_url = ngrok.connect(8501).public_url
   print(public_url)
   ```
5. Click on the printed public URL to access the live Streamlit dashboard.

---

## ⚙️ Parameters Reference

| Parameter | Type | Default | Description |
| :--- | :---: | :---: | :--- |
| **Prompt** | Text | `"a cute robot in a futuristic city..."` | Blueprint description of the desired image. |
| **Negative Prompt** | Text | `"blurry, bad anatomy, worst quality"` | Negative cues to suppress unwanted traits and visual degradation. |
| **Quality Steps** | Slider | `30` | Number of denoising iterations (higher = sharper detail, longer runtime). |
| **Creativity (CFG)** | Slider | `7.5` | Classifier-Free Guidance scale for prompt fidelity. |
| **Seed** | Integer | `42` | Pseudorandom generator seed for deterministic image generation. |
| **Scheduler** | Select | `Euler A` | Denoising algorithm: `Euler A`, `DPM++`, or `DDIM`. |
| **Batch Size** | Slider | `1` | Number of simultaneous output images generated per pass (1–4). |
| **Inpainting Strength** | Slider | `0.85` | Modification strength applied over masked canvas areas. |

---

## 📹 Video Demo

A full demonstration walkthrough of the application is available in the repository root:
- [`video_demo_aplikasi_BFGAI.mp4`](video_demo_aplikasi_BFGAI.mp4)

---

## 👩‍💻 Author

**Fakhira Lahen Siregar**  
*Project Submission for BFGAI (Binar x Foundation Generative AI)*
