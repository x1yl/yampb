<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star! mayboe
*** Thanks again! Now go create something AMAZING! :D
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
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/lifewrd/yampb">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Discord Bot</h3>

  <p align="center">
    Discord bot made using discord.py
    <br />
    <a href="https://github.com/lifewrd/yampb"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/lifewrd/yampb">View Demo</a>
    ·
    <a href="https://github.com/lifewrd/yampb/issues">Report Bug</a>
    ·
    <a href="https://github.com/lifewrd/yampb/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
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
        <li><a href="#configuration">Configuration</a></li>
        <li><a href="#deploy">Deploy</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![yampb][product-screenshot]](https://yampb.cf)

This is a discord bot built in discord.py as a hobby project. This bot will most likely be moved over to either discord.js or pycord.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Next][Next.js]][Next-url]
* [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

1. Discord Bot Token <a href="https://discordjs.guide/preparations/setting-up-a-bot-application.html#creating-your-bot">Guide (from discord.js but it's the same step)</a>
2. Python 3.10.6 <a href="https://www.python.org/downloads/">Dowload</a>

### Installation

   ```sh
   git clone https://github.com/lifewrd/yampb.git
   cd yampb
   pip install -r requirements.txt
   ```

After installation finishes follow configuration instructions then run `python3 main.py` or `python main.py` to start the bot.
  
### Configuration

Fill out `config.py`

⚠️ **Note: Never commit or share your token or api keys publicly** ⚠️

```sh
token = ''
prefix = '!'
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Or Deploy
If you want to deploy to cloud

⚠️ **SUPPORT FOR DEPLOYMENTS TO ANYTHING OTHER THEN HEROKU NOT GUARANTEED** ⚠️
[![Deploy to Heroku](https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/heroku.svg)](https://heroku.com/deploy/?template=https://github.com/lifewrd/yampb)
[![Run on Replit](https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/replit.svg)](https://replit.com/github/lifewrd/yampb)
[![Remix on Glitch](https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/glitch.svg)](https://glitch.com/edit/#!/import/github/lifewrd/yampb)
[![Deploy to IBM Cloud](https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/ibmcloud.svg)](https://cloud.ibm.com/devops/setup/deploy?repository=https://github.com/lifewrd/yampb)
[![Deploy to Amplify Console](https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/amplifyconsole.svg)](https://console.aws.amazon.com/amplify/home#/deploy?repo=https://github.com/lifewrd/yampb)
[![Run on Google Cloud](https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/googlecloud.svg)](https://deploy.cloud.run/?git_repo=https://github.com/lifewrd/yampb)
[![Deploy on Railway](https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/railway.svg)](https://railway.app/new/template?template=https://github.com/lifewrd/yampb)
[![Deploy to Vercel](https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/vercel.svg)](https://vercel.com/new/clone?repository-url=https://github.com/lifewrd/yampb)
[![Deploy to Netlify](https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/netlify.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/lifewrd/yampb)

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://www.yampb.cf/docs/)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Custom Prefix
- [ ] Fix prefix
- [ ] Commands
    - [ ] connect 4

See the [open issues](https://github.com/lifewrd/yampb/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU GPLv3 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Fryvex - [@thefryvex](https://twitter.com/thefryvex) - yampb@yampb.cf

Project Link: [https://github.com/lifewrd/yampb](https://github.com/lifewrd/yampb)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Template for the README](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/lifewrd/yampb.svg?style=for-the-badge
[contributors-url]: https://github.com/lifewrd/yampb/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/lifewrd/yampb.svg?style=for-the-badge
[forks-url]: https://github.com/lifewrd/yampb/network/members
[stars-shield]: https://img.shields.io/github/stars/lifewrd/yampb.svg?style=for-the-badge
[stars-url]: https://github.com/lifewrd/yampb/stargazers
[issues-shield]: https://img.shields.io/github/issues/lifewrd/yampb.svg?style=for-the-badge
[issues-url]: https://github.com/lifewrd/yampb/issues
[license-shield]: https://img.shields.io/github/license/lifewrd/yampb.svg?style=for-the-badge
[license-url]: https://github.com/lifewrd/yampb/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/discord.py-0769AD?style=for-the-badge&logo=discord&logoColor=white
[Next-url]: https://discordpy.readthedocs.io/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 