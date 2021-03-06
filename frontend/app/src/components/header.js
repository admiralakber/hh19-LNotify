import React, { Component } from 'react'
import { Menu, Container } from 'semantic-ui-react'
import { Link } from 'gatsby'

const LinkedItem = ({ children, ...props }) => (
  <Menu.Item 
  as={Link} 
  {...props}>
    {children}
   </Menu.Item>
)

export default class Header extends Component {
  state = { activeItem: 'home' }

  handleItemClick = (e, { name }) => this.setState({ activeItem: name })

  render() {
    const { activeItem } = this.state

    return (
        <Menu pointing secondary>
          <Container>
            <LinkedItem
              name='home'
              to='/'
              active={activeItem === 'home'}
              onClick={this.handleItemClick}
            ><img src="CultureFluent.png" style={{height: '6vh', width: "auto"}}></img></LinkedItem>
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
          </Container>
        </Menu>
    )
  }
}
 