import React, { Component } from 'react'
import { Menu, Container } from 'semantic-ui-react'
import { Link } from 'gatsby'
import {withRouter} from 'react-router-dom';

const LinkedItem = ({ children, ...props }) => (
  <Menu.Item 
  as={Link} 
  {...props}>
    {children}
   </Menu.Item>
)

const RouteComponent = withRouter(props => <Header {...props}/>)

class Header extends Component {
  state = { activeItem: 'home' }

  handleItemClick = (e, { name }) => this.setState({ activeItem: name })

  render() {
    const { activeItem } = this.state

    return (
        <Menu pointing secondary style={{height: '100px'}}>
          <Container>
            <LinkedItem
              name='home'
              to='/'
              active={activeItem === 'home'}
              onClick={this.handleItemClick}
            />
            <Menu.Menu position='right'>
              <LinkedItem
                name='templates'
                to='template'
                active={activeItem === 'templates'}
                onClick={this.handleItemClick}
              />
              <LinkedItem
                name='logout'
                active={activeItem === 'logout'}
                onClick={this.handleItemClick}
              />
            </Menu.Menu>
          </Container>
        </Menu>
    )
  }
}
 