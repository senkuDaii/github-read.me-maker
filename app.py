"""
GitHub Profile README Generator

A Streamlit web application to generate professional GitHub profile README.md files.
This app provides an easy-to-use interface for creating beautiful GitHub profiles
with customizable sections including skills badges, GitHub stats, and social links.

Author: Assistant
"""

import streamlit as st
import pyperclip
import base64


# =============================================================================
# CONFIGURATION
# =============================================================================

# Available themes for GitHub stats cards
GITHUB_STATS_THEMES = [
    "default", "dark", "radical", "merko", "gruvbox", "tokyonight",
    "onedark", "cobalt", "synthwave", "highcontrast", "dracula"
]

# Skill badge color mapping for shields.io
SKILL_BADGE_COLORS = {
    "python": "3776AB",
    "javascript": "F7DF1E",
    "typescript": "3178C6",
    "react": "61DAFB",
    "node.js": "339933",
    "nodejs": "339933",
    "html": "E34F26",
    "css": "1572B6",
    "java": "007396",
    "go": "00ADD8",
    "rust": "000000",
    "c++": "00599C",
    "cpp": "00599C",
    "c#": "239120",
    "csharp": "239120",
    "php": "777BB4",
    "ruby": "CC342D",
    "swift": "FA7343",
    "kotlin": "7F52FF",
    "dart": "0175C2",
    "flutter": "02569B",
    "docker": "2496ED",
    "kubernetes": "326CE5",
    "aws": "232F3E",
    "azure": "0078D4",
    "gcp": "4285F4",
    "mongodb": "47A248",
    "postgresql": "336791",
    "mysql": "4479A1",
    "redis": "DC382D",
    "git": "F05032",
    "github": "181717",
    "gitlab": "FC6D26",
    "jenkins": "D24939",
    "terraform": "7B42BC",
    "ansible": "EE0000",
    "nginx": "269539",
    "apache": "D22128",
    "linux": "FCC624",
    "ubuntu": "E95420",
    "centos": "262577",
    "fedora": "294172",
    "arch": "1793D1",
    "windows": "0078D6",
    "macos": "000000",
    "ios": "000000",
    "android": "3DDC84",
    "react native": "61DAFB",
    "vue": "4FC08D",
    "angular": "DD0031",
    "svelte": "FF3E00",
    "next.js": "000000",
    "nextjs": "000000",
    "nuxt.js": "00C58E",
    "nuxtjs": "00C58E",
    "express": "000000",
    "fastapi": "009688",
    "django": "092E20",
    "flask": "000000",
    "spring": "6DB33F",
    "spring boot": "6DB33F",
    "laravel": "FF2D20",
    "rails": "CC0000",
    "tensorflow": "FF6F00",
    "pytorch": "EE4C2C",
    "pandas": "150458",
    "numpy": "013243",
    "scikit-learn": "F7931E",
    "opencv": "5C3EE8",
    "figma": "F24E1E",
    "sketch": "F7B500",
    "adobe": "FF0000",
    "photoshop": "31A8FF",
    "illustrator": "FF9A00",
    "xd": "FF61F6",
    "premiere": "9999FF",
    "after effects": "9999FF",
}


def get_social_icon_link(platform, username, url=None):
    """
    Generate HTML for social media icon links.
    
    Args:
        platform (str): Social media platform name
        username (str): Username on the platform
        url (str, optional): Full URL if different from pattern
        
    Returns:
        str: HTML anchor tag with icon image
    """
    icons = {
        "twitter": "https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg",
        "linkedin": "https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg",
        "github": "https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg",
        "website": "https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/web.svg",
        "instagram": "https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg",
        "youtube": "https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg",
        "facebook": "https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg",
        "discord": "https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/discord.svg",
    }
    
    if not url:
        if platform == "twitter":
            url = f"https://twitter.com/{username}"
        elif platform == "linkedin":
            url = f"https://linkedin.com/in/{username}"
        elif platform == "github":
            url = f"https://github.com/{username}"
        elif platform == "instagram":
            url = f"https://instagram.com/{username}"
        elif platform == "youtube":
            url = f"https://youtube.com/@{username}"
        elif platform == "facebook":
            url = f"https://facebook.com/{username}"
        elif platform == "discord":
            url = f"https://discord.com/users/{username}"
    
    icon_url = icons.get(platform, icons["website"])
    return f'<a href="{url}" target="blank"><img align="center" src="{icon_url}" alt="{username}" height="30" width="40" /></a>'


def get_skill_badge(skill):
    """
    Generate a shields.io badge URL for a given skill.
    
    Args:
        skill (str): The skill name
        
    Returns:
        str: Markdown formatted badge image with link
    """
    skill_lower = skill.strip().lower()
    color = SKILL_BADGE_COLORS.get(skill_lower, "666666")
    encoded_skill = skill.strip().replace(" ", "%20")
    
    # Map common skills to their simple-icons logo names
    logo_mapping = {
        "python": "python",
        "javascript": "javascript",
        "typescript": "typescript",
        "react": "react",
        "node.js": "nodedotjs",
        "nodejs": "nodedotjs",
        "html": "html5",
        "css": "css3",
        "java": "openjdk",
        "go": "go",
        "rust": "rust",
        "c++": "cplusplus",
        "cpp": "cplusplus",
        "c#": "csharp",
        "csharp": "csharp",
        "php": "php",
        "ruby": "ruby",
        "swift": "swift",
        "kotlin": "kotlin",
        "dart": "dart",
        "flutter": "flutter",
        "docker": "docker",
        "kubernetes": "kubernetes",
        "aws": "amazonaws",
        "azure": "microsoftazure",
        "gcp": "googlecloud",
        "mongodb": "mongodb",
        "postgresql": "postgresql",
        "mysql": "mysql",
        "redis": "redis",
        "git": "git",
        "github": "github",
        "gitlab": "gitlab",
        "jenkins": "jenkins",
        "terraform": "terraform",
        "ansible": "ansible",
        "nginx": "nginx",
        "apache": "apache",
        "linux": "linux",
        "ubuntu": "ubuntu",
        "react native": "react",
        "vue": "vuedotjs",
        "angular": "angular",
        "svelte": "svelte",
        "next.js": "nextdotjs",
        "nextjs": "nextdotjs",
        "nuxt.js": "nuxtdotjs",
        "nuxtjs": "nuxtdotjs",
        "express": "express",
        "fastapi": "fastapi",
        "django": "django",
        "flask": "flask",
        "spring": "spring",
        "spring boot": "springboot",
        "laravel": "laravel",
        "rails": "rubyonrails",
        "tensorflow": "tensorflow",
        "pytorch": "pytorch",
        "pandas": "pandas",
        "numpy": "numpy",
        "figma": "figma",
        "photoshop": "adobephotoshop",
        "illustrator": "adobeillustrator",
        "xd": "adobexd",
        "premiere": "adobepremierepro",
    }
    
    logo = logo_mapping.get(skill_lower)
    if logo:
        badge_url = f"https://img.shields.io/badge/-{encoded_skill}-{color}?style=flat-square&logo={logo}&logoColor=white"
    else:
        badge_url = f"https://img.shields.io/badge/-{encoded_skill}-{color}?style=flat-square"
    
    return f"![{skill.strip()}]({badge_url})"


def generate_readme(data):
    """
    Generate README.md content based on user input.
    
    Args:
        data (dict): Dictionary containing all user input fields
        
    Returns:
        str: Complete README.md content as a string
    """
    readme_parts = []

    # -------------------------------------------------------------------------
    # Profile Banner Section
    # -------------------------------------------------------------------------
    if data.get('banner_url'):
        readme_parts.append(f"![Profile Banner]({data['banner_url']})")
        readme_parts.append("")

    # -------------------------------------------------------------------------
    # Header / Greeting Section
    # -------------------------------------------------------------------------
    readme_parts.append(f"<h1 align=\"center\">Hi 👋, I'm {data['name']}</h1>")
    readme_parts.append("")

    # -------------------------------------------------------------------------
    # Profile Image Section - Centered
    # -------------------------------------------------------------------------
    if data.get('profile_image_url'):
        readme_parts.append('<p align="center">')
        readme_parts.append(f'  <img src="{data["profile_image_url"]}" alt="Profile Image" width="200" height="200" style="border-radius: 50%; object-fit: cover;" />')
        readme_parts.append('</p>')
        readme_parts.append("")

    # -------------------------------------------------------------------------
    # Bio Section
    # -------------------------------------------------------------------------
    if data.get('bio'):
        readme_parts.append(f"<p align=\"left\">{data['bio']}</p>")
        readme_parts.append("")

    # -------------------------------------------------------------------------
    # GitHub Stats Badges
    # -------------------------------------------------------------------------
    if data.get('github_username'):
        readme_parts.append("<p align=\"left\">")
        readme_parts.append(f'  <img src="https://komarev.com/ghpvc/?username={data["github_username"]}&label=Profile%20views&color=0e75b6&style=flat" alt="{data["github_username"]}" />')
        readme_parts.append("</p>")
        readme_parts.append("")
        
        readme_parts.append(f"[![GitHub followers](https://img.shields.io/github/followers/{data['github_username']}?style=social)](https://github.com/{data['github_username']})")
        readme_parts.append(f"[![GitHub stars](https://img.shields.io/github/stars/{data['github_username']}?style=social)](https://github.com/{data['github_username']})")
        readme_parts.append("")

    # -------------------------------------------------------------------------
    # Skills Section with Badges
    # -------------------------------------------------------------------------
    if data.get('skills'):
        readme_parts.append("## 🚀 Skills")
        readme_parts.append("")
        readme_parts.append("<p align=\"left\">")
        
        skills_list = [skill.strip() for skill in data['skills'].split(',') if skill.strip()]
        for skill in skills_list:
            badge = get_skill_badge(skill)
            readme_parts.append(f"  {badge}")
        
        readme_parts.append("</p>")
        readme_parts.append("")

    # -------------------------------------------------------------------------
    # GitHub Stats Cards Section
    # -------------------------------------------------------------------------
    if data.get('github_username'):
        theme = data.get('theme', 'radical')
        
        readme_parts.append("## 📊 GitHub Stats")
        readme_parts.append("")
        readme_parts.append(f'<p align="center">')
        readme_parts.append(f'  <img src="https://github-readme-stats.vercel.app/api?username={data["github_username"]}&show_icons=true&locale=en&theme={theme}" alt="{data["github_username"]}" />')
        readme_parts.append(f'</p>')
        readme_parts.append("")

    # -------------------------------------------------------------------------
    # Top Languages Section
    # -------------------------------------------------------------------------
    if data.get('github_username') and data.get('show_languages', True):
        theme = data.get('theme', 'radical')
        readme_parts.append("## 💻 Top Languages")
        readme_parts.append("")
        readme_parts.append(f'<p align="center">')
        readme_parts.append(f'  <img src="https://github-readme-stats.vercel.app/api/top-langs?username={data["github_username"]}&show_icons=true&locale=en&layout=compact&theme={theme}" alt="{data["github_username"]}" />')
        readme_parts.append(f'</p>')
        readme_parts.append("")

    # -------------------------------------------------------------------------
    # GitHub Streak Stats
    # -------------------------------------------------------------------------
    if data.get('github_username') and data.get('show_streak', True):
        theme = data.get('theme', 'radical')
        readme_parts.append("## 🔥 GitHub Streak")
        readme_parts.append("")
        readme_parts.append(f'<p align="center">')
        readme_parts.append(f'  <img src="https://github-readme-streak-stats.herokuapp.com/?user={data["github_username"]}&theme={theme}" alt="{data["github_username"]}" />')
        readme_parts.append(f'</p>')
        readme_parts.append("")

    # -------------------------------------------------------------------------
    # Fun Fact Section
    # -------------------------------------------------------------------------
    if data.get('fun_fact'):
        readme_parts.append("## ⚡ Fun Fact")
        readme_parts.append("")
        readme_parts.append(f"> *{data['fun_fact']}*")
        readme_parts.append("")

    # -------------------------------------------------------------------------
    # Connect With Me Section
    # -------------------------------------------------------------------------
    social_links = []
    
    if data.get('twitter'):
        social_links.append(get_social_icon_link('twitter', data['twitter']))
    if data.get('linkedin'):
        social_links.append(get_social_icon_link('linkedin', data['linkedin']))
    if data.get('instagram'):
        social_links.append(get_social_icon_link('instagram', data['instagram']))
    if data.get('youtube'):
        social_links.append(get_social_icon_link('youtube', data['youtube']))
    if data.get('facebook'):
        social_links.append(get_social_icon_link('facebook', data['facebook']))
    if data.get('discord'):
        social_links.append(get_social_icon_link('discord', data['discord']))
    if data.get('website'):
        social_links.append(get_social_icon_link('website', 'Website', data['website']))
    if data.get('github_username'):
        social_links.append(get_social_icon_link('github', data['github_username']))

    if social_links:
        readme_parts.append("## 🌐 Connect With Me")
        readme_parts.append("")
        readme_parts.append("<p align=\"left\">")
        readme_parts.extend(social_links)
        readme_parts.append("</p>")
        readme_parts.append("")

    # -------------------------------------------------------------------------
    # Footer Section
    # -------------------------------------------------------------------------
    readme_parts.append("---")
    readme_parts.append("")
    readme_parts.append(f"<p align=\"center\">⭐️ From [{data['github_username'] or data['name']}](https://github.com/{data.get('github_username', '')})</p>")

    return "\n".join(readme_parts)


def render_streamlit_preview(data):
    """
    Render a visual preview of the README using Streamlit components.
    This shows actual images and proper layout in the app.
    
    Args:
        data (dict): Dictionary containing all user input fields
    """
    # Header
    st.markdown(f"<h1 style='text-align: center;'>Hi 👋, I'm {data.get('name', 'Your Name')}</h1>", unsafe_allow_html=True)
    
    # Profile Image - Perfectly centered with HTML
    if data.get('profile_image_url'):
        st.markdown("<div align='center'>", unsafe_allow_html=True)
        st.image(data['profile_image_url'], width=200)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Bio - Left aligned
    if data.get('bio'):
        st.markdown(f"<p style='text-align: left;'>{data['bio']}</p>", unsafe_allow_html=True)
    
    # GitHub Stats Badges - Profile views only
    if data.get('github_username'):
        st.markdown(f"![Profile Views](https://komarev.com/ghpvc/?username={data['github_username']}&label=Profile%20views&color=0e75b6&style=flat)")
        st.markdown("<br>", unsafe_allow_html=True)
    
    # Skills - Show as markdown badges
    if data.get('skills'):
        st.markdown("## 🚀 Skills")
        skills_list = [skill.strip() for skill in data['skills'].split(',') if skill.strip()]
        if skills_list:
            # Create badge markdown for all skills
            badges_md = " ".join([f"![{skill}](https://img.shields.io/badge/{skill.replace(' ', '_')}-3776AB?style=for-the-badge&logo={skill.lower().replace(' ', '').replace('.', '')}&logoColor=white)" for skill in skills_list])
            st.markdown(badges_md, unsafe_allow_html=True)
    
    # GitHub Stats
    if data.get('github_username'):
        theme = data.get('theme', 'radical')
        st.markdown("## 📊 GitHub Stats")
        st.image(f"https://github-readme-stats.vercel.app/api?username={data['github_username']}&show_icons=true&locale=en&theme={theme}")
        
        if data.get('show_languages', True):
            st.markdown("## 💻 Top Languages")
            st.image(f"https://github-readme-stats.vercel.app/api/top-langs?username={data['github_username']}&show_icons=true&locale=en&layout=compact&theme={theme}")
        
        if data.get('show_streak', True):
            st.markdown("## 🔥 GitHub Streak")
            st.image(f"https://github-readme-streak-stats.herokuapp.com/?user={data['github_username']}&theme={theme}")
    
    # Fun Fact
    if data.get('fun_fact'):
        st.markdown("## ⚡ Fun Fact")
        st.info(data['fun_fact'])
    
    # Social Links
    social_links = []
    if data.get('twitter'):
        social_links.append("Twitter")
    if data.get('linkedin'):
        social_links.append("LinkedIn")
    if data.get('instagram'):
        social_links.append("Instagram")
    if data.get('youtube'):
        social_links.append("YouTube")
    if data.get('facebook'):
        social_links.append("Facebook")
    if data.get('discord'):
        social_links.append("Discord")
    if data.get('website'):
        social_links.append("Website")
    if data.get('github_username'):
        social_links.append("GitHub")
    
    if social_links:
        st.markdown("## 🌐 Connect With Me")
        st.write(" | ".join(social_links))


def copy_to_clipboard(text):
    """
    Copy the generated README content to the system clipboard.
    
    Args:
        text (str): The README content to copy
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        pyperclip.copy(text)
        return True
    except Exception as e:
        return False


def main():
    """
    Main function to run the Streamlit application.
    Sets up the page configuration, sidebar inputs, and main content area.
    """
    # =============================================================================
    # Page Configuration
    # =============================================================================
    st.set_page_config(
        page_title="GitHub Profile README Generator",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # =============================================================================
    # Custom CSS Styling
    # =============================================================================
    st.markdown("""
    <style>
    /* Main Header Styling */
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    /* Sub Header Styling */
    .sub-header {
        font-size: 1.2rem;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .section-header {
        font-size: 1.1rem;
        font-weight: 600;
        color: #667eea;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    /* Sidebar Header */
    .sidebar-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #667eea;
    }
    
    /* Button Styling */
    .stButton>button {
        background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        padding: 0.75rem 2rem;
        border-radius: 8px;
        border: none;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    /* Download Button */
    .stDownloadButton>button {
        background: linear-gradient(45deg, #11998e 0%, #38ef7d 100%);
        color: white;
        font-weight: 600;
        border-radius: 8px;
        border: none;
    }
    
    /* Preview Box Styling */
    .preview-box {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 12px;
        padding: 1.5rem;
        font-family: 'Courier New', monospace;
        white-space: pre-wrap;
        overflow-x: auto;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    /* Info Box */
    .info-box {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    /* Success Message */
    .success-message {
        background-color: #e8f5e9;
        border-left: 4px solid #4caf50;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # =============================================================================
    # Main Content Area - Header
    # =============================================================================
    st.markdown('<p class="main-header">🚀 GitHub Profile README Generator</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Create a stunning GitHub profile README in seconds</p>', unsafe_allow_html=True)

    # =============================================================================
    # Sidebar - Input Form
    # =============================================================================
    with st.sidebar:
        st.markdown('<p class="sidebar-header">📝 Your Information</p>', unsafe_allow_html=True)
        
        # Profile Image Upload - Outside form for immediate drag-drop
        with st.expander("🖼️ Profile Image Upload (Drag & Drop)", expanded=False):
            st.markdown("**Upload your profile picture:**")
            uploaded_file = st.file_uploader(
                "Drag and drop image here or click to browse",
                type=['png', 'jpg', 'jpeg'],
                key="profile_uploader",
                help="Supported formats: PNG, JPG, JPEG"
            )
            if uploaded_file:
                st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
                st.image(uploaded_file, width=150, caption="Preview")
                st.markdown('</div>', unsafe_allow_html=True)
                bytes_data = uploaded_file.getvalue()
                base64_image = base64.b64encode(bytes_data).decode()
                st.session_state['uploaded_image_data'] = f"data:image/{uploaded_file.type.split('/')[-1]};base64,{base64_image}"
                st.success("✅ Image ready!")
            else:
                st.session_state['uploaded_image_data'] = None
        
        with st.form("profile_form"):
            # -------------------------------------------------------------------------
            # Section 1: Basic Information
            # -------------------------------------------------------------------------
            st.markdown('<p class="section-header">👤 Basic Information</p>', unsafe_allow_html=True)
            
            name = st.text_input(
                "Full Name *",
                placeholder="e.g. senkudai",
                help="Your full name as you want it to appear on your profile"
            )
            
            github_username = st.text_input(
                "GitHub Username *",
                placeholder="yourusername",
                help="Your GitHub username (required for stats cards)"
            )
            
            bio = st.text_area(
                "About Me / Bio",
                placeholder="Passionate developer who loves building amazing things...",
                height=80,
                help="A brief description about yourself and your interests"
            )
            
            st.markdown("---")
            
            # -------------------------------------------------------------------------
            # Section 2: Profile Banner
            # -------------------------------------------------------------------------
            st.markdown('<p class="section-header">🖼️ Profile Banner</p>', unsafe_allow_html=True)
            
            banner_url = st.text_input(
                "Profile Banner URL (Optional)",
                placeholder="https://example.com/banner.png",
                help="URL to a banner image for your profile (recommended: 1280x320px)"
            )
            
            st.markdown("---")
            
            # -------------------------------------------------------------------------
            # Section 3: Skills
            # -------------------------------------------------------------------------
            st.markdown('<p class="section-header">🛠️ Skills</p>', unsafe_allow_html=True)
            
            skills = st.text_input(
                "Skills (comma separated)",
                placeholder="e.g. Python, JavaScript, React, Node.js",
                help="Enter each skill separated by commas (e.g., Python, JavaScript, HTML, CSS)"
            )
            
            st.markdown("---")
            
            # -------------------------------------------------------------------------
            # Section 4: Social Links
            # -------------------------------------------------------------------------
            st.markdown('<p class="section-header">🔗 Social Links</p>', unsafe_allow_html=True)
            
            twitter = st.text_input(
                "Twitter/X Username",
                placeholder="yourusername",
                help="Your Twitter/X handle (without @)"
            )
            
            linkedin = st.text_input(
                "LinkedIn Username",
                placeholder="yourusername",
                help="Your LinkedIn profile ID"
            )
            
            instagram = st.text_input(
                "Instagram Username",
                placeholder="yourusername",
                help="Your Instagram handle (without @)"
            )
            
            youtube = st.text_input(
                "YouTube Username/Channel",
                placeholder="yourchannel",
                help="Your YouTube channel name (without @)"
            )
            
            facebook = st.text_input(
                "Facebook Username",
                placeholder="yourusername",
                help="Your Facebook profile username"
            )
            
            discord = st.text_input(
                "Discord User ID (Optional)",
                placeholder="your_user_id",
                help="Your Discord user ID (not username#tag)"
            )
            
            website = st.text_input(
                "Website URL",
                placeholder="https://yourwebsite.com",
                help="Your personal website or portfolio"
            )
            
            st.markdown("---")
            
            # -------------------------------------------------------------------------
            # Section 5: Display Options
            # -------------------------------------------------------------------------
            st.markdown('<p class="section-header">🎨 Display Options</p>', unsafe_allow_html=True)
            
            theme = st.selectbox(
                "GitHub Stats Theme",
                options=GITHUB_STATS_THEMES,
                index=2,
                help="Choose a color theme for your GitHub stats cards"
            )
            
            col1, col2 = st.columns(2)
            with col1:
                show_languages = st.checkbox("Show Top Languages", value=True)
            with col2:
                show_streak = st.checkbox("Show Streak Stats", value=True)
            
            st.markdown("---")
            
            # -------------------------------------------------------------------------
            # Section 6: Extra
            # -------------------------------------------------------------------------
            st.markdown('<p class="section-header">✨ Extra</p>', unsafe_allow_html=True)
            
            fun_fact = st.text_input(
                "Fun Fact",
                placeholder="I can solve a Rubik's cube in under a minute!",
                help="Share an interesting fact about yourself"
            )
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Submit button
            submitted = st.form_submit_button("✨ Generate README")

    # =============================================================================
    # Main Content Area - Preview & Actions
    # =============================================================================
    
    # Initialize session state for storing generated content
    if 'readme_content' not in st.session_state:
        st.session_state.readme_content = ""
    
    # -------------------------------------------------------------------------
    # Generate README on Form Submit
    # -------------------------------------------------------------------------
    if submitted:
        if not name or not github_username:
            st.error("⚠️ Please fill in the required fields: Name and GitHub Username")
        else:
            # Use uploaded image if available
            final_profile_image = st.session_state.get('uploaded_image_data')
                
            # Collect all data
            data = {
                'name': name,
                'bio': bio,
                'github_username': github_username,
                'profile_image_url': final_profile_image,
                'banner_url': banner_url,
                'skills': skills,
                'twitter': twitter,
                'linkedin': linkedin,
                'instagram': instagram,
                'youtube': youtube,
                'facebook': facebook,
                'discord': discord,
                'website': website,
                'theme': theme,
                'show_languages': show_languages,
                'show_streak': show_streak,
                'fun_fact': fun_fact
            }
            
            # Generate README
            st.session_state.readme_content = generate_readme(data)
            st.session_state.github_username = data.get('github_username')
            st.session_state.skills = data.get('skills')
            st.session_state.theme = data.get('theme')
            st.session_state.show_languages = data.get('show_languages')
            st.session_state.show_streak = data.get('show_streak')
            st.session_state.profile_image_url = data.get('profile_image_url')
            st.session_state.name = data.get('name')
            st.session_state.bio = data.get('bio')
            st.success("✅ README generated successfully!")
    
    # -------------------------------------------------------------------------
    # Display Preview Section
    # -------------------------------------------------------------------------
    st.markdown("### 👁️ Preview")
    st.markdown("---")
    
    if st.session_state.readme_content:
        # Create tabs for different views
        preview_tab, markdown_tab = st.tabs(["📄 Rendered Preview", "📝 Markdown Code"])
        
        with markdown_tab:
            # Show the raw markdown code with edit option
            if 'editing' not in st.session_state:
                st.session_state.editing = False
            
            if st.session_state.editing:
                # Edit mode - show text area
                edited_content = st.text_area(
                    "Edit README Markdown",
                    value=st.session_state.readme_content,
                    height=400,
                    key="markdown_editor"
                )
                col_save, col_cancel = st.columns(2)
                with col_save:
                    if st.button("💾 Save Changes", use_container_width=True):
                        st.session_state.readme_content = edited_content
                        st.session_state.editing = False
                        st.success("✅ Changes saved!")
                        st.rerun()
                with col_cancel:
                    if st.button("❌ Cancel", use_container_width=True):
                        st.session_state.editing = False
            else:
                # View mode - show code block
                st.code(st.session_state.readme_content, language="markdown")
                if st.button("✏️ Edit Markdown", use_container_width=True):
                    st.session_state.editing = True
        
        with preview_tab:
            # Show visual preview using Streamlit components
            preview_data = {
                'github_username': st.session_state.get('github_username'),
                'skills': st.session_state.get('skills'),
                'theme': st.session_state.get('theme', 'radical'),
                'show_languages': st.session_state.get('show_languages', True),
                'show_streak': st.session_state.get('show_streak', True),
                'profile_image_url': st.session_state.get('profile_image_url'),
                'name': st.session_state.get('name'),
                'bio': st.session_state.get('bio')
            }
            if preview_data['github_username']:
                render_streamlit_preview(preview_data)
            else:
                st.info("Generate a README first to see the preview")
        
        # -------------------------------------------------------------------------
        # Action Buttons
        # -------------------------------------------------------------------------
        st.markdown("---")
        st.markdown("### 💾 Actions")
        
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            # Download button
            st.download_button(
                label="📥 Download README.md",
                data=st.session_state.readme_content,
                file_name="README.md",
                mime="text/markdown",
                use_container_width=True
            )
        
        with col2:
            if st.button("📋 Copy Markdown", use_container_width=True):
                if copy_to_clipboard(st.session_state.readme_content):
                    st.success("📋 Copied to clipboard!")
                else:
                    st.error("❌ Failed to copy. Please copy manually.")
        
        with col3:
            if st.button("🔄 Reset", use_container_width=True):
                st.session_state.readme_content = ""
                st.rerun()
    
    else:
        st.info("👈 Fill in the form in the sidebar and click 'Generate README' to see the preview here!")
        
        st.markdown("""
        <div style="background-color: #f0f2f6; padding: 2rem; border-radius: 12px; text-align: center;">
            <h4>✨ Your generated README will appear here</h4>
            <p style="color: #666;">
                Include GitHub stats cards, skill badges, social links and more!<br>
                Choose from 11 beautiful themes for your stats.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # =============================================================================
    # Instructions Section
    # =============================================================================
    st.markdown("---")
    with st.expander("📖 How to Use Your Generated README"):
        st.markdown("""
        ### Step-by-Step Guide:
        
        **1. Create a Special Repository**
        - Go to GitHub and create a new repository
        - Name it exactly as your GitHub username (e.g., `senkudai/senkudai`)
        - Make it **public**
        - Check "Initialize this repository with a README"
        - Click "Create repository"
        
        **2. Add Your Generated README**
        - Click on the README.md file in your new repository
        - Click the ✏️ edit icon (pencil)
        - Delete the existing content
        - Paste your generated README content
        - Scroll down and click "Commit changes"
        
        **3. View Your Profile**
        - Visit `github.com/yourusername`
        - Your new README will be displayed!
        
        ### Pro Tips:
        - 📸 **Banner Size**: Recommended 1280x320 pixels for best results
        - 🖼️ **Profile Image**: Use a square image (200x200px) for best appearance
        - 🔄 **Keep Updated**: Regularly update your skills as you learn new technologies
        - 📌 **Pin Repos**: Pin your best repositories to showcase your work
        """)


# =============================================================================
# Entry Point
# =============================================================================
if __name__ == "__main__":
    main()
