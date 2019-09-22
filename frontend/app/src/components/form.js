import React, { Component } from 'react'
import { 
    Form,
    Segment,
    Header, 
    Button,
    Divider,
    Icon,
    Grid,
    Message,
    List,
    Container
} from 'semantic-ui-react'
import moment from 'moment'
import _ from 'lodash'

import {
    DateTimeInput
} from 'semantic-ui-calendar-react'

const options = [
  { key: 'm', text: 'Arabic', value: 'arabic' },
  { key: 'f', text: 'Assyrian', value: 'assyrian' },
  { key: 'o', text: 'Other', value: 'other' },
]

class AppointmentForm extends Component {
    state = {
        interp: false,
        vision: false,
        dateTime: '',
        success: false,
        error: false,
        languageOptions: [],
        language: '',
        patientOptions: [],
        patient: '',
        doctorOptions: [],
        doctor: '',
        defaultDoctor: 'Default Practitioner if not specified',
        defaultLanguage: 'Default Practitioner if not specified'
    }

    async componentDidMount ()  {
        const doctorsR = await fetch("http://localhost:8081/FHIR/doctors", {
            headers: {
            Accept: "application/json"
            }
        })
        const doctorOptions = await doctorsR.json()
        const patientsR = await fetch("http://localhost:8081/FHIR/patients", {
            headers: {
            Accept: "application/json"
            }
        })
        const patientOptions = await patientsR.json()
        const languagesR = await fetch("http://localhost:8081/FHIR/languages", {
            headers: {
            Accept: "application/json"
            }
        })
        const languageOptions = await languagesR.json()
        this.setState({ 
            doctorOptions, 
            patientOptions, 
            languageOptions 
        })
    } 

    handleChange = (e, { name, value }) => {
        console.log(this.state)
        if (this.state.hasOwnProperty(name)) {
            this.setState({ [name]: value });
        }
    }

    handleToggle = (e, { name, value }) => {
        if (this.state.hasOwnProperty(name)) {
            this.setState({ [name]: !value });
        }
    }

    resetDates = (e) => {
        this.setState({dateTime: moment()})
    }

    handleSubmit = (e, { name, value }) => {
        const { patient, 
            doctor, 
            language, 
            vision,
            dateTime,
            interp
        } = this.state
        const get_req = "dateTime="+dateTime+"&doctor="+doctor+"&interp="+interp+"&language="+language+"&name="+name+"&patient="+patient+"&vision="+vision
        fetch("http://localhost:8081/LNotify/notify?"+get_req, {
            headers: {
                Accept: "application/json"
                },
            method: "GET",
        }).then( 
            e => e.json()
        ).then( 
            e => {
                console.log(name)
                if (name==='print') {
                    window.open(e.url, "_blank")
                }
                if (name==='sms') {
                    // Callback for SMS
                }
                if (name==='email') {
                    //callback
                }
                return
        })
        this.setState({
            success : true, 
            error: false,
            language: '',
            patient: '',
            doctor: '',
            notes: '',
            dateTime: ''
        })
    }
    
    onSelect = (e, { name, value }) => {
        this.handleChange(e, {name, value})

        this.setState({interp : _.sample([true, false])})

        fetch("http://localhost:8081/FHIR/patient/details?id=" + value, {
            headers: {
                Accept: "application/json"
                },
            method: "POST"
        }).then(
            (response) => {
                const data = response.json()
                return data
            }
        ).then( data => {
            const { doctorOptions, languageOptions } = this.state

            const doctor = doctorOptions.find( it => {
                return (it.text === data.generalPractitioner) 
            }).value
            console.log(typeof(doctor))
            if (typeof(doctor) !== undefined) {
                this.setState({
                    doctor
                })
            }
            else {
                console.log("Warn - Unregistered Doctor:", data.generalPractitioner)
            }
            const language = languageOptions.find( it => {
                return (it.text === data.communication[0].language)
            }).value
            if (typeof(language) !== undefined) {
                this.setState({
                    language
                })
            }
            else {
                console.log("Warn - Unsupported Language:",
                data.communication)
            }
        })
    }



    render() {
        const { 
            interp, 
            success, 
            error, 
            vision,
            doctor,
            patient,
            language,
            dateTime,
            doctorOptions,
            patientOptions,
            languageOptions,
            defaultDoctor,
            defaultLanguage
        } = this.state
        const disabled = (doctor === '') || (patient === '') || (language === '') || (dateTime === '')
        return (
            <div>
            <Header as='h1'>
                Appointment Reminder Translator
            </Header>
            <Segment color='teal'>
                <Divider />
                <Form error={error} 
                    success={success}
                    warning={disabled}>
                    <Form.Select 
                        search
                        fluid 
                        label='Patient' 
                        name='patient'
                        value={patient}
                        placeholder='Search ...' 
                        options={patientOptions}
                        onChange={this.onSelect}
                    />
                    <Form.Select
                        search 
                        fluid 
                        label='Healthcare Professional' 
                        name='doctor'
                        value={doctor}
                        onChange={this.handleChange}
                        placeholder={defaultDoctor}
                        options={doctorOptions}
                    />
                    <Form.Select
                        fluid
                        search
                        label='Language'
                        name='language'
                        value={language}
                        onChange={this.handleChange}
                        placeholder={defaultLanguage}
                        options={languageOptions}
                    />
                    <Divider />
                    <Form.Group inline>
                        <label>Has an interpreter been organised?</label>
                        <Form.Radio
                            toggle
                            value={interp}
                            name='interp'
                            checked={interp}
                            onChange={this.handleToggle}
                        />
                        <Icon name='audio'/>
                        <label> Send an audio accessible message?</label>
                        <Form.Radio
                            toggle
                            value={vision}
                            name='vision'
                            checked={vision}
                            onChange={this.handleToggle}
                        />
                    </Form.Group>
                    <Divider />
                    <DateTimeInput
                        inline
                        className='example-calendar-input'
                        value={this.state.dateTime}
                        name='dateTime'
                        onChange={this.handleChange}
                        minDate={moment()}
                    />
                    <Grid>
                        <Grid.Column textAlign="center">
                            <Form.Button 
                                floated='right'
                                onClick={this.resetDates}
                                // disabled
                                color='teal'
                            >
                                <Icon name='refresh'/>
                                Reset Dates
                            </Form.Button>
                        </Grid.Column>
                    </Grid>
                    <Divider />

                    <Form.TextArea 
                        label='Notes' placeholder='Additional Notes to be included with form letter ...' 
                        name='notes'
                        onChange={this.handleChange}
                    />
                     
                    <Grid>
                        <Grid.Column textAlign="center">
                            <Button.Group 
                            size='large' 
                            >
                                <Form.Button
                                    name='sms'
                                    onClick={this.handleSubmit}
                                    color='green'
                                    disabled={disabled}
                                >
                                    <Icon name='chat'/>
                                    SMS
                                </Form.Button>
                                <Button.Or />
                                <Form.Button
                                    name='email'
                                    onClick={this.handleSubmit}
                                    color='blue'
                                    disabled={disabled}
                                >
                                    <Icon name='mail'/>
                                    Email
                                </Form.Button>
                                <Button.Or />
                                <Form.Button
                                    name='print'
                                    onClick={this.handleSubmit}
                                    color='violet'
                                    disabled={disabled}
                                >
                                    <Icon name='print'/>
                                    Print
                                </Form.Button>
                            </Button.Group>
                        </Grid.Column>
                    </Grid>
                    {/* <Message
                        success
                        header='Form Completed'
                        content="Positive confirmation message"
                    /> */}
                    <Message
                        warning 
                        header='Action Items'
                    >
                        <Message.Header>Missing required fields</Message.Header>
                        <List horizontal celled>
                            {
                                (patient === '')   ? <List.Item> Select Patient </List.Item> : undefined 
                            }
                            {
                                (doctor === '')   ? <List.Item> Select Healthcare Professional </List.Item> : undefined 
                            }
                            {
                                (language === '')   ? <List.Item> Select Language </List.Item> : undefined
                            }
                            {
                                (dateTime === '')   ? <List.Item> Select Date </List.Item> : undefined 
                            }
                        </List>
                    </Message>
                </Form>
            </Segment>
            </div>
        )
    }
}

export default AppointmentForm