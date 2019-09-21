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
    Container
} from 'semantic-ui-react'
import moment from 'moment'

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
      error: false
  }

    handleChange = (e, { name, value }) => {
        console.log(value)
        if (this.state.hasOwnProperty(name)) {
            this.setState({ [name]: value });
        }
    }

    handleToggle = (e, { name, value }) => {
        console.log(value)
        if (this.state.hasOwnProperty(name)) {
            this.setState({ [name]: !value });
        }
    }

    resetDates = (e) => {
        this.setState({dateTime: moment()})
    }

    handleSubmit = (e, { name, value }) => {
        // Validate inputs
        console.log(name)
        // Set True
        this.setState({success : true, error: false})
    }

    render() {
        const { interp, success, error} = this.state
        return (
            <Segment>
                <Header as='h2'>
                   Form Title 
                </Header>
                <Divider />
                <Form error={error} success={success}>
                    <Form.Select 
                        search
                        fluid label='Patient' placeholder='Search ...' 
                    />
                    <Form.Select 
                        search
                        fluid 
                        label='Doctor' 
                        placeholder='Search ...' 
                    />
                    <Form.Select
                        fluid
                        search
                        label='Language'
                        options={options}
                        placeholder='Based on the data'
                    />
                    <Form.Group inline>
                        <label>Interpreter Organised</label>
                        <Form.Radio
                            toggle
                            value={interp}
                            name='interp'
                            checked={interp}
                            onChange={this.handleToggle}
                        />
                    </Form.Group>
                    <Form.Group inline>
                        <label>Vision Impaired</label>
                        <Form.Radio
                            toggle
                            value={vision}
                            name='interp'
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
                        disableMinute
                        onChange={this.handleChange}
                        minDate={moment()}
                    />
                    <Grid>
                        <Grid.Column textAlign="center">
                            <Form.Button 
                                floated='right'
                                onClick={this.resetDates}
                                // disabled
                            >
                                <Icon name='refresh'/>
                                Reset Dates
                            </Form.Button>
                        </Grid.Column>
                    </Grid>
                    <Divider />

                    <Form.TextArea label='Notes' placeholder='Additional Notes to be included with form letter ...' />
                     
                    <Grid>
                        <Grid.Column textAlign="center">

                            <Button.Group 
                            size='large' 
                            >
                                <Form.Button
                                    name='sms'
                                    onClick={this.handleSubmit}
                                >
                                    <Icon name='chat'/>
                                    SMS
                                </Form.Button>
                                <Button.Or />
                                <Form.Button
                                    name='email'
                                    onClick={this.handleSubmit}
                                >
                                    <Icon name='mail'/>
                                    Email
                                </Form.Button>
                                <Button.Or />
                                <Form.Button
                                    name='print'
                                    onClick={this.handleSubmit}
                                >
                                    <Icon name='print'/>
                                    Print
                                </Form.Button>
                            </Button.Group>
                        </Grid.Column>
                    </Grid>
                    <Message
                        success
                        header='Form Completed'
                        content="Positive confirmation message"
                    />
                    <Message
                        error
                        header='Action Forbidden'
                        content='Something went wrong please review your inputs.'
                    />
                </Form>
            </Segment>
        )
    }
}

export default AppointmentForm