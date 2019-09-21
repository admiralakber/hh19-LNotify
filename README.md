# CultureFluent &ndash; Appointment Translation

HealthHack 2019 &ndash; Multilingual Appointment Notifications

CultureFluent is a tool developed in response to a real-world problem as provided at HealthHack Brisbane 2019. Healthcare services in Australia currently identify and engage interpreters and/or translators when required. However, health disparities and a lack of access to services currently affect many Australians who belong to Culturally and Linguistically Diverse (CALD) communities due to language barriers.

## Getting Started

Install Docker:
1. Ensure **Docker Engine &ndash; Community** is installed by entering the following command in Terminal:
```bash
docker --version
```
- If a valid Docker version is not returned, refer to the following link to install Docker for your operating system: https://docs.docker.com/install/

2. Ensure **Docker Compose** is installed by entering the following command in Terminal:
```bash
docker-compose --version
```
- If a valid Docker Compose version is not returned, please see the following link for installation instructions: https://docs.docker.com/compose/install/


Install the Application:
1.  Navigate to the folder in which you would like to install the application;
2. Enter the following command in Terminal to create a local copy on your device: '
```bash
git clone git@github.com:admiralakber/hh19-LNotify.git
```
3. Ensure you are in the application's root directory and enter the following commands:
```bash
make compose/dev args="up --build"
```

## License

This project is licensed under the GNU Affero General Public License &ndash; see the [LICENSE.md](LICENSE) file for details.