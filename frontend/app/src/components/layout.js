import React from 'react'
import PropTypes from 'prop-types'
import Helmet from 'react-helmet'
import { StaticQuery, graphql } from 'gatsby'
import { Container, } from 'semantic-ui-react'
import Header from './header'
import 'semantic-ui-less/semantic.less'


const Layout = ({ children, data }) => (
  <StaticQuery
    query={graphql`
      query SiteTitleQuery {
        site {
          siteMetadata {
            title
          }
        }
      }
    `}
    render={data => (
      <div style={{ minHeight: '100vh', 
        display: 'flex', 
        flexDirection: 'column' 
      }}>
        <Helmet
          title={data.site.siteMetadata.title}
          meta={[
            { name: 'description', content: 'Sample' },
            { name: 'keywords', content: 'sample, something' },
          ]}
        />

        <Header/>

        <Container style={{ 
          flexGrow: '1',
          display: 'flex',
          flexDirection: 'column',
          // alignItems: 'center',
          justifyContent: 'center'
          }}>
            {children}
        </Container>
      </div>
    )}
  />
)

Layout.propTypes = {
  children: PropTypes.node.isRequired,
}

export default Layout
