<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/ahoopes16/auto-clicker">
    <img src="images/logo.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Auto-Clicker</h3>

  <p align="center">
    My personal attempt at making an auto-clicker, because why not
    <br />
    <a href="https://github.com/ahoopes16/auto-clicker/issues/new/choose">Report Bug</a>
    ·
    <a href="https://github.com/ahoopes16/auto-clicker/issues/new/choose">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
        <li><a href="#running-locally">Running Locally</a></li>
        <li><a href="#prerequisites">Executable</a></li>
        <li><a href="#prerequisites">Configuration</a></li>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#faq">FAQ</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#author">Author</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

One of my friends wanted an auto-clicker for a personal project, and it seemed easy enough to make one, so I figured I'd give it a shot!

### Built With

- [Python 3](https://www.python.org/)

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

You'll need to have at least Python 3.7 installed, but that's pretty much it.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ahoopes16/auto-clicker.git
   ```
2. Create virtual environment for the project
   ```sh
   python -m venv auto_clicker_env
   ```
3. Enter the virtual environment
   ```sh
   source auto_clicker_env/bin/activate
   ```
4. Install required packages
   ```sh
   pip install -r requirements.txt
   ```

<!-- USAGE EXAMPLES -->

## Usage

### Running Locally

To run this locally, after performing all of the installation steps, you can run it as you would any other Python script.

```sh
python auto-clicker/auto-clicker.py
```

Press the <kbd>s</kbd> key to start and stop the auto-clicker, and press the <kbd>e</kbd> key to exit the auto-clicker script completely.

### Executable

Alternatively, if you don't want to do all that work, you can download the executable file from the releases on GitHub!

### Configuration

For both the local version and the executable, you can create a `settings.ini` file in the same directory you're running the script from to easily configure the minimum and maximum click delay. Take a look at the `settings.ini` file in the root directory of this project to see how to set it up (or just use that one).

If no `settings.ini` file can be found, it will default to a minimum delay of 0 seconds and a maximum delay of 10 seconds.

<!-- ROADMAP -->

## Roadmap

As of right now, there isn't much else that I want to add.

See the [open issues](https://github.com/ahoopes16/auto-clicker/issues) for a list of proposed features (and known issues).
You can also check out my [project](https://github.com/ahoopes16/auto-clicker/projects/1) here on GitHub so you can see what I'm currently working on.

<!-- FAQ -->

## FAQ

Nobody cares enough about this thing to ask questions about it. :)

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- CONTACT -->

## Author

Author: [Alex Hoopes](https://github.com/ahoopes16)
<br>
[![LinkedIn](https://img.shields.io/badge/-LINKEDIN-blue?style=for-the-badge&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/kevin-alex-hoopes/)](https://www.linkedin.com/in/kevin-alex-hoopes/)
[![StackOverflow](https://img.shields.io/badge/-STACKOVERFLOW-orange?style=for-the-badge&logo=stack-overflow&logoColor=white&color=FE7A16&link=https://stackoverflow.com/users/14123656/kevin-hoopes)](https://stackoverflow.com/users/14123656/kevin-hoopes)
[![CodePen](https://img.shields.io/badge/-CODEPEN-black?style=for-the-badge&logo=codepen&logoColor=white&color=000000&link=https://codepen.io/ahoopes16)](https://codepen.io/ahoopes16)
[![HashNode](https://img.shields.io/badge/-HASHNODE-blue?style=for-the-badge&logo=hashnode&logoColor=white&color=2962FF&link=https://hashnode.com/@ahoopes16)](https://hashnode.com/@ahoopes16)
[![gmail](https://img.shields.io/badge/-GMAIL-orange?style=for-the-badge&logo=gmail&logoColor=white&color=EA4335&link=mailto:kevin.alex.hoopes@gmail.com)](mailto:kevin.alex.hoopes@gmail.com)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/ahoopes16/auto-clicker.svg?style=for-the-badge
[contributors-url]: https://github.com/ahoopes16/auto-clicker/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ahoopes16/auto-clicker.svg?style=for-the-badge
[forks-url]: https://github.com/ahoopes16/auto-clicker/network/members
[stars-shield]: https://img.shields.io/github/stars/ahoopes16/auto-clicker.svg?style=for-the-badge
[stars-url]: https://github.com/ahoopes16/auto-clicker/stargazers
[issues-shield]: https://img.shields.io/github/issues/ahoopes16/auto-clicker.svg?style=for-the-badge
[issues-url]: https://github.com/ahoopes16/auto-clicker/issues
[license-shield]: https://img.shields.io/github/license/ahoopes16/auto-clicker.svg?style=for-the-badge
[license-url]: https://github.com/ahoopes16/auto-clicker/blob/master/LICENSE.txt
[product-screenshot]: images/clotho-demo.gif
