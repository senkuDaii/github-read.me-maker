# 🚀 GitHub Profile README Generator

A modern, user-friendly Streamlit web application that helps you create beautiful and professional GitHub profile README.md files in seconds.

![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-red?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- 📝 **Easy Input Form** - Sidebar form to enter all your profile information
- 🖼️ **Profile Image Support** - Add profile image via URL or upload
- 🎨 **11 Beautiful Themes** - Choose from multiple color themes for GitHub stats cards
- 🛡️ **Skill Badges** - Automatic generation of shields.io badges for your skills
- 📊 **GitHub Stats** - Includes GitHub stats, top languages, streak stats
- 📸 **Project Screenshots** - Add up to 3 project screenshots
- 🔗 **Social Links** - Twitter/X, LinkedIn, Instagram, YouTube, Facebook, Discord, Website, GitHub
- 👁️ **Live Preview** - See how your README will look before downloading
- 📥 **Download** - Download your README.md file directly
- 📋 **Copy to Clipboard** - Copy generated markdown to clipboard

## 📁 Project Structure

```
github-readme-generator/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── assets/                # Assets folder for images (optional)
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download this repository:**

```bash
git clone https://github.com/yourusername/github-readme-generator.git
cd github-readme-generator
```

2. **Create a virtual environment (recommended):**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install the required dependencies:**

```bash
pip install -r requirements.txt
```

### Running the App Locally

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## 📖 How to Use

### 1. Fill in Your Information

Open the app and fill in the sidebar form with your details:

**Basic Info:**
- Full Name (default: `senkudai`)
- GitHub username
- Bio / About Me

**Profile Images:**
- Profile Image (URL or Upload)
- Profile Banner URL

**Skills:**
- Comma-separated list of technical skills

**Social Links:**
- Twitter/X, LinkedIn, Instagram
- YouTube, Facebook, Discord
- Website, GitHub

**Project Screenshots:**
- Up to 3 screenshot URLs

**Display Options:**
- Choose from 11 themes
- Toggle Top Languages and Streak Stats

**Extra:**
- Fun Fact about yourself

### 2. Generate Your README

Click the **"✨ Generate README"** button to create your README.

### 3. Preview and Download

- View the **Rendered Preview** tab to see how it will look
- View the **Markdown Code** tab to see the raw markdown
- Click **"📥 Download README.md"** to save the file
- Or click **"📋 Copy to Clipboard"** to copy the markdown

### 4. Add to Your GitHub Profile

1. Create a new repository on GitHub
2. Name it **exactly** as your GitHub username (e.g., `johndoe/johndoe`)
3. Make it **public**
4. Initialize it with a README
5. Edit the README.md file and paste your generated content
6. Commit the changes
7. Visit `github.com/yourusername` to see your new profile!

## 🎨 Available Themes

Choose from 11 beautiful themes for your GitHub stats cards:

| Theme | Preview |
|-------|---------|
| `default` | Classic GitHub style |
| `dark` | Dark mode friendly |
| `radical` | Vibrant purple/pink |
| `merko` | Bold green/red |
| `gruvbox` | Warm retro colors |
| `tokyonight` | Modern blue/purple |
| `onedark` | Atom One Dark style |
| `cobalt` | Deep blue tones |
| `synthwave` | Neon retro |
| `highcontrast` | Black & white |
| `dracula` | Purple & cyan |

## 🛠️ Supported Skills

The app supports 80+ skills with automatic badge generation including:

**Languages:** Python, JavaScript, TypeScript, Java, Go, Rust, C++, C#, PHP, Ruby, Swift, Kotlin, Dart, HTML, CSS

**Frameworks & Libraries:** React, Vue, Angular, Svelte, Next.js, Nuxt.js, Express, FastAPI, Django, Flask, Spring, Laravel, Rails, TensorFlow, PyTorch, Pandas, NumPy

**Tools & Platforms:** Docker, Kubernetes, AWS, Azure, GCP, MongoDB, PostgreSQL, MySQL, Redis, Git, GitHub, GitLab, Jenkins, Terraform, Ansible, Nginx, Linux

**Design:** Figma, Sketch, Adobe Photoshop, Illustrator, XD, Premiere, After Effects

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [GitHub Readme Stats](https://github.com/anuraghazra/github-readme-stats) - GitHub stats cards
- [GitHub Readme Streak Stats](https://github.com/DenverCoder1/github-readme-streak-stats) - Streak stats
- [Shields.io](https://shields.io) - Skill badges
- [Streamlit](https://streamlit.io) - Web app framework

## 📧 Support

If you found this project helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting new features

---

Made with ❤️ using [Streamlit](https://streamlit.io)
