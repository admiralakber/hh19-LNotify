import React from 'react'

import _ from 'lodash'
import faker from 'faker'

import Layout from '../components/layout'
import Search from '../components/search'
import Form from '../components/form'

const doctor = _.times(5, () => ({
  title: faker.name.findName(),
  description: faker.name.jobArea(),
  image: faker.internet.avatar()
}))

const patient = _.times(5, () => ({
  title: faker.name.findName(),
  description: faker.name.jobArea(),
}))

const IndexPage = () => (
  <Layout>
    <Form />
    {/* <Search 
      source={doctor}
      />
    <Search 
      source={patient}
      /> */}
  </Layout>
)

export default IndexPage
