from setuptools import setup

setup(
    name="seedance-2-api",
    version="0.1.0",
    author="Anil Matcha",
    description="Python wrapper for ByteDance's Seedance 2.5 API — realistic human faces, 1080p video, less censorship, Text-to-Video, Image-to-Video, and consistent character generation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    py_modules=["seedance_api", "mcp_server"],
    install_requires=[
        "requests",
        "python-dotenv",
        "mcp[cli]"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
