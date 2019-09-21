
export default class Configurator extends Component{

    async componentDidMount ()  {
        const languagesR = await fetch("http://localhost:8081/FHIR/languages", {
            headers: {
            Accept: "application/json"
            }
        })
        const languageOptions = await languagesR.json()
    }
}
