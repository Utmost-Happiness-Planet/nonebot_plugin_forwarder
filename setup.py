from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nonebot-plugin-forwarder",
    version="2.0.2",
    author="Kl1nge5",
    description="A plugin based on NoneBot2, which can broadcast message from Source Groups to Destination Groups.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ninthseason/nonebot_plugin_forwarder",
    project_urls={
        "Bug Tracker": "https://github.com/ninthseason/nonebot_plugin_forwarder/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages=["nonebot_plugin_forwarder"],
    python_requires=">=3.7",
    install_requires=[
        "nonebot2 >= 2.0.0b2",
        "nonebot-adapter-onebot >= 2.0.0b1"
    ],
)
