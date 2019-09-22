
export default class Configurator extends Component{

    async componentDidMount ()  {
        const languagesR = await fetch("https://api.culturefluent.thaum.io/FHIR/languages", {
            headers: {
            Accept: "application/json"
            }
        })
        const languageOptions = await languagesR.json()
    }
}
