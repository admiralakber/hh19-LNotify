# CultureFluent

![CultureFluent Logo](frontend/app/public/CultureFluent.png)

HealthHack 2019 &ndash; CultureFluent by Team Unicorns

CultureFluent is a tool developed in response to a real-world problem as provided at HealthHack Brisbane 2019. Healthcare services in Australia currently identify and engage interpreters and/or translators when required. However, health disparities and a lack of access to services currently affect many Australians who belong to Culturally and Linguistically Diverse (CALD) communities due to language barriers.

Within CALD communities, these language barriers often manifest in the form of increased risk of non-attendance and generally compound into negative health impacts due to limited health literacy and misunderstanding/lack of health information.

CultureFluent removes a part of the obstacle by providing patients with future appointment letters in their preferred language (rather than in English). This will assist in addressing the current access barriers, improve understanding and communication, as well as engage and work with differing health beliefs, preferences and traditions.

## Features

### Standards Compliance

CultureFluent is compliant with the following standards:
- Health Level-7 (HL7)
- Fast Healthcare Interoperability Resources v4.0.0 (FHIR)
- OpenAPI Standards

API
- The API communicates and integrates with the following systems:
    - Hospital Based Corporate Information System (HBCIS)
    - Patient Administration System for Hospitals (PAS)
    - Integrated Electronic Medical Record (ieMR)
    - Consumer Integrated Mental Health Application (CIMHA)
- Can be used as a plugin or as a standalone product.

### Appointment Reminders

CultureFluent provides appointment reminders in 33 languages as provided by certified translators. These are printed in seconds!

#### Text

The appointment reminder links to Maps, seamlessly providing navigation including automatic public transit route suggestions.

#### Audio

CultureFluent is able to provide audio for its 33 languages through its integration with Google Text-to-Speech (TTS).

### Technology Stack
- Docker
- Docker Compose
- React
- Flask
- Swagger
- OpenAPI Doc
- Nginx
- Let's Encrypt
- Amazon Web Services

CultureFluent is containerised to run locally or on the cloud as a platform-agnostic web app that will run everywhere.

#### The Team

The team behind CultureFluent is a true reflection of Australia's diversity, much like that of the patients in the healthcare industry. We are a gender diverse team with varying cultural backgrounds from many professional fields. As such, we have all experienced, or known someone who has experienced, difficulties in accessing healthcare services due to the barriers that CultureFluent has sought to remove.

## Getting Started

### For Local Installation

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
1.  Navigate to the folder in which you would like to install the application
2. Enter the following command in Terminal to create a local copy on your device: '
```bash
git clone git@github.com:admiralakber/hh19-LNotify.git
```
3. Ensure you are in the application's root directory and enter the following commands:
```bash
make compose/dev args="up --build"
```

### For Production

Please contact the developers of CultureFluent.

## License

This project is licensed under the GNU Affero General Public License &ndash; see the [LICENSE](LICENSE) file for details.